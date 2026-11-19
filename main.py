import yfinance as yf, pandas as pd, numpy as np, time, requests, os
from datetime import datetime, timezone, timedelta
from threading import Thread
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Medallion 1500 2-Layer is Live!"
def run_web():
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 10000)))
Thread(target=run_web, daemon=True).start()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": msg}, timeout=15)
    except Exception as e:
        print("Telegram fail:", e)

# ========== 1500 UNIVERSE ==========
BASE = ["NVDA","AMD","CRWV","AVGO","TSM","ASML","AMAT","LRCX","KLAC","MRVL","ARM","SMCI","PLTR","SOUN","AAPL","MSFT","GOOGL","AMZN","META","TSLA","ORCL","ADBE","CRM","NOW","INTU","UBER","ABNB","APP","MSTR","COIN","HOOD","RBLX","DKNG","AFRM","UPST","SOFI","LCID","RIVN","IONQ","QBTS","RGTI","ASTS","JPM","V","MA","BAC","WFC","GS","MS","BLK","C","AXP","HD","LOW","COST","WMT","TGT","NKE","SBUX","MCD","DIS","PEP","KO","PG","JNJ","UNH","PFE","LLY","MRK","ABBV","TMO","XOM","CVX","COP","SLB","CAT","DE","HON","GE","BA","LMT","UNP","FDX","UPS","DAL","UAL","MAR","HLT","BKNG","LIN","SHW","APD","NUE","FCX","NEM","EMR","ETN","PH","ITW","TXN","QCOM","ADI","NXPI","ON","CDNS","SNPS","FTNT","PANW","CRWD","ZS","DDOG","NET","SNOW","MDB","AI","PATH","SHOP","SQ","PYPL","DASH","PINS","SNAP","RDDT","NFLX","IBM","INTC","CSCO","VZ","T","CVS","WBA","KHC","GIS","CL","KMB","MO","PM","RIO","BHP","VALE","GOLD","EWJ","EWZ","EEM","FXI","SPY","QQQ","IWM","DIA","VOO","ARKK","SMH","SOXX","XLF","XLE","XLV","XLK","GLD","SLV","USO","TLT","BABA","JD","PDD","BIDU","NIO","LI","XPEV","SE","GRAB","MELI","NU","NVO","OXY","EOG","MPC","PSX","VLO","HAL","BKR","APA","DVN","FANG","EQT","CTRA","MRO","CHTR","CMCSA","WBD","PARA","FOX","NWSA","LUMN","BBY","GME","AMC","BB","NOK","ERIC","SIRI","CROX","UAA","LULU","DECK","SKX","EL","ULTA","DG","DLTR","KR","ACI","SFM","TSCO","RH","WSM","TPX","LEG","WHR","NVR","LEN","DHI","PHM","KBH","BZH","TOL","MTCH","BMBL","GRND","WYNN","LVS","MGM"]

# AI / GPU / GPU LOANERS - like CoreWeave
GPU_LOAN = ["NBIS","IREN","CIFR","WULF","APLD","HUT","BTDR","CORZ","CLSK","MARA","RIOT","CLS","DELL","ANET","MU","WDC","STX","SNDK","CRDO","ALAB","RKLB","GRRR","BBAI","VRNS","TEM","AIP","GFS","ARM","INOD","SOUN","BBAI","UPST","ONDS","LUNR","SERV","RR","AEVA","LIDR","INVZ","QS","SLDP","MVST","SES","AMPX","EOSE","FLNC","STEM","CHPT","BLNK","EVGO","RIVN","LCID","GOEV","FFIE","NKLA","ARQQ","QBTS","IONQ","RGTI","QUBT","ARBE","INDI","LSCC","MPWR","DIOD","SLAB","RMBS","HIMX","SGH","SMCI","POWI","ACLS","MKSI","ENTG","ICHR","FORM","COHU","KLIC","PLAB","UCTT","CCMP","ROG","CTSH","EPAM","GLOB","PSN","EXLS","DAVA","TWLO","FROG","GTLB","ESTC","SUMO","S","PSTG","WDAY","DOCU","ZM","PTON","SPOT","BILL","TOST","FOUR","MQ","NCNO","EVTC","SSNC","BRZE","CXM","HUBS","ZEN","FIVN","MRCY","AVAV","KTOS","RCAT","UMAC","LHX","NOC","GD","RTX","HII","CW","TDG","SPR","MOGA"]

