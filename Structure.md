recon-pipeline/
├── input/
│   └── targets.txt                  # Danh sách domains/IP đầu vào
│
├── output/
│   ├── subfinder/                   # Kết quả subdomain
│   │   └── subdomains.txt
│   ├── httpx/                       # Kết quả dò cổng, alive hosts
│   │   └── alive.txt
│   ├── nuclei/                      # Kết quả scan lỗ hổng
│   │   └── nuclei-results.txt
│   └── logs/                        # Log của từng bước trong pipeline
│
├── tool/
│   ├── nuclei                       # nuclei
│   ├── subfinder
|
├── data/
│   ├── data.py                      # data saveing for bot telegram
│   ├── .........                    #
|                    
├── pipelines/
│   ├── run_pipeline.sh              # Bash script tổng hợp
│   ├── steps/
│   │   ├── step1_subfinder.sh       # Bước 1: Subdomain enum
│   │   ├── step2_httpx.sh           # Bước 2: Kiểm tra alive
│   │   ├── step3_nuclei.sh          # Bước 3: Scan lỗ hổng
│   │   └── common.sh                # Các hàm dùng chung
│
├── templates/
│   ├── nuclei/
│   │   ├── nuclei-custom/           # Custom Nuclei templates
│   │   └── nuclei-templates/        # nuclei defaut template
|   └── subfinder                    
|                                      
│
├── config/
│   ├── nuclei 
│   │   ├── nuclei-config.yaml       
│   │   └── pipeline.env             # Biến môi trường pipeline  
│
├── ci/
│   └── github-actions.yaml          # (Tùy chọn) GitHub Actions CI
│
├── reports/
│   └── summary.md                   # Báo cáo kết quả cuối cùng
│
├── README.md                        # Hướng dẫn sử dụng
├── requirements.txt                 # Công cụ cần cài
│   │   ├── step1_subfinder.sh       
│   │   └── step2_httpx.sh
|
└── bot.py                           # Chay bot