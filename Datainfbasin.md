# 渗透塘数据库

## 数据库说明

| 字段名称        | 字段说明                                                                                       |
|-------------|--------------------------------------------------------------------------------------------|
| RecordID    | 自增长主键，仅作为标识，无含义                                                                            |
| CN          | Country Name，国家名                                                                           |
| BMPID       | 源头设施编号                                                                                     |
| BMPName     | 源头设施名称                                                                                     |
| RSID        | 研究区域编号                                                                                     |
| RSName      | 研究区域名称                                                                                     |
| ProjectID   | 项目编号                                                                                       |
| ProjectName | 项目名称                                                                                       |
| NSIR        | Natural Soil Infiltration Rate，自然土壤入渗率，单位：mm/h                                             |
| GDH         | Groundwater Depth\(High\)，地下水埋深（最浅），单位：mm                                                  |
| GDL         | Groundwater Depth\(Low\)，地下水埋深（最深），单位：mm                                                   |
| SG          | "Soil Group，土壤类型。NCRS水文土壤类别将土壤分为A,B,C,D四类，这一分类反映了土壤入渗率，A组土壤入渗率最高，D组土壤入渗率最低。"               |
| RCR         | Runoff Control Rate，年径流总量控制率，范围：0~1                                                        |
| DR          | Design Rainfall，设计雨强，单位：mm/24hr                                                            |
| DFRP        | Design Flood Return Periods，设计降水重现期，单位：yr                                                  |
| Volume      | 渗透塘体积，单位：m3                                                                                |
| Area        | 渗透塘表面积，单位：m2                                                                               |
| Depth       | 渗透塘蓄水深度，单位：mm                                                                              |
| Length      | 渗透塘长度，单位：m                                                                                 |
| DTIL        | Depth to Impermeable Layer，不透水层的深度，单位：m                                                    |
| DTSL        | Depth and Type of Each Soil Layer，各土层的厚度和类型                                                |
| PS          | Plant Species on Basin Bottom，塘底的植物种类                                                      |
| GM          | List of the type of granular material covering basin bottom if not grass，覆盖塘底的颗粒材料类型，如果没有草 |
| FCV         | "Flood control volume above the water quality detention volume, 超出容积的可以承受的洪水量，单位：m3"       |
| GHC         | Groundwater Hydraulic Conductivity，地下水的渗透系数，单位：mm/h                                        |
| GFG         | Groundwater Flow Gradient，地下水的流量梯度，单位：mm/h                                                 |
| Comments    | 注释                                                                                         |

## 渗透塘数据

| RecordID | CN | BMPID | BMPName | RSID | RSName | ProjectID | ProjectName | NSIR | GDH | GDL | SG    | RCR   | DR | DFRP | Volume | Area | Depth | Length | DTIL | DTSL | PS | GM  | FCV | GHC | GFG | Comments |
|----------|----|-------|---------|------|--------|-----------|-------------|------|-----|-----|-------|-------|----|------|--------|------|-------|--------|------|------|----|-----|-----|-----|-----|----------|
| 1        |    |       |         |      |        |           | 三亚海绵城市      | 20   | 200 |     | 砂性土   | 0\.75 |    |      | 60     | 200  |       |        |      |      |    | 砾石  |     |     |     |          |
| 2        |    |       |         |      |        |           | 上海世博城市      |      |     |     | 人工回填土 | 0\.9  |    |      | 662    | 111  |       |        |      |      |    | 碎石  |     |     |     |          |
| 3        |    |       |         |      |        |           |             |      | 200 |     | 种植土   |       |    |      |        |      |       |        |      |      |    | 厚碎石 |     |     |     |          |