# MEDICAL / BIOTECH
MED = ["AMGN","GILD","VRTX","REGN","BIIB","MRNA","BNTX","ISRG","DXCM","ABT","MDT","SYK","BSX","EW","ZTS","HUM","ELV","CI","HCA","UHS","DVA","MCK","CAH","COR","ARGX","ALNY","SMMT","UTHR","INSM","EXEL","NBIX","HALO","TARS","BBIO","KRYS","RYTM","TGTX","IONS","SRPT","CRSP","NTLA","BEAM","EDIT","VKTX","ALT","MDGL","MIRM","XENE","PCVX","IMVT","ROIV","ACAD","BHVN","AXSM","SAGE","KRTX","NRBO","MGNX","FATE","DTIL","BLUE","VYGR","RGNX","QURE","FDMT","RCKT","SLDB","PRTA","DNLI","ANNX","ARWR","CERE","CYTK","FOLD","IMCR","MRSN","ORIC","RAIN","RLAY","RVMD","SWTX","TNGX","ZLAB","IMAB","LEGN","ADAG","ANAB","APLS","ARQT","AVTE","BCYC","CGON","COGT","DAWN","EWTX","FGEN","GLUE","HOOD","IDYA","JANX","KOD","KYMR","LQDA","MREO","NRIX","OLMA","ORGO","PGEN","PRLD","REPL","RPTX","SANA","SDGR","SNDX","STRO","TCRT","TVTX","URGN","VCYT","VINC","VOR","XLO","YMAB","ZNTL","HRMY","CORT","SUPN","TGTX","ENTA","NUVL","TIL","PYXS","AURA","TARA","VRNA","WVE","XFOR","ABCL","ADMA","AKRO","ALGS","ANIP","ARVN","AVXL","BCRX","BMEA","BYSI","CBAY","CSTL","CVM","EBS","ECOR","EOLS","EPRX","EVAX","FBRX","FENC","FHTX","FUSN","GMTX","GOSS","HROW","ICVX","IMNM","INVA","IOVA","ISEE","ITCI","ITRM","KALV","KPTI","KURA","LGVN","LQDA","LVTX","MICS","MIST","MRUS","NARI","NBY","NKTX","NMRA","NRBO","OCUL","OMER","OPCH","OPT","ORMP","OTIC","PAVM","PDSB","PFGC","PHAT","PHVS","PLRX","PMVP","PRAX","PRME","PSTX","PTGX","QTRX","RCKT","RGC","RIGL","RMTI","RPTX","RXDX","SAVA","SCLX","SGMT","SHPH","SIGA","SLNO","SNCE","SRDX","STAA","STOK","TALS","TARS","TBPH","TCRX","TGTX","TIL","TNXP","TRDA","TRML","TTNP","TVTX","TYRA","UBX","VAPO","VCNX","VIGL","VIR","VRCA","VRNA","VRTX","VTYX","VYNE","XCUR","XERS","XNCR","XOMA","YMAB","ZIMV","ZYME"]

# CLOTHING / BRANDS / CONSUMER
CLOTH = ["ADDYY","PUMSY","LEVI","RL","PVH","TPR","CPRI","BIRK","ONON","WWW","SHOO","FL","DKS","ANF","URBN","AEO","GPS","JWN","M","KSS","DDS","BURL","ROST","TJX","COTY","CHWY","REAL","FIGS","COLM","GIL","VFC","HBI","CRI","OXM","GIII","CAL","PETS","GME","BBW","PLCE","EXPR","CHICO","JILL","CURV","SCVL","DSW","DBI","GES","KTB","UA","COLM","SKX","CROX","DECK","LULU","NKE","LULU","BURL","BOOT","SHOO","ACVA","ARHS","AS","BBW","CAL","CATO","CTRN","DBI","DLTH","DRVN","DXLG","FOSL","FRG","GOOS","HIBB","JWN","KSS","LE","LULU","MOV","NWL","ODP","OSK","OXM","PLCE","PRTY","RGS","RVLV","SFIX","SHOO","SIG","SIX","SKX","SMRT","SPWH","TBL","TPR","UAA","URBN","VRA","VSCO","WEYS","WWW","ZUMZ","BKE","AEO","ANF","GPS","LEVI","RL","PVH","CPRI","TPR","BIRK","ONON","DECK","CROX","SKX","CROX","FL","DKS","BOOT","CAL","WWW","SHOO","COLM","GIL","VFC","HBI","PVH","RL","TPR","CPRI","LEVI","BIRK","ONON","REAL","FIGS","EL","ULTA","COTY","ELF","IPAR","ODD","NUS","USNA","MED","PRKS","SIX","FUN","SEAS","LYV","MSGS","EDR","TKO","WWE","BATRK","FWONA","LIBY","BATRA","LSXMA","LSXMK","GRND","DKNG","PENN","CZR","MGM","WYNN","LVS","BYD","MLCO","SGMS","IGT","AGS","BALLY","CHDN","RRR","GAMB","SLQT","EVO","SEAS","CARN","RCL","NCLH","CCL","TRIP","EXPE","BKNG","ABNB","MAR","HLT","H","WH","CHH","IHG","VAC","TNL","HGV","PLYA","MCRI","CSGS","GDEN","FTCI"]

EXTRA = ["A","AAL","AAT","ABBV","ABCB","ABCL","ABEO","ABEV","ABG","ABIO","ABM","ABNB","ABOS","ABR","ABSI","ABST","ABT","ABUS","AC","ACA","ACAD","ACB","ACBI","ACCD","ACCO","ACDC","ACEL","ACET","ACGL","ACHC","ACHR","ACHV","ACI","ACIC","ACIU","ACIW","ACLS","ACM","ACMR","ACN","ACNB","ACNT","ACOG","ACOR","ACP","ACRE","ACRS","ACRV","ACT","ACU","ACV","ACVA","ACY","ADAP","ADBE","ADC","ADCT","ADD","ADEA","ADI","ADIL","ADM","ADMA","ADN","ADNT","ADP","ADPT","ADS","ADSK","ADTH","ADTN","ADUS","ADV","ADVM","ADX","AE","AEE","AEG","AEHL","AEI","AEL","AEM","AEO","AEP","AER","AES","AEY","AFBI","AFG","AFIB","AFIN","AFL","AFMD","AFRM","AFYA","AG","AGBA","AGCO","AGE","AGEN","AGFS","AGI","AGIO","AGL","AGM","AGMH","AGNC","AGO","AGR","AGRO","AGS","AGT","AGX","AGYS","AHCO","AHH","AHMA","AHP","AHPI","AHR","AHT","AI","AIF","AIG","AIM","AIN","AINC","AIR","AIRC","AIRS","AIT","AIU","AIV","AIZ","AJG","AJX","AJXA","AKA","AKAM","AKBA","AKLI","AKO","AKR","AKRO","AKTS","AKTX","AKYA","AL","ALB","ALBT","ALC","ALCO","ALCY","ALDX","ALE","ALEC","ALEX","ALG","ALGM","ALGN","ALGS","ALGT","ALHC","ALIM","ALIT","ALK","ALKS","ALL","ALLE","ALLK","ALLO","ALLT","ALLY","ALNT","ALNY","ALOT","ALPN","ALRM","ALRS","ALSA","ALSN","ALT","ALTG","ALTM","ALTO","ALTR","ALVO","ALV","ALVR","ALX","ALXO","ALYA","AM","AMAL","AMAT","AMBC","AMBI","AMBO","AMC","AMCR","AMD","AME","AMED","AMG","AMGN","AMH","AMK","AMKR","AMLI","AMN","AMNB","AMOT","AMP","AMPE","AMPG","AMPH","AMPS","AMPX","AMPY","AMR","AMRC","AMRK","AMRN","AMRS","AMRX","AMS","AMSC","AMSF","AMST","AMSWA","AMT","AMTB","AMTI","AMTX","AMWD","AMZN","AN","ANAB","ANDE","ANEB","ANET","ANF","ANGH","ANGI","ANGN","ANGO","ANIK","ANIP","ANIX","ANNX","ANSS","ANTM","ANVS","ANY","AOD","AOGN","AON","AORT","AOS","AOSL","AP","APA","APAM","APD","APDN","APEI","APG","APH","API","APLD","APLE","APLS","APLT","APM","APO","APOG","APP","APPF","APPH","APPN","APPS","APRN","APT","APTO","APTV","APVO","APYX","AQB","AQMS","AQN","AQST","AQUA","AR","ARAV","ARAY","ARBE","ARC","ARCB","ARCC","ARCH","ARCO","ARCT","ARD","ARDC","ARDX","ARE","ARES","ARGX","ARHS","ARI","ARKO","ARKR","ARL","ARLO","ARLP","ARM","ARMP","ARNC","AROC","AROW","ARQ","ARQQ","ARQT","ARR","ARRY","ART","ARTL","ARTNA","ARVN","ARWR","ASA","ASAI","ASAN","ASAQ","ASB","ASC","ASGN","ASH","ASIX","ASLE","ASMB","ASML","ASND","ASO","ASPC","ASPI","ASPN","ASPS","ASRT","ASRV","AST","ASTC","ASTE","ASTL","ASTR","ASTS","ASUR","ASX","ASYS","ATAI","ATAT","ATC","ATCO","ATCOL","ATCX","ATEC","ATEN","ATHA","ATHE","ATHM","ATI","ATIP","ATKR","ATLC","ATLO","ATLX","ATMC","ATMV","ATNI","ATNM","ATNX","ATO","ATOM","ATOS","ATR","ATRA","ATRC","ATRI","ATRO","ATSG","ATTO","ATUS","ATVI","ATXI","ATXS","ATY","AUB","AUBN","AUD","AUDC","AUPH","AUR","AURA","AUS","AUTL","AUTO","AVA","AVAH","AVAL","AVAV","AVB","AVD","AVDL","AVEO","AVGO","AVGR","AVID","AVIR","AVK","AVLR","AVNS","AVNT","AVNW","AVO","AVPT","AVRO","AVT","AVTE","AVTR","AVXL","AVY","AWF","AWI","AWK","AWP","AWR","AX","AXDX","AXGN","AXL","AXNX","AXON","AXP","AXR","AXS","AXSM","AXTA","AXTI","AXU","AY","AYI","AYRO","AYTU","AZEK","AZN","AZO","AZPN","AZRE","AZTA","AZUL","AZYO","B","BA","BABA","BAC","BACA","BAH","BAK","BALY","BAM","BANC","BAND","BANF","BANR","BAP","BARK","BASE","BATL","BATRK","BAX","BB","BBAR","BBBY","BBCP","BBD","BBDC","BBGI","BBIG","BBIO","BBL","BBN","BBSI","BBU","BBVA","BBW","BBWI","BBY","BC","BCAB","BCBP","BCC","BCDA","BCE","BCEL","BCLI","BCML","BCO","BCOV","BCOW","BCPC","BCRX","BCS","BCSF","BCTX","BCYC","BDC","BDJ","BDL","BDN","BDSX","BDTX","BDX","BE","BEAM","BEAT","BECN","BEEM","BEKE","BEL","BEN","BEP","BEPC","BERY","BEST","BFAM","BFC","BFH","BFLY","BFS","BFST","BG","BGFV","BGI","BGL","BGNE","BGR","BGS","BGSF","BH","BHB","BHC","BHE","BHF","BHIL","BHLB","BHM","BHR","BHVN","BIAF","BIDU","BIG","BIGC","BIIB","BILI","BILL","BIMI","BIO","BIOC","BIOL","BIOT","BIP","BIPC","BIT","BITE","BJ","BK","BKCC","BKD","BKE","BKH","BKI","BKNG","BKR","BKSC","BKT","BKTI","BKU","BKUT","BL","BLBD","BLBX","BLCM","BLCO","BLCT","BLD","BLDE","BLDP","BLDR","BLE","BLFS","BLI","BLIN","BLK","BLKB","BLL","BLMN","BLND","BLNK","BLPH","BLRX","BLU","BLUE","BLX","BLZE","BMA","BMBL","BMEA","BMI","BMO","BMR","BMRC","BMRN","BMY","BN","BNED","BNFT","BNGO","BNL","BNR","BNS","BNTX","BNY","BOE","BOH","BOKF","BOLT","BOMN","BOOM","BOOT","BORR","BOSC","BOTJ","BOWX","BOX","BOXL","BP","BPMC","BPOP","BPRN","BPTH","BPTX","BR","BRBR","BRC","BRCC","BRDG","BRDS","BREA","BRFH","BRFS","BRG","BRID","BRK","BRKL","BRLI","BRMK","BRN","BRO","BROG","BRP","BRS","BRSP","BRT","BRX","BRY","BSAC","BSAQ","BSBR","BSET","BSGM","BSIG","BSM","BSRR","BST","BSTZ","BSVN","BSX","BSY","BTA","BTAI","BTAQ","BTB","BTBT","BTCM","BTDR","BTE","BTG","BTI","BTN","BTO","BTRS","BTTR","BTU","BTWN","BTX","BTZ","BUD","BUFR","BURL","BUSE","BVS","BV","BWA","BWAY","BWB","BWEN","BWFG","BWG","BWMX","BWN","BXC","BXMT","BXMX","BXP","BXRX","BY","BYD","BYFC","BYND","BYSI","BZH","C","CAAP","CABA","CAC","CACC","CACG","CACT","CADE","CAE","CAF","CAG","CAH","CAI","CAJ","CAKE","CAL","CALB","CALM","CALT","CALX","CAMT","CAN","CANG","CANQ","CAPL","CAPR","CAPT","CAR","CARA","CARE","CARG","CARR","CARS","CART","CAS","CASA","CASH","CASI","CASS","CASY","CAT","CATO","CATY","CB","CBA","CBAN","CBAT","CBAY","CBD","CBFV","CBIO","CBL","CBLI","CBNK","CBOE","CBRE","CBRL","CBSH","CBT","CBU","CBZ","CC","CCA","CCB","CCBG","CCC","CCCS","CCD","CCEL","CCEP","CCF","CCI","CCJ","CCK","CCL","CCLP","CCM","CCNE","CCO","CCOI","CCRN","CCS","CCSI","CCU","CCXI","CDAK","CDE","CDK","CDLX","CDMO","CDNA","CDNS","CDR","CDTX","CDW","CDXC","CDXS","CDZI","CE","CEA","CECE","CEG","CEI","CELC","CELH","CELP","CELU","CEM","CENX","CEPU","CEQP","CERE","CERN","CERS","CET","CETX","CEVA","CEV","CF","CFB","CFFI","CFFN","CFR","CFRX","CFX","CG","CGA","CGAU","CGBD","CGC","CGEM","CGEN","CGNT","CGNX","CGO","CGON","CHCO","CHCT","CHD","CHE","CHEF","CHGG","CHH","CHI","CHK","CHKP","CHMG","CHMI","CHN","CHPT","CHRS","CHRW","CHS","CHT","CHTR","CHWY","CHX","CI","CIA","CIB","CIDM","CIEN","CIFR","CIG","CIGI","CII","CIK","CIM","CINF","CING","CIO","CIR","CISN","CIVB","CIVI","CIX","CIZN","CJJD","CKPT","CKX","CL","CLAR","CLB","CLBK","CLBR","CLBT","CLDT","CLDX","CLEU","CLF","CLFD","CLGN","CLH","CLIN","CLIR","CLLS","CLMT","CLNE","CLNN","CLOV","CLPR","CLPS","CLR","CLRB","CLRO","CLS","CLSD","CLSK","CLST","CLVR","CLVS","CLW","CLWT","CLX","CM","CMA","CMC","CMCSA","CMCO","CMCT","CME","CMG","CMI","CMMB","CMP","CMPO","CMPR","CMPS","CMRE","CMS","CMT","CMTG","CMTL","CNA","CNCE","CND","CNDT","CNET","CNF","CNHI","CNI","CNK","CNM","CNMD","CNNE","CNO","CNOB","CNP","CNQ","CNS","CNSL","CNSP","CNTA","CNTB","CNTG","CNTQ","CNX","CNXC","CNXN","CNXT","CO","COCO","CODA","CODI","CODX","COE","COF","COFS","COGT","COHN","COHR","COHU","COIN","COKE","COLB","COLD","COLL","COLM","COM","COMM","COMP","CON","CONE","CONN","CONX","COO","COOK","COOP","COP","COR","CORT","CORZ","COSM","COST","COTY","COUP","COUR","COVA","COWN","CP","CPA","CPAA","CPAC","CPE","CPF","CPG","CPHC","CPHI","CPIX","CPK","CPLP","CPNG","CPRT","CPRX","CPS","CPSH","CPSI","CPSS","CPT","CPTK","CR","CRAI","CRBP","CRC","CRCT","CRD","CRDA","CRDF","CRDL","CRDO","CREE","CREG","CRESY","CREX","CRF","CRGE","CRGY","CRH","CRI","CRIS","CRK","CRL","CRM","CRMD","CRMT","CRNC","CRNT","CRON","CROX","CRS","CRSP","CRSR","CRTO","CRUS","CRVL","CRVS","CRWD","CRWS","CRXT","CRY","CRZN","CS","CSA","CSAN","CSBR","CSCO","CSGP","CSGS","CSIQ","CSL","CSLT","CSPR","CSQ","CSR","CSSE","CSTA","CSTE","CSTL","CSTM","CSTR","CSV","CSWI","CSX","CTAS","CTBI","CTGO","CTHR","CTIB","CTIC","CTKB","CTLP","CTLT","CTMX","CTO","CTOS","CTRA","CTRE","CTRM","CTRN","CTSH","CTSO","CTVA","CTXR","CTXS","CUBB","CUBI","CUE","CUEN","CUK","CULP","CUO","CURV","CUTR","CUZ","CVAC","CVBF","CVCO","CVE","CVEO","CVET","CVGI","CVGW","CVI","CVLG","CVLT","CVLY","CVM","CVNA","CVR","CVRX","CVS","CVT","CVU","CVV","CW","CWB","CWBC","CWBR","CWCO","CWEB","CWEN","CWH","CWK","CWST","CWT","CX","CXDO","CXM","CXO","CXP","CXW","CYAN","CYBR","CYCC","CYD","CYH","CYRX","CYT","CYTH","CYTK","CYTO","CYXT","CZNC","CZR","CZWI","D","DAC","DADA","DAIO","DAKT","DAL","DAN","DAO","DAR","DARE","DASH","DATR","DAVA","DAWN","DB","DBD","DBI","DBRG","DBTX","DBVT","DBX","DC","DCBO","DCI","DCO","DCP","DCPH","DCRD","DCT","DCTH","DD","DDD","DDOG","DDS","DDT","DE","DEA","DECK","DEI","DELL","DEN","DENN","DEO","DESP","DEX","DFH","DFIN","DFP","DFS","DG","DGICA","DGII","DGLY","DGX","DHI","DHIL","DHR","DHT","DHX","DIBS","DICE","DIDI","DILA","DIN","DINO","DIOD","DIS","DISA","DISCA","DISCB","DISH","DIT","DJCO","DK","DKD","DKNG","DKS","DLB","DLHC","DLNG","DLR","DLTH","DLTR","DLX","DLY","DM","DMAC","DMLP","DMRC","DNAB","DNAC","DNAY","DNB","DNLI","DNMR","DNN","DNOW","DNP","DNUT","DOC","DOCN","DOCS","DOCU","DOMA","DOMO","DOOO","DOOR","DORM","DOUG","DOV","DOW","DOX","DOYU","DPG","DPHC","DPST","DPZ","DQ","DR","DRAD","DRCT","DRD","DRH","DRI","DRIO","DRMA","DRNA","DRQ","DRRX","DRTT","DRVN","DS","DSAC","DSEY","DSGN","DSGX","DSKX","DSL","DSLV","DSPG","DSS","DSWL","DSX","DT","DTC","DTE","DTEA","DTIL","DTM","DTOC","DTSS","DTST","DTW","DUK","DUNE","DUO","DUOL","DV","DVA","DVAX","DVD","DVN","DWIN","DWSN","DX","DXC","DXCM","DXF","DXLG","DXPE","DXR","DXYN","DY","DYAI","DYN","DYNT","DZSI","E","EAF","EARN","EAST","EAT","EB","EBAY","EBF","EBIX","EBMT","EBON","EBR","EBS","EBTC","EC","ECC","ECL","ECLN","ECOL","ECOM","ECOR","ECPG","ECVT","ECX","ED","EDAP","EDBL","EDIT","EDR","EDRY","EDTK","EDU","EDUC","EE","EEFT","EEX","EF","EFC","EFSC","EFT","EFX","EGAN","EGBN","EGHT","EGLE","EGLX","EGO","EGP","EGRX","EGY","EH","EHC","EHT","EIG","EIGR","EIX","EJL","EL","ELAN","ELBM","ELC","ELF","ELI","ELLI","ELMD","ELOX","ELP","ELS","ELSE","ELTK","ELV","ELVT","ELY","EM","EMAN","EMBC","EME","EMKR","EML","EMN","EMR","EMX","ENB","ENDP","ENE","ENFN","ENG","ENIC","ENJ","ENLC","ENLV","ENOB","ENOV","ENPH","ENR","ENS","ENSG","ENSV","ENTA","ENTG","ENTX","ENV","ENVA","ENVB","ENVX","ENZ","EOC","EOG","EOLS","EOT","EPAC","EPAM","EPAY","EPC","EPD","EPIX","EPM","EPOW","EPR","EPRT","EPSN","EPZM","EQ","EQBK","EQC","EQH","EQHA","EQIX","EQL","EQNR","EQR","EQS","EQX","ERAS","ERES","ERF","ERH","ERIC","ERIE","ERJ","ERNA","ERO","ERYP","ES","ESAB","ESBK","ESCA","ESE","ESEA","ESGR","ESI","ESLT","ESM","ESMT","ESNT","ESOA","ESP","ESPR","ESQ","ESRT","ESS","ESSA","ESTA","ESTC","ESTE","ET","ETAC","ETD","ETN","ETNB","ETON","ETR","ETRN","ETSY","ETTX","ETV","ETY","EURN","EVA","EVAX","EVBG","EVBN","EVC","EVCM","EVE","EVER","EVEX","EVGN","EVGO","EVH","EVI","EVK","EVLO","EVLV","EVO","EVOK","EVOP","EVR","EVRG","EVRI","EVTC","EVTL","EVTV","EW","EWBC","EWCZ","EWI","EWJ","EWK","EWP","EWT","EWU","EWW","EWY","EWZ","EXAS","EXC","EXEL","EXFY","EXK","EXLS","EXN","EXP","EXPD","EXPE","EXPI","EXPO","EXPR","EXR","EXTR","EYE","EYEN","EYPT","EZGO","EZPW","F","FA","FAB","FACA","FAF","FAMI","FANG","FANH","FARM","FARO","FAST","FAT","FATBB","FATE","FB","FBC","FBIN","FBIO","FBIZ","FBK","FBMS","FBNC","FBP","FBRT","FBRX","FC","FCAP","FCBC","FCCO","FCEL","FCF","FCFS","FCLD","FCN","FCNCA","FCRD","FCX","FDBC","FDMT","FDP","FDS","FDUS","FDX","FE","FEDU","FEIM","FELE","FEMY","FENC","FENG","FEO","FERG","FET","FF","FFBC","FFIC","FFIE","FFIN","FFIV","FFNW","FG","FGBI","FGEN","FGF","FGI","FGNA","FHB","FHI","FHN","FHS","FHTX","FIBK","FICO","FIF","FIGS","FINM","FINV","FINW","FIS","FISI","FISK","FITB","FIVE","FIVN","FIX","FIXX","FIZZ","FKWL","FL","FLDM","FLEX","FLGC","FLGT","FLIC","FLL","FLME","FLNC","FLNG","FLNT","FLO","FLOW","FLR","FLS","FLT","FLUX","FLWS","FLXS","FLYA","FLYW","FM","FMAO","FMBH","FMBI","FMC","FMED","FMNB","FMS","FMTX","FMX","FN","FNA","FNAC","FNB","FNCH","FND","FNF","FNGN","FNHC","FNK","FNKO","FNLC","FNV","FOA","FOCS","FOE","FOLD","FONR","FOR","FORD","FORG","FORM","FORR","FORTY","FOSL","FOUR","FOX","FOXA","FOXF","FPA","FPAY","FPI","FPL","FR","FRA","FRAF","FRBA","FRBK","FRC","FRD","FREE","FREQ","FRG","FRGI","FRGT","FRHC","FRLN","FRME","FRO","FROG","FRON","FRPH","FRPT","FRSG","FRSH","FRST","FRSX","FRT","FRTA","FRW","FRXB","FSBC","FSBW","FSEA","FSFG","FSI","FSK","FSLR","FSLY","FSM","FSNB","FSP","FSR","FSRX","FSS","FSTR","FSTX","FT","FTAI","FTCI","FTCS","FTDR","FTEK","FTFT","FTHM","FTI","FTK","FTNT","FTOC","FTRP","FTS","FTV","FTVI","FUBO","FUL","FULC","FUN","FUND","FURY","FUSB","FUSN","FUTU","FUV","FVIV","FVL","FWONA","FWONK","FWRD","FXNC","FYBR","FZT","G","GAB","GABC","GAIA","GAIN","GALT","GAMB","GAMR","GAN","GASS","GATE","GB","GBCI","GBDC","GBIO","GBL","GBLI","GBR","GBS","GBT","GCBC","GCI","GCMG","GCO","GCV","GD","GDDY","GDEN","GDEV","GDOT","GDRX","GDS","GDYN","GE","GECC","GEF","GEG","GEL","GENC","GENE","GENI","GEO","GEOS","GERN","GES","GETR","GETY","GEVO","GFAI","GFF","GFI","GFL","GFS","GGAL","GGB","GGG","GGR","GH","GHC","GHG","GHL","GHLD","GHSI","GIB","GIC","GIFI","GIII","GIL","GILD","GILT","GIM","GIS","GIVN","GJH","GJO","GJP","GJR","GJS","GJT","GKOS","GL","GLAD","GLBE","GLBS","GLBZ","GLD","GLDD","GLDG","GLEE","GLG","GLHA","GLL","GLLI","GLMD","GLNG","GLOB","GLOP","GLP","GLPG","GLPI","GLRE","GLSI","GLS","GLT","GLTA","GLTO","GLU","GLUE","GLV","GLW","GLYC","GM","GME","GMED","GMRE","GMS","GNE","GNK","GNL","GNOG","GNPX","GNRC","GNSS","GNTX","GNTY","GNW","GO","GOAC","GODN","GOED","GOEV","GOGL","GOGO","GOLD","GOLF","GOOD","GOOG","GOOGL","GOOS","GORO","GOTU","GOVX","GP","GPC","GPCO","GPI","GPK","GPL","GPM","GPMT","GPN","GPOR","GPRK","GPS","GPX","GRA","GRAB","GRBK","GRC","GRCL","GREE","GRFS","GRIL","GRIN","GRMN","GRN","GRND","GRNQ","GROM","GROW","GRP","GRPN","GRRR","GRTS","GRTX","GRVY","GRWG","GS","GSAT","GSBC","GSBD","GSHD","GSIT","GSK","GSL","GSM","GSQB","GSS","GSUN","GT","GTBP","GTE","GTEC","GTES","GTHX","GTIM","GTLB","GTLS","GTN","GTPB","GTS","GTX","GTY","GURE","GVA","GVP","GWH","GWRE","GWSN","GWTR","GXO","GYRE","H","HA","HAAC","HAE","HAFC","HAIN","HAL","HALL","HALO","HAPP","HAR","HAS","HASI","HAYN","HBAN","HBB","HBI","HBIO","HBNC","HBP","HBT","HCAT","HCC","HCCI","HCDI","HCKT","HCM","HCN","HCO","HCP","HCSG","HCTI","HCVI","HDB","HD","HDB","HDSN","HE","HEAR","HEES","HEI","HELE","HELX","HEP","HEPA","HERD","HES","HESM","HEXO","HFBL","HFFG","HFWA","HGBL","HGEN","HGLB","HGTY","HGV","HHC","HHH","HHS","HI","HIBB","HIFS","HIG","HIGR","HII","HIII","HIL","HIMS","HIMX","HIPO","HIQ","HIVE","HIW","HKD","HL","HLBZ","HLF","HLIO","HLIT","HLLY","HLMN","HLNE","HLT","HLTH","HLVX","HLX","HMC","HMLP","HMN","HMNF","HMPT","HMST","HMTV","HMY","HNGE","HNI","HNNA","HNRA","HNRG","HNSN","HNST","HOFT","HOFV","HOG","HOLX","HOMB","HOME","HON","HONE","HOOD","HOOK","HOPE","HOTH","HOV","HOWL","HP","HPE","HPK","HPP","HPQ","HPS","HQI","HQY","HR","HRB","HRC","HRI","HRL","HROW","HRT","HRTG","HRTX","HRZN","HSAQ","HSBC","HSC","HSDT","HSIC","HSII","HSKA","HSON","HST","HSTM","HSY","HT","HTA","HTBI","HTBK","HTCR","HTGC","HTH","HTHT","HTLD","HTOO","HTPA","HTZ","HUBB","HUBG","HUBS","HUDI","HUGE","HUIZ","HUM","HUMA","HUN","HURC","HURN","HUSA","HUSN","HUT","HUYA","HVBC","HVT","HWBK","HWCP","HWEL","HWKN","HX","HY","HYAC","HYFM","HYI","HYMC","HYPR","HYRE","HYZN","HZN","HZNP"]

