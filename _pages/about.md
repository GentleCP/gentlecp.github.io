---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a Ph.D. student at the Institute of Information Engineering, Chinese Academy of Sciences, supervised by [Prof. Limin Sun](https://scholar.google.com/citations?hl=zh-CN&user=ujYecNkAAAAJ). From March 2024 to March 2025, I was a visiting Ph.D. student at Nanyang Technological University under the supervision of [Assoc. Prof. Yi Li](https://liyiweb.com/).

My research interests focus on software supply chain security, IoT security, program analysis, and the application of AI in security. Please contact me via email if you are interested in my research.


# 🔥 News
- *2025.09*: 🎉🎉 Two paper were accepted by the ASE 2025. One paper was accepted by the ToSEM 2025.
- *2025.08*: 🎉🎉 One paper was accepted by the TSE 2025.

# 📝 Publications 

- <span style="color:#337AB7">[**ASE'2025**]</span> **<u>Chaopeng Dong</u>**, Jingdong Guo, Shouguo Yang, Yi Li, Dongliang Fang,
Yang Xiao, Yongle Chen, Limin Sun.  **Advancing Binary Code Similarity Detection via Context-Content Fusion and LLM Verification.**  In *IEEE/ACM International Conference on Automated Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) 
- <span style="color:#337AB7">[**ASE'2025**]</span> . Siyuan Li, Yaowen Zheng, Jingdong Guo, **<u>Chaopeng Dong</u>**, Chunpeng Yan, Weijie Wang, Yimo Ren, Limin Sun, Hongsong Zhu. **Lares: LLM-driven Code Slice Semantic Search for Patch Presence Testing.**  In *IEEE/ACM International Conference on Automated Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) 
- <span style="color:#337AB7">[**ToSEM'2025**]</span> **<u>Chaopeng Dong</u>**, Jingdong Guo, Shouguo Yang, Yang Xiao, Yi Li, Hong Li, Zhi Li, Limin Sun.  **PLocator: Fine-Grained Patch Presence Test in Binaries via Patch Code Localization.**  In *ACM Transactions on Software Engineering and Methodology*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) 
- <span style="color:#337AB7">[**TSE'2025**]</span> Yiran Cheng, Lwin Khin Shar, Ting Zhang, Shouguo Yang, **<u>Chaopeng Dong</u>**, David Lo, Shichao Lv,Zhiqiang Shi, Limin Sun.  **VERCATION: Precise Vulnerable Open-source Software Versions Identification based on Static Analysis and LLM.**  In *IEEE Transactions on Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) 
- <span style="color:#337AB7">[**NDSS'2025**]</span> Wang, Yongpan, Hong Li, Xiaojie Zhu, Siyuan Li, **<u>Chaopeng Dong</u>**, Shouguo Yang, Kangyuan Qin.  **BinEnhance: An Enhancement Framework Based on External Environment Semantics for Binary Code Search.**  In *Network and Distributed
System Security (NDSS) Symposium*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/BinEnhance_NDSS_2025.pdf)] [[DOI](https://doi.org/10.14722/ndss.2025.240568 )] [[CODE](https://github.com/wang-yongpan/BinEnhance)]
- <span style="color:#337AB7">[**ICSE'2025**]</span> Siyuan Li, Yuekang Li, Zuxin Chen, **<u>Chaopeng Dong</u>**, Yongpan Wang, Hong Li, Yongle Chen, Hongsong Zhu.  **TransferFuzz: Fuzzing with Historical Trace for Verifying Propagated Vulnerability Code.**  In *IEEE/ACM International Conference on Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/TransferFuzz_ICSE_2025.pdf)] [[DOI](https://doi.org/10.1109/ICSE55347.2025.00061)] [[CODE](https://github.com/Siyuan-Li201/TransferFuzz)]
- <span style="color:#337AB7">[**ICSE'2024**]</span> **<u>Chaopeng Dong</u>**, Siyuan Li, Shouguo Yang, Yang Xiao, Yongpan Wang, Hong Li, Zhi Li, Limin Sun.  **LibvDiff: Library Version Difference Guided OSS Version Identification in Binaries.**  In *IEEE/ACM International Conference on Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/LibvDiff_ICSE_2024.pdf)] [[DOI](https://doi.org/10.1145/3597503.3623336)] [[CODE](https://github.com/GentleCP/LibvDiff-public)]
- <span style="color:#337AB7">[**ToSEM'2023**]</span> Shouguo Yang, **<u>Chaopeng Dong</u>**(co-first author), Yang Xiao, Yiran Cheng, Zhiqiang Shi, Zhi Li and Limin Sun.  **Asteria-Pro: Enhancing Deep Learning-based Binary Code Similarity Detection by Incorporating Domain Knowledge.**  In *ACM Transactions on Software Engineering and Methodology*, 2023. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/Asteria-pro_ToSEM_2023.pdf)] [[DOI](https://doi.org/10.1145/3604611)] [[CODE](https://github.com/Asteria-BCSD/Asteria-Pro)]
- <span style="color:#337AB7">[**ToSEM'2023**]</span> Siyuan Li, Yongpan Wang, **<u>Chaopeng Dong</u>**, Shouguo Yang, Hong Li, Hao Sun, Zhe Lang, Zuxin Chen, Weijie Wang, Hongsong Zhu, Limin Sun.  **LibAM: An Area Matching Framework for Detecting Third-Party Libraries in Binaries.**  In *ACM Transactions on Software Engineering and Methodology*, 2023. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/LibAM_ToSEM_2023.pdf)] [[DOI](https://doi.org/10.1145/3625294)] [[CODE](https://github.com/Siyuan-Li201/LibAM)]
- <span style="color:#337AB7">[**ICPADS'2023**]</span> Yongpan Wang, **<u>Chaopeng Dong</u>**, Siyuan Li, Fucai Luo, Renjie Su, Zhanwei Song, Hong Li.  **FlowEmbed: Binary function embedding model based on relational control flow graph and byte sequence.**  In *ACM Transactions on Software Engineering and Methodology*, 2023. (<span style="color:#FC4E2A">**CCF-C**</span>) [[PDF](pdfs/FlowEmbed_ICPADS_2023.pdf)] [[DOI](https://doi.org/10.1109/icpads60453.2023.00141)]


# 📚 Services
- Reviewer of IEEE Transactions on Software Engineering (TSE)
- Reviewer of Frontiers of Computer Science (FCS)

# 🎖 Honors and Awards
- **2024**: National Scholarship.
- **2022**: 3rd Prize, CCF Big Data & Computing Intelligence Contest
- **2022**: 1st Prize, Datacon 2022 Big Data Security Analysis Competition
- **2021**: 2nd Prize, Datacon 2021 Big Data Security Analysis Competition
- **2018**: Honorable Prize, Mathematical Contest In Modeling 
- **2017, 2018**: 1st Prize, 8th/9th National College Student Mathematics Competition
- **2016, 2018**: National Scholarship


# 📖 Educations
- **2019.09-now**: Institute of Information Engineering, Chinese Academy of Sciences. PhD in Cyber Space Security.
- **2024.03-2025.03**: College of Computing and Data Science, Nanyang Technological University. Visiting Researcher. 
- **2015.09-2019.06**: College of Computer Science, Sichuan University, B.ENG. In Computer Science and Technology.