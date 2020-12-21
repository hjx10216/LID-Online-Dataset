# retenpond数据库

## 数据库说明

| 字段名称            | 字段说明                                                                                 |
|-----------------|--------------------------------------------------------------------------------------|
| RecordID        | 自增长主键，仅作为标识，无含义                                                                      |
| CN              | Country Name，国家名                                                                     |
| BMPID           | 源头设施编号                                                                               |
| BMPName         | 源头设施名称                                                                               |
| RSID            | 研究区域编号                                                                               |
| RSName          | 研究区域名称                                                                               |
| ProjectID       | 项目编号                                                                                 |
| ProjectName     | 项目名称                                                                                 |
| NSIR            | Natural Soil Infiltration Rate，自然土壤入渗率，单位：mm/h                                       |
| GDH             | 地下水埋深（最浅），单位：mm                                                                      |
| GDL             | 地下水埋深（最深），单位：mm                                                                      |
| SG              | "Soil Group，土壤类型。NCRS水文土壤类别将土壤分为A,B,C,D四类，这一分类反映了土壤入渗率，A组土壤入渗率最高，D组土壤入渗率最低。"         |
| RCR             | Runoff Control Rate，年径流总量控制率， 范围：0~1                                                 |
| DR              | Design Rainfall，设计雨强，单位：mm/24hr                                                      |
| DFRP            | Design Flood Return Periods，设计降雨重现期，单位：yr                                            |
| PPV             | Permanent Pool Volume，常水位时的容积，单位：m3                                                  |
| PPSA            | Permanent Pool Surface Area，常水位的面积，单位：m2                                             |
| PPL             | Permanent Pool Length，常水位的长度，单位：m。采用进水到出水的距离；如果有多个进水点，取平均值；如果有多个出水点，根据支流的不透水面积加权。    |
| PPD             | Permanent Pool Depth，常水位平均水深，单位：mm                                                   |
| SDV             | Surcharge Detention Volume，调蓄水位的体积，单位：m3。在常水位之上，短时间内可以处理的超额水量。                       |
| SSA             | Surcharge Surface Area，调蓄水位的表面积，单位：m2                                                |
| SBL             | Surcharge Basin Length，调蓄水深区域长度，单位：m。采用进水到出水的距离；如果有多个进水点，取平均值；如果有多个出水点，根据支流的不透水面积加权。 |
| SDD             | Surcharge Detention Depth，常水位以上的调蓄水深，单位：mm                                           |
| RATIOTSA        | Ratio of Tributary Area to Bioretention Surface Area，服务面积比                           |
| OM              | Outflow Method，排口方式，溢流口或底部排口                                                         |
| BET             | Brim\-full Emptying Time，全排空时间，单位：h。水量从调蓄水位释放至常水位需要的时间。                              |
| HBET            | "Half brim\-full Emptying Time,半排空时间，单位：h。水量从一半调蓄水位释放至常水位需要的时间。"                     |
| SideType        | 边坡做法                                                                                 |
| SideSlope       | 边坡坡度                                                                                 |
| VWB             | Vegetation within basin，塘内植被类型                                                       |
| VegetationRatio | 水生植物覆盖面积比例，范围：0~1                                                                    |
| FV              | Forebay Volume，前置塘容积，单位：m3                                                           |
| FSA             | Forebay Surface Area，前置塘表面积，单位：m2                                                    |
| FD              | Forebay Depth，前置塘深度，单位：mm                                                            |
| FCV             | Flood Control Volume，防洪量，单位：m3。超出水质净化容量的、可以承受的水量。                                    |
| Comments        | 注释                                                                                   |


## retenpond数据
