# -*- coding:utf-8 -*-
import json
import sys
import csv
import datetime
import time
import os
from random import randint

file_list = ["datanode-pv", "datanode-service", "datanode-statefulset", "datanode-storageclass"]
host_list = ['k8s-node02', 'k8s-node03', 'k8s-node04', 'k8s-node05', 'k8s-node06','k8s-node07',
             'k8s-node08','k8s-node09','k8s-node10','k8s-node11','k8s-node12','k8s-node13',
             'k8s-node14', 'k8s-node15', 'k8s-node16', 'k8s-node17', 'k8s-node18', 'k8s-node19']

dir_list = ['/data/ozone1', '/data/ozone2', '/data1/ozone3', '/data1/ozone4', '/data2/ozone5', '/data2/ozone6',
            '/data3/ozone7', '/data3/ozone8', '/data4/ozone9', '/data4/ozone10', '/data5/ozone11', '/data5/ozone12',
            '/data6/ozone13', '/data6/ozone14', '/data7/ozone15', '/data7/ozone16', '/data8/ozone17', '/data8/ozone18',
            '/data9/ozone19', '/data9/ozone20', '/data10/ozone21', '/data10/ozone22', '/data11/ozone23', '/data11/ozone24']
node_num = len(host_list)
pod_num_each_node = len(dir_list)
pod_num = node_num * pod_num_each_node

def readFile(filePath):
    f = 0
    try:
        f = open(filePath)
    except:
        print "read file" + filePath + " error"
        return
    lines = []
    while True:
        line = f.readline().decode("utf-8-sig").encode("utf-8")

        if not line:
            break
        line = line.rstrip()
        if len(line) == 0:
            break
        lines.append(line)
    return lines

def writeFile(filePath, lines):
    file = open(filePath, "w")
    for line in lines:
        file.write(line + "\n")
    file.close()

def main():
    global file_list
    global pod_num_each_node
    global pod_num
    for i in range(0, pod_num):
        for file_name in file_list:
            lines = readFile("template/" + file_name)
            newlines = []
            for line in lines:
                line = line.replace("{pod_index}", str(i + 1))
                node_index = i / pod_num_each_node
                line = line.replace("{host}", host_list[node_index])
                line = line.replace("{path}", dir_list[i % len(dir_list)])

                newlines.append(line)
            writeFile("result-datanode-yaml/" + file_name + "-" + str(i + 1) + ".yaml", newlines)

main()
