# 低影响开发措施数据库

## 数据库说明

中国开展城市雨洪管理研究起步较晚，在海绵城市建设中可参考借鉴的本地化数据不多。在开展“面向径
流减控与污染削减的海绵设施空间优化技术研究”的过程中累积了大量的海绵城市径流控制设施建设和运
行阶段的数据，为了更好利用这些数据支持我国海绵城市的建设，本研究初步构建了一个海绵城市径流
控制设施数据库。首先分析了我国海绵城市试点建设中源头径流控制设施相关数据的实际情况，完成了海
绵城市源头径流控制设施效能数据库的需求分析，进而通过概念设计、逻辑设计和物理设计三个步骤，设
计了一个结构清晰、管理方便、执行效率高的海绵城市径流控制设施数据库。该数据库主要分为径流控制
设施、研究区域、监测站、监测事件和监测数据五个实体集，包含45张表格和上千条字段属性。后续通过
中国海绵城市径流控制设施数据库的建设，可以为海绵城市径流控制设施的效能评估、运营维护和成本效
益分析提供数据支持，服务于海绵城市的规划设计和建设。

- [生物滞留池](https://github.com/hjx10216/LID-Online-Dataset/blob/main/DataBioretention.md)
- [蓄水池](https://github.com/hjx10216/LID-Online-Dataset/blob/main/DataDetentionbasin.md)
- [Assembly](https://mapbox.com/assembly/documentation/)

### Required Components

Your prototype must contain all three of the following components:

- Dropdown
- Grid
- Modal

### Choose Your Own Components

Your prototype must contain your choice of five of the following components.

- Table
- Input Group
- Button Group
- Glyph Icon
- Label
- Alert
- Tooltip

### Media Queries

One of the greatest challenges to web design and development is that your project needs to look nice
and work on a range of devices of different shapes, sizes, and operating systems. You may have
noticed that sometimes you want your design to look one way on a large screen and another way on a
small smart phone. This issue is addressed by media queries.

At the bottom of your `style.css` file you should see two media queries. Add CSS inside the media
queries that will:

- Make the sidebar slightly smaller and the map slightly larger when the screen width is between
  800px and 480px
- Move the sidebar entirely and have the map take up the full screen when the width is smaller than
  480px

### Stretch Goal

Keep going! Try to match all of the components. If you have additional time, can
you make the style look more similar to the screens?

### Extra Stretch Goal

Can you recreate the blue navigation on the left side of the screens?
