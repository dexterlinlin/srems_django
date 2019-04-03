// SPU - PDT
CREATE (nceanalyze:SPU {name: 'NCE-分析', supervisor: 'zhourui'})
CREATE (uTraffic:PDT {name: 'uTraffic', supervisor: ''})
CREATE (u2000i:PDT {name: 'U2000-I', supervisor: ''})
CREATE
  (nceanalyze)-[:IS_UPPER_DEPT]->(uTraffic),
  (nceanalyze)-[:IS_UPPER_DEPT]->(u2000i)

// Features
CREATE(pms_utrafficconn:Feature{name:'PMS-uTraffic对接',desc_en_us:'',desc_zh_cn:'PMS-uTraffic对接'})
CREATE(pms_instancemanage:Feature{name:'PMS-实例管理',desc_en_us:'',desc_zh_cn:'PMS-实例管理'})
CREATE(pms_transdatacollection:Feature{name:'PMS-传送数据采集',desc_en_us:'',desc_zh_cn:'PMS-传送数据采集'})
CREATE(pms_ipdatacollection:Feature{name:'PMS-IP数据采集',desc_en_us:'',desc_zh_cn:'PMS-IP数据采集'})
CREATE(pms_accessdatacollection:Feature{name:'PMS-接入数据采集',desc_en_us:'',desc_zh_cn:'PMS-接入数据采集'})
CREATE(pms_distributed:Feature{name:'PMS-分布式',desc_en_us:'',desc_zh_cn:'PMS-分布式'})
CREATE(pms_others:Feature{name:'PMS-其他',desc_en_us:'',desc_zh_cn:'PMS-其他'})
CREATE(clockview:Feature{name:'时钟视图',desc_en_us:'',desc_zh_cn:'时钟视图'})
CREATE(report:Feature{name:'报表',desc_en_us:'',desc_zh_cn:'报表'})
CREATE(carrier_service_license:Feature{name:'承载业务License',desc_en_us:'',desc_zh_cn:'承载业务License'})
CREATE(physical_inventory:Feature{name:'物理存量',desc_en_us:'',desc_zh_cn:'物理存量'})
CREATE(link_management:Feature{name:'链路管理',desc_en_us:'',desc_zh_cn:'链路管理'})
CREATE(line_management:Feature{name:'纤缆管理',desc_en_us:'',desc_zh_cn:'纤缆管理'})
CREATE(u2100_network_features:Feature{name:'U2100网络特性',desc_en_us:'',desc_zh_cn:'U2100网络特性'})
CREATE(utraffic_sdn:Feature{name:'uTraffic-SDN',desc_en_us:'',desc_zh_cn:'uTraffic-SDN'})
CREATE(utraffic_ipfpm:Feature{name:'uTraffic-IPFPM',desc_en_us:'',desc_zh_cn:'uTraffic-IPFPM'})
CREATE(document_newlyinstall:Feature{name:'资料-全新安装资料',desc_en_us:'',desc_zh_cn:'资料-全新安装资料'})
CREATE(document_patchinstall:Feature{name:'资料-补丁安装资料',desc_en_us:'',desc_zh_cn:'资料-补丁安装资料'})
CREATE(document_flowconfiguration:Feature{name:'资料-流量配置资料',desc_en_us:'',desc_zh_cn:'资料-流量配置资料'})
CREATE(document_qualityconfiguration:Feature{name:'资料-质量配置资料',desc_en_us:'',desc_zh_cn:'资料-质量配置资料'})
CREATE(document_sdn:Feature{name:'资料-SDN资料',desc_en_us:'',desc_zh_cn:'资料-SDN资料'})
CREATE(document_4k:Feature{name:'资料-4K资料',desc_en_us:'',desc_zh_cn:'资料-4K资料'})
CREATE(document_fault:Feature{name:'资料-故障和例行维护资料',desc_en_us:'',desc_zh_cn:'资料-故障和例行维护资料'})
CREATE(document_tanzhen:Feature{name:'资料-探针资料',desc_en_us:'',desc_zh_cn:'资料-探针资料'})
CREATE(document_northbound:Feature{name:'资料-北向资料',desc_en_us:'',desc_zh_cn:'资料-北向资料'})
CREATE(document_security:Feature{name:'资料-安全资料',desc_en_us:'',desc_zh_cn:'资料-安全资料'})
CREATE(document_others:Feature{name:'资料-其他研发资料',desc_en_us:'',desc_zh_cn:'资料-其他研发资料'})
CREATE(utraffic_database:Feature{name:'uTraffic-数据库',desc_en_us:'',desc_zh_cn:'uTraffic-数据库'})
CREATE(utraffic_atomrouter:Feature{name:'uTraffic-原子路由器管理',desc_en_us:'',desc_zh_cn:'uTraffic-原子路由器管理'})


//VersionType
CREATE (traditionalutraffic:VersionType {name:"traditianal utraffic"})
CREATE (nceversion :VersionType {name:"nce version"})


// Employee
CREATE (fengjianli:Employee{name:"fengjianli",id:"00335896"})
CREATE (zhoujihong:Employee{name:"zhoujihong",id:"00334392"})
CREATE (chenlening:Employee{name:"chenlening",id:"00294178"})
CREATE (chenli:Employee{name:"chenli",id:"00488055"})

// LM -- Feature
CREATE
  (zhoujihong) - [:MANAGE{role:"LM"}] -> (ipran_ringreport),
  (zhoujihong) - [:MANAGE{role:"LM"}] -> (utraffic_atomrouter),
  (chenlening) - [:MANAGE{role:"LM"}] -> (utraffic_sdn)

// SPU/PDT -- LM
CREATE
  (zhoujihong) - [:EMPLOYEEOF {title:"LM",team:"Quality Module"}] -> (uTraffic),
  (zhoujihong) - [:EMPLOYEEOF {title:"PD",team:"5G PTN"}] -> (nceanalyze),
  (chenlening) - [:EMPLOYEEOF {title:"LM",team:"sdn"}] -> (uTraffic),
  (chenlening) - [:EMPLOYEEOF {title:"PD",team:"basicframework"}] -> (nceanalyze)


// Dept / SPU - Feature
CREATE
  (uTraffic) - [:OWN] -> (utraffic_sdn),
  (uTraffic) - [:OWN] -> (utraffic_atomrouter)
