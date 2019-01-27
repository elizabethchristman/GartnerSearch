# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = "Gartner Magic Quadrant Search"

WELCOME = _("Welcome to Gartner Magic Quadrant Search")
HELP = _("Say a keyword to search for an article.")
ABOUT = _("Gartner Magic Quadrant research methodology provides a graphical competitive positioning of four types of technology providers in fast-growing markets: Leaders, Visionaries, Niche Players and Challengers.")
STOP = _("Okay, see you next time!")
FALLBACK = _("The {} can't help you with that. What can I help you with?")
GENERIC_REPROMPT = _("What can I help you with?")

ARTICLE_DATA = [
	"articles":[
{

    "title":'Access Management Worldwide',
    "summary":'The access management market has evolved beyond supporting traditional web applications to support mobile applications and APIs, as well as adding contextual and adaptive access features. Vendors offering an IDaaS option outnumber those that don\'t, and now there are more choices than ever.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Atos (Evidian), CA Technologies, Centrify, Covisint, ForgeRock, IBM, i-Sprint Innovations, Micro Focus, Microsoft, Okta, OneLogin, Optimal IdM, Oracle, Ping Identity, SecureAuth, Vendors Added and Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Product or Service, Overall Viability, Sales Execution/Pricing, Market Responsiveness and Track Record, Marketing Execution, Customer Experience, Operations, Completeness of Vision, Market Understanding, Marketing Strategy, Sales Strategy, Offering (Product) Strategy, Business Model, Vertical/Industry Strategy, Innovation, Geographic Strategy, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Important Decision Factors for Vendor Selection, IDaaS or Software, Use Cases and Target System Support, IoT and AM, User Authentication, Contextual and Adaptive Access, Security Concerns With IDaaS Delivery and Target Systems That Support Only Password Authentication, Pricing, Market Overview'
    },
{

    "title":'Application Performance Monitoring Suites',
    "summary":'As historically dominant vendors revamp their APM suites with analytics, machine learning and cloud-based delivery, I&O leaders will find that the differences among the leading vendors and between Leaders and Challengers are less defined than they have been in previous years.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, BMC, CA Technologies, Cisco (AppDynamics), Correlsense, Dynatrace, IBM, ManageEngine, Micro Focus (HPE Software), Microsoft, Nastel Technologies, New Relic, Oracle, Riverbed, SolarWinds, Tingyun, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Product Requirements, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Application Performance Monitoring Suites',
    "summary":'Application performance monitoring suite use and influence continue to grow beyond IT operations. Here, we evaluate APM suite capabilities across five usage scenarios to assist IT organization planners and buyers as they look to support an increasingly broad array of APM requirements.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AppDynamics, BMC, CA Technologies, Correlsense, Dynatrace, HPE, IBM, Microsoft, Nastel Technologies, New Relic, Oracle, Riverbed, Context, Product/Service Class Definition, Critical Capabilities Definition, Business Analysis, Service Monitoring, Anomaly Detection, Distributed Profiling, Application Debugging, Workload Planning, Use Cases, IT Operations, Application Support, Application Development, DevOps Release, Application Owner or LOB, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Application Release Automation',
    "summary":'Enterprise I&O leaders looking to expand on hard-won agility gains from DevOps and other automation initiatives find that application release automation solutions provide the right mix of task automation, environment modeling and coordination capabilities.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Automic, BMC, CA Technologies, Clarive Software, Electric Cloud, IBM, Inedo, Micro Focus (Serena Software), Microsoft, MidVision, OpenMake Software, Puppet, XebiaLabs, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Product-Related Criteria, Non-Product-Related Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Application Release Automation',
    "summary":'ARA solutions are rapidly evolving to meet demand for faster, better delivery of new applications and updates. This evaluation is shaped by the enterprise\'s need to successfully manage a diverse combination of activities, roles, skills and systems associated with automating an application release.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Automic, BMC, CA Technologies, Clarive Software, Electric Cloud, IBM, Inedo, Micro Focus (Serena Software), Microsoft, MidVision, OpenMake Software, Puppet, XebiaLabs, Context, Product/Service Class Definition, Critical Capabilities Definition, Automation, Environment Modeling, Release Coordination, Use Cases, Release Manager, AppOps/Support Team Member, DevOps Team Member, Release Automation/AppOps Team Lead, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Application Security Testing',
    "summary":'DevSecOps, modern web application design and high-profile breaches are affecting the growing application security testing market. Security and risk management leaders will need to meet tighter deadlines and test more-complex applications by integrating and automating AST in the software life cycle.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Checkmarx, CA Technologies (Veracode), Contrast Security, IBM, Micro Focus, Positive Technologies, Qualys, Rapid7, SiteLock, Synopsys, Trustwave, WhiteHat Security, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Open-Source Software Considerations, Other Players, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Application Security Testing',
    "summary":'Application security testing evolves from supporting basic web app testing to enabling DevSecOps, and securing mobile and single page apps. Security and risk management leaders must select AST solutions focusing on SDLC integration, software composition analysis, automation and speed.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, CA Technologies (Veracode), Checkmarx, Contrast Security, IBM, Micro Focus, Positive Technologies, Qualys, Rapid7, SiteLock, Synopsys, Trustwave, WhiteHat Security, Context, Product/Service Class Definition, Critical Capabilities Definition, Static AST, Dynamic AST, Interactive AST, SDLC Integration, Automation and Turnaround, Software Composition Analysis, Testing as a Service, Behavioral Analysis, Certifications, Use Cases, Commercial, Regulated, Custom, DevOps, Mobile, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Application Testing Services Worldwide',
    "summary":'Application testing service outsourcing is a mature market, which continues to evolve with offerings tailored to support digitalization. Sourcing managers can use this Magic Quadrant to develop a shortlist of service providers appropriate for the desired scope of work.',
    "keywords":'Market Definition/Description, Vendor Profiles, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Applause, Atos, Capgemini, CGI, Cigniti Technologies, Cognizant, CSC, Deloitte, Hewlett Packard Enterprise, IBM, Infosys, NTT Data, QualiTest Group, SQS, Tata Consultancy Services, Tech Mahindra, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Quantitative Criteria, Qualitative Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Business Analytics Services Worldwide',
    "summary":'Data and analytics leaders expect business analytics to drive organization performance and guide digital transformation. Service providers are changing delivery toward IP assets and automation for support. We profile 20 of the most significant companies that offer business analytics services.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Atos, Capgemini, CGI, Cognizant, Deloitte, EY, HCL Technologies, Hewlett Packard Enterprise, IBM Global Business Services, Infosys, KPMG, NEC, NTT Data, PwC, SAP, Tata Consultancy Services, Tech Mahindra, Teradata, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Business Analytics Services Worldwide',
    "summary":'The capabilities of service providers are uneven across the four use cases of commonly executed data and analytics service initiatives. Data and analytics leaders can improve their chances of project success by selecting a provider that aligns with their own use case.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Accenture, Atos, Capgemini, Cognizant, Deloitte, DXC Technology, EY, Genpact, HCL Technologies, IBM Global Business Services, Infosys, KPMG, NEC, NTT DATA, PwC, Tata Consultancy Services, Teradata, Wipro, Context, Product/Service Class Definition, Critical Capabilities Definition, Business Process Consulting, Business Change Management, Design-Led Approach, Managed D&A/D&A as a Service, Asset+ Consulting, Technology Enablement, Use Cases, Strategy and Consulting, Analytics and BI Implementation, Data Management Implementation, Data Science and Machine Learning Implementation, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Business Continuity Management Planning Solutions Worldwide',
    "summary":'The BCMP software market  with a global market revenue estimate of $250 million  is broadening its capabilities and becoming closer to operational risk management solutions. Gartner\'s Magic Quadrant on this growing market evaluates 13 vendors to help in your vendor selection process.',
    "keywords":'Market Definition/Description, The Future of the BCMP Software Market, Guidance for the Magic Quadrant Analysis, Magic Quadrant, Vendor Strengths and Cautions, Avalution, ClearView, Continuity Logic, EMC (RSA), Fusion, Global AlertLink, LockPath, MetricStream, Quantivate, RecoveryPlanner, Strategic BCP, Sungard Availability Services, Virtual, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Cloud Access Security Brokers',
    "summary":'Cloud access security brokers have become an essential element of any cloud security strategy, helping organizations govern the use of cloud and protect sensitive data in the cloud. Security and risk management leaders should align CASB vendors to address specific use-case requirements.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Bitglass, CensorNet, CipherCloud, Cisco, Microsoft, Netskope, Oracle, Palo Alto Networks, Saviynt, Skyhigh Networks, Symantec, Vendors Added and Dropped, Inclusion and Exclusion Criteria, Vendors to Watch, Forcepoint, ManagedMethods, Vaultive, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Cloud Core Financial Management Suites for Midsize Large and Global Enterprises',
    "summary":'The core financial management suites market is transitioning from traditional on-premises deployment to cloud services. Application leaders in midsize, large and global enterprises should use this new Magic Quadrant to identify viable solutions for moving core finance processes to the cloud.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Acumatica, Deltek, Epicor Software, FinancialForce, Intacct, Microsoft, Oracle (NetSuite), Oracle (Oracle ERP Cloud), Ramco Systems, SAP, Workday, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Appendix'
    },
{

    "title":'Cloud ERP for Product-Centric Midsize Enterpr',
    "summary":'The market for ERP suites for product-centric enterprises is shifting from on-premises deployments to cloud services. Application leaders in midsize enterprises should use this Magic Quadrant to identify viable vendors and solutions for moving ERP business processes to the cloud.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Acumatica, Epicor Software (Epicor ERP), Infor (CloudSuite Industrial), Infor (CloudSuites (LN)), Infor (CloudSuites (M3)), IQMS, Microsoft (Dynamics 365), Oracle (NetSuite ERP), Oracle (Oracle ERP Cloud), Plex, QAD, Ramco Systems, Rootskeywordsk Software, SAP (Business ByDesign), Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Cloud HCM Suites for Midmarket and Large Enterprises',
    "summary":'HCM suites enable core HR, payroll, talent, workforce management and HR service delivery processes. Application leaders in entities with over 1,000 workers and emerging global needs that are pursuing a cloud HCM strategy should use this research to help identify vendors for further evaluation.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, ADP, Ceridian, Infor, Kronos, Meta4, Oracle, Ramco Systems, SAP, Talentia Software, Ultimate Software, Workday, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Appendix'
    },
{

    "title":'Cloud HCM Suites for Midmarket and Large Enterprises',
    "summary":'HCM suite vendors are building out their offerings to address administrative, strategic and operational needs of users, but solutions still vary. Application leaders transforming HCM should use this research to identify best-fit vendors based on their own critical product and service/support needs.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, ADP, Ceridian, Infor, Kronos, Meta4, Oracle, Ramco Systems, SAP, Talentia Software, Ultimate Software, Workday, Context, Product/Service Class Definition, Critical Capabilities Definition, Core HR/Benefits Admin, Payroll Admin, Workforce Management, Prehire Talent Management, Posthire Talent Management, Reporting Tools/WFA/WFP, Technology/UX, Overall Product Satisfaction, Overall VCR Satisfaction, Geo/Complexity/Value Fit to UC 1, Geo/Complexity/Value Fit to UC 2, Geo/Complexity/Value Fit to UC 3, Geo/Complexity/Value Fit to UC 4, Use Cases, Core HR+Talent HCM Suite, Larger Global Org (>5k), North America Midmarket HCM Suite (1k-5k), European-HQ'd Midmarket HCM Suite (1k-5k), NA Admin Compliance Suite, Hourly Workers (>1k), Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Cloud Infrastructure as a Service Japan',
    "summary":'This new Magic Quadrant for cloud IaaS focuses on the Japanese market, because its players, market characteristics and situations are different from the global market. Gartner recommends I&O leaders use this research to assess cloud IaaS offerings by key players in Japan.',
    "keywords":'Market Definition/Description, Notes on the Japan Version, The Difference Between the Global Version and the Japan Version, Key Evaluation Points in This Magic Quadrant, Publication of Appropriate Information, Clear Scenario for Cloudization, Training and Certification, The Relationship Between the User and System Integrator, and the Cannibalization Situation, Go-to-Market Scenario of Cloud IaaS, Based on the Digital Business Vision, Notes on Foreign Providers, 'Better to Have' Attributes for the Japanese Market, Magic Quadrant, Vendor Strengths and Cautions, Amazon Web Services, Fujitsu, IBM, IIJ, KDDI, Microsoft, NEC, NTT Communications, SoftBank, Added, Dropped, Inclusion and Exclusion Criteria, Criteria Included in the Global Magic Quadrant, but Not Included in the Japanese Version, Mandatory Criteria in the Global Magic Quadrant, but Not Essential in the Japanese Version, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Expectations for Providers in Japan'
    },
{

    "title":'Cloud Infrastructure as a Service Worldwide',
    "summary":'The global market for cloud IaaS has consolidated around hyperscale service providers. Infrastructure and operations leaders should adopt strategically, but consider scenario-specific providers as well.',
    "keywords":'Market Definition/Description, Understanding the Vendor Profiles, Strengths and Cautions, Format of the Vendor Descriptions, Magic Quadrant, Vendor Strengths and Cautions, Alibaba Cloud, Amazon Web Services, Google, IBM, Microsoft, Oracle, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, What Does the Cloud IaaS Market Include?, What Types of Workload Are Being Placed on Cloud IaaS?, What Trends Are Currently Influencing Buyers?, What Key Market Aspects Should Buyers Be Aware Of?'
    },
{

    "title":'Configure Price Quote Application Suites',
    "summary":'Gartner estimates that market revenue for configure, price and quote software was approximately $878 million in 2016, with growth of 20% per year expected through 2020. Our evaluation of 11 key vendors will help application leaders choose the solution that best meets their cloud CPQ requirements.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Apttus, CallidusCloud, CloudSense, ConnectWise, FPX, IBM, Oracle, PROS, Salesforce, Vendavo, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Contact Center as a Service Europe',
    "summary":'The CCaaS market in Western Europe has matured and now offers customer service organizations a range of competitive offerings to consider as substitutes for traditional on-premises contact center infrastructure. We assess 10 vendors to help you make the right choice for your business.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, BT, Capgemini (Prosodie), Content Guru, Genesys, IFS (mplsystems), NewVoiceMedia, Orange Business Services, Puzzel, SAP, Vocalcom, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Market Drivers and Inhibitors, Drivers, Inhibitors'
    },
{

    "title":'Contact Center as a Service North America',
    "summary":'North America\'s CCaaS market has matured to provide application leaders and customer service organizations with a range of competitive offers to consider substituting for traditional on-premises contact center infrastructure. This Magic Quadrant assesses 11 vendors to help you make the right choice.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, 8x8, Aspect, BroadSoft, Evolve IP, Five9, Genesys, Nice inContact, Serenova, Talkdesk, TeleTech, West, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Market Drivers and Inhibitors, Drivers, Inhibitors'
    },
{

    "title":'Contact Center Infrastructure Worldwide',
    "summary":'Contact center infrastructure vendors are expanding their functional depth and breadth to deliver omnichannel solutions while enhancing their cloud delivery capabilities. Application leaders should evaluate Vendors technology and their ability to deliver in relevant regions.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Aspect, Avaya, Cisco, Enghouse Interactive, Genesys, Huawei, Mitel, NEC, SAP, Unify, Vocalcom, ZTE, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Contact Center Infrastructure Worldwide',
    "summary":'Application leaders in customer service should consider today\'s contact center infrastructure as a legitimate option for holistically managing both employees and the increasing number of communications channels with customers. We present three use cases that represent the most common configurations.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Aspect, Avaya, Cisco, Enghouse Interactive, Genesys, Huawei, Mitel, NEC, SAP, Unify, Vocalcom, ZTE, Context, Product/Service Class Definition, Critical Capabilities Definition, Architecture, Scalability, High Availability, Management, Open Standards, UCC Integration, Workflow, Multichannel, Workforce Engagement, Single Server Deployment, Use Cases, Multichannel Compact Suite, High-Volume Call Center, Customer Engagement Center, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Content Collaboration Platforms',
    "summary":'EFSS continues to evolve its support for common use cases: workforce productivity, extended collaboration and infrastructure modernization. As capabilities expand, the fit gap for EFSS choices is widening, requiring application leaders to develop a strategic approach to EFSS buying and deployment.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Accellion, BlackBerry, Box, Citrix, Dropbox, Egnyte, Google, Huddle, Intralinks, Microsoft, Syncplicity, Thru, Varonis, Context, Product/Service Class Definition, Critical Capabilities Definition, Mobility, Security, Integration, Collaboration and Social, Content Management, User Productivity, Deployment and Administration, Data Infrastructure, Use Cases, Workforce Productivity, Extended Collaboration, Infrastructure Modernization, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Content Collaboration Platforms',
    "summary":'EFSS destination vendors increasingly address digital workplace enablement. IT leaders can consider this market and choose among a range of maturing options for cloud-based content collaboration and data infrastructure modernization.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accellion, Box, Citrix, Dropbox, Egnyte, Google, Huddle, Intralinks, Microsoft, Syncplicity, Thru, Varonis, WatchDox by BlackBerry, Vendors Added and Dropped, Added, Dropped, Honorable Mentions, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Market Future'
    },
{

    "title":'Content Marketing Platforms',
    "summary":'Marketing leaders must boost the scale, relevance and return on content marketing investments. To meet these needs, content marketing platform vendors are merging editorial planning, content sourcing and analysis capabilities. Use this research to find a CMP that drives efficiency and results.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Contently, Kapost, NewsCred, Percolate, ScribbleLive, Skyword, Spredfast, Sprinklr, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Revenue and New Customers, Required Capabilities, Optional Capabilities, Notable Mentions, Curata, DivvyHQ, Mintent, Oracle Content Marketing, Scoop.it, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Customer Demands Drive a Fervent Content Marketing Focus, CMP Penetration and Future Adoption'
    },
{

    "title":'Content Marketing Platforms',
    "summary":'As brands demand greater content marketing scale, relevance and ROI, marketing leaders must balance operational efficiency with performance. Use this research to evaluate your organization\'s content marketing needs and identify solutions aligned to business goals.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Contently, Kapost, NewsCred, Percolate, ScribbleLive, Skyword, Spredfast, Sprinklr, Context, Product/Service Class Definition, Critical Capabilities Definition, Ideation Insight, Editorial Planning, Creative Workflow, Content Metadata Management, Publishing, Content Performance Analytics, Integrations, Content Storage/DAM, Content Curation, Content Sourcing, Multibrand/Multigeo Support, Use Cases, Brand Publishing and Traffic Generation, B2B Demand Generation, Complex, Distributed Content Marketing, Inclusion Criteria, Revenue and New Customers, Required Capabilities, Optional Capabilities, Critical Capabilities Rating'
    },
{

    "title":'Content Services Platforms',
    "summary":'Shifting business requirements for digital content and new technologies are changing the ECM market. This Magic Quadrant analyzes these dynamics, their impact on ECM vendors and their implications for application leaders in charge of content management.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Alfresco, Dell EMC, Everteam, Hyland, IBM, Laserfiche, Lexmark, M-Files, Microsoft, Newgen Software, Objective, OpenText, Oracle, SER Group, Xerox, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Content Services Platforms',
    "summary":'ECM solutions must address a range of user constituencies, within and outside the enterprise, while meeting a broad set of functional requirements. This document will help application leaders of ECM initiatives identify the solutions they can deploy to address uses important to their organizations.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Alfresco, Dell EMC, Everteam, Hyland, IBM, Laserfiche, Lexmark, M-Files, Microsoft, Newgen Software, Objective, OpenText, Oracle, SER Group, Xerox, Context, Product/Service Class Definition, Critical Capabilities Definition, Document Capture/Ingestion, Classification/Categorization, Insight Engine, Content Security, Regulations/Certifications, Mobility, Integration/Interoperability, Social/Collaboration, BPM/Rule Engine, Analytics/BI, Use Cases, Personal and Team Productivity, Records Management and Compliance, Process Applications, Content Ecosystem, Digital Transformation/Modernization, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'CRM and Customer Experience Implementation Service Providers',
    "summary":'Service providers\' capabilities differ across the four use cases of commonly executed CRM and customer experience initiatives. Sourcing and vendor management leaders can use this document to choose a provider with the capabilities matching their own use case.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Accenture, Atos, BearingPoint, Business & Decision, Capgemini, Cognizant, Deloitte, EY, HCL Technologies, IBM iX, Infosys, NTT Data, PwC, Reply, Salesforce Services, Slalom, Tata Consultancy Services, Tech Mahindra, Wipro, Context, Product/Service Class Definition, Critical Capabilities Definition, Business Acumen, Business Process Transformation, Business Change Management, Sales Solution Competency, Customer Svc. Solution Competency, Marketing Solution Competency, Commerce Solution Competency, Customer Information Architecture, Customer Analytics Competency, Digital Design and User Experience, Use Cases, Core CRM Technology Implementation, Single View of Customer and Analytics, Commerce and Digital Experience Implementation, Customer Experience Strategy and Consulting, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'CRM and Customer Experience Implementation Services Worldwide',
    "summary":'Customer experience and CRM implementation services continue to be in high demand, fueled by digital business transformation. Here, we position the largest customer experience and CRM consulting and implementation service providers to help enterprises identify providers that best fit their needs.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Atos, BearingPoint, Business & Decision, Capgemini, Cognizant, Deloitte, EY, HCL Technologies, HPE, IBM iX, Infosys, NTT Data, PwC, Reply, Salesforce Services, Slalom, Tata Consultancy Services, Tech Mahindra, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, What Happened?, What's Happening?, How to Use This Magic Quadrant'
    },
{

    "title":'CRM Customer Engagement Center',
    "summary":'Vendor positions in this Magic Quadrant reflect the growing demand for cloud-based customer service applications to support customer engagement through multiple channels, including those powered by AI. It remains the case that no vendor offers a suite that meets all global and cross-industry needs.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, bpm\'online, CRMNEXT, eGain, Eptica, Freshdesk, Lithium, Microsoft, mplsystems, Oracle, Pegasystems, Salesforce, SAP, ServiceNow, SugarCRM, Zendesk, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'CRM Customer Engagement Center',
    "summary":'Application leaders supporting customer relationship management and customer experience can use this research  which defines eight critical capabilities and four use-case scenarios  to select the right customer engagement center software products and vendors.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, bpm\'online, CRMnext, eGain, Eptica, Freshdesk, Lithium, Microsoft, mplsystems, Oracle, Pegasystems, Salesforce, SAP, ServiceNow, SugarCRM, Zendesk, Context, Product/Service Class Definition, Critical Capabilities Definition, Case Management, Self-Service/Knowledge Management, Integration, Digital Engagement Channels, Mobile Support, Real-Time Guidance/Decision Support, Predictive Customer Analytics, Social Media Engagement Management, Use Cases, Global, Business to Business, Complex Processes, Business to Consumer, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'CRM Lead Management',
    "summary":'The market for CRM lead management applications continues to grow, evolve and mature. This Magic Quadrant evaluates 17 providers to help IT leaders find the right choice for their company, in collaboration with marketing, sales and digital commerce leaders.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Act-On, Adobe, bpm\'online, CallidusCloud, CRMNEXT, HubSpot, IBM, Impartner, Marketo, Microsoft, MMIT, Oracle, Pegasystems, Salesforce, Salesfusion, SugarCRM, Zoho, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria: Company, Inclusion Criteria: Technology, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Center Backup and Recovery Solutions',
    "summary":'Enterprise backup is among the most critical tasks for infrastructure and operations professionals. Gartner provides analysis and evaluation of the leading data center backup solution vendors that offer a range of traditional to innovative availability capabilities.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Actifio, Arcserve, Commvault, Dell EMC, HPE, IBM, Rubrik, Unitrends, Veeam, Veritas Technologies, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Center Backup and Recovery Solutions',
    "summary":'Data center backup solution evaluation is complex, because of the blend of modern and legacy systems, including backup repositories on-premises or in the cloud. I&O leaders can maintain traditional, comprehensive backup solutions or adopt emerging solutions focusing on simplicity and performance.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Actifio Enterprise and Sky, Arcserve Software and UDP Appliances, Commvault Software and Appliances, Dell EMC Avamar/Data Protection Suite/IDPA, Dell EMC NetWorker/Data Protection Suite, HPE Data Protector and ABR Suite, IBM Spectrum Protect, Rubrik Cloud Data Management, Unitrends Enterprise Backup and Recovery Series, Veeam Backup & Replication and Availability Suite, Veritas NetBackup Software and Appliances, Context, Product/Service Class Definition, Critical Capabilities Definition, Cloud Instances and Applications, Ease of Deployment and Use, On-Premises Databases/Applications, On-Premises NAS, On-Premises Physical Servers, On-Premises Storage Integration, On-Premises Virtual Machines, Public IaaS Storage Integration, Storage and Network Efficiency, User Self-Service, Use Cases, Balanced Physical and Virtual Environments, Fully Virtualized Environments, Public Cloud Environments, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating, Critical Capabilities Methodology''
    },
{

    "title":'Data Center Networking',
    "summary":'Data center networking continues to evolve, with increasing choices for open and disaggregated network solutions, while other vendors aim for more closed, proprietary systems. Enterprises should evaluate different vendor approaches and architectures, with a particular focus on software capabilities.',
    "keywords":'Market Definition/Description, What\'s Changed?, Differentiation Shifting Toward Software, SDN Garners Mainstream Interest, but Limited Deployments, SDN Overlays, White-Box, Disaggregated Switching and Open Networking, Integrated Systems, What Is Required in New Data Center Networks?, Simplified Networks With Improved Agility, Changing Size and Density, Changing Application Architectures, Long-Term Innovation and Choice, Migration and Investment Protection, Magic Quadrant, Vendor Strengths and Cautions, Arista Networks, Avaya, Brocade, Cisco, Dell, Extreme Networks, Hewlett Packard Enterprise, Huawei, Juniper Networks, Lenovo, NEC, New H3C Group, VMware, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Center Outsourcing and Infrastructure Utility Services Asia/Pacific',
    "summary":'Gartner assesses the top eight panregional providers of data center outsourcing in Asia/Pacific with a proven ability to deliver in multiple regional countries. Our analysis of the market, its providers and their services will help sourcing executives choose a data center provider.',
    "keywords":'Market Definition/Description, Geography, Data Center, Data Center Outsourcing, Infrastructure Utility Services, Remote Infrastructure Management-Based Service Delivery, Hybrid Infrastructure Managed Services, Magic Quadrant, Vendor Strengths and Cautions, Atos, CSC, Fujitsu, HCL Technologies, HPE, IBM, Tech Mahindra, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Center Outsourcing and Infrastructure Utility Services Europe',
    "summary":'Gartner analyzes the execution and strategic vision of 16 leading providers and their DCO/IUS and cloud service offerings worth $19.5 billion in annual revenue in Europe. Sourcing executives can use this analysis to select a strategic provider from this market.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Atos, Capgemini, CGI, Cognizant, CSC (DXC), Fujitsu, HCL Technologies, HPE ES (DXC), IBM, Infosys, Sopra Steria, Tata Consultancy Services, Tech Mahindra, T-Systems, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Center Outsourcing and Infrastructure Utility Services North America',
    "summary":'Gartner analyzed 19 service providers  with a combined annual revenue of nearly $18.8 billion  on their vision and ability to deliver DCO/IUS services in North America. Sourcing and vendor management leaders should use this analysis in their selection process.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Atos, Capgemini, CGI, Cognizant, CSC (DXC), Ensono, Fujitsu, HCL Technologies, HPE ES (DXC), IBM, Infosys, NTT Data, Sungard AS, Tata Consultancy Services, Tech Mahindra, Unisys, Wipro, Zensar, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Integration Tools',
    "summary":'It\'s not acceptable for architects or developers to use only postdeployment data resolution. The need for rapid data integration requires tools and platforms with increased ability to read, analyze, and react to local and foreign metadata in a dynamic model with distributed processing capabilities.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Actian, Adeptia, Attunity, Cisco, Denodo, IBM, Informatica, Information Builders, Microsoft, Oracle, SAP, SAS, Syncsort, Talend, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Integration Tools',
    "summary":'Data integration tools address a wide range of use cases that rely on key data delivery capabilities for their success. Application leaders need to understand the relative strengths that vendors exhibit across these capabilities in order to pick the right tools for their needs.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Actian, Adeptia, Attunity, Cisco, Denodo, IBM, Informatica, Information Builders, Microsoft, Oracle, SAP, SAS, Syncsort, Talend, Context, Product/Service Class Definition, Critical Capabilities Definition, Bulk/Batch Data Movement, Data Federation/Virtualization, Message-Oriented Movement, Data Replication/Synchronization, Cloud Enablement, Support for Big Data, Use Cases, BI, Analytics and (Logical) Data Warehousing, Data Consistency Between Operational Applications, Data or System Migrations and Consolidations, Master Data Management, Interenterprise Data Acquisition or Sharing, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Data Management Solutions for Analytics',
    "summary":'Disruption is accelerating in this market, with more demand for broad solutions that address multiple data types and offer distributed processing and repository. Cloud solutions are also gaining traction. We help data and analytics leaders to weigh up the vendors in an increasingly dynamic space.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, 1010data, Amazon Web Services, Cloudera, EnterpriseDB, Google, Hewlett Packard Enterprise, Hortonworks, Huawei, IBM, MapR Technologies, MarkLogic, MemSQL, Microsoft, MongoDB, Oracle, Pivotal, SAP, Snowflake Computing, Teradata, Transwarp Technology, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Management Solutions for Analytics',
    "summary":'Data management solutions for analytics are continuing to improve, with key capabilities consolidating across all vendors. Real-time data analytics have moved to their own distinct use case. Data and analytics leaders can use this research to guide evaluation for modern DMSA offerings.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Actian, Alibaba Cloud (MaxCompute), Amazon Web Services (Amazon Redshift), Cloudera (Cloudera Enterprise), GBase (GBase 8a), Google (BigQuery), Hortonworks (Hortonworks Data Platform), IBM (Db2), MapR Technologies (Converged Data Platform), MarkLogic, MemSQL, Micro Focus (Vertica), Microsoft (SQL Server), Neo4j, Oracle, Pivotal (Greenplum), Qubole, SAP HANA, Snowflake, Teradata, Treasure Data, Context, Product/Service Class Definition, Critical Capabilities Definition, Access to Multiple Data Sources, Administration and Management, Advanced Analytics, Data Ingest, Managing Large Volumes of Data, Optimized Performance (Traditional), Optimized Performance (Exploratory), Flexible Scalability, Variety of Data Types, Workload Management, Traditional Use Support, Exploratory Use Support, Use Cases, Traditional Data Warehouse, Real-Time Data Warehouse, Logical Data Warehouse, Context-Independent Data Warehouse, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Data Quality Tools',
    "summary":'The data quality tools market continues to innovate, fueled by desire for cost reductions, information governance and digital business. This Magic Quadrant evaluates 16 vendors to help you find the most suitable one for your organization\'s needs and deliver greater business value.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Ataccama, BackOffice Associates, Experian, IBM, Informatica, Information Builders, Innovative Systems, MIOsoft, Oracle, Pitney Bowes, Quadient, RedPoint Global, SAP, SAS, Syncsort, Talend, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Quality Tools',
    "summary":'Market disruption caused by digital business sees new developments such as machine learning and predictive analytics emerging in data quality tools. Selecting the right tools is essential if data and analytics leaders are to exploit their business value in both traditional and emerging use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Ataccama, BackOffice Associates, Experian, IBM, Informatica, Information Builders, Innovative Systems, MIOsoft, Oracle, Pitney Bowes, Quadient, RedPoint Global, SAP, SAS, Syncsort, Talend, Context, Product/Service Class Definition, Critical Capabilities Definition, Profiling, Parsing, Standardizing & Cleansing, Interactive Visualization, Matching, Linking & Merging, Multidomain Support, Business-Driven Workflow, Scalability/Performance, Business-Centric Usability, Use Cases, Big Data & Analytics, Data Integration, Data Migration, Information Governance, Master Data Management, Operational/Transactional Data Quality, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Data Science &amp; Machine Learning Platforms',
    "summary":'Data science and machine-learning platforms enable organizations to take an end-to-end approach to building and deploying data science models. This Magic Quadrant evaluates 16 vendors to help you identify the right one for your organization\'s needs.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Alteryx, Anaconda, Angoss, Databricks, Dataiku, Domino, H2O.ai, IBM, KNIME, MathWorks, Microsoft, RapidMiner, SAP, SAS, Teradata, TIBCO Software, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Data Science &amp; Machine Learning Platforms',
    "summary":'The functions and features of data science and machine learning platforms are evolving quickly to keep pace with a highly innovative and hyped space. This research helps data and analytics leaders evaluate 17 data science and machine learning platforms across 15 critical capabilities.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Alteryx, Anaconda, Angoss, Databricks, Dataiku, Domino Data Lab, H2O.ai, IBM, KNIME, MathWorks, Microsoft, RapidMiner, SAP, SAS (Enterprise Miner), SAS (Visual Analytics Suite), Teradata, TIBCO Software, Context, Product/Service Class Definition, Critical Capabilities Definition, Data Access, Data Preparation, Data Exploration and Visualization, Automation, User Interface, Machine Learning, Other Advanced Analytics, Flexibility and Openness, Performance and Scalability, Delivery, Platform and Project Management, Model Management, Precanned Solutions, Collaboration, Coherence, Use Cases, Business Exploration, Advanced Prototyping, Production Refinement, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Gate 1, Gate 2, Gate 3, Critical Capabilities Rating, Appendix''
    },
{

    "title":'Digital Commerce',
    "summary":'The number of digital commerce platform vendors continues to grow along with the breadth of those platforms, adding to the complexity of vendor evaluations. This report evaluates 21 providers of digital commerce platforms to assist application leaders supporting digital commerce.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Aptos, Apttus, BigCommerce, CloudCraze, Digital River, Elastic Path, Episerver, IBM, Insite Software, Intershop, Kibo, Kooomo, Magento, NetSuite, Oracle, Salesforce, SAP Hybris, Shopify, Sitecore, Unilog, VTEX, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Digital Commerce',
    "summary":'Agility, customer experience and headless commerce are key features in the next wave of digital commerce platforms, as application leaders guiding B2C, B2B and B2B2C organizations try to keep pace with the digital economy.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Aptos, Apttus, CloudCraze, Digital River, Elastic Path, Episerver, IBM, Insite Software, Intershop, Kibo, Kooomo, Magento, NetSuite, Oracle (Commerce), Oracle (Commerce Cloud), Salesforce, SAP Hybris, Sitecore, Unilog, VTEX, Context, Product/Service Class Definition, Critical Capabilities Definition, Agility, Customer Experience, Time to Productivity, Embedded Commerce, Globalization, Total Cost of Ownership, Ecosystem, Vertical Industry Support, Scale and Complexity, Interoperability, Use Cases, Global and Enterprise, Digital Business, B2C, B2B, Midsize Business, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Digital Experience Platforms',
    "summary":'Organizations are looking to use DXPs as they move from web-centric to more pervasive, multichannel digital experiences. This Magic Quadrant will help those responsible for a range of customer-, employee- and partner-facing initiatives find the most suitable vendor for their needs.',
    "keywords":'Market Definition/Description, Functional Components of Digital Experience Platforms, DXP Use Cases, Magic Quadrant, Vendor Strengths and Cautions, Acquia, Adobe, BloomReach, censhare, CoreMedia, Crownpeak, Episerver, GX Software, IBM, Jahia, Kentico Software, Liferay, Microsoft, OpenText, Oracle, Oxcyon, Salesforce, SAP, SDL, Sitecore, Squiz, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Product Packaging Criteria, Business Inclusion Criteria, Functional Inclusion Criteria, Evaluation Criteria, Ability to Execute, Product or Service, Overall Viability, Sales Execution/Pricing, Market Responsiveness and Track Record, Marketing Execution, Customer Experience, Operations, Completeness of Vision, Market Understanding, Marketing Strategy, Sales Strategy, Offering (Product) Strategy, Business Model, Vertical/Industry Strategy, Innovation, Geographic Strategy, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Digital Experience Platforms',
    "summary":'The DXP market offers a new generation of platforms to create and continually improve user experience across digital channels. This Critical Capabilities will help application leaders responsible for customer-, employee- and partner-facing initiatives find an offering that aligns with their goals.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Acquia, Adobe, BloomReach, censhare, CoreMedia, Crownpeak, Episerver, GX Software, IBM, Jahia, Kentico Software, Liferay, Microsoft, OpenText, Oracle, Oxcyon, Salesforce, SAP, SDL, Sitecore, Squiz, Context, Product/Service Class Definition, Critical Capabilities Definition, Analytics and Optimization, Applied Artificial Intelligence, Architecture and Development, Collaboration and Knowledge Sharing, Cloud Capability, Content Management, Integration and Interoperability, Mobility and Multichannel Support, Navigation, Search and Insight, Personalization & Context Awareness, Security Admin and Access Control, Usability, User Experience Management, Use Cases, Horizontal Portal, B2C Experience, B2B Partner and Supplier Portals and Extranets, B2E Digital Workplace and Intranets, Internet of Things-Enabled Experience, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Digital Marketing Agencies, Worldwide',
    "summary":'To match the CMO\'s broader remit and fill critical gaps, marketing agencies and consulting firms are expanding their digital transformation capabilities. Marketing leaders seeking a partner for global marketing strategy and execution should use these insights to guide agency selection.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture Interactive, AKQA, Cognizant, Deloitte Digital, Digitas, Epsilon, Havas, Huge, IBM iX, iCrossing, Isobar, Merkle, Mirum, MRM//McCann, Ogilvy & Mather, Proximity, PwC Digital Services, R/GA, SapientRazorfish, VML, Wunderman, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Agencies Struggle to Differentiate, The Broader CMO Remit Changes the Competitive Scope, Agencies Strive to Fill Gaps and Secure Relevance, Providing Business Value With Customer Data, Embedding Agency Talent In-House, Ensuring Diversity, Gender Equality and Safe Work Environments'
    },
{

    "title":'Digital Marketing Hubs',
    "summary":'Vendors from advertising, marketing automation and analytics are racing to deliver personalized digital marketing at scale. Marketing leaders need a system that can integrate and coordinate data and activities across channels, devices and contexts, continuously and in real time.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adobe, BlueConic, Cxense, DataXu, Eulerian Technologies, IBM, IgnitionOne, Kitewheel, Marketo, MediaMath, Neustar, Nielsen, Oracle, RedPoint, Salesforce, SAP, SAS, Sitecore, Turn, Viant Technology, Ysance, Zeta Global, Vendors Added and Dropped, Added, Dropped, Vendors to Watch, Acxiom, Cake, Collective, Ensighten, Epsilon (Conversant), Experian Marketing Services, FIS, Google, HubSpot, Kenshoo, Lytics, Marin, mParticle, Pegasystems, Rocket Fuel, Sizmek, Tealium, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Distributed File Systems and Object Storage',
    "summary":'IT leaders are looking to deliver agile, scalable and cost-effective storage for ever-increasing amount of unstructured data. This research assesses the key attributes, vision and executional prowess of distributed file systems and object storage vendors.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Caringo, Cloudian, DDN, Dell EMC, HGST, Hitachi Vantara, Huawei, IBM, NetApp, Qumulo, Red Hat, Scality, StorageCraft (Exablox), SUSE, SwiftStack, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Vendors to Watch, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Startups and Innovation, Choice in Deployment, Amazon S3 API Standardization'
    },
{

    "title":'Endpoint Protection Platforms',
    "summary":'Endpoint protection is evolving to address more of Gartner\'s adaptive security architecture tasks such as hardening, investigation, incident detection, and incident response. Security and risk management leaders should ensure that their EPP vendor evolves fast enough to keep up with modern threats.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Bitdefender, Carbon Black, Cisco, Comodo, CrowdStrike, Cylance, Endgame, ESET, FireEye, Fortinet, F-Secure, Kaspersky Lab, Malwarebytes, McAfee, Microsoft, Palo Alto Networks, Panda Security, SentinelOne, Sophos, Symantec, Trend Micro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Testing, Transparency and Evaluation, EPP, EDR and IT Operations'
    },
{

    "title":'Endpoint Protection Platforms',
    "summary":'Endpoint protection is evolving to address security architecture tasks such as hardening, investigation, incident detection and incident response. Security and risk management leaders should evaluate EPP Vendors ability to keep up with modern endpoint threats and their deployment requirements.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Bitdefender, Carbon Black, Cisco, Comodo, CrowdStrike, Cylance, Endgame, ESET, FireEye, Fortinet, F-Secure, Kaspersky Lab, Malwarebytes, McAfee, Microsoft, Palo Alto Networks, Panda Security, SentinelOne, Sophos, Symantec, Trend Micro, Context, Product/Service Class Definition, Critical Capabilities Definition, Prevention, EPP Suite, Console Alerting and Reporting, EDR Core Functionality, EDR Advanced Response, Third-Party Integration, Managed Services, Geographic Support, OS Support, Use Cases, Type A, Type B, Type C, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Enterprise Agile Planning Tools',
    "summary":'Enterprise-scale agile adoption continues to grow, driving evolution in the market for planning and management. Application leaders looking to facilitate coordination and collaboration while enabling insight into their organizations\' flow of work should consider enterprise agile planning tools.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AgileCraft, Atlassian, Blueprint, CA Technologies, CollabNet, IBM, Inflectra, Micro Focus, Microsoft, Planview, Targetprocess, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Enterprise Architecture Tools',
    "summary":'Leading EA tools feature new capabilities to address digital business, and accelerate support for business architecture to help achieve business-outcome-driven EA. EA and technology innovation leaders choosing EA tools should assess the tools\' performance against unique organizational use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Avolution (Abacus), BiZZdesign (Enterprise Studio), Casewise (Modeler and Evolve), Mega (HOPEX), Planview (Troux and Projectplace), QualiWare (Enterprise Architecture), SAP (PowerDesigner), Software AG (Alfabet and ARIS), Unicom Systems (System Architect and Focal Point), Context, Product/Service Class Definition, Critical Capabilities Definition, Repository/Metamodel, Modeling, Decision Analysis, Presentation, Administration, Configurability, Frameworks and Standards, Usability, Use Cases, Speeding Time to Value, Creating Signature-Ready Actionable Deliverables, Making Smarter Decisions Faster, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Enterprise Architecture Tools',
    "summary":'Enterprise architecture and technology innovation leaders face unprecedented change and will likely require an EA tool to enable them to manage complexity more effectively. This research informs them of the main EA tool vendors in an evolving marketplace driven by the dynamics of digital business.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Avolution, BiZZdesign, BOC Group, erwin, Mega, Orbus Software, Planview, QualiWare, Software AG, Sparx Systems, Unicom Systems, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, About EA Tools and Digital Business, About This Magic Quadrant and How to Use It, Market Overview'
    },
{

    "title":'Enterprise High-Productivity Application Platform as a Service, Worldwide',
    "summary":'High-productivity application platform as a service continues to increase its footprint across enterprise IT as businesses juggle the demand for applications, digital business requirements and skill set challenges. We examine these market forces and the leading enterprise vendors for such platforms.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AgilePoint, Appian, Betty Blocks, bpm\'online, Caspio, Fujitsu, Kintone, Kony, MatsSoft, Mendix, Microsoft, Oracle, OrangeScape, OutSystems, Pegasystems, Quick Base, Salesforce, ServiceNow, TrackVia, Zoho, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Enterprise Information Archiving',
    "summary":'Compliance, discovery and preservation are key drivers of the enterprise information archiving market, which now covers email, social media, IM, file, SMS and voice. I&O leaders should leverage this research to assess Vendors products, services and capabilities before sourcing EIA solutions.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Actiance, Barracuda Networks, Bloomberg, Capax Discovery, Commvault, Global Relay, Google, Micro Focus, Microsoft, Mimecast, Proofpoint, Smarsh, Veritas Technologies, ZL, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Enterprise Information Archiving',
    "summary":'Enterprise information archiving products provide governance, archiving and retrieval of enterprise digital information. I&O leaders should review suitability of the 16 EIA products evaluated here, based on the ability to support four use cases and seven critical capabilities.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Actiance (Alcatraz, Vantage, Socialite), Barracuda (Message Archiver, Cloud Archiving Service), Bloomberg (Vault), Capax Discovery (Capax Archive Solutions, Zovy), Commvault, Dell EMC (SourceOne), Global Relay (Archive), Google (Vault), HPE (Digital Safe), Micro Focus (GWAVA Retain), Microsoft (Exchange Archiving), Mimecast (Cloud Archive for Email), Proofpoint (Enterprise Archive), Smarsh (The Archiving Platform), Veritas (Enterprise Vault, Enterprise Vault.cloud), ZL Technologies (Unified Archive), Context, Product/Service Class Definition, Critical Capabilities Definition, Policy Management, Data Management, Search/Index, Administration, Content Type Support, E-Discovery, End-User Archiving and Access, Use Cases, Compliance, Operational Efficiency, E-Discovery, End-User Archiving, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Enterprise Integration Platform as a Service, Worldwide',
    "summary":'The integration-platform-as-a-service market has bifurcated into: vendors with a broad go-to-market strategy that tackle a wide range of enterprise integration scenarios; vendors that focus on the more specific use cases. This Magic Quadrant focuses on the first category, enterprise iPaaS.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adaptris, Built.io, Celigo, Cloud Elements, DBSync, Dell Boomi, IBM, Informatica, Jitterbit, Microsoft, Moskitos, MuleSoft, Oracle, SAP, Scribe Software, SnapLogic, Workato, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Enterprise Network Firewalls',
    "summary":''Next generation' capability has been achieved by the products in the network firewall market, and vendors differentiate on feature strengths. Buyers must consider the trade-offs between best-of-breed function and costs.',
    "keywords":'Market Definition/Description, What Has Changed, Magic Quadrant, Vendor Strengths and Cautions, AhnLab, Barracuda Networks, Check Point Software Technologies, Cisco, Dell SonicWALL, Forcepoint, Fortinet, Hillstone Networks, Huawei, Juniper Networks, Palo Alto Networks, Sangfor, Sophos, Stormshield, WatchGuard, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria, Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Next-Generation Firewalls, UTM Still Can't Compete With NGFWs in Enterprises, Virtualized Firewalls: Hype Accelerates, and Demand Stirs Slowly, The Firewall Market Is Roiled by Acquisitions and Remains Dynamic, But Absence of Significant Innovation Brings Challengers Closer to Leaders, Have Some Advanced Threat Detection With That Firewall, Confusing Use of 'Application' and 'Firewall' in Three Distinct Products'
    },
{

    "title":'Enterprise Video Content Management',
    "summary":'As enterprise video content management stabilizes into an early mainstream phase of maturity, cloud and hybrid architectures dominate. Our assessment of 15 key vendors in this market will help application leaders to make the best choice for their organization\'s digital workplace program.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Agile Content, Brightcove, Genus Technologies, Haivision, IBM (Ustream), Kaltura, Kollective, KZO Innovations, MediaPlatform, Panopto, Polycom, Qumu, Sonic Foundry, VBrick, Vidizmo, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Enterprise Video Content Management',
    "summary":'Video content management serves a wide range of existing and new use cases, but no single product covers them all. Application leaders that manage video content, portals, e-commerce, collaboration and communications must assess their core needs and weigh the options against current and planned uses.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Agile Content, Brightcove, Genus Technologies, Haivision, Kaltura, Kollective, KZO Innovations, MediaPlatform, Panopto, Polycom, Qumu, Sonic Foundry, IBM (Ustream), VBrick Systems, Vidizmo, Context, Product/Service Class Definition, Critical Capabilities Definition, External Delivery Optimization, Delivery Model  Cloud/SaaS, Delivery Model  Hybrid, Capturing Video From Collaboration, Integration (Portal/Collaboration), Search, Video Creation/Modification, Video Interactivity, Workflow Richness, Streaming, External Marketing, Security, Quality of Service View, Mobile Capture, Use Cases, Internal Executive Messaging, Internal Training, Internal Collaboration, External Video for Sales, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'European Life Insurance Policy Administration Systems',
    "summary":'The highly competitive European vendor market continues to drive life insurance policy administration system vendors toward their own development or integration of partnership noncore solutions. Life insurance CIOs should consider these developments to help accelerate digital transformation.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, DXC Technology (GraphTalk A.I.A), Edlund (Lifelink+), Fadata (Insis), IN2 (INsurance2), Keylane (LeanApps Life), Mphasis Wyde (Wynsure), msg life (msg.Life Factory), Sapiens (Sapiens Alis), Vermeg (Solife), Context, Product/Service Class Definition, Critical Capabilities Definition, Product Development and Maintenance, New Business Management, Workflow and Process Management, Component-Based Architecture, Ongoing Policy Administration, Group Servicing Functionality, Use Cases, Product Configuration, Straight-Through Processing of Applications, Contract Changes, Group Business Support, Adaptability of the System, Digital Business Support, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'European Life Insurance Policy Administration Systems',
    "summary":'A highly competitive market characterized by low sales has driven European policy administration vendors to extend their system offerings. Life insurance CIOs should focus their core replacement business cases on wider digital capabilities as well as legacy modernization benefits.',
    "keywords":'Market Definition/Description, Product Development and Maintenance, Software-Oriented Architecture, SaaS Deployments, Digital Accelerators, Vendor Viability and Success, Market Awareness and Package Direction, Magic Quadrant, Vendor Strengths and Cautions, DXC Technology, Edlund, Fadata, IN2, Keylane, Mphasis (Wyde), msg life, Sapiens, Vermeg, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Field Service Management',
    "summary":'Vendors positions in this Magic Quadrant reflect the demand to align technicians and contractors using technologies like AI, streaming video and the Internet of Things, for effectiveness in all interactions. It is more important than ever to identify vendors that can adapt new technologies for FSM.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accruent (Verisae), Astea International, ClickSoftware, Comarch, Coresystems, FieldAware, Geoconcept, IFS, Microsoft, Oracle, OverIT, Praxedo, Salesforce, SAP, ServiceMax, ServicePower, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Field Service Management',
    "summary":'We evaluate vendor products for three common use cases using nine product capabilities. Application leaders supporting field service initiatives as part of the customer experience should use this research and its companion Magic Quadrant as part of a broader vendor evaluation process.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Accruent (Verisae), Astea International, ClickSoftware, Comarch, Coresystems, FieldAware, GE Digital (ServiceMax), GEOCONCEPT, IFS, Microsoft, Oracle, OverIT, Praxedo, Salesforce, SAP, ServicePower, Context, Product/Service Class Definition, Critical Capabilities Definition, Integration, Scalability, Industry, Extensibility, Connected Equipment Diagnostics, Work Planning and Scheduling, Technician Enablement, Digital Service Support Channels, Work Order Debrief, Invoicing and Reporting, Contracts, Operations, Contractors, Use Cases, High-Volume and Volatile Schedules, Complex Service and Support, Equipment as a Service, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'General-Purpose Disk Arrays',
    "summary":'Storage vendor consolidation, competition from SDS vendors and cloud providers, and new sales and support models are continuing to change the storage market. I&O leaders who understand the opportunities and risks created by these changes will make better infrastructure refresh decisions.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, DDN, Dell EMC, Fujitsu, Hitachi Vantara, HPE, Huawei, IBM, Infinidat, Infortrend, Inspur, Lenovo, NEC, NetApp, Oracle, Promise Technology, Quantum, Synology, Tegile, Tintri, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'General-Purpose High-End Storage Arrays',
    "summary":'This research assesses the capabilities of high-end storage arrays and evaluates products against key use cases of interest to infrastructure and operations. When choosing storage arrays, I&O leaders should weigh these ratings in the context of their vendor ecosystem.',
    "keywords":'What You Need to Know, Analysis, Introduction, Critical Capabilities Use-Case Graphics, Vendors, DataDirect Networks, Dell EMC, Fujitsu, Hewlett Packard Enterprise 3PAR StoreServ 20800, Hewlett Packard Enterprise XP7, Hitachi Vantara VSP G1500, Huawei, IBM DS8886, IBM XIV, Infinidat, NetApp, Context, Product/Service Class Definition, Architectural Definitions, Critical Capabilities Definition, Manageability, RAS, Performance, Snapshot and Replication, Scalability, Ecosystem, Multitenancy and Security, Storage Efficiency, Use Cases, Consolidation, OLTP, Server Virtualization and VDI, Analytics, Cloud, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'General-Purpose Midrange Storage Arrays',
    "summary":'Eight critical product attributes enable infrastructure and operations leaders to quantify storage array product attractiveness across user scenarios. I&O leaders should use this methodology with specific weightings adjusted to reflect their priorities and requirements and optimize array selection.',
    "keywords":'What You Need to Know, Analysis, Introduction, Critical Capabilities Use-Case Graphics, Vendors, DataDirect Networks SFA 7700 Series, Dell EMC SC Series, Dell EMC Unity, Fujitsu Eternus DX500 S3 and DX600 S3, Hitachi Vantara VSP Gx00 Systems, HPE 3PAR StoreServ Series, HPE Nimble Storage CS-Series, Huawei OceanStor 5000 V3, IBM Storwize V5000 and V7000 Unified, Infortrend EonStor GS, NEC Mx10 Series, NetApp E-Series, NetApp FAS8200, Oracle ZFS Storage Appliance, Quantum QXS, Tegile T-Series IntelliFlash, Tintri VMstore T800 Series, Context, Product/Service Class Definition, Architectural Definitions, Critical Capabilities Definition, Manageability, RAS, Performance, Snapshot and Replication, Scalability, Ecosystem, Multitenancy and Security, Storage Efficiency, Use Cases, Consolidation, OLTP, Server Virtualization and VDI, Analytics, Cloud, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Global Retail Core Banking',
    "summary":'Selecting a core banking system that meets a bank\'s specific business and technology needs remains a complex and risky undertaking. Gartner\'s framework of critical capabilities and use cases will guide bank CIOs through the critical task of evaluating core banking vendors and their products.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Avaloq (Avaloq Banking Suite), EdgeVerve Systems (Finacle Core Banking), FIS (Profile), Fiserv (Signature), Intellect Design Arena (Intellect Digital Core), Misys (FusionBanking Essence), SAP (Transactional Banking), Sopra Banking Software (Sopra Banking Amplitude), Sopra Banking Software (Sopra Banking Platform), TCS (TCS BaNCS), Temenos (Temenos Core Banking), Context, Product/Service Class Definition, Critical Capabilities Definition, Component-Based Architecture, Internationality, Interoperability, Functional Granularity, Small Bank Segment, Midsize Bank Segment, Large Bank Segment, Use Cases, Small Bank/Simple Deployment, Small Bank/Complex Deployment, Midsize Bank/Simple Deployment, Midsize Bank/Complex Deployment, Large Bank/Complex Deployment, Worldwide Multinational Deployment, Challenger Bank Deployment, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Global Retail Core Banking',
    "summary":'The core banking market demand for practical and enabling technology to support significant business initiatives, such as a digital banking strategy, is surging. Lack of agility and the high cost of technology are driving more banks to build the business case for core banking renewal.',
    "keywords":'Market Definition/Description, Platform-Independent, Open Banking, Leveraging Service-Oriented Architecture and Event-Driven Architecture, Componentization, Functional Commodity, Bottom Line, Magic Quadrant, Vendor Strengths and Cautions, Avaloq, BML Istisharat, Datapro, FIS, Fiserv (DNA), Fiserv (Signature), Infosys, Intellect Design Arena, Misys, Oracle, SAB, SAP, Silverlake Axis, Sopra Banking Software (Sopra Banking Amplitude), Sopra Banking Software (Sopra Banking Platform), TCS, Temenos, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Changes From 2014, Inclusion Criteria, GRCB Product Capabilities, Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Targeted Research, Vendor Landscape and Quadrant Movements, 2015 Market Movers, Banking Business Power, Drivers and Decision Makers'
    },
{

    "title":'Hyperconverged Infrastructure',
    "summary":'Hyperconvergence is disrupting the integrated system market, with major system vendors joining the growing number of startups (some of which are now mature). I&O leaders should still recognize a role for solutions based on SANs and either blades or rack servers, depending on workload requirements.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Atlantis Computing, Atos, Cisco, Dell, EMC, Fujitsu, Hitachi, HPE, Huawei, Lenovo, NetApp, Nutanix, Oracle, Pivot3, Riverbed, Scale Computing, SGI, SimpliVity, Teradata, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Hyperconverged Infrastructure',
    "summary":'This research focuses on 15 critical capabilities and four use cases for infrastructure and operations leaders to assess product features and functions. I&O leaders should align their project portfolios with the use cases, rationalize technology and vendor choices, and standardize across use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Atlantis Computing, Atos, Cisco, Dell, EMC, Fujitsu, Hitachi, HPE, Huawei, Lenovo, NetApp, Nutanix, Oracle, Pivot3, Riverbed, Scale Computing, SGI, SimpliVity, Teradata, Context, Product/Service Class Definition, Critical Capabilities Definition, Product Viability, Hardware, Baseline Criteria, Hypervisors, Containers, Data Services, Software-Defined Infrastructure, Stack Integration, Management, Vertical Scaling, Horizontal Scaling, Data Protection, Software-Defined Data Center, Security, Service and Support, Use Cases, Infrastructure Modernization, Infrastructure Consolidation, Infrastructure Agility, Point Projects, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Identity Governance and Administration',
    "summary":'Several vendors are accelerating efforts to offer cloud-delivered IGA, improve analytics and align with PAM products. Security and risk management leaders responsible for IAM should be aware of functional differences and trade-offs between on-premises and cloud-delivered IGA and plan accordingly.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AlertEnterprise, Atos (Evidian), CA Technologies, Core Security, Dell Technologies (RSA), IBM, Micro Focus (NetIQ), Omada, One Identity, Oracle, SailPoint, SAP, Saviynt, Vendors Added and Dropped, Added, Dropped, Other Notable Vendors, Free Open-Source Software (FOSS) Alternatives, Inclusion and Exclusion Criteria, Changes in Inclusion Criteria From Last Year, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Alternatives to IGA Software, Selection Criteria, Market Overview'
    },
{

    "title":'Identity Governance and Administration',
    "summary":'IGA tools control digital identities linked to accounts and entitlements maintained in systems enterprisewide. Security and risk management leaders responsible for identity and asset management programs should evaluate critical capabilities during IGA tool selection processes.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AlertEnterprise, Atos (Evidian), CA Technologies, Core Security, Dell Technologies (RSA), Hitachi ID Systems, IBM, Micro Focus (NetIQ), Omada, One Identity, Oracle, SailPoint IdentityIQ, SailPoint IdentityNow, SAP, Saviynt, Context, Product/Service Class Definition, Critical Capabilities Definition, Identity Life Cycle, Entitlements Management, Access Requests, Workflow, Policy and Role Management, Access Certification, Fulfillment, Auditing, Reporting and Analytics, Ease of Deployment, Scalability and Performance, Use Cases, Global Enterprise, Midsize or Large Enterprise, Governance-Focused, Automation-Focused, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Insight Engines',
    "summary":'Insight engines provide more-natural access to information for knowledge workers and other constituents in ways that enterprise search has not. Application leaders will benefit from comparing insight engine and search vendors with their own current and future needs.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Attivio, Coveo, Dassault Systèmes, Expert System, Funnelback, Hewlett Packard Enterprise, IBM, IHS Markit, Lucidworks, Microsoft, Mindbreeze, Sinequa, Smartlogic, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Integrated IT Portfolio Analysis Applications',
    "summary":'CIOs and IT leaders must balance IT investments and resource usage against strategic IT needs across a complex, interrelated set of portfolios. The IIPA software market offers tools that unlock insights into the true state of the overall IT portfolio and the impact of portfolio-level decisions.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, CA Technologies, Changepoint, EOS Software, Forsythe, Hewlett Packard Enterprise, Planview, Software AG, UMT360, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Integrated Revenue and Customer Management for CSPs',
    "summary":'We rate solutions that provide billing, customer care, rating, charging, pricing, partner relationship management, policy management, mediation, self-service, analytics and other related functions. Target buyers are communications service provider CIOs.',
    "keywords":'Market Definition/Description, Functional Footprint, Core Functionality, Adjunct Functionality, Magic Quadrant, Vendor Strengths and Cautions, Amdocs, BearingPoint, Cerillion, Comarch, CSG International, Ericsson, FTS, Huawei, Mahindra Comviva, Matrixx Software, Mind CTI, Netcracker, Nokia, Openet, Oracle, Peter-Service, Redknee, Sterlite Technologies, Tecnotree, Xius, ZTEsoft, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Changes From the 2016 Magic Quadrant, Key Findings, Market Overview, Vendors Not in the Magic Quadrant'
    },
{

    "title":'Integrated Risk Management Solutions',
    "summary":'Security and risk management leaders are seeking to integrate their risk management solutions to gain a more holistic view of risk across the enterprise. Operational risk management solutions serve as the core element of integrated risk management.',
    "keywords":'Market Definition/Description, Risk and Control Documentation/Assessment, Risk Mitigation Action Planning, KRI Monitoring/Reporting, Risk Quantification and Analytics, Incident Management/Loss Event Capture and Analysis, Magic Quadrant, Vendor Strengths and Cautions, Cura Software, Dell Technologies (RSA), Enablon, IBM, LockPath, MetricStream, Nasdaq, Protiviti, SAI Global, SAP, SAS, ServiceNow, Sphera Solutions, Thomson Reuters, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Integrated Risk Management Solutions',
    "summary":'Operational risk management solutions are integrated risk management solutions focused on more formal ORM practices as a key component of a broader enterprise risk management program. Security and risk management leaders should use this research to focus their ORM solution evaluation efforts.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Cura Software, Dell Technologies (RSA), Enablon, IBM, LockPath, MetricStream, Nasdaq, Protiviti, SAI Global, SAP, SAS, ServiceNow, Sphera Solutions, Thomson Reuters, Context, Product/Service Class Definition, Critical Capabilities Definition, Documentation/Assessment, Incident Mgt./Loss Event Analysis, Risk Mitigation Action Planning, KRI Monitoring/Reporting, Risk Quantification and Analysis, Use Cases, Basic Approach, Intermediate Approach, Advanced Approach, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Intelligent Business Process Management Suites',
    "summary":'Intelligent business process management suites use actionable, real-time insights from operations intelligence to augment the orchestration and automation of adaptive business processes. They help application leaders deliver better business outcomes by improving and transforming business processes.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AgilePoint, Appian, AuraPortal, Axon Ivy, Bizagi, Bonitasoft, BP Logix, bpm\'online, Genpact (PNMsoft), IBM, Itesoft | W4, K2, Kofax, Newgen Software, Oracle, Pegasystems, Software AG, TIBCO Software, Whitestein, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Intelligent Business Process Management Suites',
    "summary":'Intelligent business process management suites shorten the observation-to-action-to-outcome cycle and help business transformation leaders, business process directors, and solution architects reinvent or transform their business processes. We assess how the leading iBPMSs address the main use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AgilePoint, Appian, AuraPortal, Axon Ivy, Bizagi, BP Logix, IBM, K2, Lexmark, Newgen Software, Oracle, Pegasystems, PNMsoft, Software AG, TIBCO Software, Context, Product/Service Class Definition, Critical Capabilities Definition, Interaction Management, High-Productivity App Authoring, Monitoring and Business Alignment, Rule and Decision Management, Analytics, Interoperability, Intelligent Mobility, Process Discovery and Optimization, Context and Behavior History, Use Cases, Composition of Intelligent Process-Centric Apps, Continuous Process Improvement, Business Transformation, Digitalized Process, Citizen Developer Application Composition, Case Management, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Intrusion Detection and Prevention Systems',
    "summary":'Security and risk management leaders should know that while IDPSs are being absorbed by firewall placements at the perimeter, they give the best protection. They\'re also responding to pressure from uptake of other threat defense solutions, and providing credible internal and cloud placement options.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AhnLab, Alert Logic, Cisco, Hillstone Networks, Huawei, IBM, Intel Security (McAfee), NSFOCUS, Trend Micro (TippingPoint), Venustech, Wins, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Vendors to Watch, Bricata, Fidelis Cybersecurity, FireEye, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Next-Generation IDPSs Are Available From Leading Vendors, Advanced Threat Detection Is Now Available From Next-Generation IDPSs, IDPS Appliance Market Consolidation Continues, but Internal Deployments, Cloud and Pure Managed Security Service Offerings Gain Traction, More IDPSs Get Absorbed by NGFWs, but the Stand-Alone IDPS Market Will Persist, IDS Is Still Widely Deployed and Effective, Endpoint Context Is Increasingly Important and Available, Retrospective Analysis Is Useful as an IDS Use Case, Developments in Threat Intelligence Have Implications for IDPSs'
    },
{

    "title":'IT Risk Management Solutions',
    "summary":'The ITRM market has seen increased demand due to cybersecurity initiatives and board risk oversight. Security and risk management leaders must navigate a complex landscape of deployment and pricing models, as well as ITRM buyers\' process maturity needs.',
    "keywords":'Market Definition/Description, Background, Definition, Policy Management, Control Mapping and Reporting, Security Operations Analysis and Reporting, IT Risk Assessment, Incident Management, Magic Quadrant, Vendor Strengths and Cautions, Allgress, Dell Technologies (RSA), IBM, LockPath, MetricStream, Nasdaq, RiskVision, Rsam, SAI Global, ServiceNow, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Notable Mentions, Evaluation Criteria, Ability to Execute, Product or Service, Overall Viability, Sales Execution/Pricing, Market Responsiveness and Track Record, Marketing Execution, Customer Experience, Completeness of Vision, Market Understanding, Marketing Strategy, Sales Strategy, Offering (Product Strategy), Business Model, Vertical/Industry Strategy, Innovation, Geographic Strategy, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'IT Service Management Tools',
    "summary":'IT service support management tools enable infrastructure and operations organizations to support and deliver IT services. To choose the correct tool, I&O leaders should determine which of the popular ITSSM products are best-suited to their I&O maturity levels.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Axios Systems assyst v.10.7, BMC Remedy Service Management Suite v.9.1.00, BMC Remedyforce Summer 15, CA Service Management v.14.1.02, Cherwell Service Management v.8.02, EasyVista IT Service Manager 2015, Heat Service Management v.2015.2, HPE Service Anywhere March 2016, HPE Service Manager v.9.41, IBM Control Desk v.7.6, Landesk Service Desk v.2016, ServiceNow Service Management Suite, Geneva Release, Context, Product/Service Class Definition, Critical Capabilities Definition, Incident and Problem Management, Change and Release Management, Configuration Management, Self-Service/Request Fulfillment, IT Knowledge Management, Collaboration, Reporting and SLA Management, Process and Workflow Design, Data Source/ITOM Tool Integration, Total Cost of Ownership, User Experience and Flexibility, Use Cases, Basic-Maturity I&O, Intermediate-Maturity I&O, High-Maturity I&O, Basic Digital Workplace ITSSM, Advanced Digital Workplace ITSSM, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'IT Service Management Tools',
    "summary":'IT service support management tools are vital for infrastructure and operations organizations to manage support and delivery of IT services. This research profiles key vendors of enterprise ITSSM tools to help I&O leaders make better selections.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Axios Systems, BMC, CA Technologies, Cherwell Software, EasyVista, Heat Software, HPE, IBM, Landesk, ServiceNow, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'IT Services for Communications Service Providers Worldwide',
    "summary":'This Magic Quadrant helps communications service provider CIOs identify and evaluate suppliers to meet their operational IT service needs. The profiled vendors have expertise in discrete and multiyear engagements around CSPs\' operational IT in a multiregional context.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Amdocs, Atos, Capgemini, CGI, Cognizant, Deloitte, Ericsson, HCL Technologies, Hewlett Packard Enterprise, Huawei, IBM, Infosys, Tata Consultancy Services, Tech Mahindra, VirtusaPolaris, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria, Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Life Insurance Policy Administration Systems North America',
    "summary":'North American life insurance policy administration system vendors are expanding their offerings outside core administration processes. Insurance CIOs who require system support for digitalization, data analytics and integration will have to carefully study their options.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Accenture (ALIP), Andesa Services (AFAS), Concentrix (GIAS), CSC (CyberLife, nbA, BPS Portal), CSC (wmA, nbA, BPS Portal), EXL (LifePRO), FAST Technology (FAST), Infosys McCamish (VPAS), InsPro Technologies (InsPro Enterprise), Majesco (Majesco Policy for L&A and Group), MDI (FIMMAS), Mphasis Wyde (Wynsure), Oracle (OIPA), Sapiens (ALIS), Vitech (V3), Context, Product/Service Class Definition, Critical Capabilities Definition, Rule and Calculation Management, Straight-Through Processing, Policy Life Cycle Management, Reporting and Data Management, Digital Business Support, System Modularity and Integration, Use Cases, New Product Development/Launch, New Application/Automated Underwriting, New Application/Manual Underwriting, Policy Change, Reporting and Data Management, Service Through Portals/Mobile, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Life Insurance Policy Administration Systems North America',
    "summary":'Net new sales of packaged policy administration systems in North America declined in 2016, indicating a buyers\' market. In a market with widely divergent product strategies, product depth, and market share, North American life insurance CIOs have many trade-offs to evaluate when selecting a vendor.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Accenture, Concentrix, DXC Technology, EXL, FAST Technology, Infosys McCamish, InsPro Technologies, Majesco, MDI, Oracle, Sapiens, Vitech Systems Group, Wyde, An Mphasis Group Company, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Managed Hybrid Cloud Hosting, Asia/Pac',
    "summary":'Managed cloud providers in Asia/Pacific are beginning to introduce early hybrid cloud capabilities. This Magic Quadrant helps infrastructure and operations leaders choose providers that can support their use cases and geographic requirements.',
    "keywords":'Market Definition/Description, Use Cases Covered by This Magic Quadrant, Types of Business Covered by This Magic Quadrant, Magic Quadrant, Vendor Strengths and Cautions, BT, CenturyLink, CtrlS Datacenters, Datapipe, Fujitsu, IBM, IIJ, NxtGen, NTT Communications, Orange Business Services, Rackspace, Sify Technologies, Singtel, Tata Communications, Telstra, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Products and Services Excluded From This Evaluation, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Managed M2M Services, Worldwide',
    "summary":'Managed cloud providers in Asia/Pacific are beginning to introduce early hybrid cloud capabilities. This Magic Quadrant helps infrastructure and operations leaders choose providers that can support their use cases and geographic requirements.',
    "keywords":'Market Definition/Description, Use Cases Covered by This Magic Quadrant, Types of Business Covered by This Magic Quadrant, Magic Quadrant, Vendor Strengths and Cautions, BT, CenturyLink, CtrlS Datacenters, Datapipe, Fujitsu, IBM, IIJ, NxtGen, NTT Communications, Orange Business Services, Rackspace, Sify Technologies, Singtel, Tata Communications, Telstra, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Products and Services Excluded From This Evaluation, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Managed Mobility Services Worldwide',
    "summary":'Over the past year, enterprises have been looking to broaden the scope for which they use a third party to manage their mobile estates. To maximize the value from MMS, I&O leaders should use closely match their functional and operational requirements to the provider who meets them best.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, DMI, DXC Technology, Fujitsu, Honeywell Enterprise Mobility, IBM, MOBI, Orange, Tangoe, Telefónica, Vodafone, Vox Mobile-GEMA, Zensar, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Provider Investments in Innovation Have Abated, Pricing of Managed Mobility Services Continues to Decline, No Dominant Provider Type, Buying Behavior and Satisfaction'
    },
{

    "title":'Managed Mobility Services Global',
    "summary":'Enterprise spending on mobile device outsourcing is expected to grow from $4.8 billion in 2017 to $8.2 billion in 2021, which is an 88% increase. To build and sustain their mobile estates, infrastructure and operations leaders should demand more from providers and develop their sourcing approaches.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Digital Dimension, DMI, DXC Technology, Fujitsu, Honeywell Enterprise Mobility, IBM Global Services, MOBI, Orange, Stratix, Tangoe, Telefonica, Vodafone, Vox Mobile-GEMA, Zensar Technologies, Context, Product/Service Class Definition, Critical Capabilities Definition, Sourcing and Logistics Management, Managed EMM, Security Management, Financial Management, Program Management, Use Cases, Secure Access to Information, Resource and Cost Visibility and Control, Mobility Outsourcing, Business Extension and Transformation, Europe, Asia/Pacific Region, U.S., Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, , Critical Capabilities Rating'
    },
{

    "title":'Managed Security Services Worldwide',
    "summary":'Security and risk management leaders considering managed security services should use this Magic Quadrant to help identify and evaluate providers with effective threat detection and compliance capabilities, and their ability to deliver services globally.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AT&T, Atos, BAE Systems, BT, CenturyLink, CSC, HCL Technologies, HPE, IBM, NTT Security, Orange Business Services, SecureWorks, Symantec, Trustwave, Verizon, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria, Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, MSS Portfolio, Threat Intelligence, Incident Response and Advanced Analytics, Threat Intelligence Capabilities and Services, Incident Response Capabilities and Services, Advanced Analytics Capabilities, Pricing Models, Service-Level Agreements, MSSP Landscape, MSSP Market Activity in 2016, MSSPs Not Evaluated in the Magic Quadrant'
    },
{

    "title":'Managed Workplace Services Europe',
    "summary":'As digital capabilities become increasingly important, choosing the right managed workplace service provider involves an in-depth understanding of their overall capabilities. Sourcing and vendor management leaders can use this research to quickly find suitable providers for specific needs.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Atos, Capgemini, Cognizant, Computacenter, CSC, Dell Services, Fujitsu, Getronics/GWA, HCL Technologies, HPE (Enterprise Services), IBM, Stefanini, T-Systems, Unisys, Wipro, Context, Product/Service Class Definition, Critical Capabilities Definition, Remote Support, Alternative Support Models, Desktop, Mobility & Virtualization, Use Cases, Service Desk, End-User Device, Digital Workplace, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Managed Workplace Services North America',
    "summary":'This research evaluates 21 service providers on three critical capabilities across three use cases concerning their ability to provide managed workplace services. This research helps sourcing and vendor management leaders select the best MWS vendor for their specific needs.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Atos, Bell Techlogix, C3i Healthcare Connections, Capgemini, Cognizant, CompuCom, CSC, Dell Services, Fujitsu, Genpact, HCL Technologies, HPE (Enterprise Services), IBM, Insight, Long View, Pomeroy, Stefanini, TCS, Unisys, Wipro, Zensar, Context, Product/Service Class Definition, Critical Capabilities Definition, Remote Support, Alternative Support Models, Desktop, Mobility & Virtualization, Use Cases, Service Desk, End-User Device, Digital Workplace, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Master Data Management Solutions',
    "summary":'The MDM market is progressing toward all-encompassing solutions at the same time as the need to apply MDM capabilities to more than just master data is complicating matters. This Magic Quadrant evaluates 11 vendors to help you identify the most suitable one(s) for your needs.',
    "keywords":'Market Definition/Description, Revenue and License Count Estimates, Magic Quadrant, Vendor Strengths and Cautions, Ataccama, EnterWorks, IBM, Informatica, Oracle, Orchestra Networks, Profisee, Riversand, SAP, Stibo Systems, TIBCO Software, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Market Growth Continues, How the Vendors Stack Up, Disruptive Forces in the MDM Market, MDM and the Cloud, MDM and the Internet of Things'
    },
{

    "title":'Master Data Management Solutions',
    "summary":'Selecting the right packaged MDM solution requires clear understanding of how it can meet business or mission requirements. These critical capabilities for MDM solutions enable a use-case-based approach that data and analytics leaders can refer to during the vendor evaluation process.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Ataccama, EnterWorks, IBM, Informatica, Oracle, Orchestra Networks, Profisee, Riversand, SAP, Stibo Systems, TIBCO Software, Context, Product/Service Class Definition, Critical Capabilities Definition, Workflow/BPM, Loading/Sync/Bus Svcs/Integration, Data Modeling, Information Quality/Semantics, Perform/Scale/Availability/Security, Hierarchy Management, Information Stewardship, Information Governance, Multiple Implementation Styles, Multiple Usage Scenarios, Multiple Domain and Multidomain, Product Suite Internal Integration, Use Cases, MDM of B2C Customer Data, MDM of B2B Customer Data, MDM of Buy-Side Product Data, MDM of Sell-Side Product Data, Multidomain MDM, Multivector MDM, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Meeting Solutions',
    "summary":'Meeting solutions blend communications, collaboration and content to enable real-time group work from anywhere. This report, along with its partner Critical Capabilities research, helps application leaders pursuing digital workplace initiatives find vendors suited to their needs.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adobe, Arkadin, BlueJeans Network, Cisco, Google, Huawei, LogMeIn, Microsoft, PGi, Polycom, Vidyo, West, Zoom, ZTE, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Meeting Solutions',
    "summary":'Meeting solutions can be used in many scenarios, from internal collaboration to presentations, training and large events. Application leaders must examine the use cases that will drive their requirements for a portfolio of offerings.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Adobe, Arkadin, BlueJeans Network, Cisco, Google, Huawei, LogMeIn, Microsoft, PGi, Polycom, Vidyo, West, Zoom, ZTE, Context, Product/Service Class Definition, Critical Capabilities Definition, Collaboration Integration, Delivery Model, Enterprise Integration, Extensions, Host Controls, Instructional, Scalability, User Experience, Workspace Integration, Workstream Collaboration, Use Cases, Internal Collaboration, Learning and Training, External Presentation, Webinars, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Metadata Management Solutions',
    "summary":'Selecting the right MDM product in a rapidly maturing technology market shaped by global trends, such as IoT, is a challenge for CIOs focused on digital utility transformation. To help CIOs and IT leaders understand Vendors capabilities and deployment risks, we update MDM product positioning.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Cuculus, ElectSolve, Energyworx, Enoro, Ferranti Computer Systems, Fluentgrid, Gruppo Engineering, Honeywell (Elster), Itron, Landis+Gyr, Oracle Utilities, Siemens, Terranova, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, MDM Market Drivers, The MDM Market's Diverse Needs, MDM Product and Service Providers' Challenges, MDM as a Consumption-Data-Analytics-Enabling Platform, Impact of IoT on the MDM Market'
    },
{

    "title":'Meter Data Management Products',
    "summary":'Selecting the right solution in a rapidly maturing MDM market affected by global trends such as IoT is a challenge for CIOs and buyers of smart metering solutions. To help clients understand Vendors capabilities and deployment risks, we provide an update of product positioning.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Cuculus, ElectSolve, Elster EnergyICT, Energyworx, Enoro, Ferranti Computer Systems, Fluentgrid, Gruppo Engineering, Itron, Landis+Gyr, Oracle Utilities, Robotron, Siemens, Terranova, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Mobile App Development Platforms',
    "summary":'Application leaders face an increasing array of digital channels to support, from apps to virtual personal assistants. We evaluate the major MADP vendors used to accelerate and scale mobile app development, as well as to deliver post-app experiences supporting digital business.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adobe, Axway (Appcelerator), DSI, GeneXus, IBM, i-exceed, Kony, Mendix, Microsoft, MobileFrame, Oracle, OutSystems, Pegasystems, Progress, Red Hat, Salesforce, SAP, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Mobile App Development Platforms',
    "summary":'IT faces increasing pressure to deliver a wide variety of mobile apps  quickly and cost-effectively  but the mobile tools market continues to evolve quickly. This research helps mobile and app development leaders evaluate the most appropriate MADP across four common enterprise mobile app use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Adobe, IBM, Kony, Mendix, Microsoft, Oracle, OutSystems, Pegasystems, Progress, Red Hat, Salesforce, SAP, Context, Product/Service Class Definition, Critical Capabilities Definition, Low-Code/No-Code App Building Tool, High-Productivity IDE, Cloud and Mobile Back-End Services, Integration and API Management, Platform Security and Certification, UX, Process and Data Modeling, UI and Native API Support, Omnichannel Support, Content Management/Dynamic Updates, App Analytics and Reporting, App Testing/Life Cycle Management, Use Cases, B2C Informational, B2C Transactional, B2E Simple, B2E Complex, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Multichannel Campaign Management',
    "summary":'Marketing leaders will find a host of new vendors in this year\'s Magic Quadrant for multichannel campaign management. Vendors are focused on integrating machine learning, personalization and ad tech capabilities into big data foundations for deeper customer engagement.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adobe, AgilOne, Emarsys, Episerver, Experian, IBM, Listrak, Marketo, Maropost, Oracle, Pegasystems, Pitney Bowes, RedPoint, Resulticks, Sailthru, Salesforce, SAP, SAS, Selligent, Sitecore, Teradata, Zeta Global, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Functions, Digital Marketing Capability, Market Presence, Momentum and Viability, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Multichannel Campaign Management',
    "summary":'This year, MCCM vendors strengthened their offerings with advanced analytics, event processing infrastructure and connections to programmatic advertising. As the complexity of MCCM engagements grow, marketers must weigh the risks of emerging tactics against their potential reward.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Adobe, AgilOne, Experian, IBM, Listrak, Marketo, Microsoft, Oracle, Pegasystems, Pitney Bowes, RedPoint, Salesforce, SAP, SAS, SDL, Selligent, Sitecore, Teradata, Zeta Interactive, Context, Product/Service Class Definition, Critical Capabilities Definition, Multidimensional Segmentation, Campaign Workflow, Predictive Analytics, Event Triggering, Real-Time Decisioning, Content Marketing, Social Marketing, Ad Management, Email Marketing, Mobile Marketing, Use Cases, Campaign Creation, Campaign Orchestration, Campaign Execution, Campaign Measurement, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Functions, Digital Marketing Capability, Market Presence, Momentum and Viability, Critical Capabilities Rating'
    },
{

    "title":'Network Performance Monitoring and Diagnostics',
    "summary":'NPMD tools enable infrastructure and operations organizations to support and deliver IT services. To choose the correct tool, I&O leaders responsible for network performance should determine which of the popular NPMD products are best-suited to their requirements and maturity level.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AppNeta Suite, CA Technologies CA Performance Management, Cisco Prime Infrastructure, NAM and Collaboration, Corvil Analytics Platform Tera+, ExtraHop Platform, Flowmon Networks Flowmon Platform, Genie Networks GenieATM, HPE Network Node Manager i and Real User Monitoring, InfoVista VistaInsight for Networks and 5View Suite, Ipswitch WhatsUp Gold, LiveAction LiveNX, NetScout nGeniusONE Platform and nGeniusPULSE, Paessler PRTG Network Monitor, Riverbed SteelCentral Suite, SevOne PAS, SevOne PLA and SevOne EUE, SolarWinds NPM and SolarWinds NTA, Viavi Observer Performance Management Platform, Context, Product/Service Class Definition, Critical Capabilities Definition, Endpoint/Component/Link Monitoring, Service Delivery Monitoring, Diagnostics, Algorithmic IT Operations (AIOps), Integration and Interoperability, Use Cases, Network Operator, Network Architect, IT Operations Generalist, IT Operations Manager, Line-of-Business User, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Product-Related Criteria, Critical Capabilities Rating'
    },
{

    "title":'Network Performance Monitoring and Diagnostics',
    "summary":'NPMD solutions are key in helping I&O leaders support more complex technologies and services with network visibility, performance issue detection and root cause analysis. Vendors are innovating with cloud monitoring, support for software-defined environments and more flexible deployment models.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AppNeta, CA Technologies, Cisco, Corvil, ExtraHop, Flowmon Networks, Genie Networks, HPE, InfoVista, Ipswitch, LiveAction, NetScout, Paessler, Riverbed, SevOne, SolarWinds, Viavi, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Product-Related Criteria, Non-Product-Related Criteria, Honorable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, NPMD: A Mature Market Evolves in Response to New Demands, Device Polling Technology, Flow-Based Technology, Packet-Based Technology, Adjacent and Overlapping Markets, Application Performance Monitoring, IT Infrastructure Monitoring, Algorithmic IT Operations Platforms (Formerly IT Operations Analytics), Network Packet Brokers'
    },
{

    "title":'Network Services Asia/Pacific',
    "summary":'Enterprises with regional networking requirements in Asia/Pacific have a wide choice of service providers. I&O leaders responsible for WAN sourcing should evaluate these provider\'s newly available services such as direct cloud connections, hybrid WAN, SD-WAN, vCPE and NFV services.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AT&T, BT, CenturyLink, China Telecom Global, Global Cloud Xchange, NTT Communications, Orange Business Services, PCCW Global, Singtel, Tata Communications, Telstra, Verizon, Vodafone, Context, Product/Service Class Definition, Critical Capabilities Definition, Managed MPLS VPNs, Ethernet Services, Managed Hybrid WAN/SD-WAN, Managed vCPE and VNFs, Use Cases, Midsize Asia/Pacific Network, Large Asia/Pacific Network, High-Performance Network, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Network Services Global',
    "summary":'Driven by cloud IT service adoption, the market for global enterprise network services is undergoing a generational shift in both technologies and the provider landscape. Infrastructure and operations leaders must adapt their network sourcing approaches to reflect this transformation.',
    "keywords":'Market Definition/Description, Established Global Network Services, Emerging Global Network Services, Additional Network Services, What\'s Changed?, Magic Quadrant, Vendor Strengths and Cautions, AT&T, BT, CenturyLink, Global Cloud Xchange, GTT, Level 3 Communications, Masergy, NTT Communications, Orange Business Services, Sprint, Tata Communications, Telefonica, Telstra, T-Systems, Verizon, Vodafone, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Contracting Trends, Network Architectures, Access Options, Managed and Virtualized Services, SIP Trunks, Pricing Trends'
    },
{

    "title":'Network Services Pan-European',
    "summary":'Enterprises\' digital business initiatives drive increased adoption of IaaS and SaaS, and Pan-European network service providers\' offers are shifting in response. To maximize agility, I&O leaders must evolve their network architectures and sourcing approaches.',
    "keywords":'What You Need to Know, What Has Changed, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AT&T, BT, Colt, Global Cloud Xchange, Interoute, Level 3 Communications, Masergy, NTT, Orange Business Services, Telefónica, T-Systems, Verizon, Vodafone, Context, Product/Service Class Definition, Critical Capabilities Definition, Ethernet Services, Internet Services, Managed Hybrid WAN/SD-WAN, Managed LAN/WLAN, Managed MPLS VPN Incl. Cloud Conn., Managed vCPE and VNFs, SIP Trunk Services, Use Cases, High-Performance Network, Large European Network, Midsize European Network, Multicountry Branch Network, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Object Storage',
    "summary":'Growing investments in Mode 2 IT projects and cost reduction efforts in core enterprise workloads are driving the demand for object storage. Here, we compare 12 object storage products against seven critical capabilities in use cases relevant to infrastructure and operations leaders.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Caringo Swarm, Cloudian HyperStore, DataDirect Networks WOS, EMC Elastic Cloud Storage, HGST Active Archive System, Hitachi Data Systems HCP, Huawei OceanStor UDS, IBM Cleversafe dsNet, NetApp StorageGRID, Red Hat Ceph Storage, Scality Ring, SwiftStack Object Storage, Context, Product/Service Class Definition, Critical Capabilities Definition, Capacity, Storage Efficiency, Interoperability, Manageability, Performance, Resilience, Security and Multitenancy, Use Cases, Analytics, Archiving, Backup, Cloud Storage, Content Distribution, Overall, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Operational Database Management Systems',
    "summary":'After rapid expansion of vendors and features, players in the operational DBMS market continue converging toward feature parity. Data and analytics leaders will be interested in the lack of Visionaries, competition in the Challengers quadrant and the maturing cloud capabilities among these vendors.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Actian, Amazon Web Services, Basho Technologies, Clustrix, Couchbase, DataStax, EnterpriseDB, Fujitsu, Google, IBM, InterSystems, MapR, MarkLogic, MemSQL, Microsoft, MongoDB, Neo Technology, NuoDB, Oracle, Redis Labs, SAP, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Other Vendors to Consider, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Operational Database Management Systems',
    "summary":'New products for operational DBMS use cases are maturing, challenging data and analytics leaders to select the right technology. This research and companion Magic Quadrant report combine vendor capabilities and client implementation experience to identify products that meet requirements.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Actian, Amazon, Basho Technologies, Clustrix, Couchbase, DataStax, EnterpriseDB, Fujitsu, Google, IBM, InterSystems, MapR, MarkLogic, MemSQL, Microsoft, MongoDB, Neo Technology, NuoDB, Oracle, Redis Labs, SAP, Context, Product/Service Class Definition, Critical Capabilities Definitions, High-Speed Ingest and Processing, ACID Support, Tunable Consistency, Multimodel Support, Automated Data Distribution, Cloud/Hybrid Deployment, Programmability for HTAP, Security, Administration and Management, Use Cases, Traditional Transactions, Distributed Variable Data, Lightweight Events and Observations, Hybrid Transactional/Analytical Processing (HTAP), Inclusion Criteria, Vendors Added and Dropped, Added, Dropped, Other Vendors to Consider, Other Changes, Critical Capabilities Rating'
    },
{

    "title":'Operations Support Systems',
    "summary":'This Magic Quadrant rates major vendors that sell end-to-end OSSs to communications service providers in the global marketplace. The OSS becomes a critical incubator that enables CSPs to shift from traditional to digital service provider.',
    "keywords":'Market Definition/Description, OSS Functionality, Market Evolution, Magic Quadrant, Vendor Strengths and Cautions, Amdocs, Comarch, Ericsson, Hewlett Packard Enterprise, Huawei, IBM, Netcracker, Nokia, Oracle, ZTEsoft, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Recommendations, Market Overview, Process- and Technology-Driven OSS: Best-of-Suite Approach, Enabling Third-Party Ecosystems for Digital Business Models, OSS/BSS Enabling IOT Frameworks, CEM Embraces Networks and OSSs, Vendors Not in the Magic Quadrant'
    },
{

    "title":'P&amp;C Core Platforms North America',
    "summary":'The North American market for P&C core systems has consolidated as policy, billing and claims management modules have become increasingly commoditized. Buyer attention and vendor investment have shifted to broader platform capabilities, supporting customer engagement and more effective use of data.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adaptik, BriteCore, CodeObjects, Duck Creek, DXC Technology, EIS Group, Guidewire (InsuranceNow), Guidewire (InsuranceSuite), Insuresoft, Insurity, Oceanwide, Majesco, OneShield, Sapiens, StoneRiver, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'P&amp;C Core Platforms North America',
    "summary":'P&C insurance CIOs have broadened the scope of legacy modernization efforts beyond traditional core systems to key areas such as customer experience and partner ecosystems. Vendors are responding with expanded offerings that form core platforms, but uneven capabilities will complicate selection.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Adaptik, BriteCore, CodeObjects, Duck Creek, DXC Technology, EIS Group, Guidewire (InsuranceNow), Guidewire (InsuranceSuite), Insuresoft, Insurity, Majesco, Oceanwide, OneShield, Sapiens, StoneRiver, Context, Product/Service Class Definition, Critical Capabilities Definition, Multichannel Support, Policy Management, Billing Management, Claims Management, Data and Analytics, Partner Ecosystem Support, Configuration, Alternative Delivery, Internationality, Use Cases, Process Definition, New Product Development, New Business Submission, Bill-to-Pay Cycle, Claim Submission and Processing, Multiregional Deployment, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Procure-to-Pay Suites',
    "summary":'This year, specialist vendors completely dominate the procure-to-pay suite market with extensive portfolios, a superior UX and better access to innovation. Procurement, IT and supply chain leaders can use this report to identify global P2P vendors to meet their needs in the postmodern ERP era.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Basware, Basware (Verian), BirchStreet Systems, Capgemini (IBX), Coupa, Determine (b-pack), GEP, Ivalua, Perfect Commerce, Proactis, SAP (Ariba and Fieldglass), Wax Digital, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Procure-to-Pay Suites',
    "summary":'Procure-to-pay suite vendors are expanding their solutions to handle an ever-increasing number of financial processes and spending work streams. IT leaders responsible for applications can use this research for insight into how well P2P suite vendors support common P2P use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Basware, Basware (Verian), BirchStreet Systems, BuyerQuest, Capgemini (IBX), Coupa, Determine (b-pack), GEP, Ivalua, Mercado Eletrônico, Perfect Commerce, Pool4Tool, Proactis, SAP (Ariba and Fieldglass), Wax Digital, Xeeva, Context, Product/Service Class Definition, Critical Capabilities Definition, Personal Consumables Shopping, Requisitioning Inventory, Planned Inventory Order Dispatch, Planned Inventory Change Order, Travel Expense Management, Contingent Personnel Procurement, Contingent Personnel Tracking, SOW Services Governance, No Purchase Order, Pay on Invoice, Automated Invoice to Contract Match, Rule-Based Invoice-to-PO Match, Local E-Invoicing, Supplier Information Management, Remittance Advice to Suppliers, Supply Chain Finance, Use Cases, Employee Self-Service P2P, Digital Workplace for Accounts Payable, Services Procurement Governance, Requisitioned, Mission-Critical Inventory P2P, Planned Inventory P2P, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Public Cloud Infrastructure as a Service Worldwide',
    "summary":'Market-leading cloud IaaS providers deliver significantly greater capabilities than their competitors, which are relegated to niches. Enterprise architecture and technology innovation leaders must make both strategic and tactical use-case-specific provider selections.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Alibaba Cloud, Amazon Web Services, CenturyLink Cloud, Fujitsu Cloud Service K5 IaaS, Google Cloud Platform, IBM Bluemix Infrastructure, Interoute Virtual Data Centre, Joyent Triton Public Cloud, Microsoft Azure, NTT Com Enterprise Cloud 2.0, Oracle Cloud Infrastructure, Rackspace Public Cloud, Skytap Cloud, vCloud Air, Virtustream Enterprise Cloud, Context, Product/Service Class Definition, Critical Capabilities Definition, Compute Resilience, Architecture Flexibility, Security and Compliance, User Management, Enterprise Integration, Automation and DevOps Enablement, Scaling, Big Data Enablement, Use Cases, Application Development, Batch Computing, Cloud-Native Applications, General Business Applications, Internet of Things, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Public Cloud Infrastructure Managed Service Providers Worldwide',
    "summary":'Enterprise architecture and technology innovation leaders can benefit from selecting a high-quality-managed service provider when implementing and operating solutions on Amazon Web Services, Microsoft Azure and Google Cloud Platform.',
    "keywords":'Market Definition/Description, When to Use This Magic Quadrant, Format of the Vendor Descriptions, Magic Quadrant, Vendor Strengths and Cautions, 2nd Watch, Accenture, AllCloud, BESPIN GLOBAL, Capgemini, Cloudnexa, Cloudreach, Cognizant, DXC Technology, Deloitte, HCL Technologies, Infosys, Logicworks, Nordcloud, Onica, Rackspace, REAN Cloud, Smartronix, Tata Consultancy Services, Wipro, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Public Cloud Storage Services Worldwide',
    "summary":'Hyperscale providers are dominating the market for public cloud storage in terms of product innovation, scale and revenue. Customers should be wary of using providers that lack meaningful scale and global presence due to slow product innovation and the realistic possibility of service closure.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Alibaba, Amazon Web Services, AT&T, Google, IBM (SoftLayer), Microsoft, Oracle, Rackspace, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria, Vendors Considered but Not Included, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Sales and Operations Planning Systems of Differentiation',
    "summary":'This Magic Quadrant examines the main vendors that provide S&OP systems of differentiation. Supply chain leaders in IT can use this report when evaluating and selecting such a system to help enable Stage 4 S&OP maturity for their business.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AIMMS, Anaplan, Arkieva, Demand Solutions, Infor, JDA, Jonova, Kinaxis, LLamasoft, Logility, o9 Solutions, OM Partners, Oracle (VCP), Outperform, QAD (DynaSys), Quintiq, River Logic, SAP, Steelwedge, ToolsGroup, Vendors Added and Dropped, Added, Dropped, Honorable Mentions, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Sales Force Automation',
    "summary":'The sales force automation market grew 9.8% in 2015, to almost $6 billion. IT leaders supporting sales have new mobile, business process modeling, and predictive analytics options. Our evaluation of 19 products from 17 vendors will help them to choose the solution that best fits their requirements.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Aptean, Base, bpm\'online, Bullhorn, CRMNEXT, Infor, Microsoft (Dynamics CRM), Microsoft (Dynamics CRM Online), NetSuite, Oracle, Pegasystems, PipelineDeals, Sage, Salesforce, SAP (CRM), SAP (Hybris Cloud for Sales), SugarCRM, Tour de Force, Zoho, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Sales Performance Management',
    "summary":'The SPM software market grew 5% in 2016 to an estimated $753 million. Application leaders supporting sales should focus on sales incentive compensation in the short term, but also support use cases for operations, planning and corporate performance management in the midterm.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Anaplan, beqom, CallidusCloud, IBM, Incentives Solutions, Nice, Optymyze, Oracle, SAP, Vistex, Xactly, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Honorary Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Sales Performance Management',
    "summary":'SPM solutions maximize sales operational efficiencies, are gaining in effectiveness and align go-to-market plans with sales execution. To assist application leaders in selecting SPM solutions, Gartner has evaluated the capabilities of 11 vendors, covering four use cases and 10 critical capabilities.',
    "keywords":'What You Need to Know, Critical Capabilities Use-Case Graphics, Vendors, Anaplan, beqom, CallidusCloud, IBM, Incentives Solutions, Nice, Optymyze, Oracle, SAP, Vistex, Xactly, Context, Product/Service Class Definition, Critical Capabilities Definition, Calculations, Rule Definitions, Modeling, Workflow and Collaboration, Scalability, Audit, Integration (Data & Product Suite), Data Transformation (ETL), Advanced Analytics, Customization and Extensibility, Use Cases, Incentive Compensation, Quota Management and Planning, Territory Management and Planning, Objectives Management, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'SAP Application Services, Worldwide',
    "summary":'SPM solutions maximize sales operational efficiencies, are gaining in effectiveness and align go-to-market plans with sales execution. To assist application leaders in selecting SPM solutions, Gartner has evaluated the capabilities of 11 vendors, covering four use cases and 10 critical capabilities.',
    "keywords":'What You Need to Know, Critical Capabilities Use-Case Graphics, Vendors, Anaplan, beqom, CallidusCloud, IBM, Incentives Solutions, Nice, Optymyze, Oracle, SAP, Vistex, Xactly, Context, Product/Service Class Definition, Critical Capabilities Definition, Calculations, Rule Definitions, Modeling, Workflow and Collaboration, Scalability, Audit, Integration (Data & Product Suite), Data Transformation (ETL), Advanced Analytics, Customization and Extensibility, Use Cases, Incentive Compensation, Quota Management and Planning, Territory Management and Planning, Objectives Management, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'SAP Application Services, Worldwide',
    "summary":'SPM solutions maximize sales operational efficiencies, are gaining in effectiveness and align go-to-market plans with sales execution. To assist application leaders in selecting SPM solutions, Gartner has evaluated the capabilities of 11 vendors, covering four use cases and 10 critical capabilities.',
    "keywords":'What You Need to Know, Critical Capabilities Use-Case Graphics, Vendors, Anaplan, beqom, CallidusCloud, IBM, Incentives Solutions, Nice, Optymyze, Oracle, SAP, Vistex, Xactly, Context, Product/Service Class Definition, Critical Capabilities Definition, Calculations, Rule Definitions, Modeling, Workflow and Collaboration, Scalability, Audit, Integration (Data & Product Suite), Data Transformation (ETL), Advanced Analytics, Customization and Extensibility, Use Cases, Incentive Compensation, Quota Management and Planning, Territory Management and Planning, Objectives Management, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Secondary Site of Disaster Recovery, Japan',
    "summary":'Enterprises continuously seek to improve their disaster recovery capability with less cost. External providers\' data center facilities and services are one option for effective DR. This Magic Quadrant helps I&O leaders address DR deployment in their business continuity management program in Japan.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, CTC, Fujitsu, IBM, INTEC, NEC, OGIS-RI, TIS, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Secure Web Gateways',
    "summary":'On-premises appliances continue to rule the SWG market, with a 71% market share (as measured by revenue). However, cloud-based SWG services are growing more rapidly, with a five-year historical compound annual growth rate of 32%, versus only 5% for appliances.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Barracuda Networks, Cisco, ContentKeeper, Forcepoint, iboss, McAfee, Sangfor, Sophos, Symantec, Trend Micro, Zscaler, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Security Awareness Computer-Based Training',
    "summary":'People influence security far more than any technology or policy. Security leaders must invest in tools that increase security awareness and influence behavior to support critical security business objectives through computer-based training.',
    "keywords":'Market Definition/Description, Market Trends, Market Growth, A Word to Security and Risk Management Leaders Seeking to Purchase Security Awareness CBTs, Magic Quadrant, Vendor Strengths and Cautions, Global Learning Systems, InfoSec Institute, Inspired eLearning, KnowBe4, MediaPro, PhishLine, PhishMe, SANS Institute, Security Innovation, Security Mentor, Terranova WW, Wombat Security Technologies, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Other Vendors of Note'
    },
{

    "title":'Security Information and Event Management',
    "summary":'Security and risk management leaders are implementing and expanding SIEM to improve early targeted attack detection and response. Advanced users seek SIEM with advanced profiling, analytics and response features.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AlienVault, BlackStratus, Dell Technologies (RSA), EventTracker, Exabeam, FireEye, Fortinet, IBM, LogRhythm, ManageEngine, McAfee, Micro Focus (ArcSight), Micro Focus (NetIQ), Rapid7, Securonix, SolarWinds, Splunk, Trustwave, Venustech, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, SIEM Vendor Landscape, Customer Requirements  Security Monitoring and Compliance Reporting for Systems, Users, Data and Applications, Scalability, SIEM Services, SIEM Alternatives'
    },
{

    "title":'Security Information and Event Management',
    "summary":'SIEM solution purchases are primarily driven by threat detection use cases. Security and risk management leaders buying a SIEM solution should leverage this research to evaluate their use cases and requirements against an increasingly complex vendor landscape with varying degrees of capabilities.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AlienVault, BlackStratus, Dell Technologies (RSA Security), EventTracker, Exabeam, FireEye, Fortinet, IBM, LogRhythm, ManageEngine, McAfee, Micro Focus (ArcSight), Micro Focus (NetIQ), Rapid7, Securonix, SolarWinds, Splunk, Trustwave, Venustech, Context, Product/Service Class Definition, Critical Capabilities Definition, Real-Time Monitoring, Incident Response and Management, Advanced Threat Defense, Business Context and Security Intel, User Monitoring, Data and Application Monitoring, Advanced Analytics, Deployment and Support Simplicity, Use Cases, Basic Security Monitoring, Advanced Threat Detection, Forensics and Incident Response, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Small Cell Equipment',
    "summary":'Via deployment of small cells, CSPs are now meeting the increasing demands of subscribers in terms of both network capacity and coverage. We assess 15 vendors of LTE and 3G femkeywordsells and picocells plus carrier Wi-Fi equipment, and we give guidance to infrastructure and operations leaders.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Airspan, Baicells, Cisco, Comba Telecom, CommScope, Corning, Ericsson, Fujitsu, Huawei, ip.access, NEC, Nokia, Ruckus, Samsung, ZTE, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Software Test Automation',
    "summary":'The need to support faster time to market with higher quality is driving the demand for effective functional test automation tools. We evaluate vendors in this space to help application leaders who are modernizing software development select test automation tools that best match their needs.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Hewlett Packard Enterprise, IBM, Micro Focus, Microsoft, Ranorex, SmartBear, TestPlant, Tricentis, Worksoft, Vendors Added and Dropped, Added, Dropped, Honorable Mentions, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Software Test Automation',
    "summary":'Selecting effective test automation tools is becoming more critical as business demands for faster application delivery and high quality intensify. This research helps application leaders who are modernizing software development to evaluate test automation tools across five common testing use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Hewlett Packard Enterprise, IBM, Micro Focus, Microsoft, Ranorex, SmartBear, TestPlant, Tricentis, Worksoft, Context, Product/Service Class Definition, Critical Capabilities Definition, Match to Nontechnical Role Skills, Match to Technical Role Skills, Templates and Accelerators, Business Process Validation, Change Impact Analysis, Cross-Platform Support, Cross-Browser Support, Real Device Testing, Dashboards and Reporting, Integration Capabilities, Open Source Support, Depth and Breadth of Testing, Custom Controls Extensibility, Prokeywordsols and Message Formats, Use Cases, Mobile Applications, Responsive Design, Packaged Applications, API Testing, Enterprise End-to-End Testing, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Solid-State Arrays',
    "summary":'Solid-state arrays have matured beyond performance-oriented workloads, and the benefits are now compelling for all primary storage plus old and new unexpected workloads. This Magic Quadrant will help IT leaders better understand SSA Vendors positioning in the market.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, EMC, Fujitsu, Hitachi Data Systems, HPE, Huawei, IBM, Kaminario, NetApp, Pure Storage, Tegile, Tintri, Violin Memory, X-IO Technologies, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Solid-State Arrays',
    "summary":'As concerns regarding their high price recede, solid-state arrays have improved performance, efficiency and manageability. Here, we analyze and evaluate 13 SSAs across five high-impact use cases and quantify product attractiveness against seven critical capabilities that are important to IT leaders.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, EMC XtremIO, Fujitsu Storage Eternus DX200F, Hitachi Data Systems VSP F, HPE 3PAR StoreServ All-Flash Arrays, IBM FlashSystem V9000, Kaminario K2, NetApp AFF, Pure Storage M-Series, SolidFire SF Series, Tegile T-Series, Tintri VMstore T5000 Series, Violin Memory Flash Storage Platform 7000 Series, X-IO ISE 800 Series, Context, Product/Service Class Definition, SSA, Critical Capabilities Definition, Ecosystem, Manageability, Multitenancy and Security, Performance, RAS, Scalability, Storage Efficiency, Use Cases, Online Transaction Processing, Server Virtualization, High-Performance Computing, Analytics, Virtual Desktop Infrastructure, Vendors Added and Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Strategic Sourcing Application Suites',
    "summary":'As end users increasingly require integrated suites and consumerlike user experiences to support and automate their strategic sourcing processes, vendors are investing to meet these expectations. Application leaders for procurement can use this report to assess the top solutions in this market.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, BravoSolution, Coupa, Determine, Digital Dimension (SynerTrade), Gatewit, GEP, IBM (Emptoris), Ivalua, Jaggaer, POOL4TOOL, SAP (Ariba), Scanmarket, Vortal, Zycus, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Supply Chain Planning System of Record',
    "summary":'This Magic Quadrant examines vendors that provide supply chain planning system-of-record solutions. Supply chain and IT leaders can use this research when evaluating and selecting an SCP system to underpin their journey to Stage 3 SCP maturity and beyond.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adexa, Arkieva, Barloworld Supply Chain Software, Blue Ridge, Demand Solutions, FuturMaster, GAINSystems, Infor, JDA Software, Kinaxis, Logility, NeoGrid, OM Partners, Oracle, Quintiq, SAP APO, SAS, Slimskeywordsk, Steelwedge, Syncron, ToolsGroup, Vendors Added and Dropped, Added, Dropped, Notable Mentions, E2open, Manhattan Associates, One Network Enterprises, Outperform, Relex Solutions, SAP IBP, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, How Gartner Analyzes the SCP SOR Market, Trends in the Market That Are Driving SCP Technology, The Five-Stage SCP Maturity Model, Key Actions to Help With SCP Technology Selection, Market Overview, Top-Rated SCP Capabilities by End Users, Best Practices and Common Issues for Companies Using SCP Technology, Top 10 Evolutions of SCP Technology to Counter These Issues, A Word of Advice for End-User Companies, A Word of Advice for SCP Vendors'
    },
{

    "title":'Supply Chain Planning System of Record',
    "summary":'This Magic Quadrant examines vendors that provide supply chain planning system-of-record solutions. Supply chain and IT leaders can use this research when evaluating and selecting an SCP system to underpin their journey to Stage 3 SCP maturity and beyond.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Adexa, Arkieva, Barloworld Supply Chain Software, Blue Ridge, Demand Solutions, FuturMaster, GAINSystems, Infor, JDA Software, Kinaxis, Logility, NeoGrid, OM Partners, Oracle, Quintiq, SAP APO, SAS, Slimskeywordsk, Steelwedge, Syncron, ToolsGroup, Vendors Added and Dropped, Added, Dropped, Notable Mentions, E2open, Manhattan Associates, One Network Enterprises, Outperform, Relex Solutions, SAP IBP, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, How Gartner Analyzes the SCP SOR Market, Trends in the Market That Are Driving SCP Technology, The Five-Stage SCP Maturity Model, Key Actions to Help With SCP Technology Selection, Market Overview, Top-Rated SCP Capabilities by End Users, Best Practices and Common Issues for Companies Using SCP Technology, Top 10 Evolutions of SCP Technology to Counter These Issues, A Word of Advice for End-User Companies, A Word of Advice for SCP Vendors'
    },
{

    "title":'Talent Management Suites',
    "summary":'Talent management suites help enterprises manage the key workforce processes of plan to source, acquire to onboard, perform to reward, and assess to develop. Chief HR officers and HR IT leaders developing workforce strategies should use this research to help them identify key and best-fit vendors.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Cornerstone OnDemand, Halogen Software, Haufe, Oracle, Saba, SAP (SuccessFactors), Skillsoft (SumTotal Systems), Talentsoft, Technomedia, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Talent Management Suites',
    "summary":'Talent management suite providers continue to add functionality to meet the growing demands of the digital workplace. Application leaders responsible for HR should focus on a product\'s critical capabilities when evaluating the vendors in this maturing market.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Cornerstone, Halogen Software, Haufe, Oracle, Saba Software, SAP, Skillsoft, Talentsoft, Technomedia, Context, Product/Service Class Definition, Critical Capabilities Definition, Recruiting, Onboarding, Performance and Goals, Learning Management, Career and Succession, Compensation Planning, Reporting and Analytics Tools, Overall Product Satisfaction, Vendor-Customer Relationships, Use Cases, Attract and Retain Talent, Develop the Workforce, Pay for Performance, High-Volume Talent Management, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Transportation Management Systems',
    "summary":'Controlling transportation costs, creating internal efficiencies, increasing visibility and securing transport capacity are currently the top motivators for investing in a TMS. Supply chain leaders should use this research to evaluate the TMS marketplace.',
    "keywords":'Market Definition/Description, Market Size and Vendors, Key Criteria for the 2018 TMS Magic Quadrant, Magic Quadrant, Vendor Strengths and Cautions, 3Gtms, 3T Logistics, BluJay, C.H. Robinson (TMC), Cloud Logistics, inet-logistics, JDA, Kuebix, Manhattan Associates, MercuryGate, Oracle, SAP, Transplace, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Notable Mentions, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Unified Communications',
    "summary":'As the enterprise UC market continues to mature, we expect more consolidation and increased user expectations  prompting an emphasis on Vendors telephony capabilities and financial viability. Enterprise planners must match their own priorities to vendor strengths before committing to a solution.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, ALE, Avaya, Cisco, Huawei, Interactive Intelligence, Microsoft, Mitel, NEC, ShoreTel, Unify, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Unified Communications',
    "summary":'Changes to the ways people work together are redefining how IT leaders should assess the product capabilities of unified communications providers. This is placing an increased focus on single-vendor platforms to meet the majority of core UC functional requirements.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, ALE, Avaya, Cisco, Huawei, Interactive Intelligence, Microsoft, Mitel, NEC, ShoreTel, Unify, Context, Product/Service Class Definition, Critical Capabilities Definition, Telephony, Conferencing, Instant Messaging and Presence, Workstream Collaboration, Clients, Interoperability/Integration, Administration, Hybrid On-Premises/Cloud, Use Cases, Full UC With Strong Telephony, Full UC With Strong Collaboration, Full UC for Midsize Organization, Ability to Offer Hybrid Solutions, Vendors Added and Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Unified Communications as a Service, North America',
    "summary":'UCaaS products vary in richness of services, scalability, functionality, regional coverage and ability to address different use cases. To assist application leaders in their UCaaS vendor selection process, we evaluated 15 vendors using 10 critical capabilities and four use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, 8x8, AT&T, BroadSoft, BT, Fuze, Google, Masergy, Microsoft, Mitel, NTT Group, Orange Business Services, RingCentral, Star2Star, Verizon, West, Context, Product/Service Class Definition, Critical Capabilities Definition, Telephony, Mobility, Meetings (Conferencing), Customer Self-Provisioning Portals, Installation and Integration, Hybrid Capabilities, Customer Service and Support, Packaged for Midsize Enterprise, Scaled for Large Enterprise Support, Integrated Contact Center Support, Use Cases, Enterprise UC Requirement, Midmarket UC Requirement, Hybrid UC Requirement, Integrated Contact Center Requirement, Vendors Added and Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Unified Endpoint Management Tools',
    "summary":'Enterprise mobility management suites connect mobile devices to enterprise workflows while supporting the perpetual growth in device numbers and types. I&O leaders responsible for mobile and endpoint strategies, must maintain focus on near- and long-term goals in this rapidly changing market.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, BlackBerry, Cisco, Citrix, IBM, Ivanti, Matrix42, Microsoft, MobileIron, NationSky, Snow Software, Sophos, SOTI, VMware, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, EMM Is the \'Glue', Mobile Device Management, Mobile Application Management, Containment, Mobile Identity and Access, EMM Executes File-Level Protection at the Edge, Unified Endpoint Management'
    },
{

    "title":'Unified Endpoint Management Tools',
    "summary":'Enterprise mobility management suite functionality is evolving into unified endpoint management, which adds traditional client and select EMM manageable IoT use-case management. Before selecting an EMM vendor in this constantly changing market, I&O leaders need to determine their desired use cases.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, BlackBerry, Citrix, IBM, Ivanti, Microsoft, MobileIron, Sophos, SOTI, VMware, Context, Product/Service Class Definition, Critical Capabilities Definition, Architecture and Scalability, Administration and Usability, Device Configuration and Management, Mobile App Management, Secure Content Access/Distribution, Mobile Identity and Access, Containment, Client Management, Device Security and Compliance, EMM Manageable IoT Devices, Use Cases, General-Purpose, Regulated Industries, Unified Endpoint Management, Special-Purpose Device Support, Cloud-Centric, Unmanaged Device Support, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Unified Threat Management',
    "summary":'SMB multifunction firewalls, or UTM, provide SMBs and distributed enterprises with multiple security functions in a single appliance. Network security leaders should use this research to evaluate performance, security, ease of use, local support and technology\'s ability to handle new SMB practices.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Barracuda Networks, Check Point Software Technologies, Cisco, Fortinet, Hillstone Networks, Huawei, Juniper Networks, Rohde & Schwarz Cybersecurity, SonicWall, Sophos, Stormshield, Untangle, Venustech, WatchGuard, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Inclusion Criteria, Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Will UTM Become a Meta-Security Platform?, Ease of Use and Price Continue to Drive SMB Purchases, Ransomware and Encrypted Traffic Are Top Challenges for SMBs, The End of the Thick 'All-in-One' Physical Appliance Era Is Slowly Approaching'
    },
{

    "title":'Utilities Customer Information Systems',
    "summary":'We provide updated Vendors positioning in this important utility software market. CIOs should use this research to identify vendors that address evolving business needs in billing and customer service areas such as rising consumers\' expectations and the impact of sector digital transformation.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Advanced Utility Systems, Cayenta, efluid, Ferranti Computer Systems, Fluentgrid, Engineering, Indra, Itineris, Open International, Oracle, SAP, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Pace Layering as an Architectural Approach to Address Emerging Requirements'
    },
{

    "title":'Warehouse Management Systems',
    "summary":'The WMS market is very mature, but differentiation continues to exist  most notably in usability, adaptability, intelligence and how well solutions orchestrate end-to-end logistics processes. Supply chain and IT leaders should use this research to understand the current state of the WMS market.',
    "keywords":'Market Definition/Description, Macro Issues Influencing the WMS Market, Supply Chain Execution Convergence, Deployment Model, Global Go-to-Market, User Experience, Cost of Ownership, Warehouse Environment, Small and Midsize Enterprise WMS, Extreme Verticalization, Zero-Modification Implementations, Partner Ecosystems, Magic Quadrant, Vendor Strengths and Cautions, HighJump, Infor, JDA Software, Made4net, Manhattan Associates, Microlistics, Oracle, Reply, SAP, Softeon, Synergy Logistics, Tecsys, Vinculum, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Web Application Firewalls',
    "summary":'The WAF market is growing, with new use cases and security requirements ranging from \'good enough\' security for compliance to protection against targeted attacks. Enterprise security teams should evaluate how WAFs can provide high security that is also easy to consume and manage.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, AdNovum, Akamai, Barracuda Networks, Citrix, CloudFlare, DenyAll, Ergon Informatik, F5, Fortinet, Imperva, NSFOCUS, Penta Security Systems, Positive Technologies, Radware, Trustwave, United Security Providers, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Enterprises Need a Next-Generation WAF, but the Vendors Are Missing, The Future of WAF Is Brighter in the Cloud'
    },
{

    "title":'Web Content Management',
    "summary":'Digitalization brings both new opportunities and confusion to even the most carefully planned selection processes for WCM. CIOs and IT leaders aiming to boost the effectiveness of their digital business strategy should use this document to help them select the most appropriate vendor and solution.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Acquia, Adobe, Automattic, CoreMedia, Crownpeak, Episerver, e-Spirit, eZ Systems, GX Software, Hippo, IBM, Kentico Software, OpenText, Oracle, Progress, SDL, Sitecore, Squiz, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Web Content Management',
    "summary":'Organizations find little differentiation in WCM products, yet selecting the right product remains complex. Application leaders responsible for CRM and customer experience need to pay extra close attention to long-range future plans in order to make the right choice today.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Acquia, Adobe, Automattic, CoreMedia, Crownpeak, Episerver, e-Spirit, eZ Systems, GX Software, Hippo, IBM, Kentico Software, OpenText (TeamSite), OpenText (WEM), Oracle, Progress, SDL, Sitecore, Squiz, Context, Product/Service Class Definition, Critical Capabilities Definition, Usability, Interoperability, Engagement Analytics, Mobility/Multichannel, Content Delivery, Personalization, Architecture, Cloud Capabilities, Use Cases, Digital Marketing Effectiveness, Contextualization of Delivered Experiences, Digital Commerce, Digital Workplace Initiatives, Composite Content Applications, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Wired and Wireless LAN Access Infrastructure',
    "summary":'Enterprise LAN vendors providing access layer connectivity must respond to changing demands. Infrastructure and operations leaders should evaluate vendors based on their ability to provide an intelligent access layer capable of network automation that addresses all of the business requirements.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Aerohive, ALE, Allied Telesis, Brocade (Ruckus), Cisco, Dell EMC, D-Link, Extreme Networks, Fortinet, HPE (Aruba), Huawei, Juniper Networks, Mist Systems, Mojo Networks, New H3C, Riverbed (Xirrus), Vendors Added and Dropped, Added, Dropped, Other Vendors, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview, Clients Seek Stability, Flexibility, What\'s Changed in the Market, Enterprise Requirements Focus on Network Application Services, IoT Requirements Drive Software Innovation, Consolidation Continues, New Providers Emerge'
    },
{

    "title":'Wired and Wireless LAN Access Infrastructure',
    "summary":'Wired and wireless LAN vendors have differing abilities to meet mobile enterprise requirements. Gartner has examined 16 vendors to determine how each addresses the needs of infrastructure and operations leaders for five distinct enterprise use cases, based on five critical capabilities.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Aerohive Networks, ALE, Avaya, Allied Telesis, Brocade (Ruckus Wireless), Cisco, D-Link, Dell, Extreme Networks, Fortinet, HPE (Aruba Networks), Huawei Technologies, Juniper Networks, Xirrus, Zebra, ZTE, Context, Product/Service Class Definition, Critical Capabilities Definition, Wired Access, WLAN Access, Network Access/Guest Access/BYOD, Management and Administration, Additional Network Services, Use Cases, Enterprise Unified Wired and WLAN Access, Enterprise Wired-Only Connectivity, All-Wireless Office, SME and/or Remote Branch Office, IaaS or Managed Service, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Wireline Telecom Services U.S.',
    "summary":'Enterprises with regional networking requirements in the U.S. have a wide choice of service providers. I&O leaders responsible for WAN infrastructure modernization should evaluate these providers\' newly available services, such as direct cloud connections, hybrid WAN, SD-WAN, vCPE and NFV services.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, AT&T, CenturyLink, Comcast Business, GTT, Level 3 Communications, Masergy, Spectrum Enterprise, Sprint, Verizon, Windstream Communications, Context, Product/Service Class Definition, Critical Capabilities Definition, MPLS Services, SIP Trunks, IPTF and On-Net Voice, Dedicated Internet, Metro (SONET, Wavelength, Ethernet), Managed and Redundant Broadband, Ethernet WAN, Public Cloud Connect, Managed SD-WAN, Use Cases, Large Enterprise, Midsize Enterprise, Data Center Interconnect, Branch Office, Vendors Added and Dropped, Added, Dropped, Inclusion Criteria, Critical Capabilities Rating'
    },
{

    "title":'Workforce Engagement Management',
    "summary":'A growing market awareness of the importance of the employees in customer engagement centers is triggering an adjustment in the technologies needed to manage their day-to-day roles. Our vendor evaluation will help sourcing and vendor management leaders make the right choice for their organizations.',
    "keywords":'Market Definition/Description, Magic Quadrant, Vendor Strengths and Cautions, Aspect, Calabrio, Genesys, Interactive Intelligence, Nice, Noble Systems, Teleopti, Verint, Vendors Added and Dropped, Added, Dropped, Inclusion and Exclusion Criteria, Evaluation Criteria, Ability to Execute, Completeness of Vision, Quadrant Descriptions, Leaders, Challengers, Visionaries, Niche Players, Context, Market Overview'
    },
{

    "title":'Workforce Engagement Management',
    "summary":'Application leaders need to elevate their commitment to enhancing employee engagement. What drives this engagement will depend on the type of work undertaken and employee personalities. Here we look at the capabilities that technology providers need to offer to support stronger employee engagement.',
    "keywords":'What You Need to Know, Analysis, Critical Capabilities Use-Case Graphics, Vendors, Aspect, Calabrio, Genesys, NICE, OpenText, Verint, Zoom, Context, Product/Service Class Definition, Critical Capabilities Definition, Recruitment and Onboarding, Evaluation and Improvement, Time Management, Assistance and Task Management, Metrics and Recognition, Voice of the Employee, Use Cases, Information Access, Process Efficiency, Customer Intelligence, Intelligent Dialogue, Inclusion Criteria, Critical Capabilities Rating'
    },

],

]


