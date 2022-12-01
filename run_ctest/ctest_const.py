# constant for ctest generation

import os

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.join(CUR_DIR, "../../")
GEN_CTEST_DIR = os.path.join(CUR_DIR, "generate_ctest")
RUN_CTEST_DIR = os.path.join(CUR_DIR, "run_ctest")

HCOMMON = "hadoop-common"
HDFS = "hadoop-hdfs"
YARN = "hadoop-yarn-common"
DISTCP = "hadoop-distcp"
HBASE = "hbase-server"
ZOOKEEPER = "zookeeper-server"
ALLUXIO = "alluxio-core"
HDFSRBF = "hadoop-hdfs-rbf"

CTEST_HADOOP_DIR = os.path.join(APP_DIR, "hadoop")
CTEST_HBASE_DIR = os.path.join(APP_DIR, "ctest-hbase")
CTEST_ZK_DIR = os.path.join(APP_DIR, "ctest-zookeeper")
CTEST_ALLUXIO_DIR = os.path.join(APP_DIR, "ctest-alluxio")

PROJECT_DIR = {
    HCOMMON: CTEST_HADOOP_DIR,
    HDFS: CTEST_HADOOP_DIR,
    YARN: CTEST_HADOOP_DIR,
    DISTCP: CTEST_HADOOP_DIR,
    HBASE: CTEST_HBASE_DIR,
    ZOOKEEPER: CTEST_ZK_DIR,
    ALLUXIO: CTEST_ALLUXIO_DIR,
    HDFSRBF: CTEST_HADOOP_DIR,
}


# the module of the project we experimented on
MODULE_SUBDIR = {
    HCOMMON: "hadoop-common-project/hadoop-common",
    HDFS: "hadoop-hdfs-project/hadoop-hdfs",
    YARN: "hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common",
    DISTCP: "hadoop-tools/hadoop-distcp",
    HBASE: "hbase-server",
    ZOOKEEPER: "zookeeper-server",
    ALLUXIO: "core",
    HDFSRBF: "hadoop-hdfs-project/hadoop-hdfs-rbf",
}


# surefire report
SUREFIRE_SUBDIR = "target/surefire-reports/"
SUREFIRE_XML = "TEST-{}.xml" # slot is the classname
SUREFIRE_TXT = "{}.txt" # testclass
SUREFIRE_OUTTXT = "{}-output.txt" #testclass 

SUREFIRE_DIR = {
    HCOMMON: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[HCOMMON], SUREFIRE_SUBDIR)],
    HDFS: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[HDFS], SUREFIRE_SUBDIR)],
    YARN: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[YARN], SUREFIRE_SUBDIR)],
    DISTCP: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[DISTCP], SUREFIRE_SUBDIR)],
    HBASE: [os.path.join(CTEST_HBASE_DIR, MODULE_SUBDIR[HBASE], SUREFIRE_SUBDIR)],
    ZOOKEEPER: [os.path.join(CTEST_ZK_DIR, MODULE_SUBDIR[ZOOKEEPER], SUREFIRE_SUBDIR)],
    ALLUXIO: [
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "base", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "client/fs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "client/hdfs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/proxy", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/worker", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/master", SUREFIRE_SUBDIR),
    ],
    HDFSRBF: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[HDFSRBF], SUREFIRE_SUBDIR)],
}

# default or deprecate conf path
DEPRECATE_CONF_DIR = os.path.join(CUR_DIR, "deprecated_configs")
DEFAULT_CONF_DIR = os.path.join(CUR_DIR, "../hadoop/")

DEPRECATE_CONF_FILE = {
    HCOMMON: os.path.join(DEPRECATE_CONF_DIR, "hadoop.list"),
    HDFS: os.path.join(DEPRECATE_CONF_DIR, "hadoop.list"),
    HDFSRBF: os.path.join(DEPRECATE_CONF_DIR, "hadoop.list"),
    YARN: os.path.join(DEPRECATE_CONF_DIR, "hadoop.list"),
    DISTCP: os.path.join(DEPRECATE_CONF_DIR, "hadoop.list")
}

DEFAULT_CONF_FILE = {
    HCOMMON: os.path.join(DEFAULT_CONF_DIR, HCOMMON + "-default.tsv"),
    HDFS: os.path.join(DEFAULT_CONF_DIR, HDFS + "-default.tsv"),
    YARN: os.path.join(DEFAULT_CONF_DIR, YARN + "-default.tsv"),
    DISTCP: os.path.join(DEFAULT_CONF_DIR, DISTCP + "-default.tsv"),
    HBASE: os.path.join(DEFAULT_CONF_DIR, HBASE + "-default.tsv"),
    ALLUXIO: os.path.join(DEFAULT_CONF_DIR, ALLUXIO + "-default.tsv"),
    ZOOKEEPER: os.path.join(DEFAULT_CONF_DIR, ZOOKEEPER + "-default.tsv"),
    HDFSRBF: os.path.join(DEFAULT_CONF_DIR, HDFSRBF + "-default.tsv")
}


# injecting config file location
INJECTION_PATH = {
    HCOMMON: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-common-project/hadoop-common/target/classes/core-ctest.xml")
    ],
    HDFS: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs/target/classes/core-ctest.xml"),
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs/target/classes/hdfs-ctest.xml")
    ],
    YARN: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs/target/classes/core-ctest.xml"),
        os.path.join(CTEST_HADOOP_DIR, "hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common/target/classes/yarn-common-ctest.xml")
    ],
    DISTCP: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs/target/classes/core-ctest.xml"),
        os.path.join(CTEST_HADOOP_DIR, "hadoop-tools/hadoop-distcp/target/classes/distcp-ctest.xml")
    ],
    HBASE: [
        os.path.join(CTEST_HBASE_DIR, "hbase-server/target/classes/core-ctest.xml"),
        os.path.join(CTEST_HBASE_DIR, "hbase-server/target/classes/hbase-ctest.xml")
    ],
    ZOOKEEPER: [
        os.path.join(CTEST_ZK_DIR, "zookeeper-server/ctest.cfg")
    ],
    ALLUXIO: [
        os.path.join(CTEST_ALLUXIO_DIR, "core/alluxio-ctest.properties")
    ],
    HDFSRBF: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs/target/classes/core-ctest.xml"),
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs-rbf/target/classes/hdfs-rbf-ctest.xml")
    ]
}


# constants for ctest generation -- generated test result file
GENCTEST_TR_DIR = os.path.join(GEN_CTEST_DIR, "test_result") # test result directory
os.makedirs(GENCTEST_TR_DIR, exist_ok=True)
TR_FILE = "test_result_{id}.tsv"
MT_FILE = "missing_test_{id}.list"
FAIL = "f" # test failed
PASS = "p" # test passed
GOOD_VAL = "GOOD"
BAD_VAL = "BAD"
SKIP_VAL = "SKIP"

CTESTS_DIR = os.path.join(GEN_CTEST_DIR, "ctest_mapping")
os.makedirs(CTESTS_DIR, exist_ok=True)
CTESTS_FILE = "ctests-{project}.json"

# constants for running ctests
RUNCTEST_TR_DIR = os.path.join(RUN_CTEST_DIR, "run_ctest_result") # test result directory
os.makedirs(RUNCTEST_TR_DIR, exist_ok=True)