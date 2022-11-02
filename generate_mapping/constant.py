import os

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.join(CUR_DIR, "../../")

CTEST_HADOOP_DIR = os.path.join(APP_DIR, "hadoop")
CTEST_HBASE_DIR = os.path.join(APP_DIR, "hbase")
CTEST_ZOOKEEPER_DIR = os.path.join(APP_DIR, "zookeeper")
CTEST_ALLUXIO_DIR = os.path.join(APP_DIR, "alluxio")
CTEST_FELIX_DIR = os.path.join(APP_DIR, "felix-dev")

MODULE_PATH = {
    "hadoop-common": CTEST_HADOOP_DIR,
    "hadoop-hdfs": CTEST_HADOOP_DIR,
    "hbase-server": CTEST_HBASE_DIR,
    "alluxio-core": CTEST_ALLUXIO_DIR,
    "felix-dev": CTEST_FELIX_DIR
}

SRC_SUBDIR = {
    "hadoop-common": "hadoop-common-project/hadoop-common",
    "hadoop-hdfs": "hadoop-hdfs-project/hadoop-hdfs",
    "hadoop-hdfs-rbf": "hadoop-hdfs-project/hadoop-hdfs-rbf",
    "hadoop-yarn-common": "hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common",
    "hadoop-distcp": "hadoop-tools/hadoop-distcp",
    "hbase-server": "hbase-server",
    "zookeeper-server": "zookeeper-server",
    "alluxio-core": "core",
    "felix-dev-bundlerepository": "bundlerepository",
    "felix-dev-cm.json": "cm.json",
    "felix-dev-configadmin": "configadmin"
}

MVN_TEST_PATH = {
    "hadoop-common": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-common"]),
    "hadoop-hdfs": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs"]),
    "hadoop-hdfs-rbf": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs-rbf"]),
    "hadoop-yarn-common": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-yarn-common"]),
    "hadoop-distcp": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-distcp"]),
    "hbase-server": os.path.join(CTEST_HBASE_DIR, SRC_SUBDIR["hbase-server"]),
    "zookeeper-server": os.path.join(CTEST_ZOOKEEPER_DIR, SRC_SUBDIR["zookeeper-server"]),
    "alluxio-core": os.path.join(CTEST_ALLUXIO_DIR, SRC_SUBDIR["alluxio-core"]),
    "felix-dev-bundlerepository": os.path.join(CTEST_FELIX_DIR, SRC_SUBDIR["felix-dev-bundlerepository"]),
    "felix-dev-cm.json": os.path.join(CTEST_FELIX_DIR, SRC_SUBDIR["felix-dev-cm.json"]),
    "felix-dev-configadmin": os.path.join(CTEST_FELIX_DIR, SRC_SUBDIR["felix-dev-configadmin"])
}

LOCAL_CONF_PATH = {
    "hadoop-common": "results/hadoop-common/conf_params.txt",
    "hadoop-hdfs": "results/hadoop-hdfs/conf_params.txt",
    "hadoop-hdfs-rbf": "results/hadoop-hdfs-rbf/conf_params.txt",
    "hadoop-yarn-common": "results/hadoop-yarn-common/conf_params.txt",
    "hadoop-distcp": "results/hadoop-distcp/conf_params.txt",
    "hbase-server": "results/hbase-server/conf_params.txt",
    "zookeeper-server": "results/zookeeper-server/conf_params.txt",
    "alluxio-core": "results/alluxio-core/conf_params.txt",
    "felix-dev-bundlerepository": "results/felix-dev-bundlerepository/conf_params.txt",
    "felix-dev-cm.json": "results/felix-dev-cm.json/conf_params.txt",
    "felix-dev-configadmin": "results/felix-dev-configadmin/conf_params.txt"
}

SUREFIRE_SUBDIR = "target/surefire-reports/*"

CTEST_SUREFIRE_PATH = {
    "hadoop-common": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-common"], SUREFIRE_SUBDIR)
    ],
    "hadoop-hdfs": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs"], SUREFIRE_SUBDIR)
    ],
    "hadoop-hdfs-rbf": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs-rbf"], SUREFIRE_SUBDIR)
    ],
    "hadoop-yarn-common": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-yarn-common"], SUREFIRE_SUBDIR)
    ],
    "hadoop-distcp": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-distcp"], SUREFIRE_SUBDIR)
    ],
    "hbase-server": [
        os.path.join(CTEST_HBASE_DIR, "hbase-server", SUREFIRE_SUBDIR)
    ],
    "zookeeper-server": [
        os.path.join(CTEST_ZOOKEEPER_DIR, "zookeeper-server", SUREFIRE_SUBDIR)
    ],
    "alluxio-core": [
        os.path.join(CTEST_ALLUXIO_DIR, "core/base", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/client/fs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/client/hdfs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/proxy", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/worker", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/master", SUREFIRE_SUBDIR)
    ],
    "felix-dev-bundlerepository": [
        os.path.join(CTEST_FELIX_DIR, "bundlerepository", SUREFIRE_SUBDIR)
    ],
    "felix-dev-cm.json": [
        os.path.join(CTEST_FELIX_DIR, "cm.json", SUREFIRE_SUBDIR)
    ],
    "felix-dev-configadmin": [
        os.path.join(CTEST_FELIX_DIR, "configadmin", SUREFIRE_SUBDIR)
    ]
}

LOCAL_SUREFIRE_SUFFIX = "surefire-reports/*"

LOCAL_SUREFIRE_PATH = {
    "hadoop-common": [
        os.path.join("surefire-reports/common/hadoop-common", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hadoop-hdfs": [
        os.path.join("surefire-reports/hdfs/hadoop-hdfs", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hadoop-hdfs-rbf": [
        os.path.join("surefire-reports/hadoop-hdfs-rbf", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hadoop-yarn-common": [
        os.path.join("surefire-reports/hadoop-yarn-common", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hadoop-distcp": [
        os.path.join("surefire-reports/hadoop-distcp", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hbase-server": [
        os.path.join("surefire-reports/hbase/hbase-server", LOCAL_SUREFIRE_SUFFIX)
    ],
    "zookeeper-server": [
        os.path.join("surefire-reports/zk/zookeeper-server", LOCAL_SUREFIRE_SUFFIX)
    ],
    "alluxio-core": [
        os.path.join("surefire-reports/alluxio-core", LOCAL_SUREFIRE_SUFFIX)
    ],
    "felix-dev-bundlerepository": [
        os.path.join("surefire-reports/felix-dev-bundlerepository", LOCAL_SUREFIRE_SUFFIX)
    ],
    "felix-dev-cm.json": [
        os.path.join("surefire-reports/felix-dev-cm.json", LOCAL_SUREFIRE_SUFFIX)
    ],
    "felix-dev-configadmin": [
        os.path.join("surefire-reports/felix-dev-configadmin", LOCAL_SUREFIRE_SUFFIX)
    ]
}
