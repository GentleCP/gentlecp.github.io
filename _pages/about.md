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


I am currently an Associate Professor at the College of Cyberspace Security, Hangzhou Dianzi University (HDU). I received my Ph.D. from the Institute of Information Engineering, Chinese Academy of Sciences, under the supervision of [Prof. Limin Sun](https://scholar.google.com/citations?hl=zh-CN&user=ujYecNkAAAAJ). During my doctoral studies, I also served as a visiting scholar at Nanyang Technological University, working with [Assoc. Prof. Yi Li](https://liyiweb.com/).

My research primarily focuses on software supply chain security, IoT security, program analysis, and the integration of AI in cybersecurity. See my publication list for details. I am actively looking for self-motivated students/collaborators to work with. Please contact me via email if you are interested in my research. 


# 🔥 News
- *2025.12*: 🎉🎉 One paper was accepted by the FSE 2026. Congrats, Jingdong!
- *2025.09*: 🎉🎉 Two papers were accepted by the ASE 2025. One paper was accepted by the ToSEM 2025. Congrats, Siyuan!
- *2025.08*: 🎉🎉 One paper was accepted by the TSE 2025. Congrats, Yiran!

# 📝 Publications 
1. <span style="color:#337AB7">[**FSE'2026**]</span>  Jingdong Guo, **<u>Chaopeng Dong</u>**(co-first author), Yimo Ren, Siyuan Li, Jie Liu, Hong Li, Hongsong Zhu.  **Understanding Binary Code Similarity for Real-World Vulnerability Detection: A Large-Scale Empirical Study.**  In *ACM International Conference on the Foundations of Software Engineering*, 2026. (<span style="color:#FC4E2A">**CCF-A**</span>) 
1.  <span style="color:#337AB7">[**ASE'2025**]</span> **<u>Chaopeng Dong</u>**, Jingdong Guo, Shouguo Yang, Yi Li, Dongliang Fang,
Yang Xiao, Yongle Chen, Limin Sun.  **Advancing Binary Code Similarity Detection via Context-Content Fusion and LLM Verification.**  In *IEEE/ACM International Conference on Automated Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/Co2FuLL_ASE_2025.pdf)] [[CODE](https://github.com/GentleCP/Co2FuLL-public)]
1. <span style="color:#337AB7">[**ASE'2025**]</span> Siyuan Li, Yaowen Zheng, Jingdong Guo, **<u>Chaopeng Dong</u>**, Chunpeng Yan, Weijie Wang, Yimo Ren, Limin Sun, Hongsong Zhu. **Lares: LLM-driven Code Slice Semantic Search for Patch Presence Testing.**  In *IEEE/ACM International Conference on Automated Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) 
1. <span style="color:#337AB7">[**ToSEM'2025**]</span> **<u>Chaopeng Dong</u>**, Jingdong Guo, Shouguo Yang, Yang Xiao, Yi Li, Hong Li, Zhi Li, Limin Sun.  **PLocator: Fine-Grained Patch Presence Test in Binaries via Patch Code Localization.**  In *ACM Transactions on Software Engineering and Methodology*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[DOI](https://doi.org/10.1145/3770079)] [[CODE](https://github.com/GentleCP/PLocator-public)]
1. <span style="color:#337AB7">[**TSE'2025**]</span> Yiran Cheng, Lwin Khin Shar, Ting Zhang, Shouguo Yang, **<u>Chaopeng Dong</u>**, David Lo, Shichao Lv,Zhiqiang Shi, Limin Sun.  **VERCATION: Precise Vulnerable Open-source Software Versions Identification based on Static Analysis and LLM.**  In *IEEE Transactions on Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/VERCATION_TSE_2025.pdf)] [[DOI](https://doi.org/10.1109/tse.2025.3599581)] [[CODE](https://github.com/Veronica-L/Vercation)]
1. <span style="color:#337AB7">[**NDSS'2025**]</span> Wang, Yongpan, Hong Li, Xiaojie Zhu, Siyuan Li, **<u>Chaopeng Dong</u>**, Shouguo Yang, Kangyuan Qin.  **BinEnhance: An Enhancement Framework Based on External Environment Semantics for Binary Code Search.**  In *Network and Distributed
System Security (NDSS) Symposium*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/BinEnhance_NDSS_2025.pdf)] [[DOI](https://doi.org/10.14722/ndss.2025.240568 )] [[CODE](https://github.com/wang-yongpan/BinEnhance)]
1. <span style="color:#337AB7">[**ICSE'2025**]</span> Siyuan Li, Yuekang Li, Zuxin Chen, **<u>Chaopeng Dong</u>**, Yongpan Wang, Hong Li, Yongle Chen, Hongsong Zhu.  **TransferFuzz: Fuzzing with Historical Trace for Verifying Propagated Vulnerability Code.**  In *IEEE/ACM International Conference on Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/TransferFuzz_ICSE_2025.pdf)] [[DOI](https://doi.org/10.1109/ICSE55347.2025.00061)] [[CODE](https://github.com/Siyuan-Li201/TransferFuzz)]
1. <span style="color:#337AB7">[**ICSE'2024**]</span> **<u>Chaopeng Dong</u>**, Siyuan Li, Shouguo Yang, Yang Xiao, Yongpan Wang, Hong Li, Zhi Li, Limin Sun.  **LibvDiff: Library Version Difference Guided OSS Version Identification in Binaries.**  In *IEEE/ACM International Conference on Software Engineering*, 2025. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/LibvDiff_ICSE_2024.pdf)] [[DOI](https://doi.org/10.1145/3597503.3623336)] [[CODE](https://github.com/GentleCP/LibvDiff-public)]
1. <span style="color:#337AB7">[**ToSEM'2023**]</span> Shouguo Yang, **<u>Chaopeng Dong</u>**(co-first author), Yang Xiao, Yiran Cheng, Zhiqiang Shi, Zhi Li and Limin Sun.  **Asteria-Pro: Enhancing Deep Learning-based Binary Code Similarity Detection by Incorporating Domain Knowledge.**  In *ACM Transactions on Software Engineering and Methodology*, 2023. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/Asteria-pro_ToSEM_2023.pdf)] [[DOI](https://doi.org/10.1145/3604611)] [[CODE](https://github.com/Asteria-BCSD/Asteria-Pro)]
1. <span style="color:#337AB7">[**ToSEM'2023**]</span> Siyuan Li, Yongpan Wang, **<u>Chaopeng Dong</u>**, Shouguo Yang, Hong Li, Hao Sun, Zhe Lang, Zuxin Chen, Weijie Wang, Hongsong Zhu, Limin Sun.  **LibAM: An Area Matching Framework for Detecting Third-Party Libraries in Binaries.**  In *ACM Transactions on Software Engineering and Methodology*, 2023. (<span style="color:#FC4E2A">**CCF-A**</span>) [[PDF](pdfs/LibAM_ToSEM_2023.pdf)] [[DOI](https://doi.org/10.1145/3625294)] [[CODE](https://github.com/Siyuan-Li201/LibAM)]
1. <span style="color:#337AB7">[**ICPADS'2023**]</span> Yongpan Wang, **<u>Chaopeng Dong</u>**, Siyuan Li, Fucai Luo, Renjie Su, Zhanwei Song, Hong Li.  **FlowEmbed: Binary function embedding model based on relational control flow graph and byte sequence.**  In *IEEE 29th International Conference on Parallel and Distributed Systems*, 2023. (<span style="color:#FC4E2A">**CCF-C**</span>) [[PDF](pdfs/FlowEmbed_ICPADS_2023.pdf)] [[DOI](https://doi.org/10.1109/icpads60453.2023.00141)]
1. <span style="color:#337AB7">[**MILCOM'2023**]</span> Siyuan Li, **<u>Chaopeng Dong</u>**, Yongpan Wang, Wenming Liu, Weijie Wang, Hong Li, Hongsong Zhu and Limin Sun.  **LibDI: A Direction Identification Framework for Detecting Complex Reuse Relationships in Binaries.**  In *IEEE Military Communications Conference*, 2023. (<span style="color:#FC4E2A">**IIE-B**</span>)



# 📚 Services
- Referee of IEEE Transactions on Software Engineering (TSE)
- Referee of Frontiers of Computer Science (FCS)

# 🎖 Honors and Awards
- **2024/2025**: National Scholarship.
- **2025**: Director's Special Award, Institute of Information Engineering, Chinese Academy of Sciences
- **2023**: Director's Excellence Award, Institute of Information Engineering, CAS.
- **2022**: 3rd Prize, CCF Big Data & Computing Intelligence Contest
- **2022**: 1st Prize, Datacon 2022 Big Data Security Analysis Competition
- **2021**: 2nd Prize, Datacon 2021 Big Data Security Analysis Competition
- **2018**: Honorable Prize, Mathematical Contest In Modeling 
- **2017, 2018**: 1st Prize, 8th/9th National College Student Mathematics Competition
- **2016, 2018**: National Scholarship


# 📖 Educations
- **2019.09-2025.12**: Institute of Information Engineering, Chinese Academy of Sciences. PhD in Cyber Space Security.
- **2024.03-2025.03**: College of Computing and Data Science, Nanyang Technological University. Visiting Scholar. 
- **2015.09-2019.06**: College of Computer Science, Sichuan University, B.ENG. In Computer Science and Technology.