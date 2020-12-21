# 干塘数据库

## 数据库说明

| 字段名称        | 字段说明                                                                         |
|-------------|------------------------------------------------------------------------------|
| RecordID    | 自增长主键，仅作为标识，无含义                                                              |
| CN          | Country Name，国家名                                                             |
| BMPID       | 源头设施编号                                                                       |
| BMPName     | 源头设施名称                                                                       |
| RSID        | 研究区域编号                                                                       |
| RSName      | 研究区域名称                                                                       |
| ProjectID   | 项目编号                                                                         |
| ProjectName | 项目名称                                                                         |
| NSIR        | Natural Soil Infiltration Rate，自然土壤入渗率，单位：mm/h                               |
| GDH         | Groundwater Depth\(High\)，地下水埋深（最浅），单位：mm                                    |
| GDL         | Groundwater Depth\(Low\)，地下水埋深（最深），单位：mm                                     |
| SG          | "Soil Group，土壤类型。NCRS水文土壤类别将土壤分为A,B,C,D四类，这一分类反映了土壤入渗率，A组土壤入渗率最高，D组土壤入渗率最低。" |
| RCR         | Runoff Control Rate，年径流总量控制率，范围：0~1                                          |
| DR          | Design Rainfall，设计雨强，单位：mm/24hr                                              |
| DFRP        | Design Flood Return Periods，设计降雨重现期，单位：yr                                    |
| SA          | Surface Area，面积，单位：m2                                                        |
| Volume      | 容积，单位：m3。干塘可以收集并缓慢排出、使水质得到净化的径流容量。                                           |
| Length      | 干塘长度，单位：m。采用进水到出水的距离；如果有多个进水点，取平均值；如果有多个出水点，根据支流的不透水面积加权                     |
| CA          | Catchment Area，服务区面积，单位：m2                                                   |
| RATIOTSA    | Ratio of Tributary Area to Bioretention Surface Area，服务面积比                   |
| HOOA        | Height of Outlet Above，溢流口高度（相对于底部），单位：mm                                    |
| BFVET       | Brim\-full Volume Emptying Time，全排空时间，单位：h                                   |
| HBFVET      | Half Brim\-full Volume Emptying Time，半排空时间，单位：h                              |
| BSV         | "Bottom Stage Volume,底层平台的容积，单位：m3。底层平台用于收集规模小、频率高的雨洪。"                      |
| BSSA        | "Bottom Stage Surface Area,底层平台的表面积，单位：m2"                                   |
| SideType    | 边坡做法                                                                         |
| SideSlope   | 边坡坡度                                                                         |
| FV          | Forebay Volume，前置塘容积，单位：m3。前置塘收集了进入干塘最初的入流，去除其中大块的沉淀物，并引导溢流进入干塘，使干塘的入流稳定。    |
| FSA         | Forebay Surface Area，前置塘表面积，单位：m2                                            |
| FD          | "Forebay Depth,前置塘深度，单位：mm"                                                  |
| PS          | "Plant Species,塘内植被类型"                                                       |
| FCV         | "Flood Control Volume,防洪量，单位：m3。超出水质净化容量的、可以承受的洪水量。"                         |
| Comments    | 注释                                                                           |


## 干塘数据

| RecordID | CN | BMPID | BMPName | RSID | RSName | ProjectID | ProjectName | NSIR | GDH | GDL | SG  | RCR   | DR | DFRP | SA  | Volume | Length | CA | RATIOTSA | HOOA | BFVET | HBFVET | BSV | BSSA | SideType | SideSlope | FV | FSA | FD | PS       | FCV | Comments |
|----------|----|-------|---------|------|--------|-----------|-------------|------|-----|-----|-----|-------|----|------|-----|--------|--------|----|----------|------|-------|--------|-----|------|----------|-----------|----|-----|----|----------|-----|----------|
| 1        |    |       |         |      |        |           | 武汉海绵城市      | 20   | 200 |     | 砂性土 | 0\.75 |    |      | 200 | 6      |        |    |          | 60   | 2     |        |     |      |          |           |    | 3   | 3  | 金娃娃萱草，石竹 |     |          |