NGX = ["DANGCEM.LG","MTNN.LG","GTCO.LG","ZENITHBANK.LG","UBA.LG","ACCESSCORP.LG","BUACEMENT.LG","BUAFOODS.LG","SEPLAT.LG","ARADEL.LG","FBNH.LG","STANBIC.LG","DANGSUGAR.LG","NASCON.LG","NESTLE.LG","UNILEVER.LG","CADBURY.LG","NB.LG","GUINNESS.LG","INTBREW.LG","PRESCO.LG","OKOMUOIL.LG","FIDELITYBK.LG","STERLINGNG.LG","WEMABANK.LG","JAIZBANK.LG","TRANSCORP.LG","TRANSPOWER.LG","AIRTELAFRI.LG","FLOURMILL.LG","HONYFLOUR.LG","VITAFOAM.LG","BERGER.LG","JULIUS.LG","CUTIX.LG","ETERNA.LG","TOTAL.LG","CONOIL.LG","MRS.LG","ARDOVA.LG","OANDO.LG","LIVESTOCK.LG","AIICO.LG","CUSTODIAN.LG","MANSARD.LG","CHAMS.LG","CWG.LG","AFRIPRUD.LG","UCAP.LG","FCMB.LG","UNITYBNK.LG"]

ALL_TICKERS = list(dict.fromkeys(BASE+GPU_LOAN+MED+CLOTH+EXTRA+NGX))
print(f"Universe: {len(ALL_TICKERS)} tickers")
US_TICKERS = [t for t in ALL_TICKERS if ".LG" not in t]

