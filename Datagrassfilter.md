# grassfilter数据库

## 数据库说明

| 字段名称        | 字段说明                                                                         |
|-------------|------------------------------------------------------------------------------|
| RecordID    | 自增长主键，仅作为标识，无含义                                                              |
| CN          | "Country Name,国家名"                                                           |
| BMPID       | 源头设施编号                                                                       |
| BMPName     | 源头设施名称                                                                       |
| RSID        | 研究区域编号                                                                       |
| RSName      | 研究区域名称                                                                       |
| ProjectID   | 项目编号                                                                         |
| ProjectName | 项目名称                                                                         |
| NSIR        | "Natural Soil Infiltration Rate,自然土壤入渗率，单位：mm/h"                             |
| GDH         | "Groundwater Depth\(High\),地下水埋深（最浅），单位：mm"                                  |
| GDL         | "Groundwater Depth\(Low\),地下水埋深（最深），单位：mm"                                   |
| SG          | "Soil group,土壤类型。NCRS水文土壤类别将土壤分为A,B,C,D四类，这一分类反映了土壤入渗率，A组土壤入渗率最高，D组土壤入渗率最低。" |
| RCR         | "Runoff Control Rate,年径流总量控制率，范围：0~1"                                        |
| DR          | "Design Rainfall,设计雨强，单位：mm/24hr"                                            |
| Length      | 流程方向的草带长度，单位：m                                                               |
| Width       | 垂直于流程方向的草带宽度，单位：m                                                            |
| LS          | "Longtitudinal Slope,流程方向的纵向坡度，单位：度"                                         |
| DFD         | "Design Flow Depth,设计重现期的水深，单位：mm"                                           |
| DFV         | "Design Flow Velocity,设计重现期的峰值流速，单位：m/s"                                     |
| GSD         | "Grass Species and Densities,植被的种类和密度"                                       |
| ISI         | "Is strip irrigated（1 for yes, 0 for no\) 是否被人工灌溉"                           |
| Manning     | Manning’s n设计重现期最大径流量的曼宁系数                                                   |
| Comments    | 注释                                                                           |

## grassfilter数据
