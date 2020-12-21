# wetlandbasin数据库

## 数据库说明

| 字段名称        | 字段说明                                                                         |
|-------------|------------------------------------------------------------------------------|
| Record ID   | 自增长主键，仅作为标识，无含义                                                              |
| CN          | Country Name，国家名                                                             |
| BMPID       | 源头设施编号                                                                       |
| BMPName     | 源头设施名称                                                                       |
| RSID        | 研究区域编号                                                                       |
| RSName      | 研究区域名称                                                                       |
| ProjectID   | 项目编号                                                                         |
| ProjectName | 项目名称                                                                         |
| Type        | 人工湿地类型，包括表流型和潜流型（分为水平潜流和垂直潜流）                                                |
| NSIR        | Natural Soil Infiltration Rate，自然土壤入渗率，单位：mm/h                               |
| GDH         | Groundwater Depth\(High\)，地下水埋深（最浅），单位：mm                                    |
| GDL         | Groundwater Depth\(Low\)，地下水埋深（最深），单位：mm                                     |
| SG          | "Soil Group，土壤类型。NCRS水文土壤类别将土壤分为A,B,C,D四类，这一分类反映了土壤入渗率，A组土壤入渗率最高，D组土壤入渗率最低。" |
| RCR         | "Runoff Control Rate,年径流总量控制率，范围：0~1"                                        |
| DR          | Design Rainfall，设计雨强，单位：mm/24hr                                              |
| DFRP        | Design Flood Return Periods，设计降雨重现期，单位：m2                                    |
| TC          | Treatment Capacity，处理能力，单位：m3/d                                              |
| TSA         | Total Surface Area，总表面积，单位：m2                                                |
| RATIOTSA    | Ratio of Tributary Area to Bioretention Surface Area，服务面积比                   |
| PPV         | Permanent Pool Volume，常水位的体积，单位：m3                                           |
| PPSA        | Permanent Pool Surface Area，常水位的表面积，单位：m2                                    |
| PPL         | Permanent Pool Length，常水位的长度，单位：m                                            |
| PPD         | Permanent Pool Depth，常水位以下水深，单位：mm                                           |
| SDV         | Surcharge Detention Volume，调蓄水深体积，单位：m3                                      |
| DSA         | Detention Surface Area，调蓄水深的表面积，单位：m2                                        |
| DBL         | Detention Basin Length，调蓄水深区域长度，单位：m                                         |
| HRT         | Hdraulic Retention Time，水力停留时间，单位：h                                          |
| BET         | Brim\-full Emptying Time，全排空时间，单位：h                                          |
| HBET        | Half brim\-full Emptying Time，半排空时间，单位：h                                     |
| FV          | Forebay Volume，前置塘容积，单位：m3                                                   |
| FSA         | Forebay Surface Area，前置塘表面积，单位：m2                                            |
| FD          | Forebay Depth，前置塘深度，单位：mm                                                    |
| OPA         | Outlet Pool Area，出水池面积，单位：m2                                                 |
| OPD         | Outlet Pool Depth，出水池深度，单位：mm                                                |
| HOOA        | Height of Outlet Above，溢流口相对高度，单位：mm                                         |
| PS          | Plant Species，主要植物种类                                                         |
| PD          | Planting Density，种植密度                                                        |
| FCV         | Flood Control Volume，超出调蓄水深的防洪量，单位：m3                                        |
| FLM         | Filter Layer Material，滤水层材质，包括材质类型及比例                                        |
| FLT         | Filter Layer Thickness，滤水层深度，单位：mm                                           |
| PDL         | Porosity of Drainage Layer，排水层的孔隙率，范围：0~1                                    |
| DLT         | Drainage Layer Thickness，砾石排水层厚度，单位：mm                                       |
| Comments    | 注释                                                                           |

## wetlandbasin数据
