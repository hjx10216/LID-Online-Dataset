# rainwaterharvest数据库

## 数据库说明

| 字段名称        | 字段说明                                                                  |
|-------------|-----------------------------------------------------------------------|
| RecordID    | 自增长主键，仅作为标识，无含义                                                       |
| CN          | "Country Name,国家名"                                                    |
| BMPID       | 源头设施编号                                                                |
| BMPName     | 源头设施名称                                                                |
| RSID        | 研究区域编号                                                                |
| RSName      | 研究区域名称                                                                |
| ProjectID   | 项目编号                                                                  |
| ProjectName | 项目名称                                                                  |
| Type        | 雨水收集系统的类型，如水箱/水桶/水桶？                                                  |
| RCR         | Runoff Control Rate，年径流总量控制率，范围：0~1                                   |
| DR          | Design Rainfall，设计雨强，单位：mm/24hr                                       |
| SV          | Storage Volume，存储容积，单位：m3                                             |
| NOUIW       | Number of Units in Watershed，汇水区内雨水收集系统的数量                            |
| CRS         | Contributing Rooftop Size，有效屋顶尺寸，单位：m2                                |
| RAGMD       | Roofing and Gutter Material Description，屋顶和排水沟材料描述                    |
| Material    | 雨水收集系统的材质                                                             |
| Area        | 雨水收集系统的面积，单位：m2                                                       |
| Height      | 雨水收集系统的深度，单位：m                                                        |
| DT          | Drain Time，最大速度下的排空时间，单位：h                                            |
| DEOP        | Describe Emergency Overflow Provision，描述紧急情况的溢流准备                     |
| DMP         | Describe Mosquito Prevention，描述蚊虫防护                                   |
| IUOCW       | Intended Use of Captured Water，预计的雨水用途（如灌溉，冲厕）                        |
| CPWST       | "Can Potable Water Supplement Tank?（1 for yes, 0 for no）可以用饮用水补充水箱吗？" |
| Comments    | 注释                                                                    |

## rainwaterharvest数据

| RecordID | CN | BMPID | BMPName | RSID | RSName | ProjectID | ProjectName   | Type  | RCR | DR | SV        | NOUIW | CRS     | RAGMD | Material     | Area | Height | DT  | DEOP | DMP | IUOCW                        | CPWST | Comments |
|----------|----|-------|---------|------|--------|-----------|---------------|-------|-----|----|-----------|-------|---------|-------|--------------|------|--------|-----|------|-----|------------------------------|-------|----------|
| 1        |    |       |         |      |        |           | 厦门海绵城市        | CN    |     |    | 3         |       | 60      |       | 水泥           |      |        | 6   |      |     | 灌溉                           |       |          |
| 2        |    |       |         |      |        |           | 厦门市海绵城市       | 蓄水桶   |     |    | 28        |       |         |       | 加厚PP塑料       |      |        |     |      |     | 道路冲洗和绿化浇灌                    |       |          |
| 3        |    |       |         |      |        |           | 喀斯特地区         | 集雨桶   |     |    |           |       | 3\.14   |       |              |      |        |     |      |     | 人畜饮水                         |       |          |
| 4        |    |       |         |      |        |           | 沈阳市雨水收集       | 储水池   |     |    | 36299\.88 |       | 58000   |       |              |      |        |     |      |     | 灌溉植物，清洗道路                    |       |          |
| 5        |    |       |         |      |        |           | 重庆市           | 水箱    |     |    | 11        |       | 1500    |       |              |      |        |     |      |     | 发电                           |       |          |
| 6        |    |       |         |      |        |           | 汉口北地铁停车场      | 储水池   |     |    | 145\.41   |       | 18686   |       |              |      |        |     |      |     | 洗车、绿化、道路浇洒                   |       |          |
| 7        |    |       |         |      |        |           | 沈阳市雷明雅阁小区     |       |     |    | 60        |       | 713\.61 |       |              |      |        |     |      |     | 区景观水体用水、道路冲洗、花草灌溉以及居民非饮用生活用水 |       |          |
| 8        |    |       |         |      |        |           | 某酒店办公商业综合体    | 蓄水池   |     |    | 150       |       | 19530   |       | 钢筋混凝土结构      |      |        | 120 |      |     | 绿化浇撒用水                       |       |          |
| 9        |    |       |         |      |        |           | 哈尔滨市群力区绿园居住小区 | 蓄水池   |     |    | 152       |       | 46472   |       |              |      |        |     |      |     | 小区绿地用水                       |       |          |
| 10       |    |       |         |      |        |           | 首都机场T3A 航站楼   | 雨水斗   |     |    |           |       | 187000  |       | 304 不锈钢管材及管件 |      |        |     |      |     |                              |       |          |
| 11       |    |       |         |      |        |           | 北京通州芙蓉小学      | 雨水储水罐 |     |    |           |       |         |       |              |      |        |     |      |     | 就近浇洒绿化                       |       |          |