LEDGER = "signals.csv"
HORIZON_MIN = 240
COOLDOWN_MIN = 60
TOP_N = 5

def calc_rsi(close, period=14):
    d = close.diff()
    gain = d.clip(lower=0).ewm(alpha=1/period, adjust=False).mean()
    loss = (-d.clip(upper=0)).ewm(alpha=1/period, adjust=False).mean()
    return 100 - 100/(1 + gain/loss)

def load_ledger():
    cols = ["t", "signal_time", "entry", "exit", "ret_pct", "closed"]
    if os.path.exists(LEDGER):
        try:
            df = pd.read_csv(LEDGER)
            return df
        except:
            pass
    return pd.DataFrame(columns=cols)

def save_ledger(df):
    try:
        df.to_csv(LEDGER, index=False)
    except Exception as e:
        print("Ledger fail:", e)

def get_market_regime():
    try:
        spy = yf.download("SPY", period="5d", interval="1d", progress=False, auto_adjust=True)['Close']
        if hasattr(spy, 'columns'):
            spy = spy.iloc[:,0]
        spy_pct = float((spy.iloc[-1]-spy.iloc[-2])/spy.iloc[-2]*100)
        if spy_pct > 0.5: return "BULLISH 🟢", spy_pct
        elif spy_pct < -0.5: return "BEARISH 🔴", spy_pct
        else: return "NEUTRAL 🟡", spy_pct
    except:
        return "NEUTRAL 🟡", 0

