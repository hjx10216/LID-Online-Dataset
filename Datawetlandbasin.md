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

| Record ID | CN | BMPID | BMPName | RSID | RSName | ProjectID | ProjectName        | Type | NSIR | GDH | GDL | SG              | RCR    | DR | DFRP | TC | TSA      | RATIOTSA | PPV | PPSA | PPL | PPD | SDV | DSA | DBL | HRT     | BET | HBET | FV | FSA    | FD   | OPA | OPD | HOOA   | PS                  | PD | FCV | FLM | FLT | PDL | DLT | Comments |
|-----------|----|-------|---------|------|--------|-----------|--------------------|------|------|-----|-----|-----------------|--------|----|------|----|----------|----------|-----|------|-----|-----|-----|-----|-----|---------|-----|------|----|--------|------|-----|-----|--------|---------------------|----|-----|-----|-----|-----|-----|----------|
| 1         |    |       |         |      |        |           | 武汉海绵城市             |      | 20   | 200 | 200 | 砂性土             | 0\.75  |    |      |    | 200      |          |     | 2    |     | 60  | 3   | 3   |     | 6       |     |      |    | 20     | 20   | 30  | 3   | 47\.55 | "金娃娃萱草,八宝景天"        |    |     |     |     |     |     |          |
| 2         |    |       |         |      |        |           | 重庆市北部新区高新棕榈泉雨水人工湿地 |      |      |     |     |                 | 0\.72  |    |      |    | 1200     |          |     |      |     |     |     |     |     |         |     |      |    | 28106  |      |     |     |        |                     |    |     |     |     |     |     |          |
| 3         |    |       |         |      |        |           | 人工湿地污水处理（垂直潜流人工湿地） |      |      |     |     | 粗砂，砾石           |        |    |      |    | 520      |          |     |      |     |     |     |     |     | 40\.8   |     |      |    | 20\.25 | 5500 |     |     |        | "芦苇,菖蒲"             |    |     |     |     |     |     |          |
| 4         |    |       |         |      |        |           | 人工湿地污水处理（水平潜流人工湿地） |      |      |     |     | 砾石              |        |    |      |    | 640      |          |     |      |     |     |     |     |     | 34\.56  |     |      |    | 20\.2  | 5500 |     |     |        | "芦苇,菖蒲"             |    |     |     |     |     |     |          |
| 5         |    |       |         |      |        |           | 湖南省茶陵县高陇镇水头村人工湿地   |      |      |     |     | 水稻土             |        |    |      |    | 1715\.75 |          |     |      |     | 60  |     |     |     | 17\.184 |     |      |    |        |      |     |     |        | 梭鱼草、狐尾藻、轮叶黑藻        |    |     |     |     |     |     |          |
| 6         |    |       |         |      |        |           | 玉溪大河北侧人工湿地         |      |      |     |     |                 | 0\.127 |    |      |    | 92000    |          |     |      |     | 500 |     |     |     |         |     |      |    |        |      |     |     |        |                     |    |     |     |     |     |     |          |
| 7         |    |       |         |      |        |           | 汉阳桃花岛示范区           |      |      |     |     | 不同粒径的碎石和砂子、土壤级配 |        |    |      |    | 5000     |          |     |      |     | 60  |     |     |     | 72      |     |      |    |        |      |     |     |        | 美人蕉、香蒲和芦苇           |    |     |     |     |     |     |          |
| 8         |    |       |         |      |        |           | 棕榈泉人工湿地系统          |      |      |     |     |                 |        |    |      |    | 1200     |          |     |      |     | 40  |     |     |     | 72      |     |      |    |        |      |     |     |        |                     |    |     |     |     |     |     |          |
| 9         |    |       |         |      |        |           | 盐龙湖人工湿地            |      |      |     |     | 原位土壤            |        |    |      |    | 2200000  |          |     |      |     |     |     |     |     | 12      |     |      |    |        |      |     |     |        | 芦苇、茭草               |    |     |     |     |     |     |          |
| 10        |    |       |         |      |        |           | 阿坝州农村生活污水处理        |      |      |     |     | 矿物土壤和高铝土壤       |        |    |      |    |          |          |     |      |     |     |     |     |     | 72      |     |      |    |        |      |     |     |        | 香蒲、花叶芦竹、纸莎草、美人蕉、风车草 |    |     |     |     |     |     |          |