def ai_score(rsi, vs_sma, residual, vr, regime):
    score = 50
    reasons = []
    if residual < -4: score += 25; reasons.append("Huge dislocation")
    elif residual < -2.5: score += 18; reasons.append("Strong dislocation")
    elif residual < -1.5: score += 10; reasons.append("Dislocation")
    if rsi < 20: score += 15; reasons.append("Extremely oversold")
    elif rsi < 30: score += 10; reasons.append("Oversold")
    elif rsi < 35: score += 5
    if vs_sma < -12: score += 10; reasons.append("Deep discount")
    elif vs_sma < -8: score += 6
    if vr > 2: score += 8; reasons.append("Panic vol 2x")
    elif vr > 1.5: score += 5
    elif vr < 0.7: score -= 8; reasons.append("Low vol")
    if "BEARISH" in regime: score -= 12; reasons.append("Market bearish")
    elif "BULLISH" in regime: score += 5
    return max(0, min(100, score)), ", ".join(reasons)

# ===== LAYER 1 + LAYER 2 =====
last_alerted = {}
open_signals = []

def scan_once():
    global open_signals
    now = datetime.now(timezone.utc)
    ledger = load_ledger()
    regime, regime_pct = get_market_regime()
    print("Layer 1: scanning 1500 daily...")
    suspects = []
    for i in range(0, len(US_TICKERS), 200):
        chunk = US_TICKERS[i:i+200]
        try:
            df = yf.download(chunk, period="3mo", interval="1d", progress=False, group_by='ticker', threads=True, auto_adjust=True)
        except:
            continue
        for t in chunk:
            try:
                h = df[t] if len(chunk)>1 else df
                close = h['Close'].dropna()
                if len(close) < 40: continue
                r = float(calc_rsi(close).iloc[-1])
                sma20 = float(close.rolling(20).mean().iloc[-1])
                vs = (float(close.iloc[-1]) - sma20)/sma20*100
                if r < 38 and vs < -6:
                    suspects.append(t)
            except:
                continue
    print(f"Layer 1 suspects: {len(suspects)} -> {suspects[:20]}")
    suspects = suspects[:40]
    if not suspects:
        send_telegram(f"🤖 MEDALLION 1500 2-LAYER\nMarket: {regime} ({regime_pct:+.2f}%)\n🟢 No daily dislocation — WAIT.")
        return
    print(f"Layer 2: scanning {len(suspects)} on 15m...")
    prices, candidates = {}, []
    try:
        df15 = yf.download(suspects, period="5d", interval="15m", progress=False, group_by='ticker', threads=True, auto_adjust=True)
    except:
        return
    for t in suspects:
        try:
            h = df15[t] if len(suspects)>1 else df15
            h = h.dropna()
            if len(h) < 40: continue
            close = h['Close']
            last = float(close.iloc[-1]); prev = float(close.iloc[-2])
            prices[t] = last
            bar_ret = (last/prev-1)*100
            r = float(calc_rsi(close).iloc[-1])
            sma20_15 = float(close.rolling(20).mean().iloc[-1])
            vs_sma = (last - sma20_15)/sma20_15*100
            vol = float(h['Volume'].iloc[-1]); avg_vol = float(h['Volume'].rolling(20).mean().iloc[-1])
            vr = vol/avg_vol if avg_vol>0 else 1
            candidates.append({"t":t,"p":last,"rsi":r,"bar":bar_ret,"vs":vs_sma,"vr":vr})
        except:
            continue
    still_open, closed_rows = [], []
    for s in open_signals:
        p_now = prices.get(s["t"])
        if p_now is None:
            still_open.append(s); continue
        if (now - s["ts"]) < timedelta(minutes=HORIZON_MIN):
            still_open.append(s); continue
        ret = (float(p_now)/s["p"]-1)*100
        closed_rows.append({"t":s["t"],"signal_time":s["ts"].strftime("%Y-%m-%d %H:%M"),"entry":round(s["p"],2),"exit":round(float(p_now),2),"ret_pct":round(ret,2),"closed":True})
    open_signals = still_open
    if closed_rows:
        ledger = pd.concat([ledger, pd.DataFrame(closed_rows)], ignore_index=True)
        save_ledger(ledger)
    if not candidates:
        return
    rets = np.array([c["bar"] for c in candidates])
    market = float(np.median(rets))
    spread = float(np.std(rets)) or 1.0
    buys = []
    for c in candidates:
        residual = c["bar"] - market
        c["res"] = residual
        cool = last_alerted.get(c["t"])
        if cool and (now - cool).total_seconds() < COOLDOWN_MIN*60:
            continue
        if residual < -1.0*spread and c["rsi"] < 38:
            sc, rsn = ai_score(c["rsi"], c["vs"], residual, c["vr"], regime)
            if sc >= 55:
                c["score"] = sc; c["reason"] = rsn; c["ts"] = now
                buys.append(c)
    buys = sorted(buys, key=lambda x: x["score"], reverse=True)[:TOP_N]
    for b in buys:
        last_alerted[b["t"]] = now
    open_signals += [{"t":b["t"],"p":b["p"],"ts":b["ts"]} for b in buys]
    msg = f"🤖 MEDALLION 1500 2-LAYER - AI QUANT\nMarket: {regime} ({regime_pct:+.2f}%) | L1: 1500 scanned -> {len(suspects)} suspects | Median 15m: {market:+.2f}%\n\n"
    if "BEARISH" in regime:
        msg += "⚠️ AI: Market bearish — only STRONG 💎, small size, tight stop.\n\n"
    elif "BULLISH" in regime:
        msg += "✅ AI: Market bullish — good for bounce plays.\n\n"
    if buys:
        msg += "🟢 AI QUANT BUY (Dislocation + Score):\n"
        for b in buys:
            flag = "🇳🇬" if ".LG" in b["t"] else "🇺🇸"
            strength = "STRONG 💎" if b["score"]>=75 else "WATCH 👀" if b["score"]>=65 else "RISKY ⚠️"
            clean_t = b["t"].replace(".LG","")
            tp = b["p"] * 1.10
            sl = b["p"] * 0.95
            bamboo = f"https://app.investbamboo.com/stock/{clean_t}"
            chaka = f"https://chaka.com/stocks/{clean_t}"
            msg += f"{flag} {b['t']} ${b['p']:.2f} RSI {b['rsi']:.0f} Res {b['res']:+.2f}% Score {b['score']:.0f}% {strength}\n  👉 {b['reason']} | Vol {b['vr']:.1f}x vs SMA {b['vs']:.1f}%\n  🎯 TP ${tp:.2f} (+10%) | 🛑 SL ${sl:.2f} (-5%)\n  🛒 Bamboo: {bamboo}\n  📈 Chaka: {chaka}\n\n"
    else:
        msg += "🟢 No high-quality dislocation now — AI say WAIT. No fake trades.\n"
    hist = pd.to_numeric(ledger["ret_pct"], errors='coerce').dropna()
    if len(hist) >= 5:
        msg += f"\n📈 LIVE SCORE: {(hist>0).mean()*100:.0f}% win over {len(hist)} closed | avg {hist.mean():+.2f}%"
    msg += "\n💡 Only STRONG 💎 + Bullish market = consider buy. Stop -5%."
    send_telegram(msg)
    print(f"[{now:%H:%M}] L1 1500 -> {len(suspects)} -> {len(buys)} buys")

send_telegram(f"✅ Medallion 1500 2-Layer is live! {len(ALL_TICKERS)} tickers | Layer1 Daily + Layer2 15m | Bamboo links active.")
while True:
    try:
        scan_once()
    except Exception as e:
        print("Scan error:", e)
    time.sleep(600)
