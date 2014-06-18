# -*- coding: utf-8 -*-

# This script maps wikipedia language codes to its corresponding iso-639-3 code.

import codecs, re

# from http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab
iso6963 = """Id  Print_Name  Inverted_Name
aaa  Ghotuo  Ghotuo
aab  Alumu-Tesu  Alumu-Tesu
aac  Ari  Ari
aad  Amal  Amal
aae  Arbëreshë Albanian  Albanian, Arbëreshë
aaf  Aranadan  Aranadan
aag  Ambrak  Ambrak
aah  Abu' Arapesh  Arapesh, Abu'
aai  Arifama-Miniafia  Arifama-Miniafia
aak  Ankave  Ankave
aal  Afade  Afade
aam  Aramanik  Aramanik
aan  Anambé  Anambé
aao  Algerian Saharan Arabic  Arabic, Algerian Saharan
aap  Pará Arára  Arára, Pará
aaq  Eastern Abnaki  Abnaki, Eastern
aar  Afar  Afar
aas  Aasáx  Aasáx
aat  Arvanitika Albanian  Albanian, Arvanitika
aau  Abau  Abau
aaw  Solong  Solong
aax  Mandobo Atas  Mandobo Atas
aaz  Amarasi  Amarasi
aba  Abé  Abé
abb  Bankon  Bankon
abc  Ambala Ayta  Ayta, Ambala
abd  Manide  Manide
abe  Western Abnaki  Abnaki, Western
abf  Abai Sungai  Abai Sungai
abg  Abaga  Abaga
abh  Tajiki Arabic  Arabic, Tajiki
abi  Abidji  Abidji
abj  Aka-Bea  Aka-Bea
abk  Abkhazian  Abkhazian
abl  Lampung Nyo  Lampung Nyo
abm  Abanyom  Abanyom
abn  Abua  Abua
abo  Abon  Abon
abp  Abellen Ayta  Ayta, Abellen
abq  Abaza  Abaza
abr  Abron  Abron
abs  Ambonese Malay  Malay, Ambonese
abt  Ambulas  Ambulas
abu  Abure  Abure
abv  Baharna Arabic  Arabic, Baharna
abw  Pal  Pal
abx  Inabaknon  Inabaknon
aby  Aneme Wake  Aneme Wake
abz  Abui  Abui
aca  Achagua  Achagua
acb  Áncá  Áncá
acd  Gikyode  Gikyode
ace  Achinese  Achinese
acf  Saint Lucian Creole French  Creole French, Saint Lucian
ach  Acoli  Acoli
aci  Aka-Cari  Aka-Cari
ack  Aka-Kora  Aka-Kora
acl  Akar-Bale  Akar-Bale
acm  Mesopotamian Arabic  Arabic, Mesopotamian
acn  Achang  Achang
acp  Eastern Acipa  Acipa, Eastern
acq  Ta'izzi-Adeni Arabic  Arabic, Ta'izzi-Adeni
acr  Achi  Achi
acs  Acroá  Acroá
act  Achterhoeks  Achterhoeks
acu  Achuar-Shiwiar  Achuar-Shiwiar
acv  Achumawi  Achumawi
acw  Hijazi Arabic  Arabic, Hijazi
acx  Omani Arabic  Arabic, Omani
acy  Cypriot Arabic  Arabic, Cypriot
acz  Acheron  Acheron
ada  Adangme  Adangme
adb  Adabe  Adabe
add  Dzodinka  Dzodinka
ade  Adele  Adele
adf  Dhofari Arabic  Arabic, Dhofari
adg  Andegerebinha  Andegerebinha
adh  Adhola  Adhola
adi  Adi  Adi
adj  Adioukrou  Adioukrou
adl  Galo  Galo
adn  Adang  Adang
ado  Abu  Abu
adp  Adap  Adap
adq  Adangbe  Adangbe
adr  Adonara  Adonara
ads  Adamorobe Sign Language  Adamorobe Sign Language
adt  Adnyamathanha  Adnyamathanha
adu  Aduge  Aduge
adw  Amundava  Amundava
adx  Amdo Tibetan  Tibetan, Amdo
ady  Adygei  Adygei
ady  Adyghe  Adyghe
adz  Adzera  Adzera
aea  Areba  Areba
aeb  Tunisian Arabic  Arabic, Tunisian
aec  Saidi Arabic  Arabic, Saidi
aed  Argentine Sign Language  Argentine Sign Language
aee  Northeast Pashayi  Pashayi, Northeast
aek  Haeke  Haeke
ael  Ambele  Ambele
aem  Arem  Arem
aen  Armenian Sign Language  Armenian Sign Language
aeq  Aer  Aer
aer  Eastern Arrernte  Arrernte, Eastern
aes  Alsea  Alsea
aeu  Akeu  Akeu
aew  Ambakich  Ambakich
aey  Amele  Amele
aez  Aeka  Aeka
afb  Gulf Arabic  Arabic, Gulf
afd  Andai  Andai
afe  Putukwam  Putukwam
afg  Afghan Sign Language  Afghan Sign Language
afh  Afrihili  Afrihili
afi  Akrukay  Akrukay
afk  Nanubae  Nanubae
afn  Defaka  Defaka
afo  Eloyi  Eloyi
afp  Tapei  Tapei
afr  Afrikaans  Afrikaans
afs  Afro-Seminole Creole  Creole, Afro-Seminole
aft  Afitti  Afitti
afu  Awutu  Awutu
afz  Obokuitai  Obokuitai
aga  Aguano  Aguano
agb  Legbo  Legbo
agc  Agatu  Agatu
agd  Agarabi  Agarabi
age  Angal  Angal
agf  Arguni  Arguni
agg  Angor  Angor
agh  Ngelima  Ngelima
agi  Agariya  Agariya
agj  Argobba  Argobba
agk  Isarog Agta  Agta, Isarog
agl  Fembe  Fembe
agm  Angaataha  Angaataha
agn  Agutaynen  Agutaynen
ago  Tainae  Tainae
agq  Aghem  Aghem
agr  Aguaruna  Aguaruna
ags  Esimbi  Esimbi
agt  Central Cagayan Agta  Agta, Central Cagayan
agu  Aguacateco  Aguacateco
agv  Remontado Dumagat  Dumagat, Remontado
agw  Kahua  Kahua
agx  Aghul  Aghul
agy  Southern Alta  Alta, Southern
agz  Mt. Iriga Agta  Agta, Mt. Iriga
aha  Ahanta  Ahanta
ahb  Axamb  Axamb
ahg  Qimant  Qimant
ahh  Aghu  Aghu
ahi  Tiagbamrin Aizi  Aizi, Tiagbamrin
ahk  Akha  Akha
ahl  Igo  Igo
ahm  Mobumrin Aizi  Aizi, Mobumrin
ahn  Àhàn  Àhàn
aho  Ahom  Ahom
ahp  Aproumu Aizi  Aizi, Aproumu
ahr  Ahirani  Ahirani
ahs  Ashe  Ashe
aht  Ahtena  Ahtena
aia  Arosi  Arosi
aib  Ainu (China)  Ainu (China)
aic  Ainbai  Ainbai
aid  Alngith  Alngith
aie  Amara  Amara
aif  Agi  Agi
aig  Antigua and Barbuda Creole English  Creole English, Antigua and Barbuda
aih  Ai-Cham  Ai-Cham
aii  Assyrian Neo-Aramaic  Neo-Aramaic, Assyrian
aij  Lishanid Noshan  Lishanid Noshan
aik  Ake  Ake
ail  Aimele  Aimele
aim  Aimol  Aimol
ain  Ainu (Japan)  Ainu (Japan)
aio  Aiton  Aiton
aip  Burumakok  Burumakok
aiq  Aimaq  Aimaq
air  Airoran  Airoran
ais  Nataoran Amis  Amis, Nataoran
ait  Arikem  Arikem
aiw  Aari  Aari
aix  Aighon  Aighon
aiy  Ali  Ali
aja  Aja (Sudan)  Aja (Sudan)
ajg  Aja (Benin)  Aja (Benin)
aji  Ajië  Ajië
ajn  Andajin  Andajin
ajp  South Levantine Arabic  Arabic, South Levantine
ajt  Judeo-Tunisian Arabic  Arabic, Judeo-Tunisian
aju  Judeo-Moroccan Arabic  Arabic, Judeo-Moroccan
ajw  Ajawa  Ajawa
ajz  Amri Karbi  Karbi, Amri
aka  Akan  Akan
akb  Batak Angkola  Batak Angkola
akc  Mpur  Mpur
akd  Ukpet-Ehom  Ukpet-Ehom
ake  Akawaio  Akawaio
akf  Akpa  Akpa
akg  Anakalangu  Anakalangu
akh  Angal Heneng  Angal Heneng
aki  Aiome  Aiome
akj  Aka-Jeru  Aka-Jeru
akk  Akkadian  Akkadian
akl  Aklanon  Aklanon
akm  Aka-Bo  Aka-Bo
ako  Akurio  Akurio
akp  Siwu  Siwu
akq  Ak  Ak
akr  Araki  Araki
aks  Akaselem  Akaselem
akt  Akolet  Akolet
aku  Akum  Akum
akv  Akhvakh  Akhvakh
akw  Akwa  Akwa
akx  Aka-Kede  Aka-Kede
aky  Aka-Kol  Aka-Kol
akz  Alabama  Alabama
ala  Alago  Alago
alc  Qawasqar  Qawasqar
ald  Alladian  Alladian
ale  Aleut  Aleut
alf  Alege  Alege
alh  Alawa  Alawa
ali  Amaimon  Amaimon
alj  Alangan  Alangan
alk  Alak  Alak
all  Allar  Allar
alm  Amblong  Amblong
aln  Gheg Albanian  Albanian, Gheg
alo  Larike-Wakasihu  Larike-Wakasihu
alp  Alune  Alune
alq  Algonquin  Algonquin
alr  Alutor  Alutor
als  Tosk Albanian  Albanian, Tosk
alt  Southern Altai  Altai, Southern
alu  'Are'are  'Are'are
alw  Alaba-K’abeena  Alaba-K’abeena
alw  Wanbasana  Wanbasana
alx  Amol  Amol
aly  Alyawarr  Alyawarr
alz  Alur  Alur
ama  Amanayé  Amanayé
amb  Ambo  Ambo
amc  Amahuaca  Amahuaca
ame  Yanesha'  Yanesha'
amf  Hamer-Banna  Hamer-Banna
amg  Amurdak  Amurdak
amh  Amharic  Amharic
ami  Amis  Amis
amj  Amdang  Amdang
amk  Ambai  Ambai
aml  War-Jaintia  War-Jaintia
amm  Ama (Papua New Guinea)  Ama (Papua New Guinea)
amn  Amanab  Amanab
amo  Amo  Amo
amp  Alamblak  Alamblak
amq  Amahai  Amahai
amr  Amarakaeri  Amarakaeri
ams  Southern Amami-Oshima  Amami-Oshima, Southern
amt  Amto  Amto
amu  Guerrero Amuzgo  Amuzgo, Guerrero
amv  Ambelau  Ambelau
amw  Western Neo-Aramaic  Neo-Aramaic, Western
amx  Anmatyerre  Anmatyerre
amy  Ami  Ami
amz  Atampaya  Atampaya
ana  Andaqui  Andaqui
anb  Andoa  Andoa
anc  Ngas  Ngas
and  Ansus  Ansus
ane  Xârâcùù  Xârâcùù
anf  Animere  Animere
ang  Old English (ca. 450-1100)  English, Old (ca. 450-1100)
anh  Nend  Nend
ani  Andi  Andi
anj  Anor  Anor
ank  Goemai  Goemai
anl  Anu-Hkongso Chin  Chin, Anu-Hkongso
anm  Anal  Anal
ann  Obolo  Obolo
ano  Andoque  Andoque
anp  Angika  Angika
anq  Jarawa (India)  Jarawa (India)
anr  Andh  Andh
ans  Anserma  Anserma
ant  Antakarinya  Antakarinya
anu  Anuak  Anuak
anv  Denya  Denya
anw  Anaang  Anaang
anx  Andra-Hus  Andra-Hus
any  Anyin  Anyin
anz  Anem  Anem
aoa  Angolar  Angolar
aob  Abom  Abom
aoc  Pemon  Pemon
aod  Andarum  Andarum
aoe  Angal Enen  Angal Enen
aof  Bragat  Bragat
aog  Angoram  Angoram
aoh  Arma  Arma
aoi  Anindilyakwa  Anindilyakwa
aoj  Mufian  Mufian
aok  Arhö  Arhö
aol  Alor  Alor
aom  Ömie  Ömie
aon  Bumbita Arapesh  Arapesh, Bumbita
aor  Aore  Aore
aos  Taikat  Taikat
aot  A'tong  A'tong
aou  A'ou  A'ou
aox  Atorada  Atorada
aoz  Uab Meto  Uab Meto
apb  Sa'a  Sa'a
apc  North Levantine Arabic  Arabic, North Levantine
apd  Sudanese Arabic  Arabic, Sudanese
ape  Bukiyip  Bukiyip
apf  Pahanan Agta  Agta, Pahanan
apg  Ampanang  Ampanang
aph  Athpariya  Athpariya
api  Apiaká  Apiaká
apj  Jicarilla Apache  Apache, Jicarilla
apk  Kiowa Apache  Apache, Kiowa
apl  Lipan Apache  Apache, Lipan
apm  Mescalero-Chiricahua Apache  Apache, Mescalero-Chiricahua
apn  Apinayé  Apinayé
apo  Ambul  Ambul
app  Apma  Apma
apq  A-Pucikwar  A-Pucikwar
apr  Arop-Lokep  Arop-Lokep
aps  Arop-Sissano  Arop-Sissano
apt  Apatani  Apatani
apu  Apurinã  Apurinã
apv  Alapmunte  Alapmunte
apw  Western Apache  Apache, Western
apx  Aputai  Aputai
apy  Apalaí  Apalaí
apz  Safeyoka  Safeyoka
aqc  Archi  Archi
aqd  Ampari Dogon  Dogon, Ampari
aqg  Arigidi  Arigidi
aqm  Atohwaim  Atohwaim
aqn  Northern Alta  Alta, Northern
aqp  Atakapa  Atakapa
aqr  Arhâ  Arhâ
aqz  Akuntsu  Akuntsu
ara  Arabic  Arabic
arb  Standard Arabic  Arabic, Standard
arc  Imperial Aramaic (700-300 BCE)  Aramaic, Imperial (700-300 BCE)
arc  Official Aramaic (700-300 BCE)  Aramaic, Official (700-300 BCE)
ard  Arabana  Arabana
are  Western Arrarnta  Arrarnta, Western
arg  Aragonese  Aragonese
arh  Arhuaco  Arhuaco
ari  Arikara  Arikara
arj  Arapaso  Arapaso
ark  Arikapú  Arikapú
arl  Arabela  Arabela
arn  Mapuche  Mapuche
arn  Mapudungun  Mapudungun
aro  Araona  Araona
arp  Arapaho  Arapaho
arq  Algerian Arabic  Arabic, Algerian
arr  Karo (Brazil)  Karo (Brazil)
ars  Najdi Arabic  Arabic, Najdi
aru  Arawá  Arawá
aru  Aruá (Amazonas State)  Aruá (Amazonas State)
arv  Arbore  Arbore
arw  Arawak  Arawak
arx  Aruá (Rodonia State)  Aruá (Rodonia State)
ary  Moroccan Arabic  Arabic, Moroccan
arz  Egyptian Arabic  Arabic, Egyptian
asa  Asu (Tanzania)  Asu (Tanzania)
asb  Assiniboine  Assiniboine
asc  Casuarina Coast Asmat  Asmat, Casuarina Coast
asd  Asas  Asas
ase  American Sign Language  American Sign Language
asf  Australian Sign Language  Australian Sign Language
asg  Cishingini  Cishingini
ash  Abishira  Abishira
asi  Buruwai  Buruwai
asj  Sari  Sari
ask  Ashkun  Ashkun
asl  Asilulu  Asilulu
asm  Assamese  Assamese
asn  Xingú Asuriní  Asuriní, Xingú
aso  Dano  Dano
asp  Algerian Sign Language  Algerian Sign Language
asq  Austrian Sign Language  Austrian Sign Language
asr  Asuri  Asuri
ass  Ipulo  Ipulo
ast  Asturian  Asturian
ast  Asturleonese  Asturleonese
ast  Bable  Bable
ast  Leonese  Leonese
asu  Tocantins Asurini  Asurini, Tocantins
asv  Asoa  Asoa
asw  Australian Aborigines Sign Language  Australian Aborigines Sign Language
asx  Muratayak  Muratayak
asy  Yaosakor Asmat  Asmat, Yaosakor
asz  As  As
ata  Pele-Ata  Pele-Ata
atb  Zaiwa  Zaiwa
atc  Atsahuaca  Atsahuaca
atd  Ata Manobo  Manobo, Ata
ate  Atemble  Atemble
atg  Ivbie North-Okpela-Arhe  Ivbie North-Okpela-Arhe
ati  Attié  Attié
atj  Atikamekw  Atikamekw
atk  Ati  Ati
atl  Mt. Iraya Agta  Agta, Mt. Iraya
atm  Ata  Ata
atn  Ashtiani  Ashtiani
ato  Atong  Atong
atp  Pudtol Atta  Atta, Pudtol
atq  Aralle-Tabulahan  Aralle-Tabulahan
atr  Waimiri-Atroari  Waimiri-Atroari
ats  Gros Ventre  Gros Ventre
att  Pamplona Atta  Atta, Pamplona
atu  Reel  Reel
atv  Northern Altai  Altai, Northern
atw  Atsugewi  Atsugewi
atx  Arutani  Arutani
aty  Aneityum  Aneityum
atz  Arta  Arta
aua  Asumboa  Asumboa
aub  Alugu  Alugu
auc  Waorani  Waorani
aud  Anuta  Anuta
aue  =/Kx'au//'ein  =/Kx'au//'ein
aug  Aguna  Aguna
auh  Aushi  Aushi
aui  Anuki  Anuki
auj  Awjilah  Awjilah
auk  Heyo  Heyo
aul  Aulua  Aulua
aum  Asu (Nigeria)  Asu (Nigeria)
aun  Molmo One  One, Molmo
auo  Auyokawa  Auyokawa
aup  Makayam  Makayam
auq  Anus  Anus
auq  Korur  Korur
aur  Aruek  Aruek
aut  Austral  Austral
auu  Auye  Auye
auw  Awyi  Awyi
aux  Aurá  Aurá
auy  Awiyaana  Awiyaana
auz  Uzbeki Arabic  Arabic, Uzbeki
ava  Avaric  Avaric
avb  Avau  Avau
avd  Alviri-Vidari  Alviri-Vidari
ave  Avestan  Avestan
avi  Avikam  Avikam
avk  Kotava  Kotava
avl  Eastern Egyptian Bedawi Arabic  Arabic, Eastern Egyptian Bedawi
avm  Angkamuthi  Angkamuthi
avn  Avatime  Avatime
avo  Agavotaguerra  Agavotaguerra
avs  Aushiri  Aushiri
avt  Au  Au
avu  Avokaya  Avokaya
avv  Avá-Canoeiro  Avá-Canoeiro
awa  Awadhi  Awadhi
awb  Awa (Papua New Guinea)  Awa (Papua New Guinea)
awc  Cicipu  Cicipu
awe  Awetí  Awetí
awg  Anguthimri  Anguthimri
awh  Awbono  Awbono
awi  Aekyom  Aekyom
awk  Awabakal  Awabakal
awm  Arawum  Arawum
awn  Awngi  Awngi
awo  Awak  Awak
awr  Awera  Awera
aws  South Awyu  Awyu, South
awt  Araweté  Araweté
awu  Central Awyu  Awyu, Central
awv  Jair Awyu  Awyu, Jair
aww  Awun  Awun
awx  Awara  Awara
awy  Edera Awyu  Awyu, Edera
axb  Abipon  Abipon
axe  Ayerrerenge  Ayerrerenge
axg  Mato Grosso Arára  Arára, Mato Grosso
axk  Yaka (Central African Republic)  Yaka (Central African Republic)
axl  Lower Southern Aranda  Aranda, Lower Southern
axm  Middle Armenian  Armenian, Middle
axx  Xârâgurè  Xârâgurè
aya  Awar  Awar
ayb  Ayizo Gbe  Gbe, Ayizo
ayc  Southern Aymara  Aymara, Southern
ayd  Ayabadhu  Ayabadhu
aye  Ayere  Ayere
ayg  Ginyanga  Ginyanga
ayh  Hadrami Arabic  Arabic, Hadrami
ayi  Leyigha  Leyigha
ayk  Akuku  Akuku
ayl  Libyan Arabic  Arabic, Libyan
aym  Aymara  Aymara
ayn  Sanaani Arabic  Arabic, Sanaani
ayo  Ayoreo  Ayoreo
ayp  North Mesopotamian Arabic  Arabic, North Mesopotamian
ayq  Ayi (Papua New Guinea)  Ayi (Papua New Guinea)
ayr  Central Aymara  Aymara, Central
ays  Sorsogon Ayta  Ayta, Sorsogon
ayt  Magbukun Ayta  Ayta, Magbukun
ayu  Ayu  Ayu
ayy  Tayabas Ayta  Ayta, Tayabas
ayz  Mai Brat  Mai Brat
aza  Azha  Azha
azb  South Azerbaijani  Azerbaijani, South
azd  Eastern Durango Nahuatl  Nahuatl, Eastern Durango
aze  Azerbaijani  Azerbaijani
azg  San Pedro Amuzgos Amuzgo  Amuzgo, San Pedro Amuzgos
azj  North Azerbaijani  Azerbaijani, North
azm  Ipalapa Amuzgo  Amuzgo, Ipalapa
azn  Western Durango Nahuatl  Nahuatl, Western Durango
azo  Awing  Awing
azt  Faire Atta  Atta, Faire
azz  Highland Puebla Nahuatl  Nahuatl, Highland Puebla
baa  Babatana  Babatana
bab  Bainouk-Gunyuño  Bainouk-Gunyuño
bac  Badui  Badui
bae  Baré  Baré
baf  Nubaca  Nubaca
bag  Tuki  Tuki
bah  Bahamas Creole English  Creole English, Bahamas
baj  Barakai  Barakai
bak  Bashkir  Bashkir
bal  Baluchi  Baluchi
bam  Bambara  Bambara
ban  Balinese  Balinese
bao  Waimaha  Waimaha
bap  Bantawa  Bantawa
bar  Bavarian  Bavarian
bas  Basa (Cameroon)  Basa (Cameroon)
bau  Bada (Nigeria)  Bada (Nigeria)
bav  Vengo  Vengo
baw  Bambili-Bambui  Bambili-Bambui
bax  Bamun  Bamun
bay  Batuley  Batuley
bba  Baatonum  Baatonum
bbb  Barai  Barai
bbc  Batak Toba  Batak Toba
bbd  Bau  Bau
bbe  Bangba  Bangba
bbf  Baibai  Baibai
bbg  Barama  Barama
bbh  Bugan  Bugan
bbi  Barombi  Barombi
bbj  Ghomálá'  Ghomálá'
bbk  Babanki  Babanki
bbl  Bats  Bats
bbm  Babango  Babango
bbn  Uneapa  Uneapa
bbo  Konabéré  Konabéré
bbo  Northern Bobo Madaré  Bobo Madaré, Northern
bbp  West Central Banda  Banda, West Central
bbq  Bamali  Bamali
bbr  Girawa  Girawa
bbs  Bakpinka  Bakpinka
bbt  Mburku  Mburku
bbu  Kulung (Nigeria)  Kulung (Nigeria)
bbv  Karnai  Karnai
bbw  Baba  Baba
bbx  Bubia  Bubia
bby  Befang  Befang
bbz  Babalia Creole Arabic  Creole Arabic, Babalia
bca  Central Bai  Bai, Central
bcb  Bainouk-Samik  Bainouk-Samik
bcc  Southern Balochi  Balochi, Southern
bcd  North Babar  Babar, North
bce  Bamenyam  Bamenyam
bcf  Bamu  Bamu
bcg  Baga Binari  Baga Binari
bch  Bariai  Bariai
bci  Baoulé  Baoulé
bcj  Bardi  Bardi
bck  Bunaba  Bunaba
bcl  Central Bikol  Bikol, Central
bcm  Bannoni  Bannoni
bcn  Bali (Nigeria)  Bali (Nigeria)
bco  Kaluli  Kaluli
bcp  Bali (Democratic Republic of Congo)  Bali (Democratic Republic of Congo)
bcq  Bench  Bench
bcr  Babine  Babine
bcs  Kohumono  Kohumono
bct  Bendi  Bendi
bcu  Awad Bing  Awad Bing
bcv  Shoo-Minda-Nye  Shoo-Minda-Nye
bcw  Bana  Bana
bcy  Bacama  Bacama
bcz  Bainouk-Gunyaamolo  Bainouk-Gunyaamolo
bda  Bayot  Bayot
bdb  Basap  Basap
bdc  Emberá-Baudó  Emberá-Baudó
bdd  Bunama  Bunama
bde  Bade  Bade
bdf  Biage  Biage
bdg  Bonggi  Bonggi
bdh  Baka (Sudan)  Baka (Sudan)
bdi  Burun  Burun
bdj  Bai  Bai
bdk  Budukh  Budukh
bdl  Indonesian Bajau  Bajau, Indonesian
bdm  Buduma  Buduma
bdn  Baldemu  Baldemu
bdo  Morom  Morom
bdp  Bende  Bende
bdq  Bahnar  Bahnar
bdr  West Coast Bajau  Bajau, West Coast
bds  Burunge  Burunge
bdt  Bokoto  Bokoto
bdu  Oroko  Oroko
bdv  Bodo Parja  Bodo Parja
bdw  Baham  Baham
bdx  Budong-Budong  Budong-Budong
bdy  Bandjalang  Bandjalang
bdz  Badeshi  Badeshi
bea  Beaver  Beaver
beb  Bebele  Bebele
bec  Iceve-Maci  Iceve-Maci
bed  Bedoanas  Bedoanas
bee  Byangsi  Byangsi
bef  Benabena  Benabena
beg  Belait  Belait
beh  Biali  Biali
bei  Bekati'  Bekati'
bej  Bedawiyet  Bedawiyet
bej  Beja  Beja
bek  Bebeli  Bebeli
bel  Belarusian  Belarusian
bem  Bemba (Zambia)  Bemba (Zambia)
ben  Bengali  Bengali
beo  Beami  Beami
bep  Besoa  Besoa
beq  Beembe  Beembe
bes  Besme  Besme
bet  Guiberoua Béte  Béte, Guiberoua
beu  Blagar  Blagar
bev  Daloa Bété  Bété, Daloa
bew  Betawi  Betawi
bex  Jur Modo  Jur Modo
bey  Beli (Papua New Guinea)  Beli (Papua New Guinea)
bez  Bena (Tanzania)  Bena (Tanzania)
bfa  Bari  Bari
bfb  Pauri Bareli  Bareli, Pauri
bfc  Northern Bai  Bai, Northern
bfd  Bafut  Bafut
bfe  Betaf  Betaf
bfe  Tena  Tena
bff  Bofi  Bofi
bfg  Busang Kayan  Kayan, Busang
bfh  Blafe  Blafe
bfi  British Sign Language  British Sign Language
bfj  Bafanji  Bafanji
bfk  Ban Khor Sign Language  Ban Khor Sign Language
bfl  Banda-Ndélé  Banda-Ndélé
bfm  Mmen  Mmen
bfn  Bunak  Bunak
bfo  Malba Birifor  Birifor, Malba
bfp  Beba  Beba
bfq  Badaga  Badaga
bfr  Bazigar  Bazigar
bfs  Southern Bai  Bai, Southern
bft  Balti  Balti
bfu  Gahri  Gahri
bfw  Bondo  Bondo
bfx  Bantayanon  Bantayanon
bfy  Bagheli  Bagheli
bfz  Mahasu Pahari  Pahari, Mahasu
bga  Gwamhi-Wuri  Gwamhi-Wuri
bgb  Bobongko  Bobongko
bgc  Haryanvi  Haryanvi
bgd  Rathwi Bareli  Bareli, Rathwi
bge  Bauria  Bauria
bgf  Bangandu  Bangandu
bgg  Bugun  Bugun
bgi  Giangan  Giangan
bgj  Bangolan  Bangolan
bgk  Bit  Bit
bgk  Buxinhua  Buxinhua
bgl  Bo (Laos)  Bo (Laos)
bgm  Baga Mboteni  Baga Mboteni
bgn  Western Balochi  Balochi, Western
bgo  Baga Koga  Baga Koga
bgp  Eastern Balochi  Balochi, Eastern
bgq  Bagri  Bagri
bgr  Bawm Chin  Chin, Bawm
bgs  Tagabawa  Tagabawa
bgt  Bughotu  Bughotu
bgu  Mbongno  Mbongno
bgv  Warkay-Bipim  Warkay-Bipim
bgw  Bhatri  Bhatri
bgx  Balkan Gagauz Turkish  Turkish, Balkan Gagauz
bgy  Benggoi  Benggoi
bgz  Banggai  Banggai
bha  Bharia  Bharia
bhb  Bhili  Bhili
bhc  Biga  Biga
bhd  Bhadrawahi  Bhadrawahi
bhe  Bhaya  Bhaya
bhf  Odiai  Odiai
bhg  Binandere  Binandere
bhh  Bukharic  Bukharic
bhi  Bhilali  Bhilali
bhj  Bahing  Bahing
bhl  Bimin  Bimin
bhm  Bathari  Bathari
bhn  Bohtan Neo-Aramaic  Neo-Aramaic, Bohtan
bho  Bhojpuri  Bhojpuri
bhp  Bima  Bima
bhq  Tukang Besi South  Tukang Besi South
bhr  Bara Malagasy  Malagasy, Bara
bhs  Buwal  Buwal
bht  Bhattiyali  Bhattiyali
bhu  Bhunjia  Bhunjia
bhv  Bahau  Bahau
bhw  Biak  Biak
bhx  Bhalay  Bhalay
bhy  Bhele  Bhele
bhz  Bada (Indonesia)  Bada (Indonesia)
bia  Badimaya  Badimaya
bib  Bisa  Bisa
bib  Bissa  Bissa
bic  Bikaru  Bikaru
bid  Bidiyo  Bidiyo
bie  Bepour  Bepour
bif  Biafada  Biafada
big  Biangai  Biangai
bij  Vaghat-Ya-Bijim-Legeri  Vaghat-Ya-Bijim-Legeri
bik  Bikol  Bikol
bil  Bile  Bile
bim  Bimoba  Bimoba
bin  Bini  Bini
bin  Edo  Edo
bio  Nai  Nai
bip  Bila  Bila
biq  Bipi  Bipi
bir  Bisorio  Bisorio
bis  Bislama  Bislama
bit  Berinomo  Berinomo
biu  Biete  Biete
biv  Southern Birifor  Birifor, Southern
biw  Kol (Cameroon)  Kol (Cameroon)
bix  Bijori  Bijori
biy  Birhor  Birhor
biz  Baloi  Baloi
bja  Budza  Budza
bjb  Banggarla  Banggarla
bjc  Bariji  Bariji
bje  Biao-Jiao Mien  Mien, Biao-Jiao
bjf  Barzani Jewish Neo-Aramaic  Neo-Aramaic, Barzani Jewish
bjg  Bidyogo  Bidyogo
bjh  Bahinemo  Bahinemo
bji  Burji  Burji
bjj  Kanauji  Kanauji
bjk  Barok  Barok
bjl  Bulu (Papua New Guinea)  Bulu (Papua New Guinea)
bjm  Bajelani  Bajelani
bjn  Banjar  Banjar
bjo  Mid-Southern Banda  Banda, Mid-Southern
bjp  Fanamaket  Fanamaket
bjr  Binumarien  Binumarien
bjs  Bajan  Bajan
bjt  Balanta-Ganja  Balanta-Ganja
bju  Busuu  Busuu
bjv  Bedjond  Bedjond
bjw  Bakwé  Bakwé
bjx  Banao Itneg  Itneg, Banao
bjy  Bayali  Bayali
bjz  Baruga  Baruga
bka  Kyak  Kyak
bkc  Baka (Cameroon)  Baka (Cameroon)
bkd  Binukid  Binukid
bkd  Talaandig  Talaandig
bkf  Beeke  Beeke
bkg  Buraka  Buraka
bkh  Bakoko  Bakoko
bki  Baki  Baki
bkj  Pande  Pande
bkk  Brokskat  Brokskat
bkl  Berik  Berik
bkm  Kom (Cameroon)  Kom (Cameroon)
bkn  Bukitan  Bukitan
bko  Kwa'  Kwa'
bkp  Boko (Democratic Republic of Congo)  Boko (Democratic Republic of Congo)
bkq  Bakairí  Bakairí
bkr  Bakumpai  Bakumpai
bks  Northern Sorsoganon  Sorsoganon, Northern
bkt  Boloki  Boloki
bku  Buhid  Buhid
bkv  Bekwarra  Bekwarra
bkw  Bekwel  Bekwel
bkx  Baikeno  Baikeno
bky  Bokyi  Bokyi
bkz  Bungku  Bungku
bla  Siksika  Siksika
blb  Bilua  Bilua
blc  Bella Coola  Bella Coola
bld  Bolango  Bolango
ble  Balanta-Kentohe  Balanta-Kentohe
blf  Buol  Buol
blg  Balau  Balau
blh  Kuwaa  Kuwaa
bli  Bolia  Bolia
blj  Bolongan  Bolongan
blk  Pa'O  Pa'O
blk  Pa'o Karen  Karen, Pa'o
bll  Biloxi  Biloxi
blm  Beli (Sudan)  Beli (Sudan)
bln  Southern Catanduanes Bikol  Bikol, Southern Catanduanes
blo  Anii  Anii
blp  Blablanga  Blablanga
blq  Baluan-Pam  Baluan-Pam
blr  Blang  Blang
bls  Balaesang  Balaesang
blt  Tai Dam  Tai Dam
blv  Bolo  Bolo
blw  Balangao  Balangao
blx  Mag-Indi Ayta  Ayta, Mag-Indi
bly  Notre  Notre
blz  Balantak  Balantak
bma  Lame  Lame
bmb  Bembe  Bembe
bmc  Biem  Biem
bmd  Baga Manduri  Manduri, Baga
bme  Limassa  Limassa
bmf  Bom  Bom
bmg  Bamwe  Bamwe
bmh  Kein  Kein
bmi  Bagirmi  Bagirmi
bmj  Bote-Majhi  Bote-Majhi
bmk  Ghayavi  Ghayavi
bml  Bomboli  Bomboli
bmm  Northern Betsimisaraka Malagasy  Malagasy, Northern Betsimisaraka
bmn  Bina (Papua New Guinea)  Bina (Papua New Guinea)
bmo  Bambalang  Bambalang
bmp  Bulgebi  Bulgebi
bmq  Bomu  Bomu
bmr  Muinane  Muinane
bms  Bilma Kanuri  Kanuri, Bilma
bmt  Biao Mon  Biao Mon
bmu  Somba-Siawari  Somba-Siawari
bmv  Bum  Bum
bmw  Bomwali  Bomwali
bmx  Baimak  Baimak
bmy  Bemba (Democratic Republic of Congo)  Bemba (Democratic Republic of Congo)
bmz  Baramu  Baramu
bna  Bonerate  Bonerate
bnb  Bookan  Bookan
bnc  Bontok  Bontok
bnd  Banda (Indonesia)  Banda (Indonesia)
bne  Bintauna  Bintauna
bnf  Masiwang  Masiwang
bng  Benga  Benga
bni  Bangi  Bangi
bnj  Eastern Tawbuid  Tawbuid, Eastern
bnk  Bierebo  Bierebo
bnl  Boon  Boon
bnm  Batanga  Batanga
bnn  Bunun  Bunun
bno  Bantoanon  Bantoanon
bnp  Bola  Bola
bnq  Bantik  Bantik
bnr  Butmas-Tur  Butmas-Tur
bns  Bundeli  Bundeli
bnu  Bentong  Bentong
bnv  Beneraf  Beneraf
bnv  Bonerif  Bonerif
bnv  Edwas  Edwas
bnw  Bisis  Bisis
bnx  Bangubangu  Bangubangu
bny  Bintulu  Bintulu
bnz  Beezen  Beezen
boa  Bora  Bora
bob  Aweer  Aweer
bod  Tibetan  Tibetan
boe  Mundabli  Mundabli
bof  Bolon  Bolon
bog  Bamako Sign Language  Bamako Sign Language
boh  Boma  Boma
boi  Barbareño  Barbareño
boj  Anjam  Anjam
bok  Bonjo  Bonjo
bol  Bole  Bole
bom  Berom  Berom
bon  Bine  Bine
boo  Tiemacèwè Bozo  Bozo, Tiemacèwè
bop  Bonkiman  Bonkiman
boq  Bogaya  Bogaya
bor  Borôro  Borôro
bos  Bosnian  Bosnian
bot  Bongo  Bongo
bou  Bondei  Bondei
bov  Tuwuli  Tuwuli
bow  Rema  Rema
box  Buamu  Buamu
boy  Bodo (Central African Republic)  Bodo (Central African Republic)
boz  Tiéyaxo Bozo  Bozo, Tiéyaxo
bpa  Daakaka  Daakaka
bpb  Barbacoas  Barbacoas
bpd  Banda-Banda  Banda-Banda
bpg  Bonggo  Bonggo
bph  Botlikh  Botlikh
bpi  Bagupi  Bagupi
bpj  Binji  Binji
bpk  'Ôrôê  'Ôrôê
bpk  Orowe  Orowe
bpl  Broome Pearling Lugger Pidgin  Broome Pearling Lugger Pidgin
bpm  Biyom  Biyom
bpn  Dzao Min  Dzao Min
bpo  Anasi  Anasi
bpp  Kaure  Kaure
bpq  Banda Malay  Malay, Banda
bpr  Koronadal Blaan  Blaan, Koronadal
bps  Sarangani Blaan  Blaan, Sarangani
bpt  Barrow Point  Barrow Point
bpu  Bongu  Bongu
bpv  Bian Marind  Marind, Bian
bpw  Bo (Papua New Guinea)  Bo (Papua New Guinea)
bpx  Palya Bareli  Bareli, Palya
bpy  Bishnupriya  Bishnupriya
bpz  Bilba  Bilba
bqa  Tchumbuli  Tchumbuli
bqb  Bagusa  Bagusa
bqc  Boko (Benin)  Boko (Benin)
bqc  Boo  Boo
bqd  Bung  Bung
bqf  Baga Kaloum  Baga Kaloum
bqg  Bago-Kusuntu  Bago-Kusuntu
bqh  Baima  Baima
bqi  Bakhtiari  Bakhtiari
bqj  Bandial  Bandial
bqk  Banda-Mbrès  Banda-Mbrès
bql  Bilakura  Bilakura
bqm  Wumboko  Wumboko
bqn  Bulgarian Sign Language  Bulgarian Sign Language
bqo  Balo  Balo
bqp  Busa  Busa
bqq  Biritai  Biritai
bqr  Burusu  Burusu
bqs  Bosngun  Bosngun
bqt  Bamukumbit  Bamukumbit
bqu  Boguru  Boguru
bqv  Begbere-Ejar  Begbere-Ejar
bqv  Koro Wachi  Koro Wachi
bqw  Buru (Nigeria)  Buru (Nigeria)
bqx  Baangi  Baangi
bqy  Bengkala Sign Language  Bengkala Sign Language
bqz  Bakaka  Bakaka
bra  Braj  Braj
brb  Lave  Lave
brc  Berbice Creole Dutch  Creole Dutch, Berbice
brd  Baraamu  Baraamu
bre  Breton  Breton
brf  Bera  Bera
brg  Baure  Baure
brh  Brahui  Brahui
bri  Mokpwe  Mokpwe
brj  Bieria  Bieria
brk  Birked  Birked
brl  Birwa  Birwa
brm  Barambu  Barambu
brn  Boruca  Boruca
bro  Brokkat  Brokkat
brp  Barapasi  Barapasi
brq  Breri  Breri
brr  Birao  Birao
brs  Baras  Baras
brt  Bitare  Bitare
bru  Eastern Bru  Bru, Eastern
brv  Western Bru  Bru, Western
brw  Bellari  Bellari
brx  Bodo (India)  Bodo (India)
bry  Burui  Burui
brz  Bilbil  Bilbil
bsa  Abinomn  Abinomn
bsb  Brunei Bisaya  Bisaya, Brunei
bsc  Bassari  Bassari
bsc  Oniyan  Oniyan
bse  Wushi  Wushi
bsf  Bauchi  Bauchi
bsg  Bashkardi  Bashkardi
bsh  Kati  Kati
bsi  Bassossi  Bassossi
bsj  Bangwinji  Bangwinji
bsk  Burushaski  Burushaski
bsl  Basa-Gumna  Basa-Gumna
bsm  Busami  Busami
bsn  Barasana-Eduria  Barasana-Eduria
bso  Buso  Buso
bsp  Baga Sitemu  Baga Sitemu
bsq  Bassa  Bassa
bsr  Bassa-Kontagora  Bassa-Kontagora
bss  Akoose  Akoose
bst  Basketo  Basketo
bsu  Bahonsuai  Bahonsuai
bsv  Baga Sobané  Baga Sobané
bsw  Baiso  Baiso
bsx  Yangkam  Yangkam
bsy  Sabah Bisaya  Bisaya, Sabah
bta  Bata  Bata
btc  Bati (Cameroon)  Bati (Cameroon)
btd  Batak Dairi  Batak Dairi
bte  Gamo-Ningi  Gamo-Ningi
btf  Birgit  Birgit
btg  Gagnoa Bété  Bété, Gagnoa
bth  Biatah Bidayuh  Bidayuh, Biatah
bti  Burate  Burate
btj  Bacanese Malay  Malay, Bacanese
btl  Bhatola  Bhatola
btm  Batak Mandailing  Batak Mandailing
btn  Ratagnon  Ratagnon
bto  Rinconada Bikol  Bikol, Rinconada
btp  Budibud  Budibud
btq  Batek  Batek
btr  Baetora  Baetora
bts  Batak Simalungun  Batak Simalungun
btt  Bete-Bendi  Bete-Bendi
btu  Batu  Batu
btv  Bateri  Bateri
btw  Butuanon  Butuanon
btx  Batak Karo  Batak Karo
bty  Bobot  Bobot
btz  Batak Alas-Kluet  Batak Alas-Kluet
bua  Buriat  Buriat
bub  Bua  Bua
buc  Bushi  Bushi
bud  Ntcham  Ntcham
bue  Beothuk  Beothuk
buf  Bushoong  Bushoong
bug  Buginese  Buginese
buh  Younuo Bunu  Bunu, Younuo
bui  Bongili  Bongili
buj  Basa-Gurmana  Basa-Gurmana
buk  Bugawac  Bugawac
bul  Bulgarian  Bulgarian
bum  Bulu (Cameroon)  Bulu (Cameroon)
bun  Sherbro  Sherbro
buo  Terei  Terei
bup  Busoa  Busoa
buq  Brem  Brem
bus  Bokobaru  Bokobaru
but  Bungain  Bungain
buu  Budu  Budu
buv  Bun  Bun
buw  Bubi  Bubi
bux  Boghom  Boghom
buy  Bullom So  Bullom So
buz  Bukwen  Bukwen
bva  Barein  Barein
bvb  Bube  Bube
bvc  Baelelea  Baelelea
bvd  Baeggu  Baeggu
bve  Berau Malay  Malay, Berau
bvf  Boor  Boor
bvg  Bonkeng  Bonkeng
bvh  Bure  Bure
bvi  Belanda Viri  Belanda Viri
bvj  Baan  Baan
bvk  Bukat  Bukat
bvl  Bolivian Sign Language  Bolivian Sign Language
bvm  Bamunka  Bamunka
bvn  Buna  Buna
bvo  Bolgo  Bolgo
bvp  Bumang  Bumang
bvq  Birri  Birri
bvr  Burarra  Burarra
bvt  Bati (Indonesia)  Bati (Indonesia)
bvu  Bukit Malay  Malay, Bukit
bvv  Baniva  Baniva
bvw  Boga  Boga
bvx  Dibole  Dibole
bvy  Baybayanon  Baybayanon
bvz  Bauzi  Bauzi
bwa  Bwatoo  Bwatoo
bwb  Namosi-Naitasiri-Serua  Namosi-Naitasiri-Serua
bwc  Bwile  Bwile
bwd  Bwaidoka  Bwaidoka
bwe  Bwe Karen  Karen, Bwe
bwf  Boselewa  Boselewa
bwg  Barwe  Barwe
bwh  Bishuo  Bishuo
bwi  Baniwa  Baniwa
bwj  Láá Láá Bwamu  Bwamu, Láá Láá
bwk  Bauwaki  Bauwaki
bwl  Bwela  Bwela
bwm  Biwat  Biwat
bwn  Wunai Bunu  Bunu, Wunai
bwo  Borna (Ethiopia)  Borna (Ethiopia)
bwo  Boro (Ethiopia)  Boro (Ethiopia)
bwp  Mandobo Bawah  Mandobo Bawah
bwq  Southern Bobo Madaré  Bobo Madaré, Southern
bwr  Bura-Pabir  Bura-Pabir
bws  Bomboma  Bomboma
bwt  Bafaw-Balong  Bafaw-Balong
bwu  Buli (Ghana)  Buli (Ghana)
bww  Bwa  Bwa
bwx  Bu-Nao Bunu  Bunu, Bu-Nao
bwy  Cwi Bwamu  Bwamu, Cwi
bwz  Bwisi  Bwisi
bxa  Tairaha  Tairaha
bxb  Belanda Bor  Bor, Belanda
bxc  Molengue  Molengue
bxd  Pela  Pela
bxe  Birale  Birale
bxf  Bilur  Bilur
bxf  Minigir  Minigir
bxg  Bangala  Bangala
bxh  Buhutu  Buhutu
bxi  Pirlatapa  Pirlatapa
bxj  Bayungu  Bayungu
bxk  Bukusu  Bukusu
bxk  Lubukusu  Lubukusu
bxl  Jalkunan  Jalkunan
bxm  Mongolia Buriat  Buriat, Mongolia
bxn  Burduna  Burduna
bxo  Barikanchi  Barikanchi
bxp  Bebil  Bebil
bxq  Beele  Beele
bxr  Russia Buriat  Buriat, Russia
bxs  Busam  Busam
bxu  China Buriat  Buriat, China
bxv  Berakou  Berakou
bxw  Bankagooma  Bankagooma
bxx  Borna (Democratic Republic of Congo)  Borna (Democratic Republic of Congo)
bxz  Binahari  Binahari
bya  Batak  Batak
byb  Bikya  Bikya
byc  Ubaghara  Ubaghara
byd  Benyadu'  Benyadu'
bye  Pouye  Pouye
byf  Bete  Bete
byg  Baygo  Baygo
byh  Bhujel  Bhujel
byi  Buyu  Buyu
byj  Bina (Nigeria)  Bina (Nigeria)
byk  Biao  Biao
byl  Bayono  Bayono
bym  Bidyara  Bidyara
byn  Bilin  Bilin
byn  Blin  Blin
byo  Biyo  Biyo
byp  Bumaji  Bumaji
byq  Basay  Basay
byr  Baruya  Baruya
byr  Yipma  Yipma
bys  Burak  Burak
byt  Berti  Berti
byv  Medumba  Medumba
byw  Belhariya  Belhariya
byx  Qaqet  Qaqet
byy  Buya  Buya
byz  Banaro  Banaro
bza  Bandi  Bandi
bzb  Andio  Andio
bzc  Southern Betsimisaraka Malagasy  Malagasy, Southern Betsimisaraka
bzd  Bribri  Bribri
bze  Jenaama Bozo  Bozo, Jenaama
bzf  Boikin  Boikin
bzg  Babuza  Babuza
bzh  Mapos Buang  Buang, Mapos
bzi  Bisu  Bisu
bzj  Belize Kriol English  Kriol English, Belize
bzk  Nicaragua Creole English  Creole English, Nicaragua
bzl  Boano (Sulawesi)  Boano (Sulawesi)
bzm  Bolondo  Bolondo
bzn  Boano (Maluku)  Boano (Maluku)
bzo  Bozaba  Bozaba
bzp  Kemberano  Kemberano
bzq  Buli (Indonesia)  Buli (Indonesia)
bzr  Biri  Biri
bzs  Brazilian Sign Language  Brazilian Sign Language
bzt  Brithenig  Brithenig
bzu  Burmeso  Burmeso
bzv  Naami  Naami
bzw  Basa (Nigeria)  Basa (Nigeria)
bzx  Kɛlɛngaxo Bozo  Bozo, Kɛlɛngaxo
bzy  Obanliku  Obanliku
bzz  Evant  Evant
caa  Chortí  Chortí
cab  Garifuna  Garifuna
cac  Chuj  Chuj
cad  Caddo  Caddo
cae  Laalaa  Laalaa
cae  Lehar  Lehar
caf  Southern Carrier  Carrier, Southern
cag  Nivaclé  Nivaclé
cah  Cahuarano  Cahuarano
caj  Chané  Chané
cak  Cakchiquel  Cakchiquel
cak  Kaqchikel  Kaqchikel
cal  Carolinian  Carolinian
cam  Cemuhî  Cemuhî
can  Chambri  Chambri
cao  Chácobo  Chácobo
cap  Chipaya  Chipaya
caq  Car Nicobarese  Nicobarese, Car
car  Galibi Carib  Carib, Galibi
cas  Tsimané  Tsimané
cat  Catalan  Catalan
cat  Valencian  Valencian
cav  Cavineña  Cavineña
caw  Callawalla  Callawalla
cax  Chiquitano  Chiquitano
cay  Cayuga  Cayuga
caz  Canichana  Canichana
cbb  Cabiyarí  Cabiyarí
cbc  Carapana  Carapana
cbd  Carijona  Carijona
cbe  Chipiajes  Chipiajes
cbg  Chimila  Chimila
cbh  Cagua  Cagua
cbi  Chachi  Chachi
cbj  Ede Cabe  Ede Cabe
cbk  Chavacano  Chavacano
cbl  Bualkhaw Chin  Chin, Bualkhaw
cbn  Nyahkur  Nyahkur
cbo  Izora  Izora
cbr  Cashibo-Cacataibo  Cashibo-Cacataibo
cbs  Cashinahua  Cashinahua
cbt  Chayahuita  Chayahuita
cbu  Candoshi-Shapra  Candoshi-Shapra
cbv  Cacua  Cacua
cbw  Kinabalian  Kinabalian
cby  Carabayo  Carabayo
cca  Cauca  Cauca
ccc  Chamicuro  Chamicuro
ccd  Cafundo Creole  Creole, Cafundo
cce  Chopi  Chopi
ccg  Samba Daka  Daka, Samba
cch  Atsam  Atsam
ccj  Kasanga  Kasanga
ccl  Cutchi-Swahili  Cutchi-Swahili
ccm  Malaccan Creole Malay  Creole Malay, Malaccan
cco  Comaltepec Chinantec  Chinantec, Comaltepec
ccp  Chakma  Chakma
ccr  Cacaopera  Cacaopera
cda  Choni  Choni
cde  Chenchu  Chenchu
cdf  Chiru  Chiru
cdg  Chamari  Chamari
cdh  Chambeali  Chambeali
cdi  Chodri  Chodri
cdj  Churahi  Churahi
cdm  Chepang  Chepang
cdn  Chaudangsi  Chaudangsi
cdo  Min Dong Chinese  Chinese, Min Dong
cdr  Cinda-Regi-Tiyal  Cinda-Regi-Tiyal
cds  Chadian Sign Language  Chadian Sign Language
cdy  Chadong  Chadong
cdz  Koda  Koda
cea  Lower Chehalis  Chehalis, Lower
ceb  Cebuano  Cebuano
ceg  Chamacoco  Chamacoco
cek  Eastern Khumi Chin  Chin, Eastern Khumi
cen  Cen  Cen
ces  Czech  Czech
cet  Centúúm  Centúúm
cfa  Dijim-Bwilim  Dijim-Bwilim
cfd  Cara  Cara
cfg  Como Karim  Como Karim
cfm  Falam Chin  Chin, Falam
cga  Changriwa  Changriwa
cgc  Kagayanen  Kagayanen
cgg  Chiga  Chiga
cgk  Chocangacakha  Chocangacakha
cha  Chamorro  Chamorro
chb  Chibcha  Chibcha
chc  Catawba  Catawba
chd  Highland Oaxaca Chontal  Chontal, Highland Oaxaca
che  Chechen  Chechen
chf  Tabasco Chontal  Chontal, Tabasco
chg  Chagatai  Chagatai
chh  Chinook  Chinook
chj  Ojitlán Chinantec  Chinantec, Ojitlán
chk  Chuukese  Chuukese
chl  Cahuilla  Cahuilla
chm  Mari (Russia)  Mari (Russia)
chn  Chinook jargon  Chinook jargon
cho  Choctaw  Choctaw
chp  Chipewyan  Chipewyan
chp  Dene Suline  Dene Suline
chq  Quiotepec Chinantec  Chinantec, Quiotepec
chr  Cherokee  Cherokee
cht  Cholón  Cholón
chu  Church Slavic  Slavic, Church
chu  Church Slavonic  Slavonic, Church
chu  Old Bulgarian  Bulgarian, Old
chu  Old Church Slavonic  Slavonic, Old Church
chu  Old Slavonic  Slavonic, Old
chv  Chuvash  Chuvash
chw  Chuwabu  Chuwabu
chx  Chantyal  Chantyal
chy  Cheyenne  Cheyenne
chz  Ozumacín Chinantec  Chinantec, Ozumacín
cia  Cia-Cia  Cia-Cia
cib  Ci Gbe  Gbe, Ci
cic  Chickasaw  Chickasaw
cid  Chimariko  Chimariko
cie  Cineni  Cineni
cih  Chinali  Chinali
cik  Chitkuli Kinnauri  Kinnauri, Chitkuli
cim  Cimbrian  Cimbrian
cin  Cinta Larga  Cinta Larga
cip  Chiapanec  Chiapanec
cir  Haméa  Haméa
cir  Méa  Méa
cir  Tiri  Tiri
ciw  Chippewa  Chippewa
ciy  Chaima  Chaima
cja  Western Cham  Cham, Western
cje  Chru  Chru
cjh  Upper Chehalis  Chehalis, Upper
cji  Chamalal  Chamalal
cjk  Chokwe  Chokwe
cjm  Eastern Cham  Cham, Eastern
cjn  Chenapian  Chenapian
cjo  Ashéninka Pajonal  Ashéninka Pajonal
cjp  Cabécar  Cabécar
cjs  Shor  Shor
cjv  Chuave  Chuave
cjy  Jinyu Chinese  Chinese, Jinyu
ckb  Central Kurdish  Kurdish, Central
ckh  Chak  Chak
ckl  Cibak  Cibak
ckn  Kaang Chin  Chin, Kaang
cko  Anufo  Anufo
ckq  Kajakse  Kajakse
ckr  Kairak  Kairak
cks  Tayo  Tayo
ckt  Chukot  Chukot
cku  Koasati  Koasati
ckv  Kavalan  Kavalan
ckx  Caka  Caka
cky  Cakfem-Mushere  Cakfem-Mushere
ckz  Cakchiquel-Quiché Mixed Language  Cakchiquel-Quiché Mixed Language
cla  Ron  Ron
clc  Chilcotin  Chilcotin
cld  Chaldean Neo-Aramaic  Neo-Aramaic, Chaldean
cle  Lealao Chinantec  Chinantec, Lealao
clh  Chilisso  Chilisso
cli  Chakali  Chakali
clj  Laitu Chin  Chin, Laitu
clk  Idu-Mishmi  Idu-Mishmi
cll  Chala  Chala
clm  Clallam  Clallam
clo  Lowland Oaxaca Chontal  Chontal, Lowland Oaxaca
clt  Lautu Chin  Chin, Lautu
clu  Caluyanun  Caluyanun
clw  Chulym  Chulym
cly  Eastern Highland Chatino  Chatino, Eastern Highland
cma  Maa  Maa
cme  Cerma  Cerma
cmg  Classical Mongolian  Mongolian, Classical
cmi  Emberá-Chamí  Emberá-Chamí
cml  Campalagian  Campalagian
cmm  Michigamea  Michigamea
cmn  Mandarin Chinese  Chinese, Mandarin
cmo  Central Mnong  Mnong, Central
cmr  Mro-Khimi Chin  Chin, Mro-Khimi
cms  Messapic  Messapic
cmt  Camtho  Camtho
cna  Changthang  Changthang
cnb  Chinbon Chin  Chin, Chinbon
cnc  Côông  Côông
cng  Northern Qiang  Qiang, Northern
cnh  Haka Chin  Chin, Haka
cni  Asháninka  Asháninka
cnk  Khumi Chin  Chin, Khumi
cnl  Lalana Chinantec  Chinantec, Lalana
cno  Con  Con
cns  Central Asmat  Asmat, Central
cnt  Tepetotutla Chinantec  Chinantec, Tepetotutla
cnu  Chenoua  Chenoua
cnw  Ngawn Chin  Chin, Ngawn
cnx  Middle Cornish  Cornish, Middle
coa  Cocos Islands Malay  Malay, Cocos Islands
cob  Chicomuceltec  Chicomuceltec
coc  Cocopa  Cocopa
cod  Cocama-Cocamilla  Cocama-Cocamilla
coe  Koreguaje  Koreguaje
cof  Colorado  Colorado
cog  Chong  Chong
coh  Chichonyi-Chidzihana-Chikauma  Chichonyi-Chidzihana-Chikauma
coh  Chonyi-Dzihana-Kauma  Chonyi-Dzihana-Kauma
coj  Cochimi  Cochimi
cok  Santa Teresa Cora  Cora, Santa Teresa
col  Columbia-Wenatchi  Columbia-Wenatchi
com  Comanche  Comanche
con  Cofán  Cofán
coo  Comox  Comox
cop  Coptic  Coptic
coq  Coquille  Coquille
cor  Cornish  Cornish
cos  Corsican  Corsican
cot  Caquinte  Caquinte
cou  Wamey  Wamey
cov  Cao Miao  Cao Miao
cow  Cowlitz  Cowlitz
cox  Nanti  Nanti
coy  Coyaima  Coyaima
coz  Chochotec  Chochotec
cpa  Palantla Chinantec  Chinantec, Palantla
cpb  Ucayali-Yurúa Ashéninka  Ashéninka, Ucayali-Yurúa
cpc  Ajyíninka Apurucayali  Ajyíninka Apurucayali
cpg  Cappadocian Greek  Greek, Cappadocian
cpi  Chinese Pidgin English  Pidgin English, Chinese
cpn  Cherepon  Cherepon
cpo  Kpeego  Kpeego
cps  Capiznon  Capiznon
cpu  Pichis Ashéninka  Ashéninka, Pichis
cpx  Pu-Xian Chinese  Chinese, Pu-Xian
cpy  South Ucayali Ashéninka  Ashéninka, South Ucayali
cqd  Chuanqiandian Cluster Miao  Miao, Chuanqiandian Cluster
cqu  Chilean Quechua  Quechua, Chilean
cra  Chara  Chara
crb  Island Carib  Carib, Island
crc  Lonwolwol  Lonwolwol
crd  Coeur d'Alene  Coeur d'Alene
cre  Cree  Cree
crf  Caramanta  Caramanta
crg  Michif  Michif
crh  Crimean Tatar  Tatar, Crimean
crh  Crimean Turkish  Turkish, Crimean
cri  Sãotomense  Sãotomense
crj  Southern East Cree  Cree, Southern East
crk  Plains Cree  Cree, Plains
crl  Northern East Cree  Cree, Northern East
crm  Moose Cree  Cree, Moose
crn  El Nayar Cora  Cora, El Nayar
cro  Crow  Crow
crq  Iyo'wujwa Chorote  Chorote, Iyo'wujwa
crr  Carolina Algonquian  Algonquian, Carolina
crs  Seselwa Creole French  Creole French, Seselwa
crt  Iyojwa'ja Chorote  Chorote, Iyojwa'ja
crv  Chaura  Chaura
crw  Chrau  Chrau
crx  Carrier  Carrier
cry  Cori  Cori
crz  Cruzeño  Cruzeño
csa  Chiltepec Chinantec  Chinantec, Chiltepec
csb  Kashubian  Kashubian
csc  Catalan Sign Language  Catalan Sign Language
csc  Lengua de señas catalana  Lengua de señas catalana
csc  Llengua de Signes Catalana  Llengua de Signes Catalana
csd  Chiangmai Sign Language  Chiangmai Sign Language
cse  Czech Sign Language  Czech Sign Language
csf  Cuba Sign Language  Cuba Sign Language
csg  Chilean Sign Language  Chilean Sign Language
csh  Asho Chin  Chin, Asho
csi  Coast Miwok  Miwok, Coast
csj  Songlai Chin  Chin, Songlai
csk  Jola-Kasa  Jola-Kasa
csl  Chinese Sign Language  Chinese Sign Language
csm  Central Sierra Miwok  Miwok, Central Sierra
csn  Colombian Sign Language  Colombian Sign Language
cso  Sochiapam Chinantec  Chinantec, Sochiapam
cso  Sochiapan Chinantec  Chinantec, Sochiapan
csq  Croatia Sign Language  Croatia Sign Language
csr  Costa Rican Sign Language  Costa Rican Sign Language
css  Southern Ohlone  Ohlone, Southern
cst  Northern Ohlone  Ohlone, Northern
csv  Sumtu Chin  Chin, Sumtu
csw  Swampy Cree  Cree, Swampy
csy  Siyin Chin  Chin, Siyin
csz  Coos  Coos
cta  Tataltepec Chatino  Chatino, Tataltepec
ctc  Chetco  Chetco
ctd  Tedim Chin  Chin, Tedim
cte  Tepinapa Chinantec  Chinantec, Tepinapa
ctg  Chittagonian  Chittagonian
cth  Thaiphum Chin  Chin, Thaiphum
ctl  Tlacoatzintepec Chinantec  Chinantec, Tlacoatzintepec
ctm  Chitimacha  Chitimacha
ctn  Chhintange  Chhintange
cto  Emberá-Catío  Emberá-Catío
ctp  Western Highland Chatino  Chatino, Western Highland
cts  Northern Catanduanes Bikol  Bikol, Northern Catanduanes
ctt  Wayanad Chetti  Chetti, Wayanad
ctu  Chol  Chol
ctz  Zacatepec Chatino  Chatino, Zacatepec
cua  Cua  Cua
cub  Cubeo  Cubeo
cuc  Usila Chinantec  Chinantec, Usila
cug  Cung  Cung
cuh  Chuka  Chuka
cuh  Gichuka  Gichuka
cui  Cuiba  Cuiba
cuj  Mashco Piro  Mashco Piro
cuk  San Blas Kuna  Kuna, San Blas
cul  Culina  Culina
cul  Kulina  Kulina
cum  Cumeral  Cumeral
cuo  Cumanagoto  Cumanagoto
cup  Cupeño  Cupeño
cuq  Cun  Cun
cur  Chhulung  Chhulung
cut  Teutila Cuicatec  Cuicatec, Teutila
cuu  Tai Ya  Tai Ya
cuv  Cuvok  Cuvok
cuw  Chukwa  Chukwa
cux  Tepeuxila Cuicatec  Cuicatec, Tepeuxila
cvg  Chug  Chug
cvn  Valle Nacional Chinantec  Chinantec, Valle Nacional
cwa  Kabwa  Kabwa
cwb  Maindo  Maindo
cwd  Woods Cree  Cree, Woods
cwe  Kwere  Kwere
cwg  Cheq Wong  Cheq Wong
cwg  Chewong  Chewong
cwt  Kuwaataay  Kuwaataay
cya  Nopala Chatino  Chatino, Nopala
cyb  Cayubaba  Cayubaba
cym  Welsh  Welsh
cyo  Cuyonon  Cuyonon
czh  Huizhou Chinese  Chinese, Huizhou
czk  Knaanic  Knaanic
czn  Zenzontepec Chatino  Chatino, Zenzontepec
czo  Min Zhong Chinese  Chinese, Min Zhong
czt  Zotung Chin  Chin, Zotung
daa  Dangaléat  Dangaléat
dac  Dambi  Dambi
dad  Marik  Marik
dae  Duupa  Duupa
dag  Dagbani  Dagbani
dah  Gwahatike  Gwahatike
dai  Day  Day
daj  Dar Fur Daju  Daju, Dar Fur
dak  Dakota  Dakota
dal  Dahalo  Dahalo
dam  Damakawa  Damakawa
dan  Danish  Danish
dao  Daai Chin  Chin, Daai
daq  Dandami Maria  Maria, Dandami
dar  Dargwa  Dargwa
das  Daho-Doo  Daho-Doo
dau  Dar Sila Daju  Daju, Dar Sila
dav  Dawida  Dawida
dav  Taita  Taita
daw  Davawenyo  Davawenyo
dax  Dayi  Dayi
daz  Dao  Dao
dba  Bangime  Bangime
dbb  Deno  Deno
dbd  Dadiya  Dadiya
dbe  Dabe  Dabe
dbf  Edopi  Edopi
dbg  Dogul Dom Dogon  Dogon, Dogul Dom
dbi  Doka  Doka
dbj  Ida'an  Ida'an
dbl  Dyirbal  Dyirbal
dbm  Duguri  Duguri
dbn  Duriankere  Duriankere
dbo  Dulbu  Dulbu
dbp  Duwai  Duwai
dbq  Daba  Daba
dbr  Dabarre  Dabarre
dbt  Ben Tey Dogon  Dogon, Ben Tey
dbu  Bondum Dom Dogon  Dogon, Bondum Dom
dbv  Dungu  Dungu
dbw  Bankan Tey Dogon  Dogon, Bankan Tey
dby  Dibiyaso  Dibiyaso
dcc  Deccan  Deccan
dcr  Negerhollands  Negerhollands
dda  Dadi Dadi  Dadi Dadi
ddd  Dongotono  Dongotono
dde  Doondo  Doondo
ddg  Fataluku  Fataluku
ddi  West Goodenough  Goodenough, West
ddj  Jaru  Jaru
ddn  Dendi (Benin)  Dendi (Benin)
ddo  Dido  Dido
ddr  Dhudhuroa  Dhudhuroa
dds  Donno So Dogon  Dogon, Donno So
ddw  Dawera-Daweloor  Dawera-Daweloor
dec  Dagik  Dagik
ded  Dedua  Dedua
dee  Dewoin  Dewoin
def  Dezfuli  Dezfuli
deg  Degema  Degema
deh  Dehwari  Dehwari
dei  Demisa  Demisa
dek  Dek  Dek
del  Delaware  Delaware
dem  Dem  Dem
den  Slave (Athapascan)  Slave (Athapascan)
dep  Pidgin Delaware  Delaware, Pidgin
deq  Dendi (Central African Republic)  Dendi (Central African Republic)
der  Deori  Deori
des  Desano  Desano
deu  German  German
dev  Domung  Domung
dez  Dengese  Dengese
dga  Southern Dagaare  Dagaare, Southern
dgb  Bunoge Dogon  Dogon, Bunoge
dgc  Casiguran Dumagat Agta  Agta, Casiguran Dumagat
dgd  Dagaari Dioula  Dagaari Dioula
dge  Degenan  Degenan
dgg  Doga  Doga
dgh  Dghwede  Dghwede
dgi  Northern Dagara  Dagara, Northern
dgk  Dagba  Dagba
dgl  Andaandi  Andaandi
dgl  Dongolawi  Dongolawi
dgn  Dagoman  Dagoman
dgo  Dogri (individual language)  Dogri (individual language)
dgr  Dogrib  Dogrib
dgs  Dogoso  Dogoso
dgt  Ndra'ngith  Ndra'ngith
dgu  Degaru  Degaru
dgw  Daungwurrung  Daungwurrung
dgx  Doghoro  Doghoro
dgz  Daga  Daga
dhd  Dhundari  Dhundari
dhg  Dhangu  Dhangu
dhg  Djangu  Djangu
dhi  Dhimal  Dhimal
dhl  Dhalandji  Dhalandji
dhm  Zemba  Zemba
dhn  Dhanki  Dhanki
dho  Dhodia  Dhodia
dhr  Dhargari  Dhargari
dhs  Dhaiso  Dhaiso
dhu  Dhurga  Dhurga
dhv  Dehu  Dehu
dhv  Drehu  Drehu
dhw  Dhanwar (Nepal)  Dhanwar (Nepal)
dhx  Dhungaloo  Dhungaloo
dia  Dia  Dia
dib  South Central Dinka  Dinka, South Central
dic  Lakota Dida  Dida, Lakota
did  Didinga  Didinga
dif  Dieri  Dieri
dig  Chidigo  Chidigo
dig  Digo  Digo
dih  Kumiai  Kumiai
dii  Dimbong  Dimbong
dij  Dai  Dai
dik  Southwestern Dinka  Dinka, Southwestern
dil  Dilling  Dilling
dim  Dime  Dime
din  Dinka  Dinka
dio  Dibo  Dibo
dip  Northeastern Dinka  Dinka, Northeastern
diq  Dimli (individual language)  Dimli (individual language)
dir  Dirim  Dirim
dis  Dimasa  Dimasa
dit  Dirari  Dirari
diu  Diriku  Diriku
div  Dhivehi  Dhivehi
div  Divehi  Divehi
div  Maldivian  Maldivian
diw  Northwestern Dinka  Dinka, Northwestern
dix  Dixon Reef  Dixon Reef
diy  Diuwe  Diuwe
diz  Ding  Ding
dja  Djadjawurrung  Djadjawurrung
djb  Djinba  Djinba
djc  Dar Daju Daju  Daju, Dar Daju
djd  Djamindjung  Djamindjung
dje  Zarma  Zarma
djf  Djangun  Djangun
dji  Djinang  Djinang
djj  Djeebbana  Djeebbana
djk  Businenge Tongo  Businenge Tongo
djk  Eastern Maroon Creole  Eastern Maroon Creole
djk  Nenge  Nenge
djm  Jamsay Dogon  Dogon, Jamsay
djn  Djauan  Djauan
djo  Jangkang  Jangkang
djr  Djambarrpuyngu  Djambarrpuyngu
dju  Kapriman  Kapriman
djw  Djawi  Djawi
dka  Dakpakha  Dakpakha
dkk  Dakka  Dakka
dkr  Kuijau  Kuijau
dks  Southeastern Dinka  Dinka, Southeastern
dkx  Mazagway  Mazagway
dlg  Dolgan  Dolgan
dlk  Dahalik  Dahalik
dlm  Dalmatian  Dalmatian
dln  Darlong  Darlong
dma  Duma  Duma
dmb  Mombo Dogon  Dogon, Mombo
dmc  Gavak  Gavak
dmd  Madhi Madhi  Madhi Madhi
dme  Dugwor  Dugwor
dmg  Upper Kinabatangan  Kinabatangan, Upper
dmk  Domaaki  Domaaki
dml  Dameli  Dameli
dmm  Dama  Dama
dmo  Kemedzung  Kemedzung
dmr  East Damar  Damar, East
dms  Dampelas  Dampelas
dmu  Dubu  Dubu
dmu  Tebi  Tebi
dmv  Dumpas  Dumpas
dmw  Mudburra  Mudburra
dmx  Dema  Dema
dmy  Demta  Demta
dmy  Sowari  Sowari
dna  Upper Grand Valley Dani  Dani, Upper Grand Valley
dnd  Daonda  Daonda
dne  Ndendeule  Ndendeule
dng  Dungan  Dungan
dni  Lower Grand Valley Dani  Dani, Lower Grand Valley
dnj  Dan  Dan
dnk  Dengka  Dengka
dnn  Dzùùngoo  Dzùùngoo
dnr  Danaru  Danaru
dnt  Mid Grand Valley Dani  Dani, Mid Grand Valley
dnu  Danau  Danau
dnv  Danu  Danu
dnw  Western Dani  Dani, Western
dny  Dení  Dení
doa  Dom  Dom
dob  Dobu  Dobu
doc  Northern Dong  Dong, Northern
doe  Doe  Doe
dof  Domu  Domu
doh  Dong  Dong
doi  Dogri (macrolanguage)  Dogri (macrolanguage)
dok  Dondo  Dondo
dol  Doso  Doso
don  Toura (Papua New Guinea)  Toura (Papua New Guinea)
doo  Dongo  Dongo
dop  Lukpa  Lukpa
doq  Dominican Sign Language  Dominican Sign Language
dor  Dori'o  Dori'o
dos  Dogosé  Dogosé
dot  Dass  Dass
dov  Dombe  Dombe
dow  Doyayo  Doyayo
dox  Bussa  Bussa
doy  Dompo  Dompo
doz  Dorze  Dorze
dpp  Papar  Papar
drb  Dair  Dair
drc  Minderico  Minderico
drd  Darmiya  Darmiya
dre  Dolpo  Dolpo
drg  Rungus  Rungus
dri  C'lela  C'lela
drl  Paakantyi  Paakantyi
drn  West Damar  Damar, West
dro  Daro-Matu Melanau  Melanau, Daro-Matu
drq  Dura  Dura
drr  Dororo  Dororo
drs  Gedeo  Gedeo
drt  Drents  Drents
dru  Rukai  Rukai
dry  Darai  Darai
dsb  Lower Sorbian  Sorbian, Lower
dse  Dutch Sign Language  Dutch Sign Language
dsh  Daasanach  Daasanach
dsi  Disa  Disa
dsl  Danish Sign Language  Danish Sign Language
dsn  Dusner  Dusner
dso  Desiya  Desiya
dsq  Tadaksahak  Tadaksahak
dta  Daur  Daur
dtb  Labuk-Kinabatangan Kadazan  Kadazan, Labuk-Kinabatangan
dtd  Ditidaht  Ditidaht
dth  Adithinngithigh  Adithinngithigh
dti  Ana Tinga Dogon  Dogon, Ana Tinga
dtk  Tene Kan Dogon  Dogon, Tene Kan
dtm  Tomo Kan Dogon  Dogon, Tomo Kan
dto  Tommo So Dogon  Dogon, Tommo So
dtp  Central Dusun  Dusun, Central
dtr  Lotud  Lotud
dts  Toro So Dogon  Dogon, Toro So
dtt  Toro Tegu Dogon  Dogon, Toro Tegu
dtu  Tebul Ure Dogon  Dogon, Tebul Ure
dty  Dotyali  Dotyali
dua  Duala  Duala
dub  Dubli  Dubli
duc  Duna  Duna
dud  Hun-Saare  Hun-Saare
due  Umiray Dumaget Agta  Agta, Umiray Dumaget
duf  Drubea  Drubea
duf  Dumbea  Dumbea
dug  Chiduruma  Chiduruma
dug  Duruma  Duruma
duh  Dungra Bhil  Dungra Bhil
dui  Dumun  Dumun
duj  Dhuwal  Dhuwal
duk  Uyajitaya  Uyajitaya
dul  Alabat Island Agta  Agta, Alabat Island
dum  Middle Dutch (ca. 1050-1350)  Dutch, Middle (ca. 1050-1350)
dun  Dusun Deyah  Dusun Deyah
duo  Dupaninan Agta  Agta, Dupaninan
dup  Duano  Duano
duq  Dusun Malang  Dusun Malang
dur  Dii  Dii
dus  Dumi  Dumi
duu  Drung  Drung
duv  Duvle  Duvle
duw  Dusun Witu  Dusun Witu
dux  Duungooma  Duungooma
duy  Dicamay Agta  Agta, Dicamay
duz  Duli  Duli
dva  Duau  Duau
dwa  Diri  Diri
dwr  Dawro  Dawro
dws  Dutton World Speedwords  Dutton World Speedwords
dww  Dawawa  Dawawa
dya  Dyan  Dyan
dyb  Dyaberdyaber  Dyaberdyaber
dyd  Dyugun  Dyugun
dyg  Villa Viciosa Agta  Agta, Villa Viciosa
dyi  Djimini Senoufo  Senoufo, Djimini
dym  Yanda Dom Dogon  Dogon, Yanda Dom
dyn  Dyangadi  Dyangadi
dyo  Jola-Fonyi  Jola-Fonyi
dyu  Dyula  Dyula
dyy  Dyaabugay  Dyaabugay
dza  Tunzu  Tunzu
dzd  Daza  Daza
dze  Djiwarli  Djiwarli
dzg  Dazaga  Dazaga
dzl  Dzalakha  Dzalakha
dzn  Dzando  Dzando
dzo  Dzongkha  Dzongkha
eaa  Karenggapa  Karenggapa
ebg  Ebughu  Ebughu
ebk  Eastern Bontok  Bontok, Eastern
ebo  Teke-Ebo  Teke-Ebo
ebr  Ebrié  Ebrié
ebu  Embu  Embu
ebu  Kiembu  Kiembu
ecr  Eteocretan  Eteocretan
ecs  Ecuadorian Sign Language  Ecuadorian Sign Language
ecy  Eteocypriot  Eteocypriot
eee  E  E
efa  Efai  Efai
efe  Efe  Efe
efi  Efik  Efik
ega  Ega  Ega
egl  Emilian  Emilian
ego  Eggon  Eggon
egy  Egyptian (Ancient)  Egyptian (Ancient)
ehu  Ehueun  Ehueun
eip  Eipomek  Eipomek
eit  Eitiep  Eitiep
eiv  Askopan  Askopan
eja  Ejamat  Ejamat
eka  Ekajuk  Ekajuk
ekc  Eastern Karnic  Karnic, Eastern
eke  Ekit  Ekit
ekg  Ekari  Ekari
eki  Eki  Eki
ekk  Standard Estonian  Estonian, Standard
ekl  Kol  Kol
ekl  Kol (Bangladesh)  Kol (Bangladesh)
ekm  Elip  Elip
eko  Koti  Koti
ekp  Ekpeye  Ekpeye
ekr  Yace  Yace
eky  Eastern Kayah  Kayah, Eastern
ele  Elepi  Elepi
elh  El Hugeirat  El Hugeirat
eli  Nding  Nding
elk  Elkei  Elkei
ell  Modern Greek (1453-)  Greek, Modern (1453-)
elm  Eleme  Eleme
elo  El Molo  El Molo
elu  Elu  Elu
elx  Elamite  Elamite
ema  Emai-Iuleha-Ora  Emai-Iuleha-Ora
emb  Embaloh  Embaloh
eme  Emerillon  Emerillon
emg  Eastern Meohang  Meohang, Eastern
emi  Mussau-Emira  Mussau-Emira
emk  Eastern Maninkakan  Maninkakan, Eastern
emm  Mamulique  Mamulique
emn  Eman  Eman
emo  Emok  Emok
emp  Northern Emberá  Emberá, Northern
ems  Pacific Gulf Yupik  Yupik, Pacific Gulf
emu  Eastern Muria  Muria, Eastern
emw  Emplawas  Emplawas
emx  Erromintxela  Erromintxela
emy  Epigraphic Mayan  Mayan, Epigraphic
ena  Apali  Apali
enb  Markweeta  Markweeta
enc  En  En
end  Ende  Ende
enf  Forest Enets  Enets, Forest
eng  English  English
enh  Tundra Enets  Enets, Tundra
enm  Middle English (1100-1500)  English, Middle (1100-1500)
enn  Engenni  Engenni
eno  Enggano  Enggano
enq  Enga  Enga
enr  Emem  Emem
enr  Emumu  Emumu
enu  Enu  Enu
env  Enwan (Edu State)  Enwan (Edu State)
enw  Enwan (Akwa Ibom State)  Enwan (Akwa Ibom State)
eot  Beti (Côte d'Ivoire)  Beti (Côte d'Ivoire)
epi  Epie  Epie
epo  Esperanto  Esperanto
era  Eravallan  Eravallan
erg  Sie  Sie
erh  Eruwa  Eruwa
eri  Ogea  Ogea
erk  South Efate  Efate, South
ero  Horpa  Horpa
err  Erre  Erre
ers  Ersu  Ersu
ert  Eritai  Eritai
erw  Erokwanas  Erokwanas
ese  Ese Ejja  Ese Ejja
esh  Eshtehardi  Eshtehardi
esi  North Alaskan Inupiatun  Inupiatun, North Alaskan
esk  Northwest Alaska Inupiatun  Inupiatun, Northwest Alaska
esl  Egypt Sign Language  Egypt Sign Language
esm  Esuma  Esuma
esn  Salvadoran Sign Language  Salvadoran Sign Language
eso  Estonian Sign Language  Estonian Sign Language
esq  Esselen  Esselen
ess  Central Siberian Yupik  Yupik, Central Siberian
est  Estonian  Estonian
esu  Central Yupik  Yupik, Central
etb  Etebi  Etebi
etc  Etchemin  Etchemin
eth  Ethiopian Sign Language  Ethiopian Sign Language
etn  Eton (Vanuatu)  Eton (Vanuatu)
eto  Eton (Cameroon)  Eton (Cameroon)
etr  Edolo  Edolo
ets  Yekhee  Yekhee
ett  Etruscan  Etruscan
etu  Ejagham  Ejagham
etx  Eten  Eten
etz  Semimi  Semimi
eus  Basque  Basque
eve  Even  Even
evh  Uvbie  Uvbie
evn  Evenki  Evenki
ewe  Ewe  Ewe
ewo  Ewondo  Ewondo
ext  Extremaduran  Extremaduran
eya  Eyak  Eyak
eyo  Keiyo  Keiyo
eza  Ezaa  Ezaa
eze  Uzekwe  Uzekwe
faa  Fasu  Fasu
fab  Fa d'Ambu  Fa d'Ambu
fad  Wagi  Wagi
faf  Fagani  Fagani
fag  Finongan  Finongan
fah  Baissa Fali  Fali, Baissa
fai  Faiwol  Faiwol
faj  Faita  Faita
fak  Fang (Cameroon)  Fang (Cameroon)
fal  South Fali  Fali, South
fam  Fam  Fam
fan  Fang (Equatorial Guinea)  Fang (Equatorial Guinea)
fao  Faroese  Faroese
fap  Palor  Palor
far  Fataleka  Fataleka
fas  Persian  Persian
fat  Fanti  Fanti
fau  Fayu  Fayu
fax  Fala  Fala
fay  Southwestern Fars  Fars, Southwestern
faz  Northwestern Fars  Fars, Northwestern
fbl  West Albay Bikol  Bikol, West Albay
fcs  Quebec Sign Language  Quebec Sign Language
fer  Feroge  Feroge
ffi  Foia Foia  Foia Foia
ffm  Maasina Fulfulde  Fulfulde, Maasina
fgr  Fongoro  Fongoro
fia  Nobiin  Nobiin
fie  Fyer  Fyer
fij  Fijian  Fijian
fil  Filipino  Filipino
fil  Pilipino  Pilipino
fin  Finnish  Finnish
fip  Fipa  Fipa
fir  Firan  Firan
fit  Tornedalen Finnish  Finnish, Tornedalen
fiw  Fiwaga  Fiwaga
fkk  Kirya-Konzəl  Kirya-Konzəl
fkv  Kven Finnish  Finnish, Kven
fla  Kalispel-Pend d'Oreille  Kalispel-Pend d'Oreille
flh  Foau  Foau
fli  Fali  Fali
fll  North Fali  Fali, North
fln  Flinders Island  Flinders Island
flr  Fuliiru  Fuliiru
fly  Tsotsitaal  Tsotsitaal
fmp  Fe'fe'  Fe'fe'
fmu  Far Western Muria  Muria, Far Western
fng  Fanagalo  Fanagalo
fni  Fania  Fania
fod  Foodo  Foodo
foi  Foi  Foi
fom  Foma  Foma
fon  Fon  Fon
for  Fore  Fore
fos  Siraya  Siraya
fpe  Fernando Po Creole English  Creole English, Fernando Po
fqs  Fas  Fas
fra  French  French
frc  Cajun French  French, Cajun
frd  Fordata  Fordata
frk  Frankish  Frankish
frm  Middle French (ca. 1400-1600)  French, Middle (ca. 1400-1600)
fro  Old French (842-ca. 1400)  French, Old (842-ca. 1400)
frp  Arpitan  Arpitan
frp  Francoprovençal  Francoprovençal
frq  Forak  Forak
frr  Northern Frisian  Frisian, Northern
frs  Eastern Frisian  Frisian, Eastern
frt  Fortsenal  Fortsenal
fry  Western Frisian  Frisian, Western
fse  Finnish Sign Language  Finnish Sign Language
fsl  French Sign Language  French Sign Language
fss  finlandssvenskt teckenspråk  finlandssvenskt teckenspråk
fss  Finland-Swedish Sign Language  Finland-Swedish Sign Language
fss  suomenruotsalainen viittomakieli  suomenruotsalainen viittomakieli
fub  Adamawa Fulfulde  Fulfulde, Adamawa
fuc  Pulaar  Pulaar
fud  East Futuna  Futuna, East
fue  Borgu Fulfulde  Fulfulde, Borgu
fuf  Pular  Pular
fuh  Western Niger Fulfulde  Fulfulde, Western Niger
fui  Bagirmi Fulfulde  Fulfulde, Bagirmi
fuj  Ko  Ko
ful  Fulah  Fulah
fum  Fum  Fum
fun  Fulniô  Fulniô
fuq  Central-Eastern Niger Fulfulde  Fulfulde, Central-Eastern Niger
fur  Friulian  Friulian
fut  Futuna-Aniwa  Futuna-Aniwa
fuu  Furu  Furu
fuv  Nigerian Fulfulde  Fulfulde, Nigerian
fuy  Fuyug  Fuyug
fvr  Fur  Fur
fwa  Fwâi  Fwâi
fwe  Fwe  Fwe
gaa  Ga  Ga
gab  Gabri  Gabri
gac  Mixed Great Andamanese  Great Andamanese, Mixed
gad  Gaddang  Gaddang
gae  Guarequena  Guarequena
gaf  Gende  Gende
gag  Gagauz  Gagauz
gah  Alekano  Alekano
gai  Borei  Borei
gaj  Gadsup  Gadsup
gak  Gamkonora  Gamkonora
gal  Galolen  Galolen
gam  Kandawo  Kandawo
gan  Gan Chinese  Chinese, Gan
gao  Gants  Gants
gap  Gal  Gal
gaq  Gata'  Gata'
gar  Galeya  Galeya
gas  Adiwasi Garasia  Garasia, Adiwasi
gat  Kenati  Kenati
gau  Mudhili Gadaba  Gadaba, Mudhili
gaw  Nobonob  Nobonob
gax  Borana-Arsi-Guji Oromo  Oromo, Borana-Arsi-Guji
gay  Gayo  Gayo
gaz  West Central Oromo  Oromo, West Central
gba  Gbaya (Central African Republic)  Gbaya (Central African Republic)
gbb  Kaytetye  Kaytetye
gbd  Karadjeri  Karadjeri
gbe  Niksek  Niksek
gbf  Gaikundi  Gaikundi
gbg  Gbanziri  Gbanziri
gbh  Defi Gbe  Gbe, Defi
gbi  Galela  Galela
gbj  Bodo Gadaba  Gadaba, Bodo
gbk  Gaddi  Gaddi
gbl  Gamit  Gamit
gbm  Garhwali  Garhwali
gbn  Mo'da  Mo'da
gbo  Northern Grebo  Grebo, Northern
gbp  Gbaya-Bossangoa  Gbaya-Bossangoa
gbq  Gbaya-Bozoum  Gbaya-Bozoum
gbr  Gbagyi  Gbagyi
gbs  Gbesi Gbe  Gbe, Gbesi
gbu  Gagadu  Gagadu
gbv  Gbanu  Gbanu
gbw  Gabi-Gabi  Gabi-Gabi
gbx  Eastern Xwla Gbe  Gbe, Eastern Xwla
gby  Gbari  Gbari
gbz  Zoroastrian Dari  Dari, Zoroastrian
gcc  Mali  Mali
gcd  Ganggalida  Ganggalida
gce  Galice  Galice
gcf  Guadeloupean Creole French  Creole French, Guadeloupean
gcl  Grenadian Creole English  Creole English, Grenadian
gcn  Gaina  Gaina
gcr  Guianese Creole French  Creole French, Guianese
gct  Colonia Tovar German  German, Colonia Tovar
gda  Gade Lohar  Lohar, Gade
gdb  Pottangi Ollar Gadaba  Gadaba, Pottangi Ollar
gdc  Gugu Badhun  Gugu Badhun
gdd  Gedaged  Gedaged
gde  Gude  Gude
gdf  Guduf-Gava  Guduf-Gava
gdg  Ga'dang  Ga'dang
gdh  Gadjerawang  Gadjerawang
gdi  Gundi  Gundi
gdj  Gurdjar  Gurdjar
gdk  Gadang  Gadang
gdl  Dirasha  Dirasha
gdm  Laal  Laal
gdn  Umanakaina  Umanakaina
gdo  Ghodoberi  Ghodoberi
gdq  Mehri  Mehri
gdr  Wipi  Wipi
gds  Ghandruk Sign Language  Ghandruk Sign Language
gdt  Kungardutyi  Kungardutyi
gdu  Gudu  Gudu
gdx  Godwari  Godwari
gea  Geruma  Geruma
geb  Kire  Kire
gec  Gboloo Grebo  Grebo, Gboloo
ged  Gade  Gade
geg  Gengle  Gengle
geh  Hutterisch  Hutterisch
geh  Hutterite German  German, Hutterite
gei  Gebe  Gebe
gej  Gen  Gen
gek  Yiwom  Yiwom
gel  ut-Ma'in  ut-Ma'in
geq  Geme  Geme
ges  Geser-Gorom  Geser-Gorom
gew  Gera  Gera
gex  Garre  Garre
gey  Enya  Enya
gez  Geez  Geez
gfk  Patpatar  Patpatar
gft  Gafat  Gafat
gfx  Mangetti Dune !Xung  !Xung, Mangetti Dune
gga  Gao  Gao
ggb  Gbii  Gbii
ggd  Gugadj  Gugadj
gge  Guragone  Guragone
ggg  Gurgula  Gurgula
ggk  Kungarakany  Kungarakany
ggl  Ganglau  Ganglau
ggm  Gugu Mini  Gugu Mini
ggn  Eastern Gurung  Gurung, Eastern
ggo  Southern Gondi  Gondi, Southern
ggt  Gitua  Gitua
ggu  Gagu  Gagu
ggu  Gban  Gban
ggw  Gogodala  Gogodala
gha  Ghadamès  Ghadamès
ghc  Hiberno-Scottish Gaelic  Gaelic, Hiberno-Scottish
ghe  Southern Ghale  Ghale, Southern
ghh  Northern Ghale  Ghale, Northern
ghk  Geko Karen  Karen, Geko
ghl  Ghulfan  Ghulfan
ghn  Ghanongga  Ghanongga
gho  Ghomara  Ghomara
ghr  Ghera  Ghera
ghs  Guhu-Samane  Guhu-Samane
ght  Kuke  Kuke
ght  Kutang Ghale  Ghale, Kutang
gia  Kitja  Kitja
gib  Gibanawa  Gibanawa
gic  Gail  Gail
gid  Gidar  Gidar
gig  Goaria  Goaria
gih  Githabul  Githabul
gil  Gilbertese  Gilbertese
gim  Gimi (Eastern Highlands)  Gimi (Eastern Highlands)
gin  Hinukh  Hinukh
gip  Gimi (West New Britain)  Gimi (West New Britain)
giq  Green Gelao  Gelao, Green
gir  Red Gelao  Gelao, Red
gis  North Giziga  Giziga, North
git  Gitxsan  Gitxsan
giu  Mulao  Mulao
giw  White Gelao  Gelao, White
gix  Gilima  Gilima
giy  Giyug  Giyug
giz  South Giziga  Giziga, South
gji  Geji  Geji
gjk  Kachi Koli  Koli, Kachi
gjm  Gunditjmara  Gunditjmara
gjn  Gonja  Gonja
gju  Gujari  Gujari
gka  Guya  Guya
gke  Ndai  Ndai
gkn  Gokana  Gokana
gko  Kok-Nar  Kok-Nar
gkp  Guinea Kpelle  Kpelle, Guinea
gla  Gaelic  Gaelic
gla  Scottish Gaelic  Gaelic, Scottish
glc  Bon Gula  Bon Gula
gld  Nanai  Nanai
gle  Irish  Irish
glg  Galician  Galician
glh  Northwest Pashayi  Pashayi, Northwest
gli  Guliguli  Guliguli
glj  Gula Iro  Gula Iro
glk  Gilaki  Gilaki
gll  Garlali  Garlali
glo  Galambu  Galambu
glr  Glaro-Twabo  Glaro-Twabo
glu  Gula (Chad)  Gula (Chad)
glv  Manx  Manx
glw  Glavda  Glavda
gly  Gule  Gule
gma  Gambera  Gambera
gmb  Gula'alaa  Gula'alaa
gmd  Mághdì  Mághdì
gmh  Middle High German (ca. 1050-1500)  German, Middle High (ca. 1050-1500)
gml  Middle Low German  German, Middle Low
gmm  Gbaya-Mbodomo  Gbaya-Mbodomo
gmn  Gimnime  Gimnime
gmu  Gumalu  Gumalu
gmv  Gamo  Gamo
gmx  Magoma  Magoma
gmy  Mycenaean Greek  Greek, Mycenaean
gmz  Mgbolizhia  Mgbolizhia
gna  Kaansa  Kaansa
gnb  Gangte  Gangte
gnc  Guanche  Guanche
gnd  Zulgo-Gemzek  Zulgo-Gemzek
gne  Ganang  Ganang
gng  Ngangam  Ngangam
gnh  Lere  Lere
gni  Gooniyandi  Gooniyandi
gnk  //Gana  //Gana
gnl  Gangulu  Gangulu
gnm  Ginuman  Ginuman
gnn  Gumatj  Gumatj
gno  Northern Gondi  Gondi, Northern
gnq  Gana  Gana
gnr  Gureng Gureng  Gureng Gureng
gnt  Guntai  Guntai
gnu  Gnau  Gnau
gnw  Western Bolivian Guaraní  Guaraní, Western Bolivian
gnz  Ganzi  Ganzi
goa  Guro  Guro
gob  Playero  Playero
goc  Gorakor  Gorakor
god  Godié  Godié
goe  Gongduk  Gongduk
gof  Gofa  Gofa
gog  Gogo  Gogo
goh  Old High German (ca. 750-1050)  German, Old High (ca. 750-1050)
goi  Gobasi  Gobasi
goj  Gowlan  Gowlan
gok  Gowli  Gowli
gol  Gola  Gola
gom  Goan Konkani  Konkani, Goan
gon  Gondi  Gondi
goo  Gone Dau  Gone Dau
gop  Yeretuar  Yeretuar
goq  Gorap  Gorap
gor  Gorontalo  Gorontalo
gos  Gronings  Gronings
got  Gothic  Gothic
gou  Gavar  Gavar
gow  Gorowa  Gorowa
gox  Gobu  Gobu
goy  Goundo  Goundo
goz  Gozarkhani  Gozarkhani
gpa  Gupa-Abawa  Gupa-Abawa
gpe  Ghanaian Pidgin English  Pidgin English, Ghanaian
gpn  Taiap  Taiap
gqa  Ga'anda  Ga'anda
gqi  Guiqiong  Guiqiong
gqn  Guana (Brazil)  Guana (Brazil)
gqr  Gor  Gor
gqu  Qau  Qau
gra  Rajput Garasia  Garasia, Rajput
grb  Grebo  Grebo
grc  Ancient Greek (to 1453)  Greek, Ancient (to 1453)
grd  Guruntum-Mbaaru  Guruntum-Mbaaru
grg  Madi  Madi
grh  Gbiri-Niragu  Gbiri-Niragu
gri  Ghari  Ghari
grj  Southern Grebo  Grebo, Southern
grm  Kota Marudu Talantang  Kota Marudu Talantang
grn  Guarani  Guarani
gro  Groma  Groma
grq  Gorovu  Gorovu
grr  Taznatit  Taznatit
grs  Gresi  Gresi
grt  Garo  Garo
gru  Kistane  Kistane
grv  Central Grebo  Grebo, Central
grw  Gweda  Gweda
grx  Guriaso  Guriaso
gry  Barclayville Grebo  Grebo, Barclayville
grz  Guramalum  Guramalum
gse  Ghanaian Sign Language  Ghanaian Sign Language
gsg  German Sign Language  German Sign Language
gsl  Gusilay  Gusilay
gsm  Guatemalan Sign Language  Guatemalan Sign Language
gsn  Gusan  Gusan
gso  Southwest Gbaya  Gbaya, Southwest
gsp  Wasembo  Wasembo
gss  Greek Sign Language  Greek Sign Language
gsw  Alemannic  Alemannic
gsw  Alsatian  Alsatian
gsw  Swiss German  German, Swiss
gta  Guató  Guató
gti  Gbati-ri  Gbati-ri
gtu  Aghu-Tharnggala  Aghu-Tharnggala
gua  Shiki  Shiki
gub  Guajajára  Guajajára
guc  Wayuu  Wayuu
gud  Yocoboué Dida  Dida, Yocoboué
gue  Gurinji  Gurinji
guf  Gupapuyngu  Gupapuyngu
gug  Paraguayan Guaraní  Guaraní, Paraguayan
guh  Guahibo  Guahibo
gui  Eastern Bolivian Guaraní  Guaraní, Eastern Bolivian
guj  Gujarati  Gujarati
guk  Gumuz  Gumuz
gul  Sea Island Creole English  Creole English, Sea Island
gum  Guambiano  Guambiano
gun  Mbyá Guaraní  Guaraní, Mbyá
guo  Guayabero  Guayabero
gup  Gunwinggu  Gunwinggu
guq  Aché  Aché
gur  Farefare  Farefare
gus  Guinean Sign Language  Guinean Sign Language
gut  Maléku Jaíka  Maléku Jaíka
guu  Yanomamö  Yanomamö
guv  Gey  Gey
guw  Gun  Gun
gux  Gourmanchéma  Gourmanchéma
guz  Ekegusii  Ekegusii
guz  Gusii  Gusii
gva  Guana (Paraguay)  Guana (Paraguay)
gvc  Guanano  Guanano
gve  Duwet  Duwet
gvf  Golin  Golin
gvj  Guajá  Guajá
gvl  Gulay  Gulay
gvm  Gurmana  Gurmana
gvn  Kuku-Yalanji  Kuku-Yalanji
gvo  Gavião Do Jiparaná  Gavião Do Jiparaná
gvp  Pará Gavião  Gavião, Pará
gvr  Western Gurung  Gurung, Western
gvs  Gumawana  Gumawana
gvy  Guyani  Guyani
gwa  Mbato  Mbato
gwb  Gwa  Gwa
gwc  Kalami  Kalami
gwd  Gawwada  Gawwada
gwe  Gweno  Gweno
gwf  Gowro  Gowro
gwg  Moo  Moo
gwi  Gwichʼin  Gwichʼin
gwj  /Gwi  /Gwi
gwm  Awngthim  Awngthim
gwn  Gwandara  Gwandara
gwr  Gwere  Gwere
gwt  Gawar-Bati  Gawar-Bati
gwu  Guwamu  Guwamu
gww  Kwini  Kwini
gwx  Gua  Gua
gxx  Wè Southern  Wè Southern
gya  Northwest Gbaya  Gbaya, Northwest
gyb  Garus  Garus
gyd  Kayardild  Kayardild
gye  Gyem  Gyem
gyf  Gungabula  Gungabula
gyg  Gbayi  Gbayi
gyi  Gyele  Gyele
gyl  Gayil  Gayil
gym  Ngäbere  Ngäbere
gyn  Guyanese Creole English  Creole English, Guyanese
gyr  Guarayu  Guarayu
gyy  Gunya  Gunya
gza  Ganza  Ganza
gzi  Gazi  Gazi
gzn  Gane  Gane
haa  Han  Han
hab  Hanoi Sign Language  Hanoi Sign Language
hac  Gurani  Gurani
had  Hatam  Hatam
hae  Eastern Oromo  Oromo, Eastern
haf  Haiphong Sign Language  Haiphong Sign Language
hag  Hanga  Hanga
hah  Hahon  Hahon
hai  Haida  Haida
haj  Hajong  Hajong
hak  Hakka Chinese  Chinese, Hakka
hal  Halang  Halang
ham  Hewa  Hewa
han  Hangaza  Hangaza
hao  Hakö  Hakö
hap  Hupla  Hupla
haq  Ha  Ha
har  Harari  Harari
has  Haisla  Haisla
hat  Haitian  Haitian
hat  Haitian Creole  Creole, Haitian
hau  Hausa  Hausa
hav  Havu  Havu
haw  Hawaiian  Hawaiian
hax  Southern Haida  Haida, Southern
hay  Haya  Haya
haz  Hazaragi  Hazaragi
hba  Hamba  Hamba
hbb  Huba  Huba
hbn  Heiban  Heiban
hbo  Ancient Hebrew  Hebrew, Ancient
hbs  Serbo-Croatian  Serbo-Croatian
hbu  Habu  Habu
hca  Andaman Creole Hindi  Creole Hindi, Andaman
hch  Huichol  Huichol
hdn  Northern Haida  Haida, Northern
hds  Honduras Sign Language  Honduras Sign Language
hdy  Hadiyya  Hadiyya
hea  Northern Qiandong Miao  Miao, Northern Qiandong
heb  Hebrew  Hebrew
hed  Herdé  Herdé
heg  Helong  Helong
heh  Hehe  Hehe
hei  Heiltsuk  Heiltsuk
hem  Hemba  Hemba
her  Herero  Herero
hgm  Hai//om  Hai//om
hgw  Haigwai  Haigwai
hhi  Hoia Hoia  Hoia Hoia
hhr  Kerak  Kerak
hhy  Hoyahoya  Hoyahoya
hia  Lamang  Lamang
hib  Hibito  Hibito
hid  Hidatsa  Hidatsa
hif  Fiji Hindi  Hindi, Fiji
hig  Kamwe  Kamwe
hih  Pamosu  Pamosu
hii  Hinduri  Hinduri
hij  Hijuk  Hijuk
hik  Seit-Kaitetu  Seit-Kaitetu
hil  Hiligaynon  Hiligaynon
hin  Hindi  Hindi
hio  Tsoa  Tsoa
hir  Himarimã  Himarimã
hit  Hittite  Hittite
hiw  Hiw  Hiw
hix  Hixkaryána  Hixkaryána
hji  Haji  Haji
hka  Kahe  Kahe
hke  Hunde  Hunde
hkk  Hunjara-Kaina Ke  Hunjara-Kaina Ke
hks  Heung Kong Sau Yue  Heung Kong Sau Yue
hks  Hong Kong Sign Language  Hong Kong Sign Language
hla  Halia  Halia
hlb  Halbi  Halbi
hld  Halang Doan  Halang Doan
hle  Hlersu  Hlersu
hlt  Matu Chin  Chin, Matu
hlu  Hieroglyphic Luwian  Luwian, Hieroglyphic
hma  Southern Mashan Hmong  Hmong, Southern Mashan
hma  Southern Mashan Miao  Miao, Southern Mashan
hmb  Humburi Senni Songhay  Songhay, Humburi Senni
hmc  Central Huishui Hmong  Hmong, Central Huishui
hmc  Central Huishui Miao  Miao, Central Huishui
hmd  A-hmaos  A-hmaos
hmd  Da-Hua Miao  Miao, Da-Hua
hmd  Large Flowery Miao  Miao, Large Flowery
hme  Eastern Huishui Hmong  Hmong, Eastern Huishui
hme  Eastern Huishui Miao  Miao, Eastern Huishui
hmf  Hmong Don  Hmong Don
hmg  Southwestern Guiyang Hmong  Hmong, Southwestern Guiyang
hmh  Southwestern Huishui Hmong  Hmong, Southwestern Huishui
hmh  Southwestern Huishui Miao  Miao, Southwestern Huishui
hmi  Northern Huishui Hmong  Hmong, Northern Huishui
hmi  Northern Huishui Miao  Miao, Northern Huishui
hmj  Ge  Ge
hmj  Gejia  Gejia
hmk  Maek  Maek
hml  Luopohe Hmong  Hmong, Luopohe
hml  Luopohe Miao  Miao, Luopohe
hmm  Central Mashan Hmong  Hmong, Central Mashan
hmm  Central Mashan Miao  Miao, Central Mashan
hmn  Hmong  Hmong
hmn  Mong  Mong
hmo  Hiri Motu  Hiri Motu
hmp  Northern Mashan Hmong  Hmong, Northern Mashan
hmp  Northern Mashan Miao  Miao, Northern Mashan
hmq  Eastern Qiandong Miao  Miao, Eastern Qiandong
hmr  Hmar  Hmar
hms  Southern Qiandong Miao  Miao, Southern Qiandong
hmt  Hamtai  Hamtai
hmu  Hamap  Hamap
hmv  Hmong Dô  Hmong Dô
hmw  Western Mashan Hmong  Hmong, Western Mashan
hmw  Western Mashan Miao  Miao, Western Mashan
hmy  Southern Guiyang Hmong  Hmong, Southern Guiyang
hmy  Southern Guiyang Miao  Miao, Southern Guiyang
hmz  Hmong Shua  Hmong Shua
hmz  Sinicized Miao  Miao, Sinicized
hna  Mina (Cameroon)  Mina (Cameroon)
hnd  Southern Hindko  Hindko, Southern
hne  Chhattisgarhi  Chhattisgarhi
hnh  //Ani  //Ani
hni  Hani  Hani
hnj  Hmong Njua  Hmong Njua
hnj  Mong Leng  Mong Leng
hnj  Mong Njua  Mong Njua
hnn  Hanunoo  Hanunoo
hno  Northern Hindko  Hindko, Northern
hns  Caribbean Hindustani  Hindustani, Caribbean
hnu  Hung  Hung
hoa  Hoava  Hoava
hob  Mari (Madang Province)  Mari (Madang Province)
hoc  Ho  Ho
hod  Holma  Holma
hoe  Horom  Horom
hoh  Hobyót  Hobyót
hoi  Holikachuk  Holikachuk
hoj  Hadothi  Hadothi
hoj  Haroti  Haroti
hol  Holu  Holu
hom  Homa  Homa
hoo  Holoholo  Holoholo
hop  Hopi  Hopi
hor  Horo  Horo
hos  Ho Chi Minh City Sign Language  Ho Chi Minh City Sign Language
hot  Hote  Hote
hot  Malê  Malê
hov  Hovongan  Hovongan
how  Honi  Honi
hoy  Holiya  Holiya
hoz  Hozo  Hozo
hpo  Hpon  Hpon
hps  Hawai'i Pidgin Sign Language  Hawai'i Pidgin Sign Language
hra  Hrangkhol  Hrangkhol
hrc  Niwer Mil  Niwer Mil
hre  Hre  Hre
hrk  Haruku  Haruku
hrm  Horned Miao  Miao, Horned
hro  Haroi  Haroi
hrp  Nhirrpi  Nhirrpi
hrt  Hértevin  Hértevin
hru  Hruso  Hruso
hrv  Croatian  Croatian
hrw  Warwar Feni  Warwar Feni
hrx  Hunsrik  Hunsrik
hrz  Harzani  Harzani
hsb  Upper Sorbian  Sorbian, Upper
hsh  Hungarian Sign Language  Hungarian Sign Language
hsl  Hausa Sign Language  Hausa Sign Language
hsn  Xiang Chinese  Chinese, Xiang
hss  Harsusi  Harsusi
hti  Hoti  Hoti
hto  Minica Huitoto  Huitoto, Minica
hts  Hadza  Hadza
htu  Hitu  Hitu
htx  Middle Hittite  Hittite, Middle
hub  Huambisa  Huambisa
huc  =/Hua  =/Hua
hud  Huaulu  Huaulu
hue  San Francisco Del Mar Huave  Huave, San Francisco Del Mar
huf  Humene  Humene
hug  Huachipaeri  Huachipaeri
huh  Huilliche  Huilliche
hui  Huli  Huli
huj  Northern Guiyang Hmong  Hmong, Northern Guiyang
huj  Northern Guiyang Miao  Miao, Northern Guiyang
huk  Hulung  Hulung
hul  Hula  Hula
hum  Hungana  Hungana
hun  Hungarian  Hungarian
huo  Hu  Hu
hup  Hupa  Hupa
huq  Tsat  Tsat
hur  Halkomelem  Halkomelem
hus  Huastec  Huastec
hut  Humla  Humla
huu  Murui Huitoto  Huitoto, Murui
huv  San Mateo Del Mar Huave  Huave, San Mateo Del Mar
huw  Hukumina  Hukumina
hux  Nüpode Huitoto  Huitoto, Nüpode
huy  Hulaulá  Hulaulá
huz  Hunzib  Hunzib
hvc  Haitian Vodoun Culture Language  Haitian Vodoun Culture Language
hve  San Dionisio Del Mar Huave  Huave, San Dionisio Del Mar
hvk  Haveke  Haveke
hvn  Sabu  Sabu
hvv  Santa María Del Mar Huave  Huave, Santa María Del Mar
hwa  Wané  Wané
hwc  Hawai'i Creole English  Creole English, Hawai'i
hwc  Hawai'i Pidgin  Hawai'i Pidgin
hwo  Hwana  Hwana
hya  Hya  Hya
hye  Armenian  Armenian
iai  Iaai  Iaai
ian  Iatmul  Iatmul
iap  Iapama  Iapama
iar  Purari  Purari
iba  Iban  Iban
ibb  Ibibio  Ibibio
ibd  Iwaidja  Iwaidja
ibe  Akpes  Akpes
ibg  Ibanag  Ibanag
ibl  Ibaloi  Ibaloi
ibm  Agoi  Agoi
ibn  Ibino  Ibino
ibo  Igbo  Igbo
ibr  Ibuoro  Ibuoro
ibu  Ibu  Ibu
iby  Ibani  Ibani
ica  Ede Ica  Ede Ica
ich  Etkywan  Etkywan
icl  Icelandic Sign Language  Icelandic Sign Language
icr  Islander Creole English  Creole English, Islander
ida  Idakho-Isukha-Tiriki  Idakho-Isukha-Tiriki
ida  Luidakho-Luisukha-Lutirichi  Luidakho-Luisukha-Lutirichi
idb  Indo-Portuguese  Indo-Portuguese
idc  Ajiya  Ajiya
idc  Idon  Idon
idd  Ede Idaca  Ede Idaca
ide  Idere  Idere
idi  Idi  Idi
ido  Ido  Ido
idr  Indri  Indri
ids  Idesa  Idesa
idt  Idaté  Idaté
idu  Idoma  Idoma
ifa  Amganad Ifugao  Ifugao, Amganad
ifb  Ayangan Ifugao  Ifugao, Ayangan
ifb  Batad Ifugao  Ifugao, Batad
ife  Ifè  Ifè
iff  Ifo  Ifo
ifk  Tuwali Ifugao  Ifugao, Tuwali
ifm  Teke-Fuumu  Teke-Fuumu
ifu  Mayoyao Ifugao  Ifugao, Mayoyao
ify  Keley-I Kallahan  Kallahan, Keley-I
igb  Ebira  Ebira
ige  Igede  Igede
igg  Igana  Igana
igl  Igala  Igala
igm  Kanggape  Kanggape
ign  Ignaciano  Ignaciano
igo  Isebe  Isebe
igs  Interglossa  Interglossa
igw  Igwe  Igwe
ihb  Iha Based Pidgin  Iha Based Pidgin
ihi  Ihievbe  Ihievbe
ihp  Iha  Iha
ihw  Bidhawal  Bidhawal
iii  Nuosu  Nuosu
iii  Sichuan Yi  Yi, Sichuan
iin  Thiin  Thiin
ijc  Izon  Izon
ije  Biseni  Biseni
ijj  Ede Ije  Ede Ije
ijn  Kalabari  Kalabari
ijs  Southeast Ijo  Ijo, Southeast
ike  Eastern Canadian Inuktitut  Inuktitut, Eastern Canadian
iki  Iko  Iko
ikk  Ika  Ika
ikl  Ikulu  Ikulu
iko  Olulumo-Ikom  Olulumo-Ikom
ikp  Ikpeshi  Ikpeshi
ikr  Ikaranggal  Ikaranggal
ikt  Inuinnaqtun  Inuinnaqtun
ikt  Western Canadian Inuktitut  Inuktitut, Western Canadian
iku  Inuktitut  Inuktitut
ikv  Iku-Gora-Ankwa  Iku-Gora-Ankwa
ikw  Ikwere  Ikwere
ikx  Ik  Ik
ikz  Ikizu  Ikizu
ila  Ile Ape  Ile Ape
ilb  Ila  Ila
ile  Interlingue  Interlingue
ile  Occidental  Occidental
ilg  Garig-Ilgar  Garig-Ilgar
ili  Ili Turki  Ili Turki
ilk  Ilongot  Ilongot
ill  Iranun  Iranun
ilo  Iloko  Iloko
ils  International Sign  International Sign
ilu  Ili'uun  Ili'uun
ilv  Ilue  Ilue
ima  Mala Malasar  Malasar, Mala
ime  Imeraguen  Imeraguen
imi  Anamgura  Anamgura
iml  Miluk  Miluk
imn  Imonda  Imonda
imo  Imbongu  Imbongu
imr  Imroing  Imroing
ims  Marsian  Marsian
imy  Milyan  Milyan
ina  Interlingua (International Auxiliary Language Association)  Interlingua (International Auxiliary Language Association)
inb  Inga  Inga
ind  Indonesian  Indonesian
ing  Degexit'an  Degexit'an
inh  Ingush  Ingush
inj  Jungle Inga  Inga, Jungle
inl  Indonesian Sign Language  Indonesian Sign Language
inm  Minaean  Minaean
inn  Isinai  Isinai
ino  Inoke-Yate  Inoke-Yate
inp  Iñapari  Iñapari
ins  Indian Sign Language  Indian Sign Language
int  Intha  Intha
inz  Ineseño  Ineseño
ior  Inor  Inor
iou  Tuma-Irumu  Tuma-Irumu
iow  Iowa-Oto  Iowa-Oto
ipi  Ipili  Ipili
ipk  Inupiaq  Inupiaq
ipo  Ipiko  Ipiko
iqu  Iquito  Iquito
iqw  Ikwo  Ikwo
ire  Iresim  Iresim
irh  Irarutu  Irarutu
iri  Irigwe  Irigwe
irk  Iraqw  Iraqw
irn  Irántxe  Irántxe
irr  Ir  Ir
iru  Irula  Irula
irx  Kamberau  Kamberau
iry  Iraya  Iraya
isa  Isabi  Isabi
isc  Isconahua  Isconahua
isd  Isnag  Isnag
ise  Italian Sign Language  Italian Sign Language
isg  Irish Sign Language  Irish Sign Language
ish  Esan  Esan
isi  Nkem-Nkum  Nkem-Nkum
isk  Ishkashimi  Ishkashimi
isl  Icelandic  Icelandic
ism  Masimasi  Masimasi
isn  Isanzu  Isanzu
iso  Isoko  Isoko
isr  Israeli Sign Language  Israeli Sign Language
ist  Istriot  Istriot
isu  Isu (Menchum Division)  Isu (Menchum Division)
ita  Italian  Italian
itb  Binongan Itneg  Itneg, Binongan
ite  Itene  Itene
iti  Inlaod Itneg  Itneg, Inlaod
itk  Judeo-Italian  Judeo-Italian
itl  Itelmen  Itelmen
itm  Itu Mbon Uzo  Itu Mbon Uzo
ito  Itonama  Itonama
itr  Iteri  Iteri
its  Isekiri  Isekiri
itt  Maeng Itneg  Itneg, Maeng
itv  Itawit  Itawit
itw  Ito  Ito
itx  Itik  Itik
ity  Moyadan Itneg  Itneg, Moyadan
itz  Itzá  Itzá
ium  Iu Mien  Mien, Iu
ivb  Ibatan  Ibatan
ivv  Ivatan  Ivatan
iwk  I-Wak  I-Wak
iwm  Iwam  Iwam
iwo  Iwur  Iwur
iws  Sepik Iwam  Iwam, Sepik
ixc  Ixcatec  Ixcatec
ixl  Ixil  Ixil
iya  Iyayu  Iyayu
iyo  Mesaka  Mesaka
iyx  Yaka (Congo)  Yaka (Congo)
izh  Ingrian  Ingrian
izr  Izere  Izere
izz  Izii  Izii
jaa  Jamamadí  Jamamadí
jab  Hyam  Hyam
jac  Jakalteko  Jakalteko
jac  Popti'  Popti'
jad  Jahanka  Jahanka
jae  Yabem  Yabem
jaf  Jara  Jara
jah  Jah Hut  Jah Hut
jaj  Zazao  Zazao
jak  Jakun  Jakun
jal  Yalahatan  Yalahatan
jam  Jamaican Creole English  Creole English, Jamaican
jan  Jandai  Jandai
jao  Yanyuwa  Yanyuwa
jaq  Yaqay  Yaqay
jas  New Caledonian Javanese  Javanese, New Caledonian
jat  Jakati  Jakati
jau  Yaur  Yaur
jav  Javanese  Javanese
jax  Jambi Malay  Malay, Jambi
jay  Yan-nhangu  Yan-nhangu
jaz  Jawe  Jawe
jbe  Judeo-Berber  Judeo-Berber
jbi  Badjiri  Badjiri
jbj  Arandai  Arandai
jbk  Barikewa  Barikewa
jbn  Nafusi  Nafusi
jbo  Lojban  Lojban
jbr  Jofotek-Bromnya  Jofotek-Bromnya
jbt  Jabutí  Jabutí
jbu  Jukun Takum  Jukun Takum
jbw  Yawijibaya  Yawijibaya
jcs  Jamaican Country Sign Language  Jamaican Country Sign Language
jct  Krymchak  Krymchak
jda  Jad  Jad
jdg  Jadgali  Jadgali
jdt  Judeo-Tat  Judeo-Tat
jeb  Jebero  Jebero
jee  Jerung  Jerung
jeg  Jeng  Jeng
jeh  Jeh  Jeh
jei  Yei  Yei
jek  Jeri Kuo  Jeri Kuo
jel  Yelmek  Yelmek
jen  Dza  Dza
jer  Jere  Jere
jet  Manem  Manem
jeu  Jonkor Bourmataguil  Jonkor Bourmataguil
jgb  Ngbee  Ngbee
jge  Judeo-Georgian  Judeo-Georgian
jgk  Gwak  Gwak
jgo  Ngomba  Ngomba
jhi  Jehai  Jehai
jhs  Jhankot Sign Language  Jhankot Sign Language
jia  Jina  Jina
jib  Jibu  Jibu
jic  Tol  Tol
jid  Bu  Bu
jie  Jilbe  Jilbe
jig  Djingili  Djingili
jih  Shangzhai  Shangzhai
jih  sTodsde  sTodsde
jii  Jiiddu  Jiiddu
jil  Jilim  Jilim
jim  Jimi (Cameroon)  Jimi (Cameroon)
jio  Jiamao  Jiamao
jiq  Guanyinqiao  Guanyinqiao
jiq  Lavrung  Lavrung
jit  Jita  Jita
jiu  Youle Jinuo  Jinuo, Youle
jiv  Shuar  Shuar
jiy  Buyuan Jinuo  Jinuo, Buyuan
jjr  Bankal  Bankal
jkm  Mobwa Karen  Karen, Mobwa
jko  Kubo  Kubo
jkp  Paku Karen  Karen, Paku
jkr  Koro (India)  Koro (India)
jku  Labir  Labir
jle  Ngile  Ngile
jls  Jamaican Sign Language  Jamaican Sign Language
jma  Dima  Dima
jmb  Zumbun  Zumbun
jmc  Machame  Machame
jmd  Yamdena  Yamdena
jmi  Jimi (Nigeria)  Jimi (Nigeria)
jml  Jumli  Jumli
jmn  Makuri Naga  Naga, Makuri
jmr  Kamara  Kamara
jms  Mashi (Nigeria)  Mashi (Nigeria)
jmw  Mouwase  Mouwase
jmx  Western Juxtlahuaca Mixtec  Mixtec, Western Juxtlahuaca
jna  Jangshung  Jangshung
jnd  Jandavra  Jandavra
jng  Yangman  Yangman
jni  Janji  Janji
jnj  Yemsa  Yemsa
jnl  Rawat  Rawat
jns  Jaunsari  Jaunsari
job  Joba  Joba
jod  Wojenaka  Wojenaka
jor  Jorá  Jorá
jos  Jordanian Sign Language  Jordanian Sign Language
jow  Jowulu  Jowulu
jpa  Jewish Palestinian Aramaic  Aramaic, Jewish Palestinian
jpn  Japanese  Japanese
jpr  Judeo-Persian  Judeo-Persian
jqr  Jaqaru  Jaqaru
jra  Jarai  Jarai
jrb  Judeo-Arabic  Judeo-Arabic
jrr  Jiru  Jiru
jrt  Jorto  Jorto
jru  Japrería  Japrería
jsl  Japanese Sign Language  Japanese Sign Language
jua  Júma  Júma
jub  Wannu  Wannu
juc  Jurchen  Jurchen
jud  Worodougou  Worodougou
juh  Hõne  Hõne
jui  Ngadjuri  Ngadjuri
juk  Wapan  Wapan
jul  Jirel  Jirel
jum  Jumjum  Jumjum
jun  Juang  Juang
juo  Jiba  Jiba
jup  Hupdë  Hupdë
jur  Jurúna  Jurúna
jus  Jumla Sign Language  Jumla Sign Language
jut  Jutish  Jutish
juu  Ju  Ju
juw  Wãpha  Wãpha
juy  Juray  Juray
jvd  Javindo  Javindo
jvn  Caribbean Javanese  Javanese, Caribbean
jwi  Jwira-Pepesa  Jwira-Pepesa
jya  Jiarong  Jiarong
jye  Judeo-Yemeni Arabic  Arabic, Judeo-Yemeni
jyy  Jaya  Jaya
kaa  Kara-Kalpak  Kara-Kalpak
kab  Kabyle  Kabyle
kac  Jingpho  Jingpho
kac  Kachin  Kachin
kad  Adara  Adara
kae  Ketangalan  Ketangalan
kaf  Katso  Katso
kag  Kajaman  Kajaman
kah  Kara (Central African Republic)  Kara (Central African Republic)
kai  Karekare  Karekare
kaj  Jju  Jju
kak  Kayapa Kallahan  Kallahan, Kayapa
kal  Greenlandic  Greenlandic
kal  Kalaallisut  Kalaallisut
kam  Kamba (Kenya)  Kamba (Kenya)
kan  Kannada  Kannada
kao  Xaasongaxango  Xaasongaxango
kap  Bezhta  Bezhta
kaq  Capanahua  Capanahua
kas  Kashmiri  Kashmiri
kat  Georgian  Georgian
kau  Kanuri  Kanuri
kav  Katukína  Katukína
kaw  Kawi  Kawi
kax  Kao  Kao
kay  Kamayurá  Kamayurá
kaz  Kazakh  Kazakh
kba  Kalarko  Kalarko
kbb  Kaxuiâna  Kaxuiâna
kbc  Kadiwéu  Kadiwéu
kbd  Kabardian  Kabardian
kbe  Kanju  Kanju
kbf  Kakauhua  Kakauhua
kbg  Khamba  Khamba
kbh  Camsá  Camsá
kbi  Kaptiau  Kaptiau
kbj  Kari  Kari
kbk  Grass Koiari  Koiari, Grass
kbl  Kanembu  Kanembu
kbm  Iwal  Iwal
kbn  Kare (Central African Republic)  Kare (Central African Republic)
kbo  Keliko  Keliko
kbp  Kabiyè  Kabiyè
kbq  Kamano  Kamano
kbr  Kafa  Kafa
kbs  Kande  Kande
kbt  Abadi  Abadi
kbu  Kabutra  Kabutra
kbv  Dera (Indonesia)  Dera (Indonesia)
kbw  Kaiep  Kaiep
kbx  Ap Ma  Ap Ma
kby  Manga Kanuri  Kanuri, Manga
kbz  Duhwa  Duhwa
kca  Khanty  Khanty
kcb  Kawacha  Kawacha
kcc  Lubila  Lubila
kcd  Ngkâlmpw Kanum  Kanum, Ngkâlmpw
kce  Kaivi  Kaivi
kcf  Ukaan  Ukaan
kcg  Tyap  Tyap
kch  Vono  Vono
kci  Kamantan  Kamantan
kcj  Kobiana  Kobiana
kck  Kalanga  Kalanga
kcl  Kala  Kala
kcl  Kela (Papua New Guinea)  Kela (Papua New Guinea)
kcm  Gula (Central African Republic)  Gula (Central African Republic)
kcn  Nubi  Nubi
kco  Kinalakna  Kinalakna
kcp  Kanga  Kanga
kcq  Kamo  Kamo
kcr  Katla  Katla
kcs  Koenoem  Koenoem
kct  Kaian  Kaian
kcu  Kami (Tanzania)  Kami (Tanzania)
kcv  Kete  Kete
kcw  Kabwari  Kabwari
kcx  Kachama-Ganjule  Kachama-Ganjule
kcy  Korandje  Korandje
kcz  Konongo  Konongo
kda  Worimi  Worimi
kdc  Kutu  Kutu
kdd  Yankunytjatjara  Yankunytjatjara
kde  Makonde  Makonde
kdf  Mamusi  Mamusi
kdg  Seba  Seba
kdh  Tem  Tem
kdi  Kumam  Kumam
kdj  Karamojong  Karamojong
kdk  Kwényi  Kwényi
kdk  Numèè  Numèè
kdl  Tsikimba  Tsikimba
kdm  Kagoma  Kagoma
kdn  Kunda  Kunda
kdp  Kaningdon-Nindem  Kaningdon-Nindem
kdq  Koch  Koch
kdr  Karaim  Karaim
kdt  Kuy  Kuy
kdu  Kadaru  Kadaru
kdw  Koneraw  Koneraw
kdx  Kam  Kam
kdy  Keder  Keder
kdy  Keijar  Keijar
kdz  Kwaja  Kwaja
kea  Kabuverdianu  Kabuverdianu
keb  Kélé  Kélé
kec  Keiga  Keiga
ked  Kerewe  Kerewe
kee  Eastern Keres  Keres, Eastern
kef  Kpessi  Kpessi
keg  Tese  Tese
keh  Keak  Keak
kei  Kei  Kei
kej  Kadar  Kadar
kek  Kekchí  Kekchí
kel  Kela (Democratic Republic of Congo)  Kela (Democratic Republic of Congo)
kem  Kemak  Kemak
ken  Kenyang  Kenyang
keo  Kakwa  Kakwa
kep  Kaikadi  Kaikadi
keq  Kamar  Kamar
ker  Kera  Kera
kes  Kugbo  Kugbo
ket  Ket  Ket
keu  Akebu  Akebu
kev  Kanikkaran  Kanikkaran
kew  West Kewa  Kewa, West
kex  Kukna  Kukna
key  Kupia  Kupia
kez  Kukele  Kukele
kfa  Kodava  Kodava
kfb  Northwestern Kolami  Kolami, Northwestern
kfc  Konda-Dora  Konda-Dora
kfd  Korra Koraga  Koraga, Korra
kfe  Kota (India)  Kota (India)
kff  Koya  Koya
kfg  Kudiya  Kudiya
kfh  Kurichiya  Kurichiya
kfi  Kannada Kurumba  Kurumba, Kannada
kfj  Kemiehua  Kemiehua
kfk  Kinnauri  Kinnauri
kfl  Kung  Kung
kfm  Khunsari  Khunsari
kfn  Kuk  Kuk
kfo  Koro (Côte d'Ivoire)  Koro (Côte d'Ivoire)
kfp  Korwa  Korwa
kfq  Korku  Korku
kfr  Kachchi  Kachchi
kfs  Bilaspuri  Bilaspuri
kft  Kanjari  Kanjari
kfu  Katkari  Katkari
kfv  Kurmukar  Kurmukar
kfw  Kharam Naga  Naga, Kharam
kfx  Kullu Pahari  Pahari, Kullu
kfy  Kumaoni  Kumaoni
kfz  Koromfé  Koromfé
kga  Koyaga  Koyaga
kgb  Kawe  Kawe
kgc  Kasseng  Kasseng
kgd  Kataang  Kataang
kge  Komering  Komering
kgf  Kube  Kube
kgg  Kusunda  Kusunda
kgi  Selangor Sign Language  Selangor Sign Language
kgj  Gamale Kham  Kham, Gamale
kgk  Kaiwá  Kaiwá
kgl  Kunggari  Kunggari
kgm  Karipúna  Karipúna
kgn  Karingani  Karingani
kgo  Krongo  Krongo
kgp  Kaingang  Kaingang
kgq  Kamoro  Kamoro
kgr  Abun  Abun
kgs  Kumbainggar  Kumbainggar
kgt  Somyev  Somyev
kgu  Kobol  Kobol
kgv  Karas  Karas
kgw  Karon Dori  Karon Dori
kgx  Kamaru  Kamaru
kgy  Kyerung  Kyerung
kha  Khasi  Khasi
khb  Lü  Lü
khc  Tukang Besi North  Tukang Besi North
khd  Bädi Kanum  Kanum, Bädi
khe  Korowai  Korowai
khf  Khuen  Khuen
khg  Khams Tibetan  Tibetan, Khams
khh  Kehu  Kehu
khj  Kuturmi  Kuturmi
khk  Halh Mongolian  Mongolian, Halh
khl  Lusi  Lusi
khm  Central Khmer  Khmer, Central
khn  Khandesi  Khandesi
kho  Khotanese  Khotanese
kho  Sakan  Sakan
khp  Kapauri  Kapauri
khp  Kapori  Kapori
khq  Koyra Chiini Songhay  Songhay, Koyra Chiini
khr  Kharia  Kharia
khs  Kasua  Kasua
kht  Khamti  Khamti
khu  Nkhumbi  Nkhumbi
khv  Khvarshi  Khvarshi
khw  Khowar  Khowar
khx  Kanu  Kanu
khy  Kele (Democratic Republic of Congo)  Kele (Democratic Republic of Congo)
khz  Keapara  Keapara
kia  Kim  Kim
kib  Koalib  Koalib
kic  Kickapoo  Kickapoo
kid  Koshin  Koshin
kie  Kibet  Kibet
kif  Eastern Parbate Kham  Kham, Eastern Parbate
kig  Kimaama  Kimaama
kig  Kimaghima  Kimaghima
kih  Kilmeri  Kilmeri
kii  Kitsai  Kitsai
kij  Kilivila  Kilivila
kik  Gikuyu  Gikuyu
kik  Kikuyu  Kikuyu
kil  Kariya  Kariya
kim  Karagas  Karagas
kin  Kinyarwanda  Kinyarwanda
kio  Kiowa  Kiowa
kip  Sheshi Kham  Kham, Sheshi
kiq  Kosadle  Kosadle
kiq  Kosare  Kosare
kir  Kirghiz  Kirghiz
kir  Kyrgyz  Kyrgyz
kis  Kis  Kis
kit  Agob  Agob
kiu  Kirmanjki (individual language)  Kirmanjki (individual language)
kiv  Kimbu  Kimbu
kiw  Northeast Kiwai  Kiwai, Northeast
kix  Khiamniungan Naga  Naga, Khiamniungan
kiy  Kirikiri  Kirikiri
kiz  Kisi  Kisi
kja  Mlap  Mlap
kjb  Kanjobal  Kanjobal
kjb  Q'anjob'al  Q'anjob'al
kjc  Coastal Konjo  Konjo, Coastal
kjd  Southern Kiwai  Kiwai, Southern
kje  Kisar  Kisar
kjf  Khalaj  Khalaj
kjg  Khmu  Khmu
kjh  Khakas  Khakas
kji  Zabana  Zabana
kjj  Khinalugh  Khinalugh
kjk  Highland Konjo  Konjo, Highland
kjl  Western Parbate Kham  Kham, Western Parbate
kjm  Kháng  Kháng
kjn  Kunjen  Kunjen
kjo  Harijan Kinnauri  Kinnauri, Harijan
kjp  Pwo Eastern Karen  Karen, Pwo Eastern
kjq  Western Keres  Keres, Western
kjr  Kurudu  Kurudu
kjs  East Kewa  Kewa, East
kjt  Phrae Pwo Karen  Karen, Phrae Pwo
kju  Kashaya  Kashaya
kjx  Ramopa  Ramopa
kjy  Erave  Erave
kjz  Bumthangkha  Bumthangkha
kka  Kakanda  Kakanda
kkb  Kwerisa  Kwerisa
kkc  Odoodee  Odoodee
kkd  Kinuku  Kinuku
kke  Kakabe  Kakabe
kkf  Kalaktang Monpa  Monpa, Kalaktang
kkg  Mabaka Valley Kalinga  Kalinga, Mabaka Valley
kkh  Khün  Khün
kki  Kagulu  Kagulu
kkj  Kako  Kako
kkk  Kokota  Kokota
kkl  Kosarek Yale  Yale, Kosarek
kkm  Kiong  Kiong
kkn  Kon Keu  Kon Keu
kko  Karko  Karko
kkp  Gugubera  Gugubera
kkq  Kaiku  Kaiku
kkr  Kir-Balar  Kir-Balar
kks  Giiwo  Giiwo
kkt  Koi  Koi
kku  Tumi  Tumi
kkv  Kangean  Kangean
kkw  Teke-Kukuya  Teke-Kukuya
kkx  Kohin  Kohin
kky  Guguyimidjir  Guguyimidjir
kkz  Kaska  Kaska
kla  Klamath-Modoc  Klamath-Modoc
klb  Kiliwa  Kiliwa
klc  Kolbila  Kolbila
kld  Gamilaraay  Gamilaraay
kle  Kulung (Nepal)  Kulung (Nepal)
klf  Kendeje  Kendeje
klg  Tagakaulo  Tagakaulo
klh  Weliki  Weliki
kli  Kalumpang  Kalumpang
klj  Turkic Khalaj  Khalaj, Turkic
klk  Kono (Nigeria)  Kono (Nigeria)
kll  Kagan Kalagan  Kalagan, Kagan
klm  Migum  Migum
kln  Kalenjin  Kalenjin
klo  Kapya  Kapya
klp  Kamasa  Kamasa
klq  Rumu  Rumu
klr  Khaling  Khaling
kls  Kalasha  Kalasha
klt  Nukna  Nukna
klu  Klao  Klao
klv  Maskelynes  Maskelynes
klw  Lindu  Lindu
klx  Koluwawa  Koluwawa
kly  Kalao  Kalao
klz  Kabola  Kabola
kma  Konni  Konni
kmb  Kimbundu  Kimbundu
kmc  Southern Dong  Dong, Southern
kmd  Majukayang Kalinga  Kalinga, Majukayang
kme  Bakole  Bakole
kmf  Kare (Papua New Guinea)  Kare (Papua New Guinea)
kmg  Kâte  Kâte
kmh  Kalam  Kalam
kmi  Kami (Nigeria)  Kami (Nigeria)
kmj  Kumarbhag Paharia  Kumarbhag Paharia
kmk  Limos Kalinga  Kalinga, Limos
kml  Tanudan Kalinga  Kalinga, Tanudan
kmm  Kom (India)  Kom (India)
kmn  Awtuw  Awtuw
kmo  Kwoma  Kwoma
kmp  Gimme  Gimme
kmq  Kwama  Kwama
kmr  Northern Kurdish  Kurdish, Northern
kms  Kamasau  Kamasau
kmt  Kemtuik  Kemtuik
kmu  Kanite  Kanite
kmv  Karipúna Creole French  Creole French, Karipúna
kmw  Komo (Democratic Republic of Congo)  Komo (Democratic Republic of Congo)
kmx  Waboda  Waboda
kmy  Koma  Koma
kmz  Khorasani Turkish  Khorasani Turkish
kna  Dera (Nigeria)  Dera (Nigeria)
knb  Lubuagan Kalinga  Kalinga, Lubuagan
knc  Central Kanuri  Kanuri, Central
knd  Konda  Konda
kne  Kankanaey  Kankanaey
knf  Mankanya  Mankanya
kng  Koongo  Koongo
kni  Kanufi  Kanufi
knj  Western Kanjobal  Kanjobal, Western
knk  Kuranko  Kuranko
knl  Keninjal  Keninjal
knm  Kanamarí  Kanamarí
knn  Konkani (individual language)  Konkani (individual language)
kno  Kono (Sierra Leone)  Kono (Sierra Leone)
knp  Kwanja  Kwanja
knq  Kintaq  Kintaq
knr  Kaningra  Kaningra
kns  Kensiu  Kensiu
knt  Panoan Katukína  Katukína, Panoan
knu  Kono (Guinea)  Kono (Guinea)
knv  Tabo  Tabo
knw  Kung-Ekoka  Kung-Ekoka
knx  Kendayan  Kendayan
knx  Salako  Salako
kny  Kanyok  Kanyok
knz  Kalamsé  Kalamsé
koa  Konomala  Konomala
koc  Kpati  Kpati
kod  Kodi  Kodi
koe  Kacipo-Balesi  Kacipo-Balesi
kof  Kubi  Kubi
kog  Cogui  Cogui
kog  Kogi  Kogi
koh  Koyo  Koyo
koi  Komi-Permyak  Komi-Permyak
koj  Sara Dunjo  Sara Dunjo
kok  Konkani (macrolanguage)  Konkani (macrolanguage)
kol  Kol (Papua New Guinea)  Kol (Papua New Guinea)
kom  Komi  Komi
kon  Kongo  Kongo
koo  Konzo  Konzo
kop  Waube  Waube
koq  Kota (Gabon)  Kota (Gabon)
kor  Korean  Korean
kos  Kosraean  Kosraean
kot  Lagwan  Lagwan
kou  Koke  Koke
kov  Kudu-Camo  Kudu-Camo
kow  Kugama  Kugama
kox  Coxima  Coxima
koy  Koyukon  Koyukon
koz  Korak  Korak
kpa  Kutto  Kutto
kpb  Mullu Kurumba  Kurumba, Mullu
kpc  Curripaco  Curripaco
kpd  Koba  Koba
kpe  Kpelle  Kpelle
kpf  Komba  Komba
kpg  Kapingamarangi  Kapingamarangi
kph  Kplang  Kplang
kpi  Kofei  Kofei
kpj  Karajá  Karajá
kpk  Kpan  Kpan
kpl  Kpala  Kpala
kpm  Koho  Koho
kpn  Kepkiriwát  Kepkiriwát
kpo  Ikposo  Ikposo
kpq  Korupun-Sela  Korupun-Sela
kpr  Korafe-Yegha  Korafe-Yegha
kps  Tehit  Tehit
kpt  Karata  Karata
kpu  Kafoa  Kafoa
kpv  Komi-Zyrian  Komi-Zyrian
kpw  Kobon  Kobon
kpx  Mountain Koiali  Koiali, Mountain
kpy  Koryak  Koryak
kpz  Kupsabiny  Kupsabiny
kqa  Mum  Mum
kqb  Kovai  Kovai
kqc  Doromu-Koki  Doromu-Koki
kqd  Koy Sanjaq Surat  Koy Sanjaq Surat
kqe  Kalagan  Kalagan
kqf  Kakabai  Kakabai
kqg  Khe  Khe
kqh  Kisankasa  Kisankasa
kqi  Koitabu  Koitabu
kqj  Koromira  Koromira
kqk  Kotafon Gbe  Gbe, Kotafon
kql  Kyenele  Kyenele
kqm  Khisa  Khisa
kqn  Kaonde  Kaonde
kqo  Eastern Krahn  Krahn, Eastern
kqp  Kimré  Kimré
kqq  Krenak  Krenak
kqr  Kimaragang  Kimaragang
kqs  Northern Kissi  Kissi, Northern
kqt  Klias River Kadazan  Kadazan, Klias River
kqu  Seroa  Seroa
kqv  Okolod  Okolod
kqw  Kandas  Kandas
kqx  Mser  Mser
kqy  Koorete  Koorete
kqz  Korana  Korana
kra  Kumhali  Kumhali
krb  Karkin  Karkin
krc  Karachay-Balkar  Karachay-Balkar
krd  Kairui-Midiki  Kairui-Midiki
kre  Panará  Panará
krf  Koro (Vanuatu)  Koro (Vanuatu)
krh  Kurama  Kurama
kri  Krio  Krio
krj  Kinaray-A  Kinaray-A
krk  Kerek  Kerek
krl  Karelian  Karelian
krm  Krim  Krim
krn  Sapo  Sapo
krp  Korop  Korop
krr  Kru'ng 2  Kru'ng 2
krs  Gbaya (Sudan)  Gbaya (Sudan)
krt  Tumari Kanuri  Kanuri, Tumari
kru  Kurukh  Kurukh
krv  Kavet  Kavet
krw  Western Krahn  Krahn, Western
krx  Karon  Karon
kry  Kryts  Kryts
krz  Sota Kanum  Kanum, Sota
ksa  Shuwa-Zamani  Shuwa-Zamani
ksb  Shambala  Shambala
ksc  Southern Kalinga  Kalinga, Southern
ksd  Kuanua  Kuanua
kse  Kuni  Kuni
ksf  Bafia  Bafia
ksg  Kusaghe  Kusaghe
ksh  Kölsch  Kölsch
ksi  I'saka  I'saka
ksi  Krisa  Krisa
ksj  Uare  Uare
ksk  Kansa  Kansa
ksl  Kumalu  Kumalu
ksm  Kumba  Kumba
ksn  Kasiguranin  Kasiguranin
kso  Kofa  Kofa
ksp  Kaba  Kaba
ksq  Kwaami  Kwaami
ksr  Borong  Borong
kss  Southern Kisi  Kisi, Southern
kst  Winyé  Winyé
ksu  Khamyang  Khamyang
ksv  Kusu  Kusu
ksw  S'gaw Karen  Karen, S'gaw
ksx  Kedang  Kedang
ksy  Kharia Thar  Kharia Thar
ksz  Kodaku  Kodaku
kta  Katua  Katua
ktb  Kambaata  Kambaata
ktc  Kholok  Kholok
ktd  Kokata  Kokata
kte  Nubri  Nubri
ktf  Kwami  Kwami
ktg  Kalkutung  Kalkutung
kth  Karanga  Karanga
kti  North Muyu  Muyu, North
ktj  Plapo Krumen  Krumen, Plapo
ktk  Kaniet  Kaniet
ktl  Koroshi  Koroshi
ktm  Kurti  Kurti
ktn  Karitiâna  Karitiâna
kto  Kuot  Kuot
ktp  Kaduo  Kaduo
ktq  Katabaga  Katabaga
ktr  Kota Marudu Tinagas  Kota Marudu Tinagas
kts  South Muyu  Muyu, South
ktt  Ketum  Ketum
ktu  Kituba (Democratic Republic of Congo)  Kituba (Democratic Republic of Congo)
ktv  Eastern Katu  Katu, Eastern
ktw  Kato  Kato
ktx  Kaxararí  Kaxararí
kty  Kango (Bas-Uélé District)  Kango (Bas-Uélé District)
ktz  Ju/'hoan  Ju/'hoan
kua  Kuanyama  Kuanyama
kua  Kwanyama  Kwanyama
kub  Kutep  Kutep
kuc  Kwinsu  Kwinsu
kud  'Auhelawa  'Auhelawa
kue  Kuman  Kuman
kuf  Western Katu  Katu, Western
kug  Kupa  Kupa
kuh  Kushi  Kushi
kui  Kuikúro-Kalapálo  Kuikúro-Kalapálo
kuj  Kuria  Kuria
kuk  Kepo'  Kepo'
kul  Kulere  Kulere
kum  Kumyk  Kumyk
kun  Kunama  Kunama
kuo  Kumukio  Kumukio
kup  Kunimaipa  Kunimaipa
kuq  Karipuna  Karipuna
kur  Kurdish  Kurdish
kus  Kusaal  Kusaal
kut  Kutenai  Kutenai
kuu  Upper Kuskokwim  Kuskokwim, Upper
kuv  Kur  Kur
kuw  Kpagua  Kpagua
kux  Kukatja  Kukatja
kuy  Kuuku-Ya'u  Kuuku-Ya'u
kuz  Kunza  Kunza
kva  Bagvalal  Bagvalal
kvb  Kubu  Kubu
kvc  Kove  Kove
kvd  Kui (Indonesia)  Kui (Indonesia)
kve  Kalabakan  Kalabakan
kvf  Kabalai  Kabalai
kvg  Kuni-Boazi  Kuni-Boazi
kvh  Komodo  Komodo
kvi  Kwang  Kwang
kvj  Psikye  Psikye
kvk  Korean Sign Language  Korean Sign Language
kvl  Kayaw  Kayaw
kvm  Kendem  Kendem
kvn  Border Kuna  Kuna, Border
kvo  Dobel  Dobel
kvp  Kompane  Kompane
kvq  Geba Karen  Karen, Geba
kvr  Kerinci  Kerinci
kvs  Kunggara  Kunggara
kvt  Lahta  Lahta
kvt  Lahta Karen  Karen, Lahta
kvu  Yinbaw Karen  Karen, Yinbaw
kvv  Kola  Kola
kvw  Wersing  Wersing
kvx  Parkari Koli  Koli, Parkari
kvy  Yintale  Yintale
kvy  Yintale Karen  Karen, Yintale
kvz  Tsakwambo  Tsakwambo
kvz  Tsaukambo  Tsaukambo
kwa  Dâw  Dâw
kwb  Kwa  Kwa
kwc  Likwala  Likwala
kwd  Kwaio  Kwaio
kwe  Kwerba  Kwerba
kwf  Kwara'ae  Kwara'ae
kwg  Sara Kaba Deme  Sara Kaba Deme
kwh  Kowiai  Kowiai
kwi  Awa-Cuaiquer  Awa-Cuaiquer
kwj  Kwanga  Kwanga
kwk  Kwakiutl  Kwakiutl
kwl  Kofyar  Kofyar
kwm  Kwambi  Kwambi
kwn  Kwangali  Kwangali
kwo  Kwomtari  Kwomtari
kwp  Kodia  Kodia
kwq  Kwak  Kwak
kwr  Kwer  Kwer
kws  Kwese  Kwese
kwt  Kwesten  Kwesten
kwu  Kwakum  Kwakum
kwv  Sara Kaba Náà  Sara Kaba Náà
kww  Kwinti  Kwinti
kwx  Khirwar  Khirwar
kwy  San Salvador Kongo  Kongo, San Salvador
kwz  Kwadi  Kwadi
kxa  Kairiru  Kairiru
kxb  Krobu  Krobu
kxc  Khonso  Khonso
kxc  Konso  Konso
kxd  Brunei  Brunei
kxe  Kakihum  Kakihum
kxf  Manumanaw  Manumanaw
kxf  Manumanaw Karen  Karen, Manumanaw
kxh  Karo (Ethiopia)  Karo (Ethiopia)
kxi  Keningau Murut  Murut, Keningau
kxj  Kulfa  Kulfa
kxk  Zayein Karen  Karen, Zayein
kxl  Nepali Kurux  Kurux, Nepali
kxm  Northern Khmer  Khmer, Northern
kxn  Kanowit-Tanjong Melanau  Melanau, Kanowit-Tanjong
kxo  Kanoé  Kanoé
kxp  Wadiyara Koli  Koli, Wadiyara
kxq  Smärky Kanum  Kanum, Smärky
kxr  Koro (Papua New Guinea)  Koro (Papua New Guinea)
kxs  Kangjia  Kangjia
kxt  Koiwat  Koiwat
kxu  Kui (India)  Kui (India)
kxv  Kuvi  Kuvi
kxw  Konai  Konai
kxx  Likuba  Likuba
kxy  Kayong  Kayong
kxz  Kerewo  Kerewo
kya  Kwaya  Kwaya
kyb  Butbut Kalinga  Kalinga, Butbut
kyc  Kyaka  Kyaka
kyd  Karey  Karey
kye  Krache  Krache
kyf  Kouya  Kouya
kyg  Keyagana  Keyagana
kyh  Karok  Karok
kyi  Kiput  Kiput
kyj  Karao  Karao
kyk  Kamayo  Kamayo
kyl  Kalapuya  Kalapuya
kym  Kpatili  Kpatili
kyn  Northern Binukidnon  Binukidnon, Northern
kyo  Kelon  Kelon
kyp  Kang  Kang
kyq  Kenga  Kenga
kyr  Kuruáya  Kuruáya
kys  Baram Kayan  Kayan, Baram
kyt  Kayagar  Kayagar
kyu  Western Kayah  Kayah, Western
kyv  Kayort  Kayort
kyw  Kudmali  Kudmali
kyx  Rapoisi  Rapoisi
kyy  Kambaira  Kambaira
kyz  Kayabí  Kayabí
kza  Western Karaboro  Karaboro, Western
kzb  Kaibobo  Kaibobo
kzc  Bondoukou Kulango  Kulango, Bondoukou
kzd  Kadai  Kadai
kze  Kosena  Kosena
kzf  Da'a Kaili  Kaili, Da'a
kzg  Kikai  Kikai
kzi  Kelabit  Kelabit
kzj  Coastal Kadazan  Kadazan, Coastal
kzk  Kazukuru  Kazukuru
kzl  Kayeli  Kayeli
kzm  Kais  Kais
kzn  Kokola  Kokola
kzo  Kaningi  Kaningi
kzp  Kaidipang  Kaidipang
kzq  Kaike  Kaike
kzr  Karang  Karang
kzs  Sugut Dusun  Dusun, Sugut
kzt  Tambunan Dusun  Dusun, Tambunan
kzu  Kayupulau  Kayupulau
kzv  Komyandaret  Komyandaret
kzw  Karirí-Xocó  Karirí-Xocó
kzx  Kamarian  Kamarian
kzy  Kango (Tshopo District)  Kango (Tshopo District)
kzz  Kalabra  Kalabra
laa  Southern Subanen  Subanen, Southern
lab  Linear A  Linear A
lac  Lacandon  Lacandon
lad  Ladino  Ladino
lae  Pattani  Pattani
laf  Lafofa  Lafofa
lag  Langi  Langi
lah  Lahnda  Lahnda
lai  Lambya  Lambya
laj  Lango (Uganda)  Lango (Uganda)
lak  Laka (Nigeria)  Laka (Nigeria)
lal  Lalia  Lalia
lam  Lamba  Lamba
lan  Laru  Laru
lao  Lao  Lao
lap  Laka (Chad)  Laka (Chad)
laq  Qabiao  Qabiao
lar  Larteh  Larteh
las  Lama (Togo)  Lama (Togo)
lat  Latin  Latin
lau  Laba  Laba
lav  Latvian  Latvian
law  Lauje  Lauje
lax  Tiwa  Tiwa
lay  Lama (Myanmar)  Lama (Myanmar)
laz  Aribwatsa  Aribwatsa
lba  Lui  Lui
lbb  Label  Label
lbc  Lakkia  Lakkia
lbe  Lak  Lak
lbf  Tinani  Tinani
lbg  Laopang  Laopang
lbi  La'bi  La'bi
lbj  Ladakhi  Ladakhi
lbk  Central Bontok  Bontok, Central
lbl  Libon Bikol  Bikol, Libon
lbm  Lodhi  Lodhi
lbn  Lamet  Lamet
lbo  Laven  Laven
lbq  Wampar  Wampar
lbr  Lohorung  Lohorung
lbs  Libyan Sign Language  Libyan Sign Language
lbt  Lachi  Lachi
lbu  Labu  Labu
lbv  Lavatbura-Lamusong  Lavatbura-Lamusong
lbw  Tolaki  Tolaki
lbx  Lawangan  Lawangan
lby  Lamu-Lamu  Lamu-Lamu
lbz  Lardil  Lardil
lcc  Legenyem  Legenyem
lcd  Lola  Lola
lce  Loncong  Loncong
lcf  Lubu  Lubu
lch  Luchazi  Luchazi
lcl  Lisela  Lisela
lcm  Tungag  Tungag
lcp  Western Lawa  Lawa, Western
lcq  Luhu  Luhu
lcs  Lisabata-Nuniali  Lisabata-Nuniali
lda  Kla-Dan  Kla-Dan
ldb  Dũya  Dũya
ldd  Luri  Luri
ldg  Lenyima  Lenyima
ldh  Lamja-Dengsa-Tola  Lamja-Dengsa-Tola
ldi  Laari  Laari
ldj  Lemoro  Lemoro
ldk  Leelau  Leelau
ldl  Kaan  Kaan
ldm  Landoma  Landoma
ldn  Láadan  Láadan
ldo  Loo  Loo
ldp  Tso  Tso
ldq  Lufu  Lufu
lea  Lega-Shabunda  Lega-Shabunda
leb  Lala-Bisa  Lala-Bisa
lec  Leco  Leco
led  Lendu  Lendu
lee  Lyélé  Lyélé
lef  Lelemi  Lelemi
leg  Lengua  Lengua
leh  Lenje  Lenje
lei  Lemio  Lemio
lej  Lengola  Lengola
lek  Leipon  Leipon
lel  Lele (Democratic Republic of Congo)  Lele (Democratic Republic of Congo)
lem  Nomaande  Nomaande
len  Lenca  Lenca
leo  Leti (Cameroon)  Leti (Cameroon)
lep  Lepcha  Lepcha
leq  Lembena  Lembena
ler  Lenkau  Lenkau
les  Lese  Lese
let  Amio-Gelimi  Amio-Gelimi
let  Lesing-Gelimi  Lesing-Gelimi
leu  Kara (Papua New Guinea)  Kara (Papua New Guinea)
lev  Lamma  Lamma
lew  Ledo Kaili  Kaili, Ledo
lex  Luang  Luang
ley  Lemolang  Lemolang
lez  Lezghian  Lezghian
lfa  Lefa  Lefa
lfn  Lingua Franca Nova  Lingua Franca Nova
lga  Lungga  Lungga
lgb  Laghu  Laghu
lgg  Lugbara  Lugbara
lgh  Laghuu  Laghuu
lgi  Lengilu  Lengilu
lgk  Lingarak  Lingarak
lgk  Neverver  Neverver
lgl  Wala  Wala
lgm  Lega-Mwenga  Lega-Mwenga
lgn  Opuuo  Opuuo
lgq  Logba  Logba
lgr  Lengo  Lengo
lgt  Pahi  Pahi
lgu  Longgu  Longgu
lgz  Ligenza  Ligenza
lha  Laha (Viet Nam)  Laha (Viet Nam)
lhh  Laha (Indonesia)  Laha (Indonesia)
lhi  Lahu Shi  Lahu Shi
lhl  Lahul Lohar  Lohar, Lahul
lhm  Lhomi  Lhomi
lhn  Lahanan  Lahanan
lhp  Lhokpu  Lhokpu
lhs  Mlahsö  Mlahsö
lht  Lo-Toga  Lo-Toga
lhu  Lahu  Lahu
lia  West-Central Limba  Limba, West-Central
lib  Likum  Likum
lic  Hlai  Hlai
lid  Nyindrou  Nyindrou
lie  Likila  Likila
lif  Limbu  Limbu
lig  Ligbi  Ligbi
lih  Lihir  Lihir
lii  Lingkhim  Lingkhim
lij  Ligurian  Ligurian
lik  Lika  Lika
lil  Lillooet  Lillooet
lim  Limburgan  Limburgan
lim  Limburger  Limburger
lim  Limburgish  Limburgish
lin  Lingala  Lingala
lio  Liki  Liki
lip  Sekpele  Sekpele
liq  Libido  Libido
lir  Liberian English  English, Liberian
lis  Lisu  Lisu
lit  Lithuanian  Lithuanian
liu  Logorik  Logorik
liv  Liv  Liv
liw  Col  Col
lix  Liabuku  Liabuku
liy  Banda-Bambari  Banda-Bambari
liz  Libinza  Libinza
lja  Golpa  Golpa
lje  Rampi  Rampi
lji  Laiyolo  Laiyolo
ljl  Li'o  Li'o
ljp  Lampung Api  Lampung Api
ljw  Yirandali  Yirandali
ljx  Yuru  Yuru
lka  Lakalei  Lakalei
lkb  Kabras  Kabras
lkb  Lukabaras  Lukabaras
lkc  Kucong  Kucong
lkd  Lakondê  Lakondê
lke  Kenyi  Kenyi
lkh  Lakha  Lakha
lki  Laki  Laki
lkj  Remun  Remun
lkl  Laeko-Libuat  Laeko-Libuat
lkm  Kalaamaya  Kalaamaya
lkn  Lakon  Lakon
lkn  Vure  Vure
lko  Khayo  Khayo
lko  Olukhayo  Olukhayo
lkr  Päri  Päri
lks  Kisa  Kisa
lks  Olushisa  Olushisa
lkt  Lakota  Lakota
lku  Kungkari  Kungkari
lky  Lokoya  Lokoya
lla  Lala-Roba  Lala-Roba
llb  Lolo  Lolo
llc  Lele (Guinea)  Lele (Guinea)
lld  Ladin  Ladin
lle  Lele (Papua New Guinea)  Lele (Papua New Guinea)
llf  Hermit  Hermit
llg  Lole  Lole
llh  Lamu  Lamu
lli  Teke-Laali  Teke-Laali
llj  Ladji Ladji  Ladji Ladji
llk  Lelak  Lelak
lll  Lilau  Lilau
llm  Lasalimu  Lasalimu
lln  Lele (Chad)  Lele (Chad)
llo  Khlor  Khlor
llp  North Efate  Efate, North
llq  Lolak  Lolak
lls  Lithuanian Sign Language  Lithuanian Sign Language
llu  Lau  Lau
llx  Lauan  Lauan
lma  East Limba  Limba, East
lmb  Merei  Merei
lmc  Limilngan  Limilngan
lmd  Lumun  Lumun
lme  Pévé  Pévé
lmf  South Lembata  Lembata, South
lmg  Lamogai  Lamogai
lmh  Lambichhong  Lambichhong
lmi  Lombi  Lombi
lmj  West Lembata  Lembata, West
lmk  Lamkang  Lamkang
lml  Hano  Hano
lmm  Lamam  Lamam
lmn  Lambadi  Lambadi
lmo  Lombard  Lombard
lmp  Limbum  Limbum
lmq  Lamatuka  Lamatuka
lmr  Lamalera  Lamalera
lmu  Lamenu  Lamenu
lmv  Lomaiviti  Lomaiviti
lmw  Lake Miwok  Miwok, Lake
lmx  Laimbue  Laimbue
lmy  Lamboya  Lamboya
lmz  Lumbee  Lumbee
lna  Langbashe  Langbashe
lnb  Mbalanhu  Mbalanhu
lnd  Lun Bawang  Lun Bawang
lnd  Lundayeh  Lundayeh
lng  Langobardic  Langobardic
lnh  Lanoh  Lanoh
lni  Daantanai'  Daantanai'
lnj  Leningitij  Leningitij
lnl  South Central Banda  Banda, South Central
lnm  Langam  Langam
lnn  Lorediakarkar  Lorediakarkar
lno  Lango (Sudan)  Lango (Sudan)
lns  Lamnso'  Lamnso'
lnu  Longuda  Longuda
lnw  Lanima  Lanima
lnz  Lonzo  Lonzo
loa  Loloda  Loloda
lob  Lobi  Lobi
loc  Inonhan  Inonhan
loe  Saluan  Saluan
lof  Logol  Logol
log  Logo  Logo
loh  Narim  Narim
loi  Loma (Côte d'Ivoire)  Loma (Côte d'Ivoire)
loj  Lou  Lou
lok  Loko  Loko
lol  Mongo  Mongo
lom  Loma (Liberia)  Loma (Liberia)
lon  Malawi Lomwe  Lomwe, Malawi
loo  Lombo  Lombo
lop  Lopa  Lopa
loq  Lobala  Lobala
lor  Téén  Téén
los  Loniu  Loniu
lot  Otuho  Otuho
lou  Louisiana Creole French  Creole French, Louisiana
lov  Lopi  Lopi
low  Tampias Lobu  Lobu, Tampias
lox  Loun  Loun
loy  Loke  Loke
loz  Lozi  Lozi
lpa  Lelepa  Lelepa
lpe  Lepki  Lepki
lpn  Long Phuri Naga  Naga, Long Phuri
lpo  Lipo  Lipo
lpx  Lopit  Lopit
lra  Rara Bakati'  Rara Bakati'
lrc  Northern Luri  Luri, Northern
lre  Laurentian  Laurentian
lrg  Laragia  Laragia
lri  Marachi  Marachi
lri  Olumarachi  Olumarachi
lrk  Loarki  Loarki
lrl  Lari  Lari
lrm  Marama  Marama
lrm  Olumarama  Olumarama
lrn  Lorang  Lorang
lro  Laro  Laro
lrr  Southern Yamphu  Yamphu, Southern
lrt  Larantuka Malay  Malay, Larantuka
lrv  Larevat  Larevat
lrz  Lemerig  Lemerig
lsa  Lasgerdi  Lasgerdi
lsd  Lishana Deni  Lishana Deni
lse  Lusengo  Lusengo
lsg  Lyons Sign Language  Lyons Sign Language
lsh  Lish  Lish
lsi  Lashi  Lashi
lsl  Latvian Sign Language  Latvian Sign Language
lsm  Olusamia  Olusamia
lsm  Saamia  Saamia
lso  Laos Sign Language  Laos Sign Language
lsp  Lengua de Señas Panameñas  Lengua de Señas Panameñas
lsp  Panamanian Sign Language  Panamanian Sign Language
lsr  Aruop  Aruop
lss  Lasi  Lasi
lst  Trinidad and Tobago Sign Language  Trinidad and Tobago Sign Language
lsy  Mauritian Sign Language  Mauritian Sign Language
ltc  Late Middle Chinese  Chinese, Late Middle
ltg  Latgalian  Latgalian
lti  Leti (Indonesia)  Leti (Indonesia)
ltn  Latundê  Latundê
lto  Olutsotso  Olutsotso
lto  Tsotso  Tsotso
lts  Lutachoni  Lutachoni
lts  Tachoni  Tachoni
ltu  Latu  Latu
ltz  Letzeburgesch  Letzeburgesch
ltz  Luxembourgish  Luxembourgish
lua  Luba-Lulua  Luba-Lulua
lub  Luba-Katanga  Luba-Katanga
luc  Aringa  Aringa
lud  Ludian  Ludian
lue  Luvale  Luvale
luf  Laua  Laua
lug  Ganda  Ganda
lui  Luiseno  Luiseno
luj  Luna  Luna
luk  Lunanakha  Lunanakha
lul  Olu'bo  Olu'bo
lum  Luimbi  Luimbi
lun  Lunda  Lunda
luo  Dholuo  Dholuo
luo  Luo (Kenya and Tanzania)  Luo (Kenya and Tanzania)
lup  Lumbu  Lumbu
luq  Lucumi  Lucumi
lur  Laura  Laura
lus  Lushai  Lushai
lut  Lushootseed  Lushootseed
luu  Lumba-Yakkha  Lumba-Yakkha
luv  Luwati  Luwati
luw  Luo (Cameroon)  Luo (Cameroon)
luy  Luyia  Luyia
luy  Oluluyia  Oluluyia
luz  Southern Luri  Luri, Southern
lva  Maku'a  Maku'a
lvk  Lavukaleve  Lavukaleve
lvs  Standard Latvian  Latvian, Standard
lvu  Levuka  Levuka
lwa  Lwalu  Lwalu
lwe  Lewo Eleng  Lewo Eleng
lwg  Oluwanga  Oluwanga
lwg  Wanga  Wanga
lwh  White Lachi  Lachi, White
lwl  Eastern Lawa  Lawa, Eastern
lwm  Laomian  Laomian
lwo  Luwo  Luwo
lwt  Lewotobi  Lewotobi
lwu  Lawu  Lawu
lww  Lewo  Lewo
lya  Layakha  Layakha
lyg  Lyngngam  Lyngngam
lyn  Luyana  Luyana
lzh  Literary Chinese  Chinese, Literary
lzl  Litzlitz  Litzlitz
lzn  Leinong Naga  Naga, Leinong
lzz  Laz  Laz
maa  San Jerónimo Tecóatl Mazatec  Mazatec, San Jerónimo Tecóatl
mab  Yutanduchi Mixtec  Mixtec, Yutanduchi
mad  Madurese  Madurese
mae  Bo-Rukul  Bo-Rukul
maf  Mafa  Mafa
mag  Magahi  Magahi
mah  Marshallese  Marshallese
mai  Maithili  Maithili
maj  Jalapa De Díaz Mazatec  Mazatec, Jalapa De Díaz
mak  Makasar  Makasar
mal  Malayalam  Malayalam
mam  Mam  Mam
man  Manding  Manding
man  Mandingo  Mandingo
maq  Chiquihuitlán Mazatec  Mazatec, Chiquihuitlán
mar  Marathi  Marathi
mas  Masai  Masai
mat  San Francisco Matlatzinca  Matlatzinca, San Francisco
mau  Huautla Mazatec  Mazatec, Huautla
mav  Sateré-Mawé  Sateré-Mawé
maw  Mampruli  Mampruli
max  North Moluccan Malay  Malay, North Moluccan
maz  Central Mazahua  Mazahua, Central
mba  Higaonon  Higaonon
mbb  Western Bukidnon Manobo  Manobo, Western Bukidnon
mbc  Macushi  Macushi
mbd  Dibabawon Manobo  Manobo, Dibabawon
mbe  Molale  Molale
mbf  Baba Malay  Malay, Baba
mbh  Mangseng  Mangseng
mbi  Ilianen Manobo  Manobo, Ilianen
mbj  Nadëb  Nadëb
mbk  Malol  Malol
mbl  Maxakalí  Maxakalí
mbm  Ombamba  Ombamba
mbn  Macaguán  Macaguán
mbo  Mbo (Cameroon)  Mbo (Cameroon)
mbp  Malayo  Malayo
mbq  Maisin  Maisin
mbr  Nukak Makú  Nukak Makú
mbs  Sarangani Manobo  Manobo, Sarangani
mbt  Matigsalug Manobo  Manobo, Matigsalug
mbu  Mbula-Bwazza  Mbula-Bwazza
mbv  Mbulungish  Mbulungish
mbw  Maring  Maring
mbx  Mari (East Sepik Province)  Mari (East Sepik Province)
mby  Memoni  Memoni
mbz  Amoltepec Mixtec  Mixtec, Amoltepec
mca  Maca  Maca
mcb  Machiguenga  Machiguenga
mcc  Bitur  Bitur
mcd  Sharanahua  Sharanahua
mce  Itundujia Mixtec  Mixtec, Itundujia
mcf  Matsés  Matsés
mcg  Mapoyo  Mapoyo
mch  Maquiritari  Maquiritari
mci  Mese  Mese
mcj  Mvanip  Mvanip
mck  Mbunda  Mbunda
mcl  Macaguaje  Macaguaje
mcm  Malaccan Creole Portuguese  Creole Portuguese, Malaccan
mcn  Masana  Masana
mco  Coatlán Mixe  Mixe, Coatlán
mcp  Makaa  Makaa
mcq  Ese  Ese
mcr  Menya  Menya
mcs  Mambai  Mambai
mct  Mengisa  Mengisa
mcu  Cameroon Mambila  Mambila, Cameroon
mcv  Minanibai  Minanibai
mcw  Mawa (Chad)  Mawa (Chad)
mcx  Mpiemo  Mpiemo
mcy  South Watut  Watut, South
mcz  Mawan  Mawan
mda  Mada (Nigeria)  Mada (Nigeria)
mdb  Morigi  Morigi
mdc  Male (Papua New Guinea)  Male (Papua New Guinea)
mdd  Mbum  Mbum
mde  Maba (Chad)  Maba (Chad)
mdf  Moksha  Moksha
mdg  Massalat  Massalat
mdh  Maguindanaon  Maguindanaon
mdi  Mamvu  Mamvu
mdj  Mangbetu  Mangbetu
mdk  Mangbutu  Mangbutu
mdl  Maltese Sign Language  Maltese Sign Language
mdm  Mayogo  Mayogo
mdn  Mbati  Mbati
mdp  Mbala  Mbala
mdq  Mbole  Mbole
mdr  Mandar  Mandar
mds  Maria (Papua New Guinea)  Maria (Papua New Guinea)
mdt  Mbere  Mbere
mdu  Mboko  Mboko
mdv  Santa Lucía Monteverde Mixtec  Mixtec, Santa Lucía Monteverde
mdw  Mbosi  Mbosi
mdx  Dizin  Dizin
mdy  Male (Ethiopia)  Male (Ethiopia)
mdz  Suruí Do Pará  Suruí Do Pará
mea  Menka  Menka
meb  Ikobi  Ikobi
mec  Mara  Mara
med  Melpa  Melpa
mee  Mengen  Mengen
mef  Megam  Megam
meh  Southwestern Tlaxiaco Mixtec  Mixtec, Southwestern Tlaxiaco
mei  Midob  Midob
mej  Meyah  Meyah
mek  Mekeo  Mekeo
mel  Central Melanau  Melanau, Central
mem  Mangala  Mangala
men  Mende (Sierra Leone)  Mende (Sierra Leone)
meo  Kedah Malay  Malay, Kedah
mep  Miriwung  Miriwung
meq  Merey  Merey
mer  Meru  Meru
mes  Masmaje  Masmaje
met  Mato  Mato
meu  Motu  Motu
mev  Mano  Mano
mew  Maaka  Maaka
mey  Hassaniyya  Hassaniyya
mez  Menominee  Menominee
mfa  Pattani Malay  Malay, Pattani
mfb  Bangka  Bangka
mfc  Mba  Mba
mfd  Mendankwe-Nkwen  Mendankwe-Nkwen
mfe  Morisyen  Morisyen
mff  Naki  Naki
mfg  Mogofin  Mogofin
mfh  Matal  Matal
mfi  Wandala  Wandala
mfj  Mefele  Mefele
mfk  North Mofu  Mofu, North
mfl  Putai  Putai
mfm  Marghi South  Marghi South
mfn  Cross River Mbembe  Mbembe, Cross River
mfo  Mbe  Mbe
mfp  Makassar Malay  Malay, Makassar
mfq  Moba  Moba
mfr  Marithiel  Marithiel
mfs  Mexican Sign Language  Mexican Sign Language
mft  Mokerang  Mokerang
mfu  Mbwela  Mbwela
mfv  Mandjak  Mandjak
mfw  Mulaha  Mulaha
mfx  Melo  Melo
mfy  Mayo  Mayo
mfz  Mabaan  Mabaan
mga  Middle Irish (900-1200)  Irish, Middle (900-1200)
mgb  Mararit  Mararit
mgc  Morokodo  Morokodo
mgd  Moru  Moru
mge  Mango  Mango
mgf  Maklew  Maklew
mgg  Mpumpong  Mpumpong
mgh  Makhuwa-Meetto  Makhuwa-Meetto
mgi  Lijili  Lijili
mgj  Abureni  Abureni
mgk  Mawes  Mawes
mgl  Maleu-Kilenge  Maleu-Kilenge
mgm  Mambae  Mambae
mgn  Mbangi  Mbangi
mgo  Meta'  Meta'
mgp  Eastern Magar  Magar, Eastern
mgq  Malila  Malila
mgr  Mambwe-Lungu  Mambwe-Lungu
mgs  Manda (Tanzania)  Manda (Tanzania)
mgt  Mongol  Mongol
mgu  Mailu  Mailu
mgv  Matengo  Matengo
mgw  Matumbi  Matumbi
mgy  Mbunga  Mbunga
mgz  Mbugwe  Mbugwe
mha  Manda (India)  Manda (India)
mhb  Mahongwe  Mahongwe
mhc  Mocho  Mocho
mhd  Mbugu  Mbugu
mhe  Besisi  Besisi
mhe  Mah Meri  Mah Meri
mhf  Mamaa  Mamaa
mhg  Margu  Margu
mhh  Maskoy Pidgin  Maskoy Pidgin
mhi  Ma'di  Ma'di
mhj  Mogholi  Mogholi
mhk  Mungaka  Mungaka
mhl  Mauwake  Mauwake
mhm  Makhuwa-Moniga  Makhuwa-Moniga
mhn  Mócheno  Mócheno
mho  Mashi (Zambia)  Mashi (Zambia)
mhp  Balinese Malay  Malay, Balinese
mhq  Mandan  Mandan
mhr  Eastern Mari  Mari, Eastern
mhs  Buru (Indonesia)  Buru (Indonesia)
mht  Mandahuaca  Mandahuaca
mhu  Darang Deng  Deng, Darang
mhu  Digaro-Mishmi  Digaro-Mishmi
mhw  Mbukushu  Mbukushu
mhx  Lhaovo  Lhaovo
mhx  Maru  Maru
mhy  Ma'anyan  Ma'anyan
mhz  Mor (Mor Islands)  Mor (Mor Islands)
mia  Miami  Miami
mib  Atatláhuca Mixtec  Mixtec, Atatláhuca
mic  Micmac  Micmac
mic  Mi'kmaq  Mi'kmaq
mid  Mandaic  Mandaic
mie  Ocotepec Mixtec  Mixtec, Ocotepec
mif  Mofu-Gudur  Mofu-Gudur
mig  San Miguel El Grande Mixtec  Mixtec, San Miguel El Grande
mih  Chayuco Mixtec  Mixtec, Chayuco
mii  Chigmecatitlán Mixtec  Mixtec, Chigmecatitlán
mij  Abar  Abar
mij  Mungbam  Mungbam
mik  Mikasuki  Mikasuki
mil  Peñoles Mixtec  Mixtec, Peñoles
mim  Alacatlatzala Mixtec  Mixtec, Alacatlatzala
min  Minangkabau  Minangkabau
mio  Pinotepa Nacional Mixtec  Mixtec, Pinotepa Nacional
mip  Apasco-Apoala Mixtec  Mixtec, Apasco-Apoala
miq  Mískito  Mískito
mir  Isthmus Mixe  Mixe, Isthmus
mis  Uncoded languages  Uncoded languages
mit  Southern Puebla Mixtec  Mixtec, Southern Puebla
miu  Cacaloxtepec Mixtec  Mixtec, Cacaloxtepec
miw  Akoye  Akoye
mix  Mixtepec Mixtec  Mixtec, Mixtepec
miy  Ayutla Mixtec  Mixtec, Ayutla
miz  Coatzospan Mixtec  Mixtec, Coatzospan
mjc  San Juan Colorado Mixtec  Mixtec, San Juan Colorado
mjd  Northwest Maidu  Maidu, Northwest
mje  Muskum  Muskum
mjg  Tu  Tu
mjh  Mwera (Nyasa)  Mwera (Nyasa)
mji  Kim Mun  Kim Mun
mjj  Mawak  Mawak
mjk  Matukar  Matukar
mjl  Mandeali  Mandeali
mjm  Medebur  Medebur
mjn  Ma (Papua New Guinea)  Ma (Papua New Guinea)
mjo  Malankuravan  Malankuravan
mjp  Malapandaram  Malapandaram
mjq  Malaryan  Malaryan
mjr  Malavedan  Malavedan
mjs  Miship  Miship
mjt  Sauria Paharia  Sauria Paharia
mju  Manna-Dora  Manna-Dora
mjv  Mannan  Mannan
mjw  Karbi  Karbi
mjx  Mahali  Mahali
mjy  Mahican  Mahican
mjz  Majhi  Majhi
mka  Mbre  Mbre
mkb  Mal Paharia  Mal Paharia
mkc  Siliput  Siliput
mkd  Macedonian  Macedonian
mke  Mawchi  Mawchi
mkf  Miya  Miya
mkg  Mak (China)  Mak (China)
mki  Dhatki  Dhatki
mkj  Mokilese  Mokilese
mkk  Byep  Byep
mkl  Mokole  Mokole
mkm  Moklen  Moklen
mkn  Kupang Malay  Malay, Kupang
mko  Mingang Doso  Mingang Doso
mkp  Moikodi  Moikodi
mkq  Bay Miwok  Miwok, Bay
mkr  Malas  Malas
mks  Silacayoapan Mixtec  Mixtec, Silacayoapan
mkt  Vamale  Vamale
mku  Konyanka Maninka  Maninka, Konyanka
mkv  Mafea  Mafea
mkw  Kituba (Congo)  Kituba (Congo)
mkx  Kinamiging Manobo  Manobo, Kinamiging
mky  East Makian  Makian, East
mkz  Makasae  Makasae
mla  Malo  Malo
mlb  Mbule  Mbule
mlc  Cao Lan  Cao Lan
mle  Manambu  Manambu
mlf  Mal  Mal
mlg  Malagasy  Malagasy
mlh  Mape  Mape
mli  Malimpung  Malimpung
mlj  Miltu  Miltu
mlk  Ilwana  Ilwana
mlk  Kiwilwana  Kiwilwana
mll  Malua Bay  Malua Bay
mlm  Mulam  Mulam
mln  Malango  Malango
mlo  Mlomp  Mlomp
mlp  Bargam  Bargam
mlq  Western Maninkakan  Maninkakan, Western
mlr  Vame  Vame
mls  Masalit  Masalit
mlt  Maltese  Maltese
mlu  To'abaita  To'abaita
mlv  Motlav  Motlav
mlv  Mwotlap  Mwotlap
mlw  Moloko  Moloko
mlx  Malfaxal  Malfaxal
mlx  Naha'ai  Naha'ai
mlz  Malaynon  Malaynon
mma  Mama  Mama
mmb  Momina  Momina
mmc  Michoacán Mazahua  Mazahua, Michoacán
mmd  Maonan  Maonan
mme  Mae  Mae
mmf  Mundat  Mundat
mmg  North Ambrym  Ambrym, North
mmh  Mehináku  Mehináku
mmi  Musar  Musar
mmj  Majhwar  Majhwar
mmk  Mukha-Dora  Mukha-Dora
mml  Man Met  Man Met
mmm  Maii  Maii
mmn  Mamanwa  Mamanwa
mmo  Mangga Buang  Buang, Mangga
mmp  Siawi  Siawi
mmq  Musak  Musak
mmr  Western Xiangxi Miao  Miao, Western Xiangxi
mmt  Malalamai  Malalamai
mmu  Mmaala  Mmaala
mmv  Miriti  Miriti
mmw  Emae  Emae
mmx  Madak  Madak
mmy  Migaama  Migaama
mmz  Mabaale  Mabaale
mna  Mbula  Mbula
mnb  Muna  Muna
mnc  Manchu  Manchu
mnd  Mondé  Mondé
mne  Naba  Naba
mnf  Mundani  Mundani
mng  Eastern Mnong  Mnong, Eastern
mnh  Mono (Democratic Republic of Congo)  Mono (Democratic Republic of Congo)
mni  Manipuri  Manipuri
mnj  Munji  Munji
mnk  Mandinka  Mandinka
mnl  Tiale  Tiale
mnm  Mapena  Mapena
mnn  Southern Mnong  Mnong, Southern
mnp  Min Bei Chinese  Chinese, Min Bei
mnq  Minriq  Minriq
mnr  Mono (USA)  Mono (USA)
mns  Mansi  Mansi
mnu  Mer  Mer
mnv  Rennell-Bellona  Rennell-Bellona
mnw  Mon  Mon
mnx  Manikion  Manikion
mny  Manyawa  Manyawa
mnz  Moni  Moni
moa  Mwan  Mwan
moc  Mocoví  Mocoví
mod  Mobilian  Mobilian
moe  Montagnais  Montagnais
mog  Mongondow  Mongondow
moh  Mohawk  Mohawk
moi  Mboi  Mboi
moj  Monzombo  Monzombo
mok  Morori  Morori
mom  Mangue  Mangue
mon  Mongolian  Mongolian
moo  Monom  Monom
mop  Mopán Maya  Mopán Maya
moq  Mor (Bomberai Peninsula)  Mor (Bomberai Peninsula)
mor  Moro  Moro
mos  Mossi  Mossi
mot  Barí  Barí
mou  Mogum  Mogum
mov  Mohave  Mohave
mow  Moi (Congo)  Moi (Congo)
mox  Molima  Molima
moy  Shekkacho  Shekkacho
moz  Gergiko  Gergiko
moz  Mukulu  Mukulu
mpa  Mpoto  Mpoto
mpb  Mullukmulluk  Mullukmulluk
mpc  Mangarayi  Mangarayi
mpd  Machinere  Machinere
mpe  Majang  Majang
mpg  Marba  Marba
mph  Maung  Maung
mpi  Mpade  Mpade
mpj  Martu Wangka  Martu Wangka
mpk  Mbara (Chad)  Mbara (Chad)
mpl  Middle Watut  Watut, Middle
mpm  Yosondúa Mixtec  Mixtec, Yosondúa
mpn  Mindiri  Mindiri
mpo  Miu  Miu
mpp  Migabac  Migabac
mpq  Matís  Matís
mpr  Vangunu  Vangunu
mps  Dadibi  Dadibi
mpt  Mian  Mian
mpu  Makuráp  Makuráp
mpv  Mungkip  Mungkip
mpw  Mapidian  Mapidian
mpx  Misima-Panaeati  Misima-Panaeati
mpy  Mapia  Mapia
mpz  Mpi  Mpi
mqa  Maba (Indonesia)  Maba (Indonesia)
mqb  Mbuko  Mbuko
mqc  Mangole  Mangole
mqe  Matepi  Matepi
mqf  Momuna  Momuna
mqg  Kota Bangun Kutai Malay  Malay, Kota Bangun Kutai
mqh  Tlazoyaltepec Mixtec  Mixtec, Tlazoyaltepec
mqi  Mariri  Mariri
mqj  Mamasa  Mamasa
mqk  Rajah Kabunsuwan Manobo  Manobo, Rajah Kabunsuwan
mql  Mbelime  Mbelime
mqm  South Marquesan  Marquesan, South
mqn  Moronene  Moronene
mqo  Modole  Modole
mqp  Manipa  Manipa
mqq  Minokok  Minokok
mqr  Mander  Mander
mqs  West Makian  Makian, West
mqt  Mok  Mok
mqu  Mandari  Mandari
mqv  Mosimo  Mosimo
mqw  Murupi  Murupi
mqx  Mamuju  Mamuju
mqy  Manggarai  Manggarai
mqz  Pano  Pano
mra  Mlabri  Mlabri
mrb  Marino  Marino
mrc  Maricopa  Maricopa
mrd  Western Magar  Magar, Western
mre  Martha's Vineyard Sign Language  Martha's Vineyard Sign Language
mrf  Elseng  Elseng
mrg  Mising  Mising
mrh  Mara Chin  Chin, Mara
mri  Maori  Maori
mrj  Western Mari  Mari, Western
mrk  Hmwaveke  Hmwaveke
mrl  Mortlockese  Mortlockese
mrm  Merlav  Merlav
mrm  Mwerlap  Mwerlap
mrn  Cheke Holo  Cheke Holo
mro  Mru  Mru
mrp  Morouas  Morouas
mrq  North Marquesan  Marquesan, North
mrr  Maria (India)  Maria (India)
mrs  Maragus  Maragus
mrt  Marghi Central  Marghi Central
mru  Mono (Cameroon)  Mono (Cameroon)
mrv  Mangareva  Mangareva
mrw  Maranao  Maranao
mrx  Dineor  Dineor
mrx  Maremgi  Maremgi
mry  Mandaya  Mandaya
mrz  Marind  Marind
msa  Malay (macrolanguage)  Malay (macrolanguage)
msb  Masbatenyo  Masbatenyo
msc  Sankaran Maninka  Maninka, Sankaran
msd  Yucatec Maya Sign Language  Yucatec Maya Sign Language
mse  Musey  Musey
msf  Mekwei  Mekwei
msg  Moraid  Moraid
msh  Masikoro Malagasy  Malagasy, Masikoro
msi  Sabah Malay  Malay, Sabah
msj  Ma (Democratic Republic of Congo)  Ma (Democratic Republic of Congo)
msk  Mansaka  Mansaka
msl  Molof  Molof
msl  Poule  Poule
msm  Agusan Manobo  Manobo, Agusan
msn  Vurës  Vurës
mso  Mombum  Mombum
msp  Maritsauá  Maritsauá
msq  Caac  Caac
msr  Mongolian Sign Language  Mongolian Sign Language
mss  West Masela  Masela, West
msu  Musom  Musom
msv  Maslam  Maslam
msw  Mansoanka  Mansoanka
msx  Moresada  Moresada
msy  Aruamu  Aruamu
msz  Momare  Momare
mta  Cotabato Manobo  Manobo, Cotabato
mtb  Anyin Morofo  Anyin Morofo
mtc  Munit  Munit
mtd  Mualang  Mualang
mte  Mono (Solomon Islands)  Mono (Solomon Islands)
mtf  Murik (Papua New Guinea)  Murik (Papua New Guinea)
mtg  Una  Una
mth  Munggui  Munggui
mti  Maiwa (Papua New Guinea)  Maiwa (Papua New Guinea)
mtj  Moskona  Moskona
mtk  Mbe'  Mbe'
mtl  Montol  Montol
mtm  Mator  Mator
mtn  Matagalpa  Matagalpa
mto  Totontepec Mixe  Mixe, Totontepec
mtp  Wichí Lhamtés Nocten  Wichí Lhamtés Nocten
mtq  Muong  Muong
mtr  Mewari  Mewari
mts  Yora  Yora
mtt  Mota  Mota
mtu  Tututepec Mixtec  Mixtec, Tututepec
mtv  Asaro'o  Asaro'o
mtw  Southern Binukidnon  Binukidnon, Southern
mtx  Tidaá Mixtec  Mixtec, Tidaá
mty  Nabi  Nabi
mua  Mundang  Mundang
mub  Mubi  Mubi
muc  Ajumbu  Ajumbu
mud  Mednyj Aleut  Aleut, Mednyj
mue  Media Lengua  Media Lengua
mug  Musgu  Musgu
muh  Mündü  Mündü
mui  Musi  Musi
muj  Mabire  Mabire
muk  Mugom  Mugom
mul  Multiple languages  Multiple languages
mum  Maiwala  Maiwala
muo  Nyong  Nyong
mup  Malvi  Malvi
muq  Eastern Xiangxi Miao  Miao, Eastern Xiangxi
mur  Murle  Murle
mus  Creek  Creek
mut  Western Muria  Muria, Western
muu  Yaaku  Yaaku
muv  Muthuvan  Muthuvan
mux  Bo-Ung  Bo-Ung
muy  Muyang  Muyang
muz  Mursi  Mursi
mva  Manam  Manam
mvb  Mattole  Mattole
mvd  Mamboru  Mamboru
mve  Marwari (Pakistan)  Marwari (Pakistan)
mvf  Peripheral Mongolian  Mongolian, Peripheral
mvg  Yucuañe Mixtec  Mixtec, Yucuañe
mvh  Mulgi  Mulgi
mvi  Miyako  Miyako
mvk  Mekmek  Mekmek
mvl  Mbara (Australia)  Mbara (Australia)
mvm  Muya  Muya
mvn  Minaveha  Minaveha
mvo  Marovo  Marovo
mvp  Duri  Duri
mvq  Moere  Moere
mvr  Marau  Marau
mvs  Massep  Massep
mvt  Mpotovoro  Mpotovoro
mvu  Marfa  Marfa
mvv  Tagal Murut  Murut, Tagal
mvw  Machinga  Machinga
mvx  Meoswar  Meoswar
mvy  Indus Kohistani  Kohistani, Indus
mvz  Mesqan  Mesqan
mwa  Mwatebu  Mwatebu
mwb  Juwal  Juwal
mwc  Are  Are
mwe  Mwera (Chimwera)  Mwera (Chimwera)
mwf  Murrinh-Patha  Murrinh-Patha
mwg  Aiklep  Aiklep
mwh  Mouk-Aria  Mouk-Aria
mwi  Labo  Labo
mwi  Ninde  Ninde
mwj  Maligo  Maligo
mwk  Kita Maninkakan  Maninkakan, Kita
mwl  Mirandese  Mirandese
mwm  Sar  Sar
mwn  Nyamwanga  Nyamwanga
mwo  Central Maewo  Maewo, Central
mwp  Kala Lagaw Ya  Kala Lagaw Ya
mwq  Mün Chin  Chin, Mün
mwr  Marwari  Marwari
mws  Mwimbi-Muthambi  Mwimbi-Muthambi
mwt  Moken  Moken
mwu  Mittu  Mittu
mwv  Mentawai  Mentawai
mww  Hmong Daw  Hmong Daw
mwx  Mediak  Mediak
mwy  Mosiro  Mosiro
mwz  Moingi  Moingi
mxa  Northwest Oaxaca Mixtec  Mixtec, Northwest Oaxaca
mxb  Tezoatlán Mixtec  Mixtec, Tezoatlán
mxc  Manyika  Manyika
mxd  Modang  Modang
mxe  Mele-Fila  Mele-Fila
mxf  Malgbe  Malgbe
mxg  Mbangala  Mbangala
mxh  Mvuba  Mvuba
mxi  Mozarabic  Mozarabic
mxj  Geman Deng  Deng, Geman
mxj  Miju-Mishmi  Miju-Mishmi
mxk  Monumbo  Monumbo
mxl  Maxi Gbe  Gbe, Maxi
mxm  Meramera  Meramera
mxn  Moi (Indonesia)  Moi (Indonesia)
mxo  Mbowe  Mbowe
mxp  Tlahuitoltepec Mixe  Mixe, Tlahuitoltepec
mxq  Juquila Mixe  Mixe, Juquila
mxr  Murik (Malaysia)  Murik (Malaysia)
mxs  Huitepec Mixtec  Mixtec, Huitepec
mxt  Jamiltepec Mixtec  Mixtec, Jamiltepec
mxu  Mada (Cameroon)  Mada (Cameroon)
mxv  Metlatónoc Mixtec  Mixtec, Metlatónoc
mxw  Namo  Namo
mxx  Mahou  Mahou
mxx  Mawukakan  Mawukakan
mxy  Southeastern Nochixtlán Mixtec  Mixtec, Southeastern Nochixtlán
mxz  Central Masela  Masela, Central
mya  Burmese  Burmese
myb  Mbay  Mbay
myc  Mayeka  Mayeka
myd  Maramba  Maramba
mye  Myene  Myene
myf  Bambassi  Bambassi
myg  Manta  Manta
myh  Makah  Makah
myi  Mina (India)  Mina (India)
myj  Mangayat  Mangayat
myk  Mamara Senoufo  Senoufo, Mamara
myl  Moma  Moma
mym  Me'en  Me'en
myo  Anfillo  Anfillo
myp  Pirahã  Pirahã
myr  Muniche  Muniche
mys  Mesmes  Mesmes
myu  Mundurukú  Mundurukú
myv  Erzya  Erzya
myw  Muyuw  Muyuw
myx  Masaaba  Masaaba
myy  Macuna  Macuna
myz  Classical Mandaic  Mandaic, Classical
mza  Santa María Zacatepec Mixtec  Mixtec, Santa María Zacatepec
mzb  Tumzabt  Tumzabt
mzc  Madagascar Sign Language  Madagascar Sign Language
mzd  Malimba  Malimba
mze  Morawa  Morawa
mzg  Monastic Sign Language  Monastic Sign Language
mzh  Wichí Lhamtés Güisnay  Wichí Lhamtés Güisnay
mzi  Ixcatlán Mazatec  Mazatec, Ixcatlán
mzj  Manya  Manya
mzk  Nigeria Mambila  Mambila, Nigeria
mzl  Mazatlán Mixe  Mixe, Mazatlán
mzm  Mumuye  Mumuye
mzn  Mazanderani  Mazanderani
mzo  Matipuhy  Matipuhy
mzp  Movima  Movima
mzq  Mori Atas  Mori Atas
mzr  Marúbo  Marúbo
mzs  Macanese  Macanese
mzt  Mintil  Mintil
mzu  Inapang  Inapang
mzv  Manza  Manza
mzw  Deg  Deg
mzx  Mawayana  Mawayana
mzy  Mozambican Sign Language  Mozambican Sign Language
mzz  Maiadomu  Maiadomu
naa  Namla  Namla
nab  Southern Nambikuára  Nambikuára, Southern
nac  Narak  Narak
nad  Nijadali  Nijadali
nae  Naka'ela  Naka'ela
naf  Nabak  Nabak
nag  Naga Pidgin  Naga Pidgin
naj  Nalu  Nalu
nak  Nakanai  Nakanai
nal  Nalik  Nalik
nam  Ngan'gityemerri  Ngan'gityemerri
nan  Min Nan Chinese  Chinese, Min Nan
nao  Naaba  Naaba
nap  Neapolitan  Neapolitan
naq  Nama (Namibia)  Nama (Namibia)
nar  Iguta  Iguta
nas  Naasioi  Naasioi
nat  Hungworo  Hungworo
nau  Nauru  Nauru
nav  Navaho  Navaho
nav  Navajo  Navajo
naw  Nawuri  Nawuri
nax  Nakwi  Nakwi
nay  Narrinyeri  Narrinyeri
naz  Coatepec Nahuatl  Nahuatl, Coatepec
nba  Nyemba  Nyemba
nbb  Ndoe  Ndoe
nbc  Chang Naga  Naga, Chang
nbd  Ngbinda  Ngbinda
nbe  Konyak Naga  Naga, Konyak
nbg  Nagarchal  Nagarchal
nbh  Ngamo  Ngamo
nbi  Mao Naga  Naga, Mao
nbj  Ngarinman  Ngarinman
nbk  Nake  Nake
nbl  South Ndebele  Ndebele, South
nbm  Ngbaka Ma'bo  Ngbaka Ma'bo
nbn  Kuri  Kuri
nbo  Nkukoli  Nkukoli
nbp  Nnam  Nnam
nbq  Nggem  Nggem
nbr  Numana-Nunku-Gbantu-Numbu  Numana-Nunku-Gbantu-Numbu
nbs  Namibian Sign Language  Namibian Sign Language
nbt  Na  Na
nbu  Rongmei Naga  Naga, Rongmei
nbv  Ngamambo  Ngamambo
nbw  Southern Ngbandi  Ngbandi, Southern
nby  Ningera  Ningera
nca  Iyo  Iyo
ncb  Central Nicobarese  Nicobarese, Central
ncc  Ponam  Ponam
ncd  Nachering  Nachering
nce  Yale  Yale
ncf  Notsi  Notsi
ncg  Nisga'a  Nisga'a
nch  Central Huasteca Nahuatl  Nahuatl, Central Huasteca
nci  Classical Nahuatl  Nahuatl, Classical
ncj  Northern Puebla Nahuatl  Nahuatl, Northern Puebla
nck  Nakara  Nakara
ncl  Michoacán Nahuatl  Nahuatl, Michoacán
ncm  Nambo  Nambo
ncn  Nauna  Nauna
nco  Sibe  Sibe
ncp  Ndaktup  Ndaktup
ncr  Ncane  Ncane
ncs  Nicaraguan Sign Language  Nicaraguan Sign Language
nct  Chothe Naga  Naga, Chothe
ncu  Chumburung  Chumburung
ncx  Central Puebla Nahuatl  Nahuatl, Central Puebla
ncz  Natchez  Natchez
nda  Ndasa  Ndasa
ndb  Kenswei Nsei  Kenswei Nsei
ndc  Ndau  Ndau
ndd  Nde-Nsele-Nta  Nde-Nsele-Nta
nde  North Ndebele  Ndebele, North
ndf  Nadruvian  Nadruvian
ndg  Ndengereko  Ndengereko
ndh  Ndali  Ndali
ndi  Samba Leko  Samba Leko
ndj  Ndamba  Ndamba
ndk  Ndaka  Ndaka
ndl  Ndolo  Ndolo
ndm  Ndam  Ndam
ndn  Ngundi  Ngundi
ndo  Ndonga  Ndonga
ndp  Ndo  Ndo
ndq  Ndombe  Ndombe
ndr  Ndoola  Ndoola
nds  Low German  German, Low
nds  Low Saxon  Saxon, Low
ndt  Ndunga  Ndunga
ndu  Dugun  Dugun
ndv  Ndut  Ndut
ndw  Ndobo  Ndobo
ndx  Nduga  Nduga
ndy  Lutos  Lutos
ndz  Ndogo  Ndogo
nea  Eastern Ngad'a  Ngad'a, Eastern
neb  Toura (Côte d'Ivoire)  Toura (Côte d'Ivoire)
nec  Nedebang  Nedebang
ned  Nde-Gbite  Nde-Gbite
nee  Nêlêmwa-Nixumwak  Nêlêmwa-Nixumwak
nef  Nefamese  Nefamese
neg  Negidal  Negidal
neh  Nyenkha  Nyenkha
nei  Neo-Hittite  Hittite, Neo-
nej  Neko  Neko
nek  Neku  Neku
nem  Nemi  Nemi
nen  Nengone  Nengone
neo  Ná-Meo  Ná-Meo
nep  Nepali (macrolanguage)  Nepali (macrolanguage)
neq  North Central Mixe  Mixe, North Central
ner  Yahadian  Yahadian
nes  Bhoti Kinnauri  Kinnauri, Bhoti
net  Nete  Nete
neu  Neo  Neo
nev  Nyaheun  Nyaheun
new  Nepal Bhasa  Bhasa, Nepal
new  Newari  Newari
nex  Neme  Neme
ney  Neyo  Neyo
nez  Nez Perce  Nez Perce
nfa  Dhao  Dhao
nfd  Ahwai  Ahwai
nfl  Äiwoo  Äiwoo
nfl  Ayiwo  Ayiwo
nfr  Nafaanra  Nafaanra
nfu  Mfumte  Mfumte
nga  Ngbaka  Ngbaka
ngb  Northern Ngbandi  Ngbandi, Northern
ngc  Ngombe (Democratic Republic of Congo)  Ngombe (Democratic Republic of Congo)
ngd  Ngando (Central African Republic)  Ngando (Central African Republic)
nge  Ngemba  Ngemba
ngg  Ngbaka Manza  Ngbaka Manza
ngh  N/u  N/u
ngi  Ngizim  Ngizim
ngj  Ngie  Ngie
ngk  Dalabon  Dalabon
ngl  Lomwe  Lomwe
ngm  Ngatik Men's Creole  Ngatik Men's Creole
ngn  Ngwo  Ngwo
ngo  Ngoni  Ngoni
ngp  Ngulu  Ngulu
ngq  Ngoreme  Ngoreme
ngq  Ngurimi  Ngurimi
ngr  Engdewu  Engdewu
ngs  Gvoko  Gvoko
ngt  Ngeq  Ngeq
ngu  Guerrero Nahuatl  Nahuatl, Guerrero
ngv  Nagumi  Nagumi
ngw  Ngwaba  Ngwaba
ngx  Nggwahyi  Nggwahyi
ngy  Tibea  Tibea
ngz  Ngungwel  Ngungwel
nha  Nhanda  Nhanda
nhb  Beng  Beng
nhc  Tabasco Nahuatl  Nahuatl, Tabasco
nhd  Ava Guaraní  Guaraní, Ava
nhd  Chiripá  Chiripá
nhe  Eastern Huasteca Nahuatl  Nahuatl, Eastern Huasteca
nhf  Nhuwala  Nhuwala
nhg  Tetelcingo Nahuatl  Nahuatl, Tetelcingo
nhh  Nahari  Nahari
nhi  Zacatlán-Ahuacatlán-Tepetzintla Nahuatl  Nahuatl, Zacatlán-Ahuacatlán-Tepetzintla
nhk  Isthmus-Cosoleacaque Nahuatl  Nahuatl, Isthmus-Cosoleacaque
nhm  Morelos Nahuatl  Nahuatl, Morelos
nhn  Central Nahuatl  Nahuatl, Central
nho  Takuu  Takuu
nhp  Isthmus-Pajapan Nahuatl  Nahuatl, Isthmus-Pajapan
nhq  Huaxcaleca Nahuatl  Nahuatl, Huaxcaleca
nhr  Naro  Naro
nht  Ometepec Nahuatl  Nahuatl, Ometepec
nhu  Noone  Noone
nhv  Temascaltepec Nahuatl  Nahuatl, Temascaltepec
nhw  Western Huasteca Nahuatl  Nahuatl, Western Huasteca
nhx  Isthmus-Mecayapan Nahuatl  Nahuatl, Isthmus-Mecayapan
nhy  Northern Oaxaca Nahuatl  Nahuatl, Northern Oaxaca
nhz  Santa María La Alta Nahuatl  Nahuatl, Santa María La Alta
nia  Nias  Nias
nib  Nakame  Nakame
nid  Ngandi  Ngandi
nie  Niellim  Niellim
nif  Nek  Nek
nig  Ngalakan  Ngalakan
nih  Nyiha (Tanzania)  Nyiha (Tanzania)
nii  Nii  Nii
nij  Ngaju  Ngaju
nik  Southern Nicobarese  Nicobarese, Southern
nil  Nila  Nila
nim  Nilamba  Nilamba
nin  Ninzo  Ninzo
nio  Nganasan  Nganasan
niq  Nandi  Nandi
nir  Nimboran  Nimboran
nis  Nimi  Nimi
nit  Southeastern Kolami  Kolami, Southeastern
niu  Niuean  Niuean
niv  Gilyak  Gilyak
niw  Nimo  Nimo
nix  Hema  Hema
niy  Ngiti  Ngiti
niz  Ningil  Ningil
nja  Nzanyi  Nzanyi
njb  Nocte Naga  Naga, Nocte
njd  Ndonde Hamba  Ndonde Hamba
njh  Lotha Naga  Naga, Lotha
nji  Gudanji  Gudanji
njj  Njen  Njen
njl  Njalgulgule  Njalgulgule
njm  Angami Naga  Naga, Angami
njn  Liangmai Naga  Naga, Liangmai
njo  Ao Naga  Naga, Ao
njr  Njerep  Njerep
njs  Nisa  Nisa
njt  Ndyuka-Trio Pidgin  Ndyuka-Trio Pidgin
nju  Ngadjunmaya  Ngadjunmaya
njx  Kunyi  Kunyi
njy  Njyem  Njyem
njz  Nyishi  Nyishi
nka  Nkoya  Nkoya
nkb  Khoibu Naga  Naga, Khoibu
nkc  Nkongho  Nkongho
nkd  Koireng  Koireng
nke  Duke  Duke
nkf  Inpui Naga  Naga, Inpui
nkg  Nekgini  Nekgini
nkh  Khezha Naga  Naga, Khezha
nki  Thangal Naga  Naga, Thangal
nkj  Nakai  Nakai
nkk  Nokuku  Nokuku
nkm  Namat  Namat
nkn  Nkangala  Nkangala
nko  Nkonya  Nkonya
nkp  Niuatoputapu  Niuatoputapu
nkq  Nkami  Nkami
nkr  Nukuoro  Nukuoro
nks  North Asmat  Asmat, North
nkt  Nyika (Tanzania)  Nyika (Tanzania)
nku  Bouna Kulango  Kulango, Bouna
nkv  Nyika (Malawi and Zambia)  Nyika (Malawi and Zambia)
nkw  Nkutu  Nkutu
nkx  Nkoroo  Nkoroo
nkz  Nkari  Nkari
nla  Ngombale  Ngombale
nlc  Nalca  Nalca
nld  Dutch  Dutch
nld  Flemish  Flemish
nle  East Nyala  Nyala, East
nlg  Gela  Gela
nli  Grangali  Grangali
nlj  Nyali  Nyali
nlk  Ninia Yali  Yali, Ninia
nll  Nihali  Nihali
nlo  Ngul  Ngul
nlq  Lao Naga  Naga, Lao
nlu  Nchumbulu  Nchumbulu
nlv  Orizaba Nahuatl  Nahuatl, Orizaba
nlw  Walangama  Walangama
nlx  Nahali  Nahali
nly  Nyamal  Nyamal
nlz  Nalögo  Nalögo
nma  Maram Naga  Naga, Maram
nmb  Big Nambas  Nambas, Big
nmb  V'ënen Taut  V'ënen Taut
nmc  Ngam  Ngam
nmd  Ndumu  Ndumu
nme  Mzieme Naga  Naga, Mzieme
nmf  Tangkhul Naga (India)  Naga, Tangkhul (India)
nmg  Kwasio  Kwasio
nmh  Monsang Naga  Naga, Monsang
nmi  Nyam  Nyam
nmj  Ngombe (Central African Republic)  Ngombe (Central African Republic)
nmk  Namakura  Namakura
nml  Ndemli  Ndemli
nmm  Manangba  Manangba
nmn  !Xóõ  !Xóõ
nmo  Moyon Naga  Naga, Moyon
nmp  Nimanbur  Nimanbur
nmq  Nambya  Nambya
nmr  Nimbari  Nimbari
nms  Letemboi  Letemboi
nmt  Namonuito  Namonuito
nmu  Northeast Maidu  Maidu, Northeast
nmv  Ngamini  Ngamini
nmw  Nimoa  Nimoa
nmx  Nama (Papua New Guinea)  Nama (Papua New Guinea)
nmy  Namuyi  Namuyi
nmz  Nawdm  Nawdm
nna  Nyangumarta  Nyangumarta
nnb  Nande  Nande
nnc  Nancere  Nancere
nnd  West Ambae  Ambae, West
nne  Ngandyera  Ngandyera
nnf  Ngaing  Ngaing
nng  Maring Naga  Naga, Maring
nnh  Ngiemboon  Ngiemboon
nni  North Nuaulu  Nuaulu, North
nnj  Nyangatom  Nyangatom
nnk  Nankina  Nankina
nnl  Northern Rengma Naga  Naga, Northern Rengma
nnm  Namia  Namia
nnn  Ngete  Ngete
nno  Norwegian Nynorsk  Norwegian Nynorsk
nnp  Wancho Naga  Naga, Wancho
nnq  Ngindo  Ngindo
nnr  Narungga  Narungga
nns  Ningye  Ningye
nnt  Nanticoke  Nanticoke
nnu  Dwang  Dwang
nnv  Nugunu (Australia)  Nugunu (Australia)
nnw  Southern Nuni  Nuni, Southern
nnx  Ngong  Ngong
nny  Nyangga  Nyangga
nnz  Nda'nda'  Nda'nda'
noa  Woun Meu  Woun Meu
nob  Norwegian Bokmål  Norwegian Bokmål
noc  Nuk  Nuk
nod  Northern Thai  Thai, Northern
noe  Nimadi  Nimadi
nof  Nomane  Nomane
nog  Nogai  Nogai
noh  Nomu  Nomu
noi  Noiri  Noiri
noj  Nonuya  Nonuya
nok  Nooksack  Nooksack
nol  Nomlaki  Nomlaki
nom  Nocamán  Nocamán
non  Old Norse  Norse, Old
nop  Numanggang  Numanggang
noq  Ngongo  Ngongo
nor  Norwegian  Norwegian
nos  Eastern Nisu  Nisu, Eastern
not  Nomatsiguenga  Nomatsiguenga
nou  Ewage-Notu  Ewage-Notu
nov  Novial  Novial
now  Nyambo  Nyambo
noy  Noy  Noy
noz  Nayi  Nayi
npa  Nar Phu  Nar Phu
npb  Nupbikha  Nupbikha
npg  Ponyo-Gongwang Naga  Naga, Ponyo-Gongwang
nph  Phom Naga  Naga, Phom
npi  Nepali (individual language)  Nepali (individual language)
npl  Southeastern Puebla Nahuatl  Nahuatl, Southeastern Puebla
npn  Mondropolon  Mondropolon
npo  Pochuri Naga  Naga, Pochuri
nps  Nipsan  Nipsan
npu  Puimei Naga  Naga, Puimei
npy  Napu  Napu
nqg  Southern Nago  Nago, Southern
nqk  Kura Ede Nago  Ede Nago, Kura
nqm  Ndom  Ndom
nqn  Nen  Nen
nqo  N'Ko  N'Ko
nqq  Kyan-Karyaw Naga  Naga, Kyan-Karyaw
nqy  Akyaung Ari Naga  Naga, Akyaung Ari
nra  Ngom  Ngom
nrb  Nara  Nara
nrc  Noric  Noric
nre  Southern Rengma Naga  Naga, Southern Rengma
nrg  Narango  Narango
nri  Chokri Naga  Naga, Chokri
nrk  Ngarla  Ngarla
nrl  Ngarluma  Ngarluma
nrm  Narom  Narom
nrn  Norn  Norn
nrp  North Picene  Picene, North
nrr  Nora  Nora
nrr  Norra  Norra
nrt  Northern Kalapuya  Kalapuya, Northern
nru  Narua  Narua
nrx  Ngurmbur  Ngurmbur
nrz  Lala  Lala
nsa  Sangtam Naga  Naga, Sangtam
nsc  Nshi  Nshi
nsd  Southern Nisu  Nisu, Southern
nse  Nsenga  Nsenga
nsf  Northwestern Nisu  Nisu, Northwestern
nsg  Ngasa  Ngasa
nsh  Ngoshie  Ngoshie
nsi  Nigerian Sign Language  Nigerian Sign Language
nsk  Naskapi  Naskapi
nsl  Norwegian Sign Language  Norwegian Sign Language
nsm  Sumi Naga  Naga, Sumi
nsn  Nehan  Nehan
nso  Northern Sotho  Sotho, Northern
nso  Pedi  Pedi
nso  Sepedi  Sepedi
nsp  Nepalese Sign Language  Nepalese Sign Language
nsq  Northern Sierra Miwok  Miwok, Northern Sierra
nsr  Maritime Sign Language  Maritime Sign Language
nss  Nali  Nali
nst  Tase Naga  Naga, Tase
nsu  Sierra Negra Nahuatl  Nahuatl, Sierra Negra
nsv  Southwestern Nisu  Nisu, Southwestern
nsw  Navut  Navut
nsx  Nsongo  Nsongo
nsy  Nasal  Nasal
nsz  Nisenan  Nisenan
nte  Nathembo  Nathembo
ntg  Ngantangarra  Ngantangarra
nti  Natioro  Natioro
ntj  Ngaanyatjarra  Ngaanyatjarra
ntk  Ikoma-Nata-Isenye  Ikoma-Nata-Isenye
ntm  Nateni  Nateni
nto  Ntomba  Ntomba
ntp  Northern Tepehuan  Tepehuan, Northern
ntr  Delo  Delo
nts  Natagaimas  Natagaimas
ntu  Natügu  Natügu
ntw  Nottoway  Nottoway
ntx  Tangkhul Naga (Myanmar)  Naga, Tangkhul (Myanmar)
nty  Mantsi  Mantsi
ntz  Natanzi  Natanzi
nua  Yuanga  Yuanga
nuc  Nukuini  Nukuini
nud  Ngala  Ngala
nue  Ngundu  Ngundu
nuf  Nusu  Nusu
nug  Nungali  Nungali
nuh  Ndunda  Ndunda
nui  Ngumbi  Ngumbi
nuj  Nyole  Nyole
nuk  Nuuchahnulth  Nuuchahnulth
nuk  Nuu-chah-nulth  Nuu-chah-nulth
nul  Nusa Laut  Nusa Laut
num  Niuafo'ou  Niuafo'ou
nun  Anong  Anong
nuo  Nguôn  Nguôn
nup  Nupe-Nupe-Tako  Nupe-Nupe-Tako
nuq  Nukumanu  Nukumanu
nur  Nukuria  Nukuria
nus  Nuer  Nuer
nut  Nung (Viet Nam)  Nung (Viet Nam)
nuu  Ngbundu  Ngbundu
nuv  Northern Nuni  Nuni, Northern
nuw  Nguluwan  Nguluwan
nux  Mehek  Mehek
nuy  Nunggubuyu  Nunggubuyu
nuz  Tlamacazapa Nahuatl  Nahuatl, Tlamacazapa
nvh  Nasarian  Nasarian
nvm  Namiae  Namiae
nvo  Nyokon  Nyokon
nwa  Nawathinehena  Nawathinehena
nwb  Nyabwa  Nyabwa
nwc  Classical Nepal Bhasa  Nepal Bhasa, Classical
nwc  Classical Newari  Newari, Classical
nwc  Old Newari  Newari, Old
nwe  Ngwe  Ngwe
nwg  Ngayawung  Ngayawung
nwi  Southwest Tanna  Tanna, Southwest
nwm  Nyamusa-Molo  Nyamusa-Molo
nwo  Nauo  Nauo
nwr  Nawaru  Nawaru
nwx  Middle Newar  Newar, Middle
nwy  Nottoway-Meherrin  Nottoway-Meherrin
nxa  Nauete  Nauete
nxd  Ngando (Democratic Republic of Congo)  Ngando (Democratic Republic of Congo)
nxe  Nage  Nage
nxg  Ngad'a  Ngad'a
nxi  Nindi  Nindi
nxk  Koki Naga  Naga, Koki
nxl  South Nuaulu  Nuaulu, South
nxm  Numidian  Numidian
nxn  Ngawun  Ngawun
nxq  Naxi  Naxi
nxr  Ninggerum  Ninggerum
nxu  Narau  Narau
nxx  Nafri  Nafri
nya  Chewa  Chewa
nya  Chichewa  Chichewa
nya  Nyanja  Nyanja
nyb  Nyangbo  Nyangbo
nyc  Nyanga-li  Nyanga-li
nyd  Nyore  Nyore
nyd  Olunyole  Olunyole
nye  Nyengo  Nyengo
nyf  Giryama  Giryama
nyf  Kigiryama  Kigiryama
nyg  Nyindu  Nyindu
nyh  Nyigina  Nyigina
nyi  Ama (Sudan)  Ama (Sudan)
nyj  Nyanga  Nyanga
nyk  Nyaneka  Nyaneka
nyl  Nyeu  Nyeu
nym  Nyamwezi  Nyamwezi
nyn  Nyankole  Nyankole
nyo  Nyoro  Nyoro
nyp  Nyang'i  Nyang'i
nyq  Nayini  Nayini
nyr  Nyiha (Malawi)  Nyiha (Malawi)
nys  Nyunga  Nyunga
nyt  Nyawaygi  Nyawaygi
nyu  Nyungwe  Nyungwe
nyv  Nyulnyul  Nyulnyul
nyw  Nyaw  Nyaw
nyx  Nganyaywana  Nganyaywana
nyy  Nyakyusa-Ngonde  Nyakyusa-Ngonde
nza  Tigon Mbembe  Mbembe, Tigon
nzb  Njebi  Njebi
nzi  Nzima  Nzima
nzk  Nzakara  Nzakara
nzm  Zeme Naga  Naga, Zeme
nzs  New Zealand Sign Language  New Zealand Sign Language
nzu  Teke-Nzikou  Teke-Nzikou
nzy  Nzakambay  Nzakambay
nzz  Nanga Dama Dogon  Dogon, Nanga Dama
oaa  Orok  Orok
oac  Oroch  Oroch
oar  Ancient Aramaic (up to 700 BCE)  Aramaic, Ancient (up to 700 BCE)
oar  Old Aramaic (up to 700 BCE)  Aramaic, Old (up to 700 BCE)
oav  Old Avar  Avar, Old
obi  Obispeño  Obispeño
obk  Southern Bontok  Bontok, Southern
obl  Oblo  Oblo
obm  Moabite  Moabite
obo  Obo Manobo  Manobo, Obo
obr  Old Burmese  Burmese, Old
obt  Old Breton  Breton, Old
obu  Obulom  Obulom
oca  Ocaina  Ocaina
och  Old Chinese  Chinese, Old
oci  Occitan (post 1500)  Occitan (post 1500)
oco  Old Cornish  Cornish, Old
ocu  Atzingo Matlatzinca  Matlatzinca, Atzingo
oda  Odut  Odut
odk  Od  Od
odt  Old Dutch  Dutch, Old
odu  Odual  Odual
ofo  Ofo  Ofo
ofs  Old Frisian  Frisian, Old
ofu  Efutop  Efutop
ogb  Ogbia  Ogbia
ogc  Ogbah  Ogbah
oge  Old Georgian  Georgian, Old
ogg  Ogbogolo  Ogbogolo
ogo  Khana  Khana
ogu  Ogbronuagum  Ogbronuagum
oht  Old Hittite  Hittite, Old
ohu  Old Hungarian  Hungarian, Old
oia  Oirata  Oirata
oin  Inebu One  One, Inebu
ojb  Northwestern Ojibwa  Ojibwa, Northwestern
ojc  Central Ojibwa  Ojibwa, Central
ojg  Eastern Ojibwa  Ojibwa, Eastern
oji  Ojibwa  Ojibwa
ojp  Old Japanese  Japanese, Old
ojs  Severn Ojibwa  Ojibwa, Severn
ojv  Ontong Java  Ontong Java
ojw  Western Ojibwa  Ojibwa, Western
oka  Okanagan  Okanagan
okb  Okobo  Okobo
okd  Okodia  Okodia
oke  Okpe (Southwestern Edo)  Okpe (Southwestern Edo)
okg  Koko Babangk  Koko Babangk
okh  Koresh-e Rostam  Koresh-e Rostam
oki  Okiek  Okiek
okj  Oko-Juwoi  Oko-Juwoi
okk  Kwamtim One  One, Kwamtim
okl  Old Kentish Sign Language  Kentish Sign Language, Old
okm  Middle Korean (10th-16th cent.)  Korean, Middle (10th-16th cent.)
okn  Oki-No-Erabu  Oki-No-Erabu
oko  Old Korean (3rd-9th cent.)  Korean, Old (3rd-9th cent.)
okr  Kirike  Kirike
oks  Oko-Eni-Osayen  Oko-Eni-Osayen
oku  Oku  Oku
okv  Orokaiva  Orokaiva
okx  Okpe (Northwestern Edo)  Okpe (Northwestern Edo)
ola  Walungge  Walungge
old  Mochi  Mochi
ole  Olekha  Olekha
olk  Olkol  Olkol
olm  Oloma  Oloma
olo  Livvi  Livvi
olr  Olrat  Olrat
oma  Omaha-Ponca  Omaha-Ponca
omb  East Ambae  Ambae, East
omc  Mochica  Mochica
ome  Omejes  Omejes
omg  Omagua  Omagua
omi  Omi  Omi
omk  Omok  Omok
oml  Ombo  Ombo
omn  Minoan  Minoan
omo  Utarmbung  Utarmbung
omp  Old Manipuri  Manipuri, Old
omr  Old Marathi  Marathi, Old
omt  Omotik  Omotik
omu  Omurano  Omurano
omw  South Tairora  Tairora, South
omx  Old Mon  Mon, Old
ona  Ona  Ona
onb  Lingao  Lingao
one  Oneida  Oneida
ong  Olo  Olo
oni  Onin  Onin
onj  Onjob  Onjob
onk  Kabore One  One, Kabore
onn  Onobasulu  Onobasulu
ono  Onondaga  Onondaga
onp  Sartang  Sartang
onr  Northern One  One, Northern
ons  Ono  Ono
ont  Ontenu  Ontenu
onu  Unua  Unua
onw  Old Nubian  Nubian, Old
onx  Onin Based Pidgin  Onin Based Pidgin
ood  Tohono O'odham  Tohono O'odham
oog  Ong  Ong
oon  Önge  Önge
oor  Oorlams  Oorlams
oos  Old Ossetic  Ossetic, Old
opa  Okpamheri  Okpamheri
opk  Kopkaka  Kopkaka
opm  Oksapmin  Oksapmin
opo  Opao  Opao
opt  Opata  Opata
opy  Ofayé  Ofayé
ora  Oroha  Oroha
orc  Orma  Orma
ore  Orejón  Orejón
org  Oring  Oring
orh  Oroqen  Oroqen
ori  Oriya (macrolanguage)  Oriya (macrolanguage)
orm  Oromo  Oromo
orn  Orang Kanaq  Orang Kanaq
oro  Orokolo  Orokolo
orr  Oruma  Oruma
ors  Orang Seletar  Orang Seletar
ort  Adivasi Oriya  Oriya, Adivasi
oru  Ormuri  Ormuri
orv  Old Russian  Russian, Old
orw  Oro Win  Oro Win
orx  Oro  Oro
ory  Oriya (individual language)  Oriya (individual language)
orz  Ormu  Ormu
osa  Osage  Osage
osc  Oscan  Oscan
osi  Osing  Osing
oso  Ososo  Ososo
osp  Old Spanish  Spanish, Old
oss  Ossetian  Ossetian
oss  Ossetic  Ossetic
ost  Osatu  Osatu
osu  Southern One  One, Southern
osx  Old Saxon  Saxon, Old
ota  Ottoman Turkish (1500-1928)  Turkish, Ottoman (1500-1928)
otb  Old Tibetan  Tibetan, Old
otd  Ot Danum  Ot Danum
ote  Mezquital Otomi  Otomi, Mezquital
oti  Oti  Oti
otk  Old Turkish  Turkish, Old
otl  Tilapa Otomi  Otomi, Tilapa
otm  Eastern Highland Otomi  Otomi, Eastern Highland
otn  Tenango Otomi  Otomi, Tenango
otq  Querétaro Otomi  Otomi, Querétaro
otr  Otoro  Otoro
ots  Estado de México Otomi  Otomi, Estado de México
ott  Temoaya Otomi  Otomi, Temoaya
otu  Otuke  Otuke
otw  Ottawa  Ottawa
otx  Texcatepec Otomi  Otomi, Texcatepec
oty  Old Tamil  Tamil, Old
otz  Ixtenco Otomi  Otomi, Ixtenco
oua  Tagargrent  Tagargrent
oub  Glio-Oubi  Glio-Oubi
oue  Oune  Oune
oui  Old Uighur  Uighur, Old
oum  Ouma  Ouma
oun  !O!ung  !O!ung
owi  Owiniga  Owiniga
owl  Old Welsh  Welsh, Old
oyb  Oy  Oy
oyd  Oyda  Oyda
oym  Wayampi  Wayampi
oyy  Oya'oya  Oya'oya
ozm  Koonzime  Koonzime
pab  Parecís  Parecís
pac  Pacoh  Pacoh
pad  Paumarí  Paumarí
pae  Pagibete  Pagibete
paf  Paranawát  Paranawát
pag  Pangasinan  Pangasinan
pah  Tenharim  Tenharim
pai  Pe  Pe
pak  Parakanã  Parakanã
pal  Pahlavi  Pahlavi
pam  Kapampangan  Kapampangan
pam  Pampanga  Pampanga
pan  Panjabi  Panjabi
pan  Punjabi  Punjabi
pao  Northern Paiute  Paiute, Northern
pap  Papiamento  Papiamento
paq  Parya  Parya
par  Panamint  Panamint
par  Timbisha  Timbisha
pas  Papasena  Papasena
pat  Papitalai  Papitalai
pau  Palauan  Palauan
pav  Pakaásnovos  Pakaásnovos
paw  Pawnee  Pawnee
pax  Pankararé  Pankararé
pay  Pech  Pech
paz  Pankararú  Pankararú
pbb  Páez  Páez
pbc  Patamona  Patamona
pbe  Mezontla Popoloca  Popoloca, Mezontla
pbf  Coyotepec Popoloca  Popoloca, Coyotepec
pbg  Paraujano  Paraujano
pbh  E'ñapa Woromaipu  E'ñapa Woromaipu
pbi  Parkwa  Parkwa
pbl  Mak (Nigeria)  Mak (Nigeria)
pbn  Kpasam  Kpasam
pbo  Papel  Papel
pbp  Badyara  Badyara
pbr  Pangwa  Pangwa
pbs  Central Pame  Pame, Central
pbt  Southern Pashto  Pashto, Southern
pbu  Northern Pashto  Pashto, Northern
pbv  Pnar  Pnar
pby  Pyu  Pyu
pca  Santa Inés Ahuatempan Popoloca  Popoloca, Santa Inés Ahuatempan
pcb  Pear  Pear
pcc  Bouyei  Bouyei
pcd  Picard  Picard
pce  Ruching Palaung  Palaung, Ruching
pcf  Paliyan  Paliyan
pcg  Paniya  Paniya
pch  Pardhan  Pardhan
pci  Duruwa  Duruwa
pcj  Parenga  Parenga
pck  Paite Chin  Chin, Paite
pcl  Pardhi  Pardhi
pcm  Nigerian Pidgin  Pidgin, Nigerian
pcn  Piti  Piti
pcp  Pacahuara  Pacahuara
pcw  Pyapun  Pyapun
pda  Anam  Anam
pdc  Pennsylvania German  German, Pennsylvania
pdi  Pa Di  Pa Di
pdn  Fedan  Fedan
pdn  Podena  Podena
pdo  Padoe  Padoe
pdt  Plautdietsch  Plautdietsch
pdu  Kayan  Kayan
pea  Peranakan Indonesian  Indonesian, Peranakan
peb  Eastern Pomo  Pomo, Eastern
ped  Mala (Papua New Guinea)  Mala (Papua New Guinea)
pee  Taje  Taje
pef  Northeastern Pomo  Pomo, Northeastern
peg  Pengo  Pengo
peh  Bonan  Bonan
pei  Chichimeca-Jonaz  Chichimeca-Jonaz
pej  Northern Pomo  Pomo, Northern
pek  Penchal  Penchal
pel  Pekal  Pekal
pem  Phende  Phende
peo  Old Persian (ca. 600-400 B.C.)  Persian, Old (ca. 600-400 B.C.)
pep  Kunja  Kunja
peq  Southern Pomo  Pomo, Southern
pes  Iranian Persian  Persian, Iranian
pev  Pémono  Pémono
pex  Petats  Petats
pey  Petjo  Petjo
pez  Eastern Penan  Penan, Eastern
pfa  Pááfang  Pááfang
pfe  Peere  Peere
pfl  Pfaelzisch  Pfaelzisch
pga  Sudanese Creole Arabic  Creole Arabic, Sudanese
pgg  Pangwali  Pangwali
pgi  Pagi  Pagi
pgk  Rerep  Rerep
pgl  Primitive Irish  Irish, Primitive
pgn  Paelignian  Paelignian
pgs  Pangseng  Pangseng
pgu  Pagu  Pagu
pha  Pa-Hng  Pa-Hng
phd  Phudagi  Phudagi
phg  Phuong  Phuong
phh  Phukha  Phukha
phk  Phake  Phake
phl  Palula  Palula
phl  Phalura  Phalura
phm  Phimbi  Phimbi
phn  Phoenician  Phoenician
pho  Phunoi  Phunoi
phq  Phana'  Phana'
phr  Pahari-Potwari  Pahari-Potwari
pht  Phu Thai  Phu Thai
phu  Phuan  Phuan
phv  Pahlavani  Pahlavani
phw  Phangduwali  Phangduwali
pia  Pima Bajo  Pima Bajo
pib  Yine  Yine
pic  Pinji  Pinji
pid  Piaroa  Piaroa
pie  Piro  Piro
pif  Pingelapese  Pingelapese
pig  Pisabo  Pisabo
pih  Pitcairn-Norfolk  Pitcairn-Norfolk
pii  Pini  Pini
pij  Pijao  Pijao
pil  Yom  Yom
pim  Powhatan  Powhatan
pin  Piame  Piame
pio  Piapoco  Piapoco
pip  Pero  Pero
pir  Piratapuyo  Piratapuyo
pis  Pijin  Pijin
pit  Pitta Pitta  Pitta Pitta
piu  Pintupi-Luritja  Pintupi-Luritja
piv  Pileni  Pileni
piv  Vaeakau-Taumako  Vaeakau-Taumako
piw  Pimbwe  Pimbwe
pix  Piu  Piu
piy  Piya-Kwonci  Piya-Kwonci
piz  Pije  Pije
pjt  Pitjantjatjara  Pitjantjatjara
pka  Ardhamāgadhī Prākrit  Prākrit, Ardhamāgadhī
pkb  Kipfokomo  Kipfokomo
pkb  Pokomo  Pokomo
pkc  Paekche  Paekche
pkg  Pak-Tong  Pak-Tong
pkh  Pankhu  Pankhu
pkn  Pakanha  Pakanha
pko  Pökoot  Pökoot
pkp  Pukapuka  Pukapuka
pkr  Attapady Kurumba  Kurumba, Attapady
pks  Pakistan Sign Language  Pakistan Sign Language
pkt  Maleng  Maleng
pku  Paku  Paku
pla  Miani  Miani
plb  Polonombauk  Polonombauk
plc  Central Palawano  Palawano, Central
pld  Polari  Polari
ple  Palu'e  Palu'e
plg  Pilagá  Pilagá
plh  Paulohi  Paulohi
pli  Pali  Pali
plj  Polci  Polci
plk  Kohistani Shina  Shina, Kohistani
pll  Shwe Palaung  Palaung, Shwe
pln  Palenquero  Palenquero
plo  Oluta Popoluca  Popoluca, Oluta
plp  Palpa  Palpa
plq  Palaic  Palaic
plr  Palaka Senoufo  Senoufo, Palaka
pls  San Marcos Tlalcoyalco Popoloca  Popoloca, San Marcos Tlalcoyalco
plt  Plateau Malagasy  Malagasy, Plateau
plu  Palikúr  Palikúr
plv  Southwest Palawano  Palawano, Southwest
plw  Brooke's Point Palawano  Palawano, Brooke's Point
ply  Bolyu  Bolyu
plz  Paluan  Paluan
pma  Paama  Paama
pmb  Pambia  Pambia
pmc  Palumata  Palumata
pmd  Pallanganmiddang  Pallanganmiddang
pme  Pwaamei  Pwaamei
pmf  Pamona  Pamona
pmh  Māhārāṣṭri Prākrit  Prākrit, Māhārāṣṭri
pmi  Northern Pumi  Pumi, Northern
pmj  Southern Pumi  Pumi, Southern
pmk  Pamlico  Pamlico
pml  Lingua Franca  Lingua Franca
pmm  Pomo  Pomo
pmn  Pam  Pam
pmo  Pom  Pom
pmq  Northern Pame  Pame, Northern
pmr  Paynamar  Paynamar
pms  Piemontese  Piemontese
pmt  Tuamotuan  Tuamotuan
pmu  Mirpur Panjabi  Panjabi, Mirpur
pmw  Plains Miwok  Miwok, Plains
pmx  Poumei Naga  Naga, Poumei
pmy  Papuan Malay  Malay, Papuan
pmz  Southern Pame  Pame, Southern
pna  Punan Bah-Biau  Punan Bah-Biau
pnb  Western Panjabi  Panjabi, Western
pnc  Pannei  Pannei
pne  Western Penan  Penan, Western
png  Pongu  Pongu
pnh  Penrhyn  Penrhyn
pni  Aoheng  Aoheng
pnj  Pinjarup  Pinjarup
pnk  Paunaka  Paunaka
pnl  Paleni  Paleni
pnm  Punan Batu 1  Punan Batu 1
pnn  Pinai-Hagahai  Pinai-Hagahai
pno  Panobo  Panobo
pnp  Pancana  Pancana
pnq  Pana (Burkina Faso)  Pana (Burkina Faso)
pnr  Panim  Panim
pns  Ponosakan  Ponosakan
pnt  Pontic  Pontic
pnu  Jiongnai Bunu  Bunu, Jiongnai
pnv  Pinigura  Pinigura
pnw  Panytyima  Panytyima
pnx  Phong-Kniang  Phong-Kniang
pny  Pinyin  Pinyin
pnz  Pana (Central African Republic)  Pana (Central African Republic)
poc  Poqomam  Poqomam
pod  Ponares  Ponares
poe  San Juan Atzingo Popoloca  Popoloca, San Juan Atzingo
pof  Poke  Poke
pog  Potiguára  Potiguára
poh  Poqomchi'  Poqomchi'
poi  Highland Popoluca  Popoluca, Highland
pok  Pokangá  Pokangá
pol  Polish  Polish
pom  Southeastern Pomo  Pomo, Southeastern
pon  Pohnpeian  Pohnpeian
poo  Central Pomo  Pomo, Central
pop  Pwapwâ  Pwapwâ
poq  Texistepec Popoluca  Popoluca, Texistepec
por  Portuguese  Portuguese
pos  Sayula Popoluca  Popoluca, Sayula
pot  Potawatomi  Potawatomi
pov  Upper Guinea Crioulo  Crioulo, Upper Guinea
pow  San Felipe Otlaltepec Popoloca  Popoloca, San Felipe Otlaltepec
pox  Polabian  Polabian
poy  Pogolo  Pogolo
ppa  Pao  Pao
ppe  Papi  Papi
ppi  Paipai  Paipai
ppk  Uma  Uma
ppl  Nicarao  Nicarao
ppl  Pipil  Pipil
ppm  Papuma  Papuma
ppn  Papapana  Papapana
ppo  Folopa  Folopa
ppp  Pelende  Pelende
ppq  Pei  Pei
pps  San Luís Temalacayuca Popoloca  Popoloca, San Luís Temalacayuca
ppt  Pare  Pare
ppu  Papora  Papora
pqa  Pa'a  Pa'a
pqm  Malecite-Passamaquoddy  Malecite-Passamaquoddy
prb  Lua'  Lua'
prc  Parachi  Parachi
prd  Parsi-Dari  Parsi-Dari
pre  Principense  Principense
prf  Paranan  Paranan
prg  Prussian  Prussian
prh  Porohanon  Porohanon
pri  Paicî  Paicî
prk  Parauk  Parauk
prl  Peruvian Sign Language  Peruvian Sign Language
prm  Kibiri  Kibiri
prn  Prasuni  Prasuni
pro  Old Occitan (to 1500)  Occitan, Old (to 1500)
pro  Old Provençal (to 1500)  Provençal, Old (to 1500)
prp  Parsi  Parsi
prq  Ashéninka Perené  Ashéninka Perené
prr  Puri  Puri
prs  Afghan Persian  Persian, Afghan
prs  Dari  Dari
prt  Phai  Phai
pru  Puragi  Puragi
prw  Parawen  Parawen
prx  Purik  Purik
pry  Pray 3  Pray 3
prz  Providencia Sign Language  Providencia Sign Language
psa  Asue Awyu  Awyu, Asue
psc  Persian Sign Language  Persian Sign Language
psd  Plains Indian Sign Language  Plains Indian Sign Language
pse  Central Malay  Malay, Central
psg  Penang Sign Language  Penang Sign Language
psh  Southwest Pashayi  Pashayi, Southwest
psi  Southeast Pashayi  Pashayi, Southeast
psl  Puerto Rican Sign Language  Puerto Rican Sign Language
psm  Pauserna  Pauserna
psn  Panasuan  Panasuan
pso  Polish Sign Language  Polish Sign Language
psp  Philippine Sign Language  Philippine Sign Language
psq  Pasi  Pasi
psr  Portuguese Sign Language  Portuguese Sign Language
pss  Kaulong  Kaulong
pst  Central Pashto  Pashto, Central
psu  Sauraseni Prākrit  Prākrit, Sauraseni
psw  Port Sandwich  Port Sandwich
psy  Piscataway  Piscataway
pta  Pai Tavytera  Pai Tavytera
pth  Pataxó Hã-Ha-Hãe  Pataxó Hã-Ha-Hãe
pti  Pintiini  Pintiini
ptn  Patani  Patani
pto  Zo'é  Zo'é
ptp  Patep  Patep
ptr  Piamatsina  Piamatsina
ptt  Enrekang  Enrekang
ptu  Bambam  Bambam
ptv  Port Vato  Port Vato
ptw  Pentlatch  Pentlatch
pty  Pathiya  Pathiya
pua  Western Highland Purepecha  Purepecha, Western Highland
pub  Purum  Purum
puc  Punan Merap  Punan Merap
pud  Punan Aput  Punan Aput
pue  Puelche  Puelche
puf  Punan Merah  Punan Merah
pug  Phuie  Phuie
pui  Puinave  Puinave
puj  Punan Tubu  Punan Tubu
puk  Pu Ko  Pu Ko
pum  Puma  Puma
puo  Puoc  Puoc
pup  Pulabu  Pulabu
puq  Puquina  Puquina
pur  Puruborá  Puruborá
pus  Pashto  Pashto
pus  Pushto  Pushto
put  Putoh  Putoh
puu  Punu  Punu
puw  Puluwatese  Puluwatese
pux  Puare  Puare
puy  Purisimeño  Purisimeño
puz  Purum Naga  Naga, Purum
pwa  Pawaia  Pawaia
pwb  Panawa  Panawa
pwg  Gapapaiwa  Gapapaiwa
pwi  Patwin  Patwin
pwm  Molbog  Molbog
pwn  Paiwan  Paiwan
pwo  Pwo Western Karen  Karen, Pwo Western
pwr  Powari  Powari
pww  Pwo Northern Karen  Karen, Pwo Northern
pxm  Quetzaltepec Mixe  Mixe, Quetzaltepec
pye  Pye Krumen  Krumen, Pye
pym  Fyam  Fyam
pyn  Poyanáwa  Poyanáwa
pys  Lengua de Señas del Paraguay  Lengua de Señas del Paraguay
pys  Paraguayan Sign Language  Paraguayan Sign Language
pyu  Puyuma  Puyuma
pyx  Pyu (Myanmar)  Pyu (Myanmar)
pyy  Pyen  Pyen
pzn  Para Naga  Naga, Para
qua  Quapaw  Quapaw
qub  Huallaga Huánuco Quechua  Quechua, Huallaga Huánuco
quc  K'iche'  K'iche'
quc  Quiché  Quiché
qud  Calderón Highland Quichua  Quichua, Calderón Highland
que  Quechua  Quechua
quf  Lambayeque Quechua  Quechua, Lambayeque
qug  Chimborazo Highland Quichua  Quichua, Chimborazo Highland
quh  South Bolivian Quechua  Quechua, South Bolivian
qui  Quileute  Quileute
quk  Chachapoyas Quechua  Quechua, Chachapoyas
qul  North Bolivian Quechua  Quechua, North Bolivian
qum  Sipacapense  Sipacapense
qun  Quinault  Quinault
qup  Southern Pastaza Quechua  Quechua, Southern Pastaza
quq  Quinqui  Quinqui
qur  Yanahuanca Pasco Quechua  Quechua, Yanahuanca Pasco
qus  Santiago del Estero Quichua  Quichua, Santiago del Estero
quv  Sacapulteco  Sacapulteco
quw  Tena Lowland Quichua  Quichua, Tena Lowland
qux  Yauyos Quechua  Quechua, Yauyos
quy  Ayacucho Quechua  Quechua, Ayacucho
quz  Cusco Quechua  Quechua, Cusco
qva  Ambo-Pasco Quechua  Quechua, Ambo-Pasco
qvc  Cajamarca Quechua  Quechua, Cajamarca
qve  Eastern Apurímac Quechua  Quechua, Eastern Apurímac
qvh  Huamalíes-Dos de Mayo Huánuco Quechua  Quechua, Huamalíes-Dos de Mayo Huánuco
qvi  Imbabura Highland Quichua  Quichua, Imbabura Highland
qvj  Loja Highland Quichua  Quichua, Loja Highland
qvl  Cajatambo North Lima Quechua  Quechua, Cajatambo North Lima
qvm  Margos-Yarowilca-Lauricocha Quechua  Quechua, Margos-Yarowilca-Lauricocha
qvn  North Junín Quechua  Quechua, North Junín
qvo  Napo Lowland Quechua  Quechua, Napo Lowland
qvp  Pacaraos Quechua  Quechua, Pacaraos
qvs  San Martín Quechua  Quechua, San Martín
qvw  Huaylla Wanca Quechua  Quechua, Huaylla Wanca
qvy  Queyu  Queyu
qvz  Northern Pastaza Quichua  Quichua, Northern Pastaza
qwa  Corongo Ancash Quechua  Quechua, Corongo Ancash
qwc  Classical Quechua  Quechua, Classical
qwh  Huaylas Ancash Quechua  Quechua, Huaylas Ancash
qwm  Kuman (Russia)  Kuman (Russia)
qws  Sihuas Ancash Quechua  Quechua, Sihuas Ancash
qwt  Kwalhioqua-Tlatskanai  Kwalhioqua-Tlatskanai
qxa  Chiquián Ancash Quechua  Quechua, Chiquián Ancash
qxc  Chincha Quechua  Quechua, Chincha
qxh  Panao Huánuco Quechua  Quechua, Panao Huánuco
qxl  Salasaca Highland Quichua  Quichua, Salasaca Highland
qxn  Northern Conchucos Ancash Quechua  Quechua, Northern Conchucos Ancash
qxo  Southern Conchucos Ancash Quechua  Quechua, Southern Conchucos Ancash
qxp  Puno Quechua  Quechua, Puno
qxq  Qashqa'i  Qashqa'i
qxr  Cañar Highland Quichua  Quichua, Cañar Highland
qxs  Southern Qiang  Qiang, Southern
qxt  Santa Ana de Tusi Pasco Quechua  Quechua, Santa Ana de Tusi Pasco
qxu  Arequipa-La Unión Quechua  Quechua, Arequipa-La Unión
qxw  Jauja Wanca Quechua  Quechua, Jauja Wanca
qya  Quenya  Quenya
qyp  Quiripi  Quiripi
raa  Dungmali  Dungmali
rab  Camling  Camling
rac  Rasawa  Rasawa
rad  Rade  Rade
raf  Western Meohang  Meohang, Western
rag  Logooli  Logooli
rag  Lulogooli  Lulogooli
rah  Rabha  Rabha
rai  Ramoaaina  Ramoaaina
raj  Rajasthani  Rajasthani
rak  Tulu-Bohuai  Tulu-Bohuai
ral  Ralte  Ralte
ram  Canela  Canela
ran  Riantana  Riantana
rao  Rao  Rao
rap  Rapanui  Rapanui
raq  Saam  Saam
rar  Cook Islands Maori  Maori, Cook Islands
rar  Rarotongan  Rarotongan
ras  Tegali  Tegali
rat  Razajerdi  Razajerdi
rau  Raute  Raute
rav  Sampang  Sampang
raw  Rawang  Rawang
rax  Rang  Rang
ray  Rapa  Rapa
raz  Rahambuu  Rahambuu
rbb  Rumai Palaung  Palaung, Rumai
rbk  Northern Bontok  Bontok, Northern
rbl  Miraya Bikol  Bikol, Miraya
rbp  Barababaraba  Barababaraba
rcf  Réunion Creole French  Creole French, Réunion
rdb  Rudbari  Rudbari
rea  Rerau  Rerau
reb  Rembong  Rembong
ree  Rejang Kayan  Kayan, Rejang
reg  Kara (Tanzania)  Kara (Tanzania)
rei  Reli  Reli
rej  Rejang  Rejang
rel  Rendille  Rendille
rem  Remo  Remo
ren  Rengao  Rengao
rer  Rer Bare  Rer Bare
res  Reshe  Reshe
ret  Retta  Retta
rey  Reyesano  Reyesano
rga  Roria  Roria
rge  Romano-Greek  Romano-Greek
rgk  Rangkas  Rangkas
rgn  Romagnol  Romagnol
rgr  Resígaro  Resígaro
rgs  Southern Roglai  Roglai, Southern
rgu  Ringgou  Ringgou
rhg  Rohingya  Rohingya
rhp  Yahang  Yahang
ria  Riang (India)  Riang (India)
rie  Rien  Rien
rif  Tarifit  Tarifit
ril  Riang (Myanmar)  Riang (Myanmar)
rim  Nyaturu  Nyaturu
rin  Nungu  Nungu
rir  Ribun  Ribun
rit  Ritarungo  Ritarungo
riu  Riung  Riung
rjg  Rajong  Rajong
rji  Raji  Raji
rjs  Rajbanshi  Rajbanshi
rka  Kraol  Kraol
rkb  Rikbaktsa  Rikbaktsa
rkh  Rakahanga-Manihiki  Rakahanga-Manihiki
rki  Rakhine  Rakhine
rkm  Marka  Marka
rkt  Kamta  Kamta
rkt  Rangpuri  Rangpuri
rkw  Arakwal  Arakwal
rma  Rama  Rama
rmb  Rembarunga  Rembarunga
rmc  Carpathian Romani  Romani, Carpathian
rmd  Traveller Danish  Danish, Traveller
rme  Angloromani  Angloromani
rmf  Kalo Finnish Romani  Romani, Kalo Finnish
rmg  Traveller Norwegian  Norwegian, Traveller
rmh  Murkim  Murkim
rmi  Lomavren  Lomavren
rmk  Romkun  Romkun
rml  Baltic Romani  Romani, Baltic
rmm  Roma  Roma
rmn  Balkan Romani  Romani, Balkan
rmo  Sinte Romani  Romani, Sinte
rmp  Rempi  Rempi
rmq  Caló  Caló
rms  Romanian Sign Language  Romanian Sign Language
rmt  Domari  Domari
rmu  Tavringer Romani  Romani, Tavringer
rmv  Romanova  Romanova
rmw  Welsh Romani  Romani, Welsh
rmx  Romam  Romam
rmy  Vlax Romani  Romani, Vlax
rmz  Marma  Marma
rna  Runa  Runa
rnd  Ruund  Ruund
rng  Ronga  Ronga
rnl  Ranglong  Ranglong
rnn  Roon  Roon
rnp  Rongpo  Rongpo
rnr  Nari Nari  Nari Nari
rnw  Rungwa  Rungwa
rob  Tae'  Tae'
roc  Cacgia Roglai  Roglai, Cacgia
rod  Rogo  Rogo
roe  Ronji  Ronji
rof  Rombo  Rombo
rog  Northern Roglai  Roglai, Northern
roh  Romansh  Romansh
rol  Romblomanon  Romblomanon
rom  Romany  Romany
ron  Moldavian  Moldavian
ron  Moldovan  Moldovan
ron  Romanian  Romanian
roo  Rotokas  Rotokas
rop  Kriol  Kriol
ror  Rongga  Rongga
rou  Runga  Runga
row  Dela-Oenale  Dela-Oenale
rpn  Repanbitip  Repanbitip
rpt  Rapting  Rapting
rri  Ririo  Ririo
rro  Waima  Waima
rrt  Arritinngithigh  Arritinngithigh
rsb  Romano-Serbian  Romano-Serbian
rsi  Rennellese Sign Language  Rennellese Sign Language
rsl  Russian Sign Language  Russian Sign Language
rtc  Rungtu Chin  Chin, Rungtu
rth  Ratahan  Ratahan
rtm  Rotuman  Rotuman
rtw  Rathawi  Rathawi
rub  Gungu  Gungu
ruc  Ruuli  Ruuli
rue  Rusyn  Rusyn
ruf  Luguru  Luguru
rug  Roviana  Roviana
ruh  Ruga  Ruga
rui  Rufiji  Rufiji
ruk  Che  Che
run  Rundi  Rundi
ruo  Istro Romanian  Romanian, Istro
rup  Aromanian  Aromanian
rup  Arumanian  Arumanian
rup  Macedo-Romanian  Romanian, Macedo-
ruq  Megleno Romanian  Romanian, Megleno
rus  Russian  Russian
rut  Rutul  Rutul
ruu  Lanas Lobu  Lobu, Lanas
ruy  Mala (Nigeria)  Mala (Nigeria)
ruz  Ruma  Ruma
rwa  Rawo  Rawo
rwk  Rwa  Rwa
rwm  Amba (Uganda)  Amba (Uganda)
rwo  Rawa  Rawa
rwr  Marwari (India)  Marwari (India)
rxd  Ngardi  Ngardi
rxw  Karuwali  Karuwali
ryn  Northern Amami-Oshima  Amami-Oshima, Northern
rys  Yaeyama  Yaeyama
ryu  Central Okinawan  Okinawan, Central
saa  Saba  Saba
sab  Buglere  Buglere
sac  Meskwaki  Meskwaki
sad  Sandawe  Sandawe
sae  Sabanê  Sabanê
saf  Safaliba  Safaliba
sag  Sango  Sango
sah  Yakut  Yakut
saj  Sahu  Sahu
sak  Sake  Sake
sam  Samaritan Aramaic  Aramaic, Samaritan
san  Sanskrit  Sanskrit
sao  Sause  Sause
sap  Sanapaná  Sanapaná
saq  Samburu  Samburu
sar  Saraveca  Saraveca
sas  Sasak  Sasak
sat  Santali  Santali
sau  Saleman  Saleman
sav  Saafi-Saafi  Saafi-Saafi
saw  Sawi  Sawi
sax  Sa  Sa
say  Saya  Saya
saz  Saurashtra  Saurashtra
sba  Ngambay  Ngambay
sbb  Simbo  Simbo
sbc  Kele (Papua New Guinea)  Kele (Papua New Guinea)
sbd  Southern Samo  Samo, Southern
sbe  Saliba  Saliba
sbf  Shabo  Shabo
sbg  Seget  Seget
sbh  Sori-Harengan  Sori-Harengan
sbi  Seti  Seti
sbj  Surbakhal  Surbakhal
sbk  Safwa  Safwa
sbl  Botolan Sambal  Sambal, Botolan
sbm  Sagala  Sagala
sbn  Sindhi Bhil  Bhil, Sindhi
sbo  Sabüm  Sabüm
sbp  Sangu (Tanzania)  Sangu (Tanzania)
sbq  Sileibi  Sileibi
sbr  Sembakung Murut  Sembakung Murut
sbs  Subiya  Subiya
sbt  Kimki  Kimki
sbu  Stod Bhoti  Bhoti, Stod
sbv  Sabine  Sabine
sbw  Simba  Simba
sbx  Seberuang  Seberuang
sby  Soli  Soli
sbz  Sara Kaba  Sara Kaba
scb  Chut  Chut
sce  Dongxiang  Dongxiang
scf  San Miguel Creole French  Creole French, San Miguel
scg  Sanggau  Sanggau
sch  Sakachep  Sakachep
sci  Sri Lankan Creole Malay  Creole Malay, Sri Lankan
sck  Sadri  Sadri
scl  Shina  Shina
scn  Sicilian  Sicilian
sco  Scots  Scots
scp  Helambu Sherpa  Helambu Sherpa
scq  Sa'och  Sa'och
scs  North Slavey  Slavey, North
scu  Shumcho  Shumcho
scv  Sheni  Sheni
scw  Sha  Sha
scx  Sicel  Sicel
sda  Toraja-Sa'dan  Toraja-Sa'dan
sdb  Shabak  Shabak
sdc  Sassarese Sardinian  Sardinian, Sassarese
sde  Surubu  Surubu
sdf  Sarli  Sarli
sdg  Savi  Savi
sdh  Southern Kurdish  Kurdish, Southern
sdj  Suundi  Suundi
sdk  Sos Kundi  Sos Kundi
sdl  Saudi Arabian Sign Language  Saudi Arabian Sign Language
sdm  Semandang  Semandang
sdn  Gallurese Sardinian  Sardinian, Gallurese
sdo  Bukar-Sadung Bidayuh  Bidayuh, Bukar-Sadung
sdp  Sherdukpen  Sherdukpen
sdr  Oraon Sadri  Sadri, Oraon
sds  Sened  Sened
sdt  Shuadit  Shuadit
sdu  Sarudu  Sarudu
sdx  Sibu Melanau  Melanau, Sibu
sdz  Sallands  Sallands
sea  Semai  Semai
seb  Shempire Senoufo  Senoufo, Shempire
sec  Sechelt  Sechelt
sed  Sedang  Sedang
see  Seneca  Seneca
sef  Cebaara Senoufo  Senoufo, Cebaara
seg  Segeju  Segeju
seh  Sena  Sena
sei  Seri  Seri
sej  Sene  Sene
sek  Sekani  Sekani
sel  Selkup  Selkup
sen  Nanerigé Sénoufo  Sénoufo, Nanerigé
seo  Suarmin  Suarmin
sep  Sìcìté Sénoufo  Sénoufo, Sìcìté
seq  Senara Sénoufo  Sénoufo, Senara
ser  Serrano  Serrano
ses  Koyraboro Senni Songhai  Songhai, Koyraboro Senni
set  Sentani  Sentani
seu  Serui-Laut  Serui-Laut
sev  Nyarafolo Senoufo  Senoufo, Nyarafolo
sew  Sewa Bay  Sewa Bay
sey  Secoya  Secoya
sez  Senthang Chin  Chin, Senthang
sfb  French Belgian Sign Language  French Belgian Sign Language
sfb  Langue des signes de Belgique Francophone  Langue des signes de Belgique Francophone
sfe  Eastern Subanen  Subanen, Eastern
sfm  Small Flowery Miao  Miao, Small Flowery
sfs  South African Sign Language  South African Sign Language
sfw  Sehwi  Sehwi
sga  Old Irish (to 900)  Irish, Old (to 900)
sgb  Mag-antsi Ayta  Ayta, Mag-antsi
sgc  Kipsigis  Kipsigis
sgd  Surigaonon  Surigaonon
sge  Segai  Segai
sgg  Swiss-German Sign Language  Swiss-German Sign Language
sgh  Shughni  Shughni
sgi  Suga  Suga
sgj  Surgujia  Surgujia
sgk  Sangkong  Sangkong
sgm  Singa  Singa
sgo  Songa  Songa
sgp  Singpho  Singpho
sgr  Sangisari  Sangisari
sgs  Samogitian  Samogitian
sgt  Brokpake  Brokpake
sgu  Salas  Salas
sgw  Sebat Bet Gurage  Sebat Bet Gurage
sgx  Sierra Leone Sign Language  Sierra Leone Sign Language
sgy  Sanglechi  Sanglechi
sgz  Sursurunga  Sursurunga
sha  Shall-Zwall  Shall-Zwall
shb  Ninam  Ninam
shc  Sonde  Sonde
shd  Kundal Shahi  Kundal Shahi
she  Sheko  Sheko
shg  Shua  Shua
shh  Shoshoni  Shoshoni
shi  Tachelhit  Tachelhit
shj  Shatt  Shatt
shk  Shilluk  Shilluk
shl  Shendu  Shendu
shm  Shahrudi  Shahrudi
shn  Shan  Shan
sho  Shanga  Shanga
shp  Shipibo-Conibo  Shipibo-Conibo
shq  Sala  Sala
shr  Shi  Shi
shs  Shuswap  Shuswap
sht  Shasta  Shasta
shu  Chadian Arabic  Arabic, Chadian
shv  Shehri  Shehri
shw  Shwai  Shwai
shx  She  She
shy  Tachawit  Tachawit
shz  Syenara Senoufo  Senoufo, Syenara
sia  Akkala Sami  Sami, Akkala
sib  Sebop  Sebop
sid  Sidamo  Sidamo
sie  Simaa  Simaa
sif  Siamou  Siamou
sig  Paasaal  Paasaal
sih  Sîshëë  Sîshëë
sih  Zire  Zire
sii  Shom Peng  Shom Peng
sij  Numbami  Numbami
sik  Sikiana  Sikiana
sil  Tumulung Sisaala  Sisaala, Tumulung
sim  Mende (Papua New Guinea)  Mende (Papua New Guinea)
sin  Sinhala  Sinhala
sin  Sinhalese  Sinhalese
sip  Sikkimese  Sikkimese
siq  Sonia  Sonia
sir  Siri  Siri
sis  Siuslaw  Siuslaw
siu  Sinagen  Sinagen
siv  Sumariup  Sumariup
siw  Siwai  Siwai
six  Sumau  Sumau
siy  Sivandi  Sivandi
siz  Siwi  Siwi
sja  Epena  Epena
sjb  Sajau Basap  Sajau Basap
sjd  Kildin Sami  Sami, Kildin
sje  Pite Sami  Sami, Pite
sjg  Assangori  Assangori
sjk  Kemi Sami  Sami, Kemi
sjl  Miji  Miji
sjl  Sajalong  Sajalong
sjm  Mapun  Mapun
sjn  Sindarin  Sindarin
sjo  Xibe  Xibe
sjp  Surjapuri  Surjapuri
sjr  Siar-Lak  Siar-Lak
sjs  Senhaja De Srair  Senhaja De Srair
sjt  Ter Sami  Sami, Ter
sju  Ume Sami  Sami, Ume
sjw  Shawnee  Shawnee
ska  Skagit  Skagit
skb  Saek  Saek
skc  Ma Manda  Ma Manda
skd  Southern Sierra Miwok  Miwok, Southern Sierra
ske  Seke (Vanuatu)  Seke (Vanuatu)
skf  Sakirabiá  Sakirabiá
skg  Sakalava Malagasy  Malagasy, Sakalava
skh  Sikule  Sikule
ski  Sika  Sika
skj  Seke (Nepal)  Seke (Nepal)
skk  Sok  Sok
skm  Kutong  Kutong
skn  Kolibugan Subanon  Subanon, Kolibugan
sko  Seko Tengah  Seko Tengah
skp  Sekapan  Sekapan
skq  Sininkere  Sininkere
skr  Seraiki  Seraiki
sks  Maia  Maia
skt  Sakata  Sakata
sku  Sakao  Sakao
skv  Skou  Skou
skw  Skepi Creole Dutch  Creole Dutch, Skepi
skx  Seko Padang  Seko Padang
sky  Sikaiana  Sikaiana
skz  Sekar  Sekar
slc  Sáliba  Sáliba
sld  Sissala  Sissala
sle  Sholaga  Sholaga
slf  Swiss-Italian Sign Language  Swiss-Italian Sign Language
slg  Selungai Murut  Selungai Murut
slh  Southern Puget Sound Salish  Salish, Southern Puget Sound
sli  Lower Silesian  Silesian, Lower
slj  Salumá  Salumá
slk  Slovak  Slovak
sll  Salt-Yui  Salt-Yui
slm  Pangutaran Sama  Sama, Pangutaran
sln  Salinan  Salinan
slp  Lamaholot  Lamaholot
slq  Salchuq  Salchuq
slr  Salar  Salar
sls  Singapore Sign Language  Singapore Sign Language
slt  Sila  Sila
slu  Selaru  Selaru
slv  Slovenian  Slovenian
slw  Sialum  Sialum
slx  Salampasu  Salampasu
sly  Selayar  Selayar
slz  Ma'ya  Ma'ya
sma  Southern Sami  Sami, Southern
smb  Simbari  Simbari
smc  Som  Som
smd  Sama  Sama
sme  Northern Sami  Sami, Northern
smf  Auwe  Auwe
smg  Simbali  Simbali
smh  Samei  Samei
smj  Lule Sami  Lule Sami
smk  Bolinao  Bolinao
sml  Central Sama  Sama, Central
smm  Musasa  Musasa
smn  Inari Sami  Sami, Inari
smo  Samoan  Samoan
smp  Samaritan  Samaritan
smq  Samo  Samo
smr  Simeulue  Simeulue
sms  Skolt Sami  Sami, Skolt
smt  Simte  Simte
smu  Somray  Somray
smv  Samvedi  Samvedi
smw  Sumbawa  Sumbawa
smx  Samba  Samba
smy  Semnani  Semnani
smz  Simeku  Simeku
sna  Shona  Shona
snb  Sebuyau  Sebuyau
snc  Sinaugoro  Sinaugoro
snd  Sindhi  Sindhi
sne  Bau Bidayuh  Bidayuh, Bau
snf  Noon  Noon
sng  Sanga (Democratic Republic of Congo)  Sanga (Democratic Republic of Congo)
snh  Shinabo  Shinabo
sni  Sensi  Sensi
snj  Riverain Sango  Sango, Riverain
snk  Soninke  Soninke
snl  Sangil  Sangil
snm  Southern Ma'di  Ma'di, Southern
snn  Siona  Siona
sno  Snohomish  Snohomish
snp  Siane  Siane
snq  Sangu (Gabon)  Sangu (Gabon)
snr  Sihan  Sihan
sns  Nahavaq  Nahavaq
sns  South West Bay  South West Bay
snu  Senggi  Senggi
snu  Viid  Viid
snv  Sa'ban  Sa'ban
snw  Selee  Selee
snx  Sam  Sam
sny  Saniyo-Hiyewe  Saniyo-Hiyewe
snz  Sinsauru  Sinsauru
soa  Thai Song  Thai Song
sob  Sobei  Sobei
soc  So (Democratic Republic of Congo)  So (Democratic Republic of Congo)
sod  Songoora  Songoora
soe  Songomeno  Songomeno
sog  Sogdian  Sogdian
soh  Aka  Aka
soi  Sonha  Sonha
soj  Soi  Soi
sok  Sokoro  Sokoro
sol  Solos  Solos
som  Somali  Somali
soo  Songo  Songo
sop  Songe  Songe
soq  Kanasi  Kanasi
sor  Somrai  Somrai
sos  Seeku  Seeku
sot  Southern Sotho  Sotho, Southern
sou  Southern Thai  Thai, Southern
sov  Sonsorol  Sonsorol
sow  Sowanda  Sowanda
sox  Swo  Swo
soy  Miyobe  Miyobe
soz  Temi  Temi
spa  Castilian  Castilian
spa  Spanish  Spanish
spb  Sepa (Indonesia)  Sepa (Indonesia)
spc  Sapé  Sapé
spd  Saep  Saep
spe  Sepa (Papua New Guinea)  Sepa (Papua New Guinea)
spg  Sian  Sian
spi  Saponi  Saponi
spk  Sengo  Sengo
spl  Selepet  Selepet
spm  Akukem  Akukem
spo  Spokane  Spokane
spp  Supyire Senoufo  Senoufo, Supyire
spq  Loreto-Ucayali Spanish  Spanish, Loreto-Ucayali
spr  Saparua  Saparua
sps  Saposa  Saposa
spt  Spiti Bhoti  Bhoti, Spiti
spu  Sapuan  Sapuan
spv  Kosli  Kosli
spv  Sambalpuri  Sambalpuri
spx  South Picene  Picene, South
spy  Sabaot  Sabaot
sqa  Shama-Sambuga  Shama-Sambuga
sqh  Shau  Shau
sqi  Albanian  Albanian
sqk  Albanian Sign Language  Albanian Sign Language
sqm  Suma  Suma
sqn  Susquehannock  Susquehannock
sqo  Sorkhei  Sorkhei
sqq  Sou  Sou
sqr  Siculo Arabic  Arabic, Siculo
sqs  Sri Lankan Sign Language  Sri Lankan Sign Language
sqt  Soqotri  Soqotri
squ  Squamish  Squamish
sra  Saruga  Saruga
srb  Sora  Sora
src  Logudorese Sardinian  Sardinian, Logudorese
srd  Sardinian  Sardinian
sre  Sara  Sara
srf  Nafi  Nafi
srg  Sulod  Sulod
srh  Sarikoli  Sarikoli
sri  Siriano  Siriano
srk  Serudung Murut  Serudung Murut
srl  Isirawa  Isirawa
srm  Saramaccan  Saramaccan
srn  Sranan Tongo  Sranan Tongo
sro  Campidanese Sardinian  Sardinian, Campidanese
srp  Serbian  Serbian
srq  Sirionó  Sirionó
srr  Serer  Serer
srs  Sarsi  Sarsi
srt  Sauri  Sauri
sru  Suruí  Suruí
srv  Southern Sorsoganon  Sorsoganon, Southern
srw  Serua  Serua
srx  Sirmauri  Sirmauri
sry  Sera  Sera
srz  Shahmirzadi  Shahmirzadi
ssb  Southern Sama  Sama, Southern
ssc  Suba-Simbiti  Suba-Simbiti
ssd  Siroi  Siroi
sse  Balangingi  Balangingi
sse  Bangingih Sama  Sama, Bangingih
ssf  Thao  Thao
ssg  Seimat  Seimat
ssh  Shihhi Arabic  Arabic, Shihhi
ssi  Sansi  Sansi
ssj  Sausi  Sausi
ssk  Sunam  Sunam
ssl  Western Sisaala  Sisaala, Western
ssm  Semnam  Semnam
ssn  Waata  Waata
sso  Sissano  Sissano
ssp  Spanish Sign Language  Spanish Sign Language
ssq  So'a  So'a
ssr  Swiss-French Sign Language  Swiss-French Sign Language
sss  Sô  Sô
sst  Sinasina  Sinasina
ssu  Susuami  Susuami
ssv  Shark Bay  Shark Bay
ssw  Swati  Swati
ssx  Samberigi  Samberigi
ssy  Saho  Saho
ssz  Sengseng  Sengseng
sta  Settla  Settla
stb  Northern Subanen  Subanen, Northern
std  Sentinel  Sentinel
ste  Liana-Seti  Liana-Seti
stf  Seta  Seta
stg  Trieng  Trieng
sth  Shelta  Shelta
sti  Bulo Stieng  Stieng, Bulo
stj  Matya Samo  Samo, Matya
stk  Arammba  Arammba
stl  Stellingwerfs  Stellingwerfs
stm  Setaman  Setaman
stn  Owa  Owa
sto  Stoney  Stoney
stp  Southeastern Tepehuan  Tepehuan, Southeastern
stq  Saterfriesisch  Saterfriesisch
str  Straits Salish  Salish, Straits
sts  Shumashti  Shumashti
stt  Budeh Stieng  Stieng, Budeh
stu  Samtao  Samtao
stv  Silt'e  Silt'e
stw  Satawalese  Satawalese
sty  Siberian Tatar  Tatar, Siberian
sua  Sulka  Sulka
sub  Suku  Suku
suc  Western Subanon  Subanon, Western
sue  Suena  Suena
sug  Suganga  Suganga
sui  Suki  Suki
suj  Shubi  Shubi
suk  Sukuma  Sukuma
sun  Sundanese  Sundanese
suq  Suri  Suri
sur  Mwaghavul  Mwaghavul
sus  Susu  Susu
sut  Subtiaba  Subtiaba
suv  Puroik  Puroik
suw  Sumbwa  Sumbwa
sux  Sumerian  Sumerian
suy  Suyá  Suyá
suz  Sunwar  Sunwar
sva  Svan  Svan
svb  Ulau-Suain  Ulau-Suain
svc  Vincentian Creole English  Creole English, Vincentian
sve  Serili  Serili
svk  Slovakian Sign Language  Slovakian Sign Language
svm  Slavomolisano  Slavomolisano
svr  Savara  Savara
svs  Savosavo  Savosavo
svx  Skalvian  Skalvian
swa  Swahili (macrolanguage)  Swahili (macrolanguage)
swb  Maore Comorian  Comorian, Maore
swc  Congo Swahili  Swahili, Congo
swe  Swedish  Swedish
swf  Sere  Sere
swg  Swabian  Swabian
swh  Kiswahili  Kiswahili
swh  Swahili (individual language)  Swahili (individual language)
swi  Sui  Sui
swj  Sira  Sira
swk  Malawi Sena  Sena, Malawi
swl  Swedish Sign Language  Swedish Sign Language
swm  Samosa  Samosa
swn  Sawknah  Sawknah
swo  Shanenawa  Shanenawa
swp  Suau  Suau
swq  Sharwa  Sharwa
swr  Saweru  Saweru
sws  Seluwasan  Seluwasan
swt  Sawila  Sawila
swu  Suwawa  Suwawa
swv  Shekhawati  Shekhawati
sww  Sowa  Sowa
swx  Suruahá  Suruahá
swy  Sarua  Sarua
sxb  Suba  Suba
sxc  Sicanian  Sicanian
sxe  Sighu  Sighu
sxg  Shixing  Shixing
sxk  Southern Kalapuya  Kalapuya, Southern
sxl  Selian  Selian
sxm  Samre  Samre
sxn  Sangir  Sangir
sxo  Sorothaptic  Sorothaptic
sxr  Saaroa  Saaroa
sxs  Sasaru  Sasaru
sxu  Upper Saxon  Saxon, Upper
sxw  Saxwe Gbe  Gbe, Saxwe
sya  Siang  Siang
syb  Central Subanen  Subanen, Central
syc  Classical Syriac  Syriac, Classical
syi  Seki  Seki
syk  Sukur  Sukur
syl  Sylheti  Sylheti
sym  Maya Samo  Samo, Maya
syn  Senaya  Senaya
syo  Suoy  Suoy
syr  Syriac  Syriac
sys  Sinyar  Sinyar
syw  Kagate  Kagate
syy  Al-Sayyid Bedouin Sign Language  Al-Sayyid Bedouin Sign Language
sza  Semelai  Semelai
szb  Ngalum  Ngalum
szc  Semaq Beri  Semaq Beri
szd  Seru  Seru
sze  Seze  Seze
szg  Sengele  Sengele
szl  Silesian  Silesian
szn  Sula  Sula
szp  Suabo  Suabo
szv  Isu (Fako Division)  Isu (Fako Division)
szw  Sawai  Sawai
taa  Lower Tanana  Tanana, Lower
tab  Tabassaran  Tabassaran
tac  Lowland Tarahumara  Tarahumara, Lowland
tad  Tause  Tause
tae  Tariana  Tariana
taf  Tapirapé  Tapirapé
tag  Tagoi  Tagoi
tah  Tahitian  Tahitian
taj  Eastern Tamang  Tamang, Eastern
tak  Tala  Tala
tal  Tal  Tal
tam  Tamil  Tamil
tan  Tangale  Tangale
tao  Yami  Yami
tap  Taabwa  Taabwa
taq  Tamasheq  Tamasheq
tar  Central Tarahumara  Tarahumara, Central
tas  Tay Boi  Tay Boi
tat  Tatar  Tatar
tau  Upper Tanana  Tanana, Upper
tav  Tatuyo  Tatuyo
taw  Tai  Tai
tax  Tamki  Tamki
tay  Atayal  Atayal
taz  Tocho  Tocho
tba  Aikanã  Aikanã
tbb  Tapeba  Tapeba
tbc  Takia  Takia
tbd  Kaki Ae  Kaki Ae
tbe  Tanimbili  Tanimbili
tbf  Mandara  Mandara
tbg  North Tairora  Tairora, North
tbh  Thurawal  Thurawal
tbi  Gaam  Gaam
tbj  Tiang  Tiang
tbk  Calamian Tagbanwa  Tagbanwa, Calamian
tbl  Tboli  Tboli
tbm  Tagbu  Tagbu
tbn  Barro Negro Tunebo  Tunebo, Barro Negro
tbo  Tawala  Tawala
tbp  Diebroud  Diebroud
tbp  Taworta  Taworta
tbr  Tumtum  Tumtum
tbs  Tanguat  Tanguat
tbt  Tembo (Kitembo)  Tembo (Kitembo)
tbu  Tubar  Tubar
tbv  Tobo  Tobo
tbw  Tagbanwa  Tagbanwa
tbx  Kapin  Kapin
tby  Tabaru  Tabaru
tbz  Ditammari  Ditammari
tca  Ticuna  Ticuna
tcb  Tanacross  Tanacross
tcc  Datooga  Datooga
tcd  Tafi  Tafi
tce  Southern Tutchone  Tutchone, Southern
tcf  Malinaltepec Me'phaa  Me'phaa, Malinaltepec
tcf  Malinaltepec Tlapanec  Tlapanec, Malinaltepec
tcg  Tamagario  Tamagario
tch  Turks And Caicos Creole English  Creole English, Turks And Caicos
tci  Wára  Wára
tck  Tchitchege  Tchitchege
tcl  Taman (Myanmar)  Taman (Myanmar)
tcm  Tanahmerah  Tanahmerah
tcn  Tichurong  Tichurong
tco  Taungyo  Taungyo
tcp  Tawr Chin  Chin, Tawr
tcq  Kaiy  Kaiy
tcs  Torres Strait Creole  Creole, Torres Strait
tct  T'en  T'en
tcu  Southeastern Tarahumara  Tarahumara, Southeastern
tcw  Tecpatlán Totonac  Totonac, Tecpatlán
tcx  Toda  Toda
tcy  Tulu  Tulu
tcz  Thado Chin  Chin, Thado
tda  Tagdal  Tagdal
tdb  Panchpargania  Panchpargania
tdc  Emberá-Tadó  Emberá-Tadó
tdd  Tai Nüa  Tai Nüa
tde  Tiranige Diga Dogon  Dogon, Tiranige Diga
tdf  Talieng  Talieng
tdg  Western Tamang  Tamang, Western
tdh  Thulung  Thulung
tdi  Tomadino  Tomadino
tdj  Tajio  Tajio
tdk  Tambas  Tambas
tdl  Sur  Sur
tdn  Tondano  Tondano
tdo  Teme  Teme
tdq  Tita  Tita
tdr  Todrah  Todrah
tds  Doutai  Doutai
tdt  Tetun Dili  Tetun Dili
tdu  Tempasuk Dusun  Dusun, Tempasuk
tdv  Toro  Toro
tdx  Tandroy-Mahafaly Malagasy  Malagasy, Tandroy-Mahafaly
tdy  Tadyawan  Tadyawan
tea  Temiar  Temiar
teb  Tetete  Tetete
tec  Terik  Terik
ted  Tepo Krumen  Krumen, Tepo
tee  Huehuetla Tepehua  Tepehua, Huehuetla
tef  Teressa  Teressa
teg  Teke-Tege  Teke-Tege
teh  Tehuelche  Tehuelche
tei  Torricelli  Torricelli
tek  Ibali Teke  Teke, Ibali
tel  Telugu  Telugu
tem  Timne  Timne
ten  Tama (Colombia)  Tama (Colombia)
teo  Teso  Teso
tep  Tepecano  Tepecano
teq  Temein  Temein
ter  Tereno  Tereno
tes  Tengger  Tengger
tet  Tetum  Tetum
teu  Soo  Soo
tev  Teor  Teor
tew  Tewa (USA)  Tewa (USA)
tex  Tennet  Tennet
tey  Tulishi  Tulishi
tfi  Tofin Gbe  Gbe, Tofin
tfn  Tanaina  Tanaina
tfo  Tefaro  Tefaro
tfr  Teribe  Teribe
tft  Ternate  Ternate
tga  Sagalla  Sagalla
tgb  Tobilung  Tobilung
tgc  Tigak  Tigak
tgd  Ciwogai  Ciwogai
tge  Eastern Gorkha Tamang  Tamang, Eastern Gorkha
tgf  Chalikha  Chalikha
tgh  Tobagonian Creole English  Creole English, Tobagonian
tgi  Lawunuia  Lawunuia
tgj  Tagin  Tagin
tgk  Tajik  Tajik
tgl  Tagalog  Tagalog
tgn  Tandaganon  Tandaganon
tgo  Sudest  Sudest
tgp  Tangoa  Tangoa
tgq  Tring  Tring
tgr  Tareng  Tareng
tgs  Nume  Nume
tgt  Central Tagbanwa  Tagbanwa, Central
tgu  Tanggu  Tanggu
tgv  Tingui-Boto  Tingui-Boto
tgw  Tagwana Senoufo  Senoufo, Tagwana
tgx  Tagish  Tagish
tgy  Togoyo  Togoyo
tgz  Tagalaka  Tagalaka
tha  Thai  Thai
thc  Tai Hang Tong  Tai Hang Tong
thd  Thayore  Thayore
the  Chitwania Tharu  Tharu, Chitwania
thf  Thangmi  Thangmi
thh  Northern Tarahumara  Tarahumara, Northern
thi  Tai Long  Tai Long
thk  Kitharaka  Kitharaka
thk  Tharaka  Tharaka
thl  Dangaura Tharu  Tharu, Dangaura
thm  Aheu  Aheu
thn  Thachanadan  Thachanadan
thp  Thompson  Thompson
thq  Kochila Tharu  Tharu, Kochila
thr  Rana Tharu  Tharu, Rana
ths  Thakali  Thakali
tht  Tahltan  Tahltan
thu  Thuri  Thuri
thv  Tahaggart Tamahaq  Tamahaq, Tahaggart
thw  Thudam  Thudam
thx  The  The
thy  Tha  Tha
thz  Tayart Tamajeq  Tamajeq, Tayart
tia  Tidikelt Tamazight  Tamazight, Tidikelt
tic  Tira  Tira
tid  Tidong  Tidong
tif  Tifal  Tifal
tig  Tigre  Tigre
tih  Timugon Murut  Murut, Timugon
tii  Tiene  Tiene
tij  Tilung  Tilung
tik  Tikar  Tikar
til  Tillamook  Tillamook
tim  Timbe  Timbe
tin  Tindi  Tindi
tio  Teop  Teop
tip  Trimuris  Trimuris
tiq  Tiéfo  Tiéfo
tir  Tigrinya  Tigrinya
tis  Masadiit Itneg  Itneg, Masadiit
tit  Tinigua  Tinigua
tiu  Adasen  Adasen
tiv  Tiv  Tiv
tiw  Tiwi  Tiwi
tix  Southern Tiwa  Tiwa, Southern
tiy  Tiruray  Tiruray
tiz  Tai Hongjin  Tai Hongjin
tja  Tajuasohn  Tajuasohn
tjg  Tunjung  Tunjung
tji  Northern Tujia  Tujia, Northern
tjl  Tai Laing  Tai Laing
tjm  Timucua  Timucua
tjn  Tonjon  Tonjon
tjo  Temacine Tamazight  Tamazight, Temacine
tjs  Southern Tujia  Tujia, Southern
tju  Tjurruru  Tjurruru
tjw  Djabwurrung  Djabwurrung
tka  Truká  Truká
tkb  Buksa  Buksa
tkd  Tukudede  Tukudede
tke  Takwane  Takwane
tkf  Tukumanféd  Tukumanféd
tkg  Tesaka Malagasy  Malagasy, Tesaka
tkl  Tokelau  Tokelau
tkm  Takelma  Takelma
tkn  Toku-No-Shima  Toku-No-Shima
tkp  Tikopia  Tikopia
tkq  Tee  Tee
tkr  Tsakhur  Tsakhur
tks  Takestani  Takestani
tkt  Kathoriya Tharu  Tharu, Kathoriya
tku  Upper Necaxa Totonac  Totonac, Upper Necaxa
tkw  Teanu  Teanu
tkx  Tangko  Tangko
tkz  Takua  Takua
tla  Southwestern Tepehuan  Tepehuan, Southwestern
tlb  Tobelo  Tobelo
tlc  Yecuatla Totonac  Totonac, Yecuatla
tld  Talaud  Talaud
tlf  Telefol  Telefol
tlg  Tofanma  Tofanma
tlh  Klingon  Klingon
tlh  tlhIngan-Hol  tlhIngan-Hol
tli  Tlingit  Tlingit
tlj  Talinga-Bwisi  Talinga-Bwisi
tlk  Taloki  Taloki
tll  Tetela  Tetela
tlm  Tolomako  Tolomako
tln  Talondo'  Talondo'
tlo  Talodi  Talodi
tlp  Filomena Mata-Coahuitlán Totonac  Totonac, Filomena Mata-Coahuitlán
tlq  Tai Loi  Tai Loi
tlr  Talise  Talise
tls  Tambotalo  Tambotalo
tlt  Teluti  Teluti
tlu  Tulehu  Tulehu
tlv  Taliabu  Taliabu
tlx  Khehek  Khehek
tly  Talysh  Talysh
tma  Tama (Chad)  Tama (Chad)
tmb  Avava  Avava
tmb  Katbol  Katbol
tmc  Tumak  Tumak
tmd  Haruai  Haruai
tme  Tremembé  Tremembé
tmf  Toba-Maskoy  Toba-Maskoy
tmg  Ternateño  Ternateño
tmh  Tamashek  Tamashek
tmi  Tutuba  Tutuba
tmj  Samarokena  Samarokena
tmk  Northwestern Tamang  Tamang, Northwestern
tml  Tamnim Citak  Citak, Tamnim
tmm  Tai Thanh  Tai Thanh
tmn  Taman (Indonesia)  Taman (Indonesia)
tmo  Temoq  Temoq
tmp  Tai Mène  Tai Mène
tmq  Tumleo  Tumleo
tmr  Jewish Babylonian Aramaic (ca. 200-1200 CE)  Aramaic, Jewish Babylonian (ca. 200-1200 CE)
tms  Tima  Tima
tmt  Tasmate  Tasmate
tmu  Iau  Iau
tmv  Tembo (Motembo)  Tembo (Motembo)
tmw  Temuan  Temuan
tmy  Tami  Tami
tmz  Tamanaku  Tamanaku
tna  Tacana  Tacana
tnb  Western Tunebo  Tunebo, Western
tnc  Tanimuca-Retuarã  Tanimuca-Retuarã
tnd  Angosturas Tunebo  Tunebo, Angosturas
tne  Tinoc Kallahan  Kallahan, Tinoc
tng  Tobanga  Tobanga
tnh  Maiani  Maiani
tni  Tandia  Tandia
tnk  Kwamera  Kwamera
tnl  Lenakel  Lenakel
tnm  Tabla  Tabla
tnn  North Tanna  Tanna, North
tno  Toromono  Toromono
tnp  Whitesands  Whitesands
tnq  Taino  Taino
tnr  Ménik  Ménik
tns  Tenis  Tenis
tnt  Tontemboan  Tontemboan
tnu  Tay Khang  Tay Khang
tnv  Tangchangya  Tangchangya
tnw  Tonsawang  Tonsawang
tnx  Tanema  Tanema
tny  Tongwe  Tongwe
tnz  Tonga (Thailand)  Tonga (Thailand)
tob  Toba  Toba
toc  Coyutla Totonac  Totonac, Coyutla
tod  Toma  Toma
toe  Tomedes  Tomedes
tof  Gizrra  Gizrra
tog  Tonga (Nyasa)  Tonga (Nyasa)
toh  Gitonga  Gitonga
toi  Tonga (Zambia)  Tonga (Zambia)
toj  Tojolabal  Tojolabal
tol  Tolowa  Tolowa
tom  Tombulu  Tombulu
ton  Tonga (Tonga Islands)  Tonga (Tonga Islands)
too  Xicotepec De Juárez Totonac  Totonac, Xicotepec De Juárez
top  Papantla Totonac  Totonac, Papantla
toq  Toposa  Toposa
tor  Togbo-Vara Banda  Banda, Togbo-Vara
tos  Highland Totonac  Totonac, Highland
tou  Tho  Tho
tov  Upper Taromi  Taromi, Upper
tow  Jemez  Jemez
tox  Tobian  Tobian
toy  Topoiyo  Topoiyo
toz  To  To
tpa  Taupota  Taupota
tpc  Azoyú Me'phaa  Me'phaa, Azoyú
tpc  Azoyú Tlapanec  Tlapanec, Azoyú
tpe  Tippera  Tippera
tpf  Tarpia  Tarpia
tpg  Kula  Kula
tpi  Tok Pisin  Tok Pisin
tpj  Tapieté  Tapieté
tpk  Tupinikin  Tupinikin
tpl  Tlacoapa Me'phaa  Me'phaa, Tlacoapa
tpl  Tlacoapa Tlapanec  Tlapanec, Tlacoapa
tpm  Tampulma  Tampulma
tpn  Tupinambá  Tupinambá
tpo  Tai Pao  Tai Pao
tpp  Pisaflores Tepehua  Tepehua, Pisaflores
tpq  Tukpa  Tukpa
tpr  Tuparí  Tuparí
tpt  Tlachichilco Tepehua  Tepehua, Tlachichilco
tpu  Tampuan  Tampuan
tpv  Tanapag  Tanapag
tpw  Tupí  Tupí
tpx  Acatepec Me'phaa  Me'phaa, Acatepec
tpx  Acatepec Tlapanec  Tlapanec, Acatepec
tpy  Trumai  Trumai
tpz  Tinputz  Tinputz
tqb  Tembé  Tembé
tql  Lehali  Lehali
tqm  Turumsa  Turumsa
tqn  Tenino  Tenino
tqo  Toaripi  Toaripi
tqp  Tomoip  Tomoip
tqq  Tunni  Tunni
tqr  Torona  Torona
tqt  Western Totonac  Totonac, Western
tqu  Touo  Touo
tqw  Tonkawa  Tonkawa
tra  Tirahi  Tirahi
trb  Terebu  Terebu
trc  Copala Triqui  Triqui, Copala
trd  Turi  Turi
tre  East Tarangan  Tarangan, East
trf  Trinidadian Creole English  Creole English, Trinidadian
trg  Lishán Didán  Lishán Didán
trh  Turaka  Turaka
tri  Trió  Trió
trj  Toram  Toram
trl  Traveller Scottish  Scottish, Traveller
trm  Tregami  Tregami
trn  Trinitario  Trinitario
tro  Tarao Naga  Naga, Tarao
trp  Kok Borok  Kok Borok
trq  San Martín Itunyoso Triqui  Triqui, San Martín Itunyoso
trr  Taushiro  Taushiro
trs  Chicahuaxtla Triqui  Triqui, Chicahuaxtla
trt  Tunggare  Tunggare
tru  Surayt  Surayt
tru  Turoyo  Turoyo
trv  Taroko  Taroko
trw  Torwali  Torwali
trx  Tringgus-Sembaan Bidayuh  Bidayuh, Tringgus-Sembaan
try  Turung  Turung
trz  Torá  Torá
tsa  Tsaangi  Tsaangi
tsb  Tsamai  Tsamai
tsc  Tswa  Tswa
tsd  Tsakonian  Tsakonian
tse  Tunisian Sign Language  Tunisian Sign Language
tsf  Southwestern Tamang  Tamang, Southwestern
tsg  Tausug  Tausug
tsh  Tsuvan  Tsuvan
tsi  Tsimshian  Tsimshian
tsj  Tshangla  Tshangla
tsk  Tseku  Tseku
tsl  Ts'ün-Lao  Ts'ün-Lao
tsm  Türk İşaret Dili  Türk İşaret Dili
tsm  Turkish Sign Language  Turkish Sign Language
tsn  Tswana  Tswana
tso  Tsonga  Tsonga
tsp  Northern Toussian  Toussian, Northern
tsq  Thai Sign Language  Thai Sign Language
tsr  Akei  Akei
tss  Taiwan Sign Language  Taiwan Sign Language
tst  Tondi Songway Kiini  Songway Kiini, Tondi
tsu  Tsou  Tsou
tsv  Tsogo  Tsogo
tsw  Tsishingini  Tsishingini
tsx  Mubami  Mubami
tsy  Tebul Sign Language  Tebul Sign Language
tsz  Purepecha  Purepecha
tta  Tutelo  Tutelo
ttb  Gaa  Gaa
ttc  Tektiteko  Tektiteko
ttd  Tauade  Tauade
tte  Bwanabwana  Bwanabwana
ttf  Tuotomb  Tuotomb
ttg  Tutong  Tutong
tth  Upper Ta'oih  Ta'oih, Upper
tti  Tobati  Tobati
ttj  Tooro  Tooro
ttk  Totoro  Totoro
ttl  Totela  Totela
ttm  Northern Tutchone  Tutchone, Northern
ttn  Towei  Towei
tto  Lower Ta'oih  Ta'oih, Lower
ttp  Tombelala  Tombelala
ttq  Tawallammat Tamajaq  Tamajaq, Tawallammat
ttr  Tera  Tera
tts  Northeastern Thai  Thai, Northeastern
ttt  Muslim Tat  Tat, Muslim
ttu  Torau  Torau
ttv  Titan  Titan
ttw  Long Wat  Long Wat
tty  Sikaritai  Sikaritai
ttz  Tsum  Tsum
tua  Wiarumus  Wiarumus
tub  Tübatulabal  Tübatulabal
tuc  Mutu  Mutu
tud  Tuxá  Tuxá
tue  Tuyuca  Tuyuca
tuf  Central Tunebo  Tunebo, Central
tug  Tunia  Tunia
tuh  Taulil  Taulil
tui  Tupuri  Tupuri
tuj  Tugutil  Tugutil
tuk  Turkmen  Turkmen
tul  Tula  Tula
tum  Tumbuka  Tumbuka
tun  Tunica  Tunica
tuo  Tucano  Tucano
tuq  Tedaga  Tedaga
tur  Turkish  Turkish
tus  Tuscarora  Tuscarora
tuu  Tututni  Tututni
tuv  Turkana  Turkana
tux  Tuxináwa  Tuxináwa
tuy  Tugen  Tugen
tuz  Turka  Turka
tva  Vaghua  Vaghua
tvd  Tsuvadi  Tsuvadi
tve  Te'un  Te'un
tvk  Southeast Ambrym  Ambrym, Southeast
tvl  Tuvalu  Tuvalu
tvm  Tela-Masbuar  Tela-Masbuar
tvn  Tavoyan  Tavoyan
tvo  Tidore  Tidore
tvs  Taveta  Taveta
tvt  Tutsa Naga  Naga, Tutsa
tvu  Tunen  Tunen
tvw  Sedoa  Sedoa
tvy  Timor Pidgin  Pidgin, Timor
twa  Twana  Twana
twb  Western Tawbuid  Tawbuid, Western
twc  Teshenawa  Teshenawa
twd  Twents  Twents
twe  Tewa (Indonesia)  Tewa (Indonesia)
twf  Northern Tiwa  Tiwa, Northern
twg  Tereweng  Tereweng
twh  Tai Dón  Tai Dón
twi  Twi  Twi
twl  Tawara  Tawara
twm  Tawang Monpa  Monpa, Tawang
twn  Twendi  Twendi
two  Tswapong  Tswapong
twp  Ere  Ere
twq  Tasawaq  Tasawaq
twr  Southwestern Tarahumara  Tarahumara, Southwestern
twt  Turiwára  Turiwára
twu  Termanu  Termanu
tww  Tuwari  Tuwari
twx  Tewe  Tewe
twy  Tawoyan  Tawoyan
txa  Tombonuo  Tombonuo
txb  Tokharian B  Tokharian B
txc  Tsetsaut  Tsetsaut
txe  Totoli  Totoli
txg  Tangut  Tangut
txh  Thracian  Thracian
txi  Ikpeng  Ikpeng
txm  Tomini  Tomini
txn  West Tarangan  Tarangan, West
txo  Toto  Toto
txq  Tii  Tii
txr  Tartessian  Tartessian
txs  Tonsea  Tonsea
txt  Citak  Citak
txu  Kayapó  Kayapó
txx  Tatana  Tatana
txy  Tanosy Malagasy  Malagasy, Tanosy
tya  Tauya  Tauya
tye  Kyanga  Kyanga
tyh  O'du  O'du
tyi  Teke-Tsaayi  Teke-Tsaayi
tyj  Tai Do  Tai Do
tyl  Thu Lao  Thu Lao
tyn  Kombai  Kombai
typ  Thaypan  Thaypan
tyr  Tai Daeng  Tai Daeng
tys  Tày Sa Pa  Tày Sa Pa
tyt  Tày Tac  Tày Tac
tyu  Kua  Kua
tyv  Tuvinian  Tuvinian
tyx  Teke-Tyee  Teke-Tyee
tyz  Tày  Tày
tza  Tanzanian Sign Language  Tanzanian Sign Language
tzh  Tzeltal  Tzeltal
tzj  Tz'utujil  Tz'utujil
tzl  Talossan  Talossan
tzm  Central Atlas Tamazight  Tamazight, Central Atlas
tzn  Tugun  Tugun
tzo  Tzotzil  Tzotzil
tzx  Tabriak  Tabriak
uam  Uamué  Uamué
uan  Kuan  Kuan
uar  Tairuma  Tairuma
uba  Ubang  Ubang
ubi  Ubi  Ubi
ubl  Buhi'non Bikol  Bikol, Buhi'non
ubr  Ubir  Ubir
ubu  Umbu-Ungu  Umbu-Ungu
uby  Ubykh  Ubykh
uda  Uda  Uda
ude  Udihe  Udihe
udg  Muduga  Muduga
udi  Udi  Udi
udj  Ujir  Ujir
udl  Wuzlam  Wuzlam
udm  Udmurt  Udmurt
udu  Uduk  Uduk
ues  Kioko  Kioko
ufi  Ufim  Ufim
uga  Ugaritic  Ugaritic
ugb  Kuku-Ugbanh  Kuku-Ugbanh
uge  Ughele  Ughele
ugn  Ugandan Sign Language  Ugandan Sign Language
ugo  Ugong  Ugong
ugy  Uruguayan Sign Language  Uruguayan Sign Language
uha  Uhami  Uhami
uhn  Damal  Damal
uig  Uighur  Uighur
uig  Uyghur  Uyghur
uis  Uisai  Uisai
uiv  Iyive  Iyive
uji  Tanjijili  Tanjijili
uka  Kaburi  Kaburi
ukg  Ukuriguma  Ukuriguma
ukh  Ukhwejo  Ukhwejo
ukl  Ukrainian Sign Language  Ukrainian Sign Language
ukp  Ukpe-Bayobiri  Ukpe-Bayobiri
ukq  Ukwa  Ukwa
ukr  Ukrainian  Ukrainian
uks  Kaapor Sign Language  Kaapor Sign Language
uks  Urubú-Kaapor Sign Language  Urubú-Kaapor Sign Language
uku  Ukue  Ukue
ukw  Ukwuani-Aboh-Ndoni  Ukwuani-Aboh-Ndoni
uky  Kuuk-Yak  Kuuk-Yak
ula  Fungwa  Fungwa
ulb  Ulukwumi  Ulukwumi
ulc  Ulch  Ulch
ule  Lule  Lule
ulf  Afra  Afra
ulf  Usku  Usku
uli  Ulithian  Ulithian
ulk  Meriam  Meriam
ull  Ullatan  Ullatan
ulm  Ulumanda'  Ulumanda'
uln  Unserdeutsch  Unserdeutsch
ulu  Uma' Lung  Uma' Lung
ulw  Ulwa  Ulwa
uma  Umatilla  Umatilla
umb  Umbundu  Umbundu
umc  Marrucinian  Marrucinian
umd  Umbindhamu  Umbindhamu
umg  Umbuygamu  Umbuygamu
umi  Ukit  Ukit
umm  Umon  Umon
umn  Makyan Naga  Naga, Makyan
umo  Umotína  Umotína
ump  Umpila  Umpila
umr  Umbugarla  Umbugarla
ums  Pendau  Pendau
umu  Munsee  Munsee
una  North Watut  Watut, North
und  Undetermined  Undetermined
une  Uneme  Uneme
ung  Ngarinyin  Ngarinyin
unk  Enawené-Nawé  Enawené-Nawé
unm  Unami  Unami
unn  Kurnai  Kurnai
unr  Mundari  Mundari
unu  Unubahe  Unubahe
unx  Munda  Munda
unz  Unde Kaili  Kaili, Unde
uok  Uokha  Uokha
upi  Umeda  Umeda
upv  Uripiv-Wala-Rano-Atchin  Uripiv-Wala-Rano-Atchin
ura  Urarina  Urarina
urb  Kaapor  Kaapor
urb  Urubú-Kaapor  Urubú-Kaapor
urc  Urningangg  Urningangg
urd  Urdu  Urdu
ure  Uru  Uru
urf  Uradhi  Uradhi
urg  Urigina  Urigina
urh  Urhobo  Urhobo
uri  Urim  Urim
urk  Urak Lawoi'  Urak Lawoi'
url  Urali  Urali
urm  Urapmin  Urapmin
urn  Uruangnirin  Uruangnirin
uro  Ura (Papua New Guinea)  Ura (Papua New Guinea)
urp  Uru-Pa-In  Uru-Pa-In
urr  Lehalurup  Lehalurup
urr  Löyöp  Löyöp
urt  Urat  Urat
uru  Urumi  Urumi
urv  Uruava  Uruava
urw  Sop  Sop
urx  Urimo  Urimo
ury  Orya  Orya
urz  Uru-Eu-Wau-Wau  Uru-Eu-Wau-Wau
usa  Usarufa  Usarufa
ush  Ushojo  Ushojo
usi  Usui  Usui
usk  Usaghade  Usaghade
usp  Uspanteco  Uspanteco
usu  Uya  Uya
uta  Otank  Otank
ute  Ute-Southern Paiute  Ute-Southern Paiute
utp  Amba (Solomon Islands)  Amba (Solomon Islands)
utr  Etulo  Etulo
utu  Utu  Utu
uum  Urum  Urum
uun  Kulon-Pazeh  Kulon-Pazeh
uur  Ura (Vanuatu)  Ura (Vanuatu)
uuu  U  U
uve  Fagauvea  Fagauvea
uve  West Uvean  Uvean, West
uvh  Uri  Uri
uvl  Lote  Lote
uwa  Kuku-Uwanh  Kuku-Uwanh
uya  Doko-Uyanga  Doko-Uyanga
uzb  Uzbek  Uzbek
uzn  Northern Uzbek  Uzbek, Northern
uzs  Southern Uzbek  Uzbek, Southern
vaa  Vaagri Booli  Vaagri Booli
vae  Vale  Vale
vaf  Vafsi  Vafsi
vag  Vagla  Vagla
vah  Varhadi-Nagpuri  Varhadi-Nagpuri
vai  Vai  Vai
vaj  Vasekela Bushman  Vasekela Bushman
val  Vehes  Vehes
vam  Vanimo  Vanimo
van  Valman  Valman
vao  Vao  Vao
vap  Vaiphei  Vaiphei
var  Huarijio  Huarijio
vas  Vasavi  Vasavi
vau  Vanuma  Vanuma
vav  Varli  Varli
vay  Wayu  Wayu
vbb  Southeast Babar  Babar, Southeast
vbk  Southwestern Bontok  Bontok, Southwestern
vec  Venetian  Venetian
ved  Veddah  Veddah
vel  Veluws  Veluws
vem  Vemgo-Mabas  Vemgo-Mabas
ven  Venda  Venda
veo  Ventureño  Ventureño
vep  Veps  Veps
ver  Mom Jango  Mom Jango
vgr  Vaghri  Vaghri
vgt  Flemish Sign Language  Flemish Sign Language
vgt  Vlaamse Gebarentaal  Vlaamse Gebarentaal
vic  Virgin Islands Creole English  Creole English, Virgin Islands
vid  Vidunda  Vidunda
vie  Vietnamese  Vietnamese
vif  Vili  Vili
vig  Viemo  Viemo
vil  Vilela  Vilela
vin  Vinza  Vinza
vis  Vishavan  Vishavan
vit  Viti  Viti
viv  Iduna  Iduna
vka  Kariyarra  Kariyarra
vki  Ija-Zuba  Ija-Zuba
vkj  Kujarge  Kujarge
vkk  Kaur  Kaur
vkl  Kulisusu  Kulisusu
vkm  Kamakan  Kamakan
vko  Kodeoha  Kodeoha
vkp  Korlai Creole Portuguese  Creole Portuguese, Korlai
vkt  Tenggarong Kutai Malay  Malay, Tenggarong Kutai
vku  Kurrama  Kurrama
vlp  Valpei  Valpei
vls  Vlaams  Vlaams
vma  Martuyhunira  Martuyhunira
vmb  Barbaram  Barbaram
vmc  Juxtlahuaca Mixtec  Mixtec, Juxtlahuaca
vmd  Mudu Koraga  Koraga, Mudu
vme  East Masela  Masela, East
vmf  Mainfränkisch  Mainfränkisch
vmg  Lungalunga  Lungalunga
vmh  Maraghei  Maraghei
vmi  Miwa  Miwa
vmj  Ixtayutla Mixtec  Mixtec, Ixtayutla
vmk  Makhuwa-Shirima  Makhuwa-Shirima
vml  Malgana  Malgana
vmm  Mitlatongo Mixtec  Mixtec, Mitlatongo
vmp  Soyaltepec Mazatec  Mazatec, Soyaltepec
vmq  Soyaltepec Mixtec  Mixtec, Soyaltepec
vmr  Marenje  Marenje
vms  Moksela  Moksela
vmu  Muluridyi  Muluridyi
vmv  Valley Maidu  Maidu, Valley
vmw  Makhuwa  Makhuwa
vmx  Tamazola Mixtec  Mixtec, Tamazola
vmy  Ayautla Mazatec  Mazatec, Ayautla
vmz  Mazatlán Mazatec  Mazatec, Mazatlán
vnk  Lovono  Lovono
vnk  Vano  Vano
vnm  Neve'ei  Neve'ei
vnm  Vinmavis  Vinmavis
vnp  Vunapu  Vunapu
vol  Volapük  Volapük
vor  Voro  Voro
vot  Votic  Votic
vra  Vera'a  Vera'a
vro  Võro  Võro
vrs  Varisi  Varisi
vrt  Banam Bay  Banam Bay
vrt  Burmbar  Burmbar
vsi  Moldova Sign Language  Moldova Sign Language
vsl  Venezuelan Sign Language  Venezuelan Sign Language
vsv  Llengua de signes valenciana  Llengua de signes valenciana
vsv  Valencian Sign Language  Valencian Sign Language
vto  Vitou  Vitou
vum  Vumbu  Vumbu
vun  Vunjo  Vunjo
vut  Vute  Vute
vwa  Awa (China)  Awa (China)
waa  Walla Walla  Walla Walla
wab  Wab  Wab
wac  Wasco-Wishram  Wasco-Wishram
wad  Wandamen  Wandamen
wae  Walser  Walser
waf  Wakoná  Wakoná
wag  Wa'ema  Wa'ema
wah  Watubela  Watubela
wai  Wares  Wares
waj  Waffa  Waffa
wal  Wolaitta  Wolaitta
wal  Wolaytta  Wolaytta
wam  Wampanoag  Wampanoag
wan  Wan  Wan
wao  Wappo  Wappo
wap  Wapishana  Wapishana
waq  Wageman  Wageman
war  Waray (Philippines)  Waray (Philippines)
was  Washo  Washo
wat  Kaninuwa  Kaninuwa
wau  Waurá  Waurá
wav  Waka  Waka
waw  Waiwai  Waiwai
wax  Marangis  Marangis
wax  Watam  Watam
way  Wayana  Wayana
waz  Wampur  Wampur
wba  Warao  Warao
wbb  Wabo  Wabo
wbe  Waritai  Waritai
wbf  Wara  Wara
wbh  Wanda  Wanda
wbi  Vwanji  Vwanji
wbj  Alagwa  Alagwa
wbk  Waigali  Waigali
wbl  Wakhi  Wakhi
wbm  Wa  Wa
wbp  Warlpiri  Warlpiri
wbq  Waddar  Waddar
wbr  Wagdi  Wagdi
wbt  Wanman  Wanman
wbv  Wajarri  Wajarri
wbw  Woi  Woi
wca  Yanomámi  Yanomámi
wci  Waci Gbe  Gbe, Waci
wdd  Wandji  Wandji
wdg  Wadaginam  Wadaginam
wdj  Wadjiginy  Wadjiginy
wdk  Wadikali  Wadikali
wdu  Wadjigu  Wadjigu
wdy  Wadjabangayi  Wadjabangayi
wea  Wewaw  Wewaw
wec  Wè Western  Wè Western
wed  Wedau  Wedau
weg  Wergaia  Wergaia
weh  Weh  Weh
wei  Kiunum  Kiunum
wem  Weme Gbe  Gbe, Weme
weo  Wemale  Wemale
wep  Westphalien  Westphalien
wer  Weri  Weri
wes  Cameroon Pidgin  Pidgin, Cameroon
wet  Perai  Perai
weu  Rawngtu Chin  Chin, Rawngtu
wew  Wejewa  Wejewa
wfg  Yafi  Yafi
wfg  Zorop  Zorop
wga  Wagaya  Wagaya
wgb  Wagawaga  Wagawaga
wgg  Wangganguru  Wangganguru
wgi  Wahgi  Wahgi
wgo  Waigeo  Waigeo
wgu  Wirangu  Wirangu
wgy  Warrgamay  Warrgamay
wha  Manusela  Manusela
whg  North Wahgi  Wahgi, North
whk  Wahau Kenyah  Kenyah, Wahau
whu  Wahau Kayan  Kayan, Wahau
wib  Southern Toussian  Toussian, Southern
wic  Wichita  Wichita
wie  Wik-Epa  Wik-Epa
wif  Wik-Keyangan  Wik-Keyangan
wig  Wik-Ngathana  Wik-Ngathana
wih  Wik-Me'anha  Wik-Me'anha
wii  Minidien  Minidien
wij  Wik-Iiyanh  Wik-Iiyanh
wik  Wikalkan  Wikalkan
wil  Wilawila  Wilawila
wim  Wik-Mungkan  Wik-Mungkan
win  Ho-Chunk  Ho-Chunk
wir  Wiraféd  Wiraféd
wiu  Wiru  Wiru
wiv  Vitu  Vitu
wiy  Wiyot  Wiyot
wja  Waja  Waja
wji  Warji  Warji
wka  Kw'adza  Kw'adza
wkb  Kumbaran  Kumbaran
wkd  Mo  Mo
wkd  Wakde  Wakde
wkl  Kalanadi  Kalanadi
wku  Kunduvadi  Kunduvadi
wkw  Wakawaka  Wakawaka
wky  Wangkayutyuru  Wangkayutyuru
wla  Walio  Walio
wlc  Mwali Comorian  Comorian, Mwali
wle  Wolane  Wolane
wlg  Kunbarlang  Kunbarlang
wli  Waioli  Waioli
wlk  Wailaki  Wailaki
wll  Wali (Sudan)  Wali (Sudan)
wlm  Middle Welsh  Welsh, Middle
wln  Walloon  Walloon
wlo  Wolio  Wolio
wlr  Wailapa  Wailapa
wls  Wallisian  Wallisian
wlu  Wuliwuli  Wuliwuli
wlv  Wichí Lhamtés Vejoz  Wichí Lhamtés Vejoz
wlw  Walak  Walak
wlx  Wali (Ghana)  Wali (Ghana)
wly  Waling  Waling
wma  Mawa (Nigeria)  Mawa (Nigeria)
wmb  Wambaya  Wambaya
wmc  Wamas  Wamas
wmd  Mamaindé  Mamaindé
wme  Wambule  Wambule
wmh  Waima'a  Waima'a
wmi  Wamin  Wamin
wmm  Maiwa (Indonesia)  Maiwa (Indonesia)
wmn  Waamwang  Waamwang
wmo  Wom (Papua New Guinea)  Wom (Papua New Guinea)
wms  Wambon  Wambon
wmt  Walmajarri  Walmajarri
wmw  Mwani  Mwani
wmx  Womo  Womo
wnb  Wanambre  Wanambre
wnc  Wantoat  Wantoat
wnd  Wandarang  Wandarang
wne  Waneci  Waneci
wng  Wanggom  Wanggom
wni  Ndzwani Comorian  Comorian, Ndzwani
wnk  Wanukaka  Wanukaka
wnm  Wanggamala  Wanggamala
wnn  Wunumara  Wunumara
wno  Wano  Wano
wnp  Wanap  Wanap
wnu  Usan  Usan
wnw  Wintu  Wintu
wny  Wanyi  Wanyi
woa  Tyaraity  Tyaraity
wob  Wè Northern  Wè Northern
woc  Wogeo  Wogeo
wod  Wolani  Wolani
woe  Woleaian  Woleaian
wof  Gambian Wolof  Wolof, Gambian
wog  Wogamusin  Wogamusin
woi  Kamang  Kamang
wok  Longto  Longto
wol  Wolof  Wolof
wom  Wom (Nigeria)  Wom (Nigeria)
won  Wongo  Wongo
woo  Manombai  Manombai
wor  Woria  Woria
wos  Hanga Hundi  Hanga Hundi
wow  Wawonii  Wawonii
woy  Weyto  Weyto
wpc  Maco  Maco
wra  Warapu  Warapu
wrb  Warluwara  Warluwara
wrd  Warduji  Warduji
wrg  Warungu  Warungu
wrh  Wiradhuri  Wiradhuri
wri  Wariyangga  Wariyangga
wrk  Garrwa  Garrwa
wrl  Warlmanpa  Warlmanpa
wrm  Warumungu  Warumungu
wrn  Warnang  Warnang
wro  Worrorra  Worrorra
wrp  Waropen  Waropen
wrr  Wardaman  Wardaman
wrs  Waris  Waris
wru  Waru  Waru
wrv  Waruna  Waruna
wrw  Gugu Warra  Gugu Warra
wrx  Wae Rana  Wae Rana
wry  Merwari  Merwari
wrz  Waray (Australia)  Waray (Australia)
wsa  Warembori  Warembori
wsi  Wusi  Wusi
wsk  Waskia  Waskia
wsr  Owenia  Owenia
wss  Wasa  Wasa
wsu  Wasu  Wasu
wsv  Wotapuri-Katarqalai  Wotapuri-Katarqalai
wtf  Watiwa  Watiwa
wth  Wathawurrung  Wathawurrung
wti  Berta  Berta
wtk  Watakataui  Watakataui
wtm  Mewati  Mewati
wtw  Wotu  Wotu
wua  Wikngenchera  Wikngenchera
wub  Wunambal  Wunambal
wud  Wudu  Wudu
wuh  Wutunhua  Wutunhua
wul  Silimo  Silimo
wum  Wumbvu  Wumbvu
wun  Bungu  Bungu
wur  Wurrugu  Wurrugu
wut  Wutung  Wutung
wuu  Wu Chinese  Chinese, Wu
wuv  Wuvulu-Aua  Wuvulu-Aua
wux  Wulna  Wulna
wuy  Wauyai  Wauyai
wwa  Waama  Waama
wwb  Wakabunga  Wakabunga
wwo  Dorig  Dorig
wwo  Wetamut  Wetamut
wwr  Warrwa  Warrwa
www  Wawa  Wawa
wxa  Waxianghua  Waxianghua
wxw  Wardandi  Wardandi
wya  Wyandot  Wyandot
wyb  Wangaaybuwan-Ngiyambaa  Wangaaybuwan-Ngiyambaa
wyi  Woiwurrung  Woiwurrung
wym  Wymysorys  Wymysorys
wyr  Wayoró  Wayoró
wyy  Western Fijian  Fijian, Western
xaa  Andalusian Arabic  Arabic, Andalusian
xab  Sambe  Sambe
xac  Kachari  Kachari
xad  Adai  Adai
xae  Aequian  Aequian
xag  Aghwan  Aghwan
xai  Kaimbé  Kaimbé
xal  Kalmyk  Kalmyk
xal  Oirat  Oirat
xam  /Xam  /Xam
xan  Xamtanga  Xamtanga
xao  Khao  Khao
xap  Apalachee  Apalachee
xaq  Aquitanian  Aquitanian
xar  Karami  Karami
xas  Kamas  Kamas
xat  Katawixi  Katawixi
xau  Kauwera  Kauwera
xav  Xavánte  Xavánte
xaw  Kawaiisu  Kawaiisu
xay  Kayan Mahakam  Kayan Mahakam
xba  Kamba (Brazil)  Kamba (Brazil)
xbb  Lower Burdekin  Burdekin, Lower
xbc  Bactrian  Bactrian
xbd  Bindal  Bindal
xbe  Bigambal  Bigambal
xbg  Bunganditj  Bunganditj
xbi  Kombio  Kombio
xbj  Birrpayi  Birrpayi
xbm  Middle Breton  Breton, Middle
xbn  Kenaboi  Kenaboi
xbo  Bolgarian  Bolgarian
xbp  Bibbulman  Bibbulman
xbr  Kambera  Kambera
xbw  Kambiwá  Kambiwá
xbx  Kabixí  Kabixí
xby  Batyala  Batyala
xcb  Cumbric  Cumbric
xcc  Camunic  Camunic
xce  Celtiberian  Celtiberian
xcg  Cisalpine Gaulish  Gaulish, Cisalpine
xch  Chemakum  Chemakum
xch  Chimakum  Chimakum
xcl  Classical Armenian  Armenian, Classical
xcm  Comecrudo  Comecrudo
xcn  Cotoname  Cotoname
xco  Chorasmian  Chorasmian
xcr  Carian  Carian
xct  Classical Tibetan  Tibetan, Classical
xcu  Curonian  Curonian
xcv  Chuvantsy  Chuvantsy
xcw  Coahuilteco  Coahuilteco
xcy  Cayuse  Cayuse
xda  Darkinyung  Darkinyung
xdc  Dacian  Dacian
xdk  Dharuk  Dharuk
xdm  Edomite  Edomite
xdy  Malayic Dayak  Dayak, Malayic
xeb  Eblan  Eblan
xed  Hdi  Hdi
xeg  //Xegwi  //Xegwi
xel  Kelo  Kelo
xem  Kembayan  Kembayan
xep  Epi-Olmec  Epi-Olmec
xer  Xerénte  Xerénte
xes  Kesawai  Kesawai
xet  Xetá  Xetá
xeu  Keoru-Ahia  Keoru-Ahia
xfa  Faliscan  Faliscan
xga  Galatian  Galatian
xgb  Gbin  Gbin
xgd  Gudang  Gudang
xgf  Gabrielino-Fernandeño  Gabrielino-Fernandeño
xgg  Goreng  Goreng
xgi  Garingbal  Garingbal
xgl  Galindan  Galindan
xgm  Guwinmal  Guwinmal
xgr  Garza  Garza
xgu  Unggumi  Unggumi
xgw  Guwa  Guwa
xha  Harami  Harami
xhc  Hunnic  Hunnic
xhd  Hadrami  Hadrami
xhe  Khetrani  Khetrani
xho  Xhosa  Xhosa
xhr  Hernican  Hernican
xht  Hattic  Hattic
xhu  Hurrian  Hurrian
xhv  Khua  Khua
xib  Iberian  Iberian
xii  Xiri  Xiri
xil  Illyrian  Illyrian
xin  Xinca  Xinca
xip  Xipináwa  Xipináwa
xir  Xiriâna  Xiriâna
xiv  Indus Valley Language  Indus Valley Language
xiy  Xipaya  Xipaya
xjb  Minjungbal  Minjungbal
xjt  Jaitmatang  Jaitmatang
xka  Kalkoti  Kalkoti
xkb  Northern Nago  Nago, Northern
xkc  Kho'ini  Kho'ini
xkd  Mendalam Kayan  Kayan, Mendalam
xke  Kereho  Kereho
xkf  Khengkha  Khengkha
xkg  Kagoro  Kagoro
xkh  Karahawyana  Karahawyana
xki  Kenyan Sign Language  Kenyan Sign Language
xkj  Kajali  Kajali
xkk  Kaco'  Kaco'
xkl  Mainstream Kenyah  Mainstream Kenyah
xkn  Kayan River Kayan  Kayan, Kayan River
xko  Kiorr  Kiorr
xkp  Kabatei  Kabatei
xkq  Koroni  Koroni
xkr  Xakriabá  Xakriabá
xks  Kumbewaha  Kumbewaha
xkt  Kantosi  Kantosi
xku  Kaamba  Kaamba
xkv  Kgalagadi  Kgalagadi
xkw  Kembra  Kembra
xkx  Karore  Karore
xky  Uma' Lasan  Uma' Lasan
xkz  Kurtokha  Kurtokha
xla  Kamula  Kamula
xlb  Loup B  Loup B
xlc  Lycian  Lycian
xld  Lydian  Lydian
xle  Lemnian  Lemnian
xlg  Ligurian (Ancient)  Ligurian (Ancient)
xli  Liburnian  Liburnian
xln  Alanic  Alanic
xlo  Loup A  Loup A
xlp  Lepontic  Lepontic
xls  Lusitanian  Lusitanian
xlu  Cuneiform Luwian  Luwian, Cuneiform
xly  Elymian  Elymian
xma  Mushungulu  Mushungulu
xmb  Mbonga  Mbonga
xmc  Makhuwa-Marrevone  Makhuwa-Marrevone
xmd  Mbudum  Mbudum
xme  Median  Median
xmf  Mingrelian  Mingrelian
xmg  Mengaka  Mengaka
xmh  Kuku-Muminh  Kuku-Muminh
xmj  Majera  Majera
xmk  Ancient Macedonian  Macedonian, Ancient
xml  Malaysian Sign Language  Malaysian Sign Language
xmm  Manado Malay  Malay, Manado
xmn  Manichaean Middle Persian  Persian, Manichaean Middle
xmo  Morerebi  Morerebi
xmp  Kuku-Mu'inh  Kuku-Mu'inh
xmq  Kuku-Mangk  Kuku-Mangk
xmr  Meroitic  Meroitic
xms  Moroccan Sign Language  Moroccan Sign Language
xmt  Matbat  Matbat
xmu  Kamu  Kamu
xmv  Antankarana Malagasy  Malagasy, Antankarana
xmv  Tankarana Malagasy  Malagasy, Tankarana
xmw  Tsimihety Malagasy  Malagasy, Tsimihety
xmx  Maden  Maden
xmy  Mayaguduna  Mayaguduna
xmz  Mori Bawah  Mori Bawah
xna  Ancient North Arabian  North Arabian, Ancient
xnb  Kanakanabu  Kanakanabu
xng  Middle Mongolian  Mongolian, Middle
xnh  Kuanhua  Kuanhua
xni  Ngarigu  Ngarigu
xnk  Nganakarti  Nganakarti
xnn  Northern Kankanay  Kankanay, Northern
xno  Anglo-Norman  Anglo-Norman
xnr  Kangri  Kangri
xns  Kanashi  Kanashi
xnt  Narragansett  Narragansett
xnu  Nukunul  Nukunul
xny  Nyiyaparli  Nyiyaparli
xnz  Kenzi  Kenzi
xnz  Mattoki  Mattoki
xoc  O'chi'chi'  O'chi'chi'
xod  Kokoda  Kokoda
xog  Soga  Soga
xoi  Kominimung  Kominimung
xok  Xokleng  Xokleng
xom  Komo (Sudan)  Komo (Sudan)
xon  Konkomba  Konkomba
xoo  Xukurú  Xukurú
xop  Kopar  Kopar
xor  Korubo  Korubo
xow  Kowaki  Kowaki
xpa  Pirriya  Pirriya
xpc  Pecheneg  Pecheneg
xpe  Liberia Kpelle  Kpelle, Liberia
xpg  Phrygian  Phrygian
xpi  Pictish  Pictish
xpj  Mpalitjanh  Mpalitjanh
xpk  Kulina Pano  Pano, Kulina
xpm  Pumpokol  Pumpokol
xpn  Kapinawá  Kapinawá
xpo  Pochutec  Pochutec
xpp  Puyo-Paekche  Puyo-Paekche
xpq  Mohegan-Pequot  Mohegan-Pequot
xpr  Parthian  Parthian
xps  Pisidian  Pisidian
xpt  Punthamara  Punthamara
xpu  Punic  Punic
xpy  Puyo  Puyo
xqa  Karakhanid  Karakhanid
xqt  Qatabanian  Qatabanian
xra  Krahô  Krahô
xrb  Eastern Karaboro  Karaboro, Eastern
xrd  Gundungurra  Gundungurra
xre  Kreye  Kreye
xrg  Minang  Minang
xri  Krikati-Timbira  Krikati-Timbira
xrm  Armazic  Armazic
xrn  Arin  Arin
xrq  Karranga  Karranga
xrr  Raetic  Raetic
xrt  Aranama-Tamique  Aranama-Tamique
xru  Marriammu  Marriammu
xrw  Karawa  Karawa
xsa  Sabaean  Sabaean
xsb  Sambal  Sambal
xsc  Scythian  Scythian
xsd  Sidetic  Sidetic
xse  Sempan  Sempan
xsh  Shamang  Shamang
xsi  Sio  Sio
xsj  Subi  Subi
xsl  South Slavey  Slavey, South
xsm  Kasem  Kasem
xsn  Sanga (Nigeria)  Sanga (Nigeria)
xso  Solano  Solano
xsp  Silopi  Silopi
xsq  Makhuwa-Saka  Makhuwa-Saka
xsr  Sherpa  Sherpa
xss  Assan  Assan
xsu  Sanumá  Sanumá
xsv  Sudovian  Sudovian
xsy  Saisiyat  Saisiyat
xta  Alcozauca Mixtec  Mixtec, Alcozauca
xtb  Chazumba Mixtec  Mixtec, Chazumba
xtc  Katcha-Kadugli-Miri  Katcha-Kadugli-Miri
xtd  Diuxi-Tilantongo Mixtec  Mixtec, Diuxi-Tilantongo
xte  Ketengban  Ketengban
xtg  Transalpine Gaulish  Gaulish, Transalpine
xth  Yitha Yitha  Yitha Yitha
xti  Sinicahua Mixtec  Mixtec, Sinicahua
xtj  San Juan Teita Mixtec  Mixtec, San Juan Teita
xtl  Tijaltepec Mixtec  Mixtec, Tijaltepec
xtm  Magdalena Peñasco Mixtec  Mixtec, Magdalena Peñasco
xtn  Northern Tlaxiaco Mixtec  Mixtec, Northern Tlaxiaco
xto  Tokharian A  Tokharian A
xtp  San Miguel Piedras Mixtec  Mixtec, San Miguel Piedras
xtq  Tumshuqese  Tumshuqese
xtr  Early Tripuri  Tripuri, Early
xts  Sindihui Mixtec  Mixtec, Sindihui
xtt  Tacahua Mixtec  Mixtec, Tacahua
xtu  Cuyamecalco Mixtec  Mixtec, Cuyamecalco
xtv  Thawa  Thawa
xtw  Tawandê  Tawandê
xty  Yoloxochitl Mixtec  Mixtec, Yoloxochitl
xtz  Tasmanian  Tasmanian
xua  Alu Kurumba  Kurumba, Alu
xub  Betta Kurumba  Kurumba, Betta
xud  Umiida  Umiida
xug  Kunigami  Kunigami
xuj  Jennu Kurumba  Kurumba, Jennu
xul  Ngunawal  Ngunawal
xum  Umbrian  Umbrian
xun  Unggaranggu  Unggaranggu
xuo  Kuo  Kuo
xup  Upper Umpqua  Umpqua, Upper
xur  Urartian  Urartian
xut  Kuthant  Kuthant
xuu  Kxoe  Kxoe
xve  Venetic  Venetic
xvi  Kamviri  Kamviri
xvn  Vandalic  Vandalic
xvo  Volscian  Volscian
xvs  Vestinian  Vestinian
xwa  Kwaza  Kwaza
xwc  Woccon  Woccon
xwd  Wadi Wadi  Wadi Wadi
xwe  Xwela Gbe  Gbe, Xwela
xwg  Kwegu  Kwegu
xwj  Wajuk  Wajuk
xwk  Wangkumara  Wangkumara
xwl  Western Xwla Gbe  Gbe, Western Xwla
xwo  Written Oirat  Oirat, Written
xwr  Kwerba Mamberamo  Kwerba Mamberamo
xwt  Wotjobaluk  Wotjobaluk
xww  Wemba Wemba  Wemba Wemba
xxb  Boro (Ghana)  Boro (Ghana)
xxk  Ke'o  Ke'o
xxm  Minkin  Minkin
xxr  Koropó  Koropó
xxt  Tambora  Tambora
xya  Yaygir  Yaygir
xyb  Yandjibara  Yandjibara
xyj  Mayi-Yapi  Mayi-Yapi
xyk  Mayi-Kulan  Mayi-Kulan
xyl  Yalakalore  Yalakalore
xyt  Mayi-Thakurti  Mayi-Thakurti
xyy  Yorta Yorta  Yorta Yorta
xzh  Zhang-Zhung  Zhang-Zhung
xzm  Zemgalian  Zemgalian
xzp  Ancient Zapotec  Zapotec, Ancient
yaa  Yaminahua  Yaminahua
yab  Yuhup  Yuhup
yac  Pass Valley Yali  Yali, Pass Valley
yad  Yagua  Yagua
yae  Pumé  Pumé
yaf  Yaka (Democratic Republic of Congo)  Yaka (Democratic Republic of Congo)
yag  Yámana  Yámana
yah  Yazgulyam  Yazgulyam
yai  Yagnobi  Yagnobi
yaj  Banda-Yangere  Banda-Yangere
yak  Yakama  Yakama
yal  Yalunka  Yalunka
yam  Yamba  Yamba
yan  Mayangna  Mayangna
yao  Yao  Yao
yap  Yapese  Yapese
yaq  Yaqui  Yaqui
yar  Yabarana  Yabarana
yas  Nugunu (Cameroon)  Nugunu (Cameroon)
yat  Yambeta  Yambeta
yau  Yuwana  Yuwana
yav  Yangben  Yangben
yaw  Yawalapití  Yawalapití
yax  Yauma  Yauma
yay  Agwagwune  Agwagwune
yaz  Lokaa  Lokaa
yba  Yala  Yala
ybb  Yemba  Yemba
ybe  West Yugur  Yugur, West
ybh  Yakha  Yakha
ybi  Yamphu  Yamphu
ybj  Hasha  Hasha
ybk  Bokha  Bokha
ybl  Yukuben  Yukuben
ybm  Yaben  Yaben
ybn  Yabaâna  Yabaâna
ybo  Yabong  Yabong
ybx  Yawiyo  Yawiyo
yby  Yaweyuha  Yaweyuha
ych  Chesu  Chesu
ycl  Lolopo  Lolopo
ycn  Yucuna  Yucuna
ycp  Chepya  Chepya
yda  Yanda  Yanda
ydd  Eastern Yiddish  Yiddish, Eastern
yde  Yangum Dey  Yangum Dey
ydg  Yidgha  Yidgha
ydk  Yoidik  Yoidik
yds  Yiddish Sign Language  Yiddish Sign Language
yea  Ravula  Ravula
yec  Yeniche  Yeniche
yee  Yimas  Yimas
yei  Yeni  Yeni
yej  Yevanic  Yevanic
yel  Yela  Yela
yer  Tarok  Tarok
yes  Nyankpa  Nyankpa
yet  Yetfa  Yetfa
yeu  Yerukula  Yerukula
yev  Yapunda  Yapunda
yey  Yeyi  Yeyi
yga  Malyangapa  Malyangapa
ygi  Yiningayi  Yiningayi
ygl  Yangum Gel  Yangum Gel
ygm  Yagomi  Yagomi
ygp  Gepo  Gepo
ygr  Yagaria  Yagaria
ygu  Yugul  Yugul
ygw  Yagwoia  Yagwoia
yha  Baha Buyang  Buyang, Baha
yhd  Judeo-Iraqi Arabic  Arabic, Judeo-Iraqi
yhl  Hlepho Phowa  Phowa, Hlepho
yia  Yinggarda  Yinggarda
yid  Yiddish  Yiddish
yif  Ache  Ache
yig  Wusa Nasu  Nasu, Wusa
yih  Western Yiddish  Yiddish, Western
yii  Yidiny  Yidiny
yij  Yindjibarndi  Yindjibarndi
yik  Dongshanba Lalo  Lalo, Dongshanba
yil  Yindjilandji  Yindjilandji
yim  Yimchungru Naga  Naga, Yimchungru
yin  Yinchia  Yinchia
yip  Pholo  Pholo
yiq  Miqie  Miqie
yir  North Awyu  Awyu, North
yis  Yis  Yis
yit  Eastern Lalu  Lalu, Eastern
yiu  Awu  Awu
yiv  Northern Nisu  Nisu, Northern
yix  Axi Yi  Yi, Axi
yiz  Azhe  Azhe
yka  Yakan  Yakan
ykg  Northern Yukaghir  Yukaghir, Northern
yki  Yoke  Yoke
ykk  Yakaikeke  Yakaikeke
ykl  Khlula  Khlula
ykm  Kap  Kap
ykn  Kua-nsi  Kua-nsi
yko  Yasa  Yasa
ykr  Yekora  Yekora
ykt  Kathu  Kathu
yku  Kuamasi  Kuamasi
yky  Yakoma  Yakoma
yla  Yaul  Yaul
ylb  Yaleba  Yaleba
yle  Yele  Yele
ylg  Yelogu  Yelogu
yli  Angguruk Yali  Yali, Angguruk
yll  Yil  Yil
ylm  Limi  Limi
yln  Langnian Buyang  Buyang, Langnian
ylo  Naluo Yi  Yi, Naluo
ylr  Yalarnnga  Yalarnnga
ylu  Aribwaung  Aribwaung
yly  Nyâlayu  Nyâlayu
yly  Nyelâyu  Nyelâyu
ymb  Yambes  Yambes
ymc  Southern Muji  Muji, Southern
ymd  Muda  Muda
yme  Yameo  Yameo
ymg  Yamongeri  Yamongeri
ymh  Mili  Mili
ymi  Moji  Moji
ymk  Makwe  Makwe
yml  Iamalele  Iamalele
ymm  Maay  Maay
ymn  Sunum  Sunum
ymn  Yamna  Yamna
ymo  Yangum Mon  Yangum Mon
ymp  Yamap  Yamap
ymq  Qila Muji  Muji, Qila
ymr  Malasar  Malasar
yms  Mysian  Mysian
ymt  Mator-Taygi-Karagas  Mator-Taygi-Karagas
ymx  Northern Muji  Muji, Northern
ymz  Muzi  Muzi
yna  Aluo  Aluo
ynd  Yandruwandha  Yandruwandha
yne  Lang'e  Lang'e
yng  Yango  Yango
ynh  Yangho  Yangho
ynk  Naukan Yupik  Yupik, Naukan
ynl  Yangulam  Yangulam
ynn  Yana  Yana
yno  Yong  Yong
ynq  Yendang  Yendang
yns  Yansi  Yansi
ynu  Yahuna  Yahuna
yob  Yoba  Yoba
yog  Yogad  Yogad
yoi  Yonaguni  Yonaguni
yok  Yokuts  Yokuts
yol  Yola  Yola
yom  Yombe  Yombe
yon  Yongkom  Yongkom
yor  Yoruba  Yoruba
yot  Yotti  Yotti
yox  Yoron  Yoron
yoy  Yoy  Yoy
ypa  Phala  Phala
ypb  Labo Phowa  Phowa, Labo
ypg  Phola  Phola
yph  Phupha  Phupha
ypm  Phuma  Phuma
ypn  Ani Phowa  Phowa, Ani
ypo  Alo Phola  Phola, Alo
ypp  Phupa  Phupa
ypz  Phuza  Phuza
yra  Yerakai  Yerakai
yrb  Yareba  Yareba
yre  Yaouré  Yaouré
yri  Yarí  Yarí
yrk  Nenets  Nenets
yrl  Nhengatu  Nhengatu
yrm  Yirrk-Mel  Yirrk-Mel
yrn  Yerong  Yerong
yrs  Yarsun  Yarsun
yrw  Yarawata  Yarawata
yry  Yarluyandi  Yarluyandi
ysc  Yassic  Yassic
ysd  Samatao  Samatao
ysg  Sonaga  Sonaga
ysl  Yugoslavian Sign Language  Yugoslavian Sign Language
ysn  Sani  Sani
yso  Nisi (China)  Nisi (China)
ysp  Southern Lolopo  Lolopo, Southern
ysr  Sirenik Yupik  Yupik, Sirenik
yss  Yessan-Mayo  Yessan-Mayo
ysy  Sanie  Sanie
yta  Talu  Talu
ytl  Tanglang  Tanglang
ytp  Thopho  Thopho
ytw  Yout Wam  Yout Wam
yty  Yatay  Yatay
yua  Yucatec Maya  Maya, Yucatec
yua  Yucateco  Yucateco
yub  Yugambal  Yugambal
yuc  Yuchi  Yuchi
yud  Judeo-Tripolitanian Arabic  Arabic, Judeo-Tripolitanian
yue  Yue Chinese  Chinese, Yue
yuf  Havasupai-Walapai-Yavapai  Havasupai-Walapai-Yavapai
yug  Yug  Yug
yui  Yurutí  Yurutí
yuj  Karkar-Yuri  Karkar-Yuri
yuk  Yuki  Yuki
yul  Yulu  Yulu
yum  Quechan  Quechan
yun  Bena (Nigeria)  Bena (Nigeria)
yup  Yukpa  Yukpa
yuq  Yuqui  Yuqui
yur  Yurok  Yurok
yut  Yopno  Yopno
yuu  Yugh  Yugh
yuw  Yau (Morobe Province)  Yau (Morobe Province)
yux  Southern Yukaghir  Yukaghir, Southern
yuy  East Yugur  Yugur, East
yuz  Yuracare  Yuracare
yva  Yawa  Yawa
yvt  Yavitero  Yavitero
ywa  Kalou  Kalou
ywg  Yinhawangka  Yinhawangka
ywl  Western Lalu  Lalu, Western
ywn  Yawanawa  Yawanawa
ywq  Wuding-Luquan Yi  Yi, Wuding-Luquan
ywr  Yawuru  Yawuru
ywt  Central Lalo  Lalo, Central
ywt  Xishanba Lalo  Lalo, Xishanba
ywu  Wumeng Nasu  Nasu, Wumeng
yww  Yawarawarga  Yawarawarga
yxa  Mayawali  Mayawali
yxg  Yagara  Yagara
yxl  Yardliyawarra  Yardliyawarra
yxm  Yinwum  Yinwum
yxu  Yuyu  Yuyu
yxy  Yabula Yabula  Yabula Yabula
yyr  Yir Yoront  Yir Yoront
yyu  Yau (Sandaun Province)  Yau (Sandaun Province)
yyz  Ayizi  Ayizi
yzg  E'ma Buyang  Buyang, E'ma
yzk  Zokhuo  Zokhuo
zaa  Sierra de Juárez Zapotec  Zapotec, Sierra de Juárez
zab  San Juan Guelavía Zapotec  Zapotec, San Juan Guelavía
zac  Ocotlán Zapotec  Zapotec, Ocotlán
zad  Cajonos Zapotec  Zapotec, Cajonos
zae  Yareni Zapotec  Zapotec, Yareni
zaf  Ayoquesco Zapotec  Zapotec, Ayoquesco
zag  Zaghawa  Zaghawa
zah  Zangwal  Zangwal
zai  Isthmus Zapotec  Zapotec, Isthmus
zaj  Zaramo  Zaramo
zak  Zanaki  Zanaki
zal  Zauzou  Zauzou
zam  Miahuatlán Zapotec  Zapotec, Miahuatlán
zao  Ozolotepec Zapotec  Zapotec, Ozolotepec
zap  Zapotec  Zapotec
zaq  Aloápam Zapotec  Zapotec, Aloápam
zar  Rincón Zapotec  Zapotec, Rincón
zas  Santo Domingo Albarradas Zapotec  Zapotec, Santo Domingo Albarradas
zat  Tabaa Zapotec  Zapotec, Tabaa
zau  Zangskari  Zangskari
zav  Yatzachi Zapotec  Zapotec, Yatzachi
zaw  Mitla Zapotec  Zapotec, Mitla
zax  Xadani Zapotec  Zapotec, Xadani
zay  Zaysete  Zaysete
zay  Zayse-Zergulla  Zayse-Zergulla
zaz  Zari  Zari
zbc  Central Berawan  Berawan, Central
zbe  East Berawan  Berawan, East
zbl  Bliss  Bliss
zbl  Blissymbolics  Blissymbolics
zbl  Blissymbols  Blissymbols
zbt  Batui  Batui
zbw  West Berawan  Berawan, West
zca  Coatecas Altas Zapotec  Zapotec, Coatecas Altas
zch  Central Hongshuihe Zhuang  Zhuang, Central Hongshuihe
zdj  Ngazidja Comorian  Comorian, Ngazidja
zea  Zeeuws  Zeeuws
zeg  Zenag  Zenag
zeh  Eastern Hongshuihe Zhuang  Zhuang, Eastern Hongshuihe
zen  Zenaga  Zenaga
zga  Kinga  Kinga
zgb  Guibei Zhuang  Zhuang, Guibei
zgh  Standard Moroccan Tamazight  Tamazight, Standard Moroccan
zgm  Minz Zhuang  Zhuang, Minz
zgn  Guibian Zhuang  Zhuang, Guibian
zgr  Magori  Magori
zha  Chuang  Chuang
zha  Zhuang  Zhuang
zhb  Zhaba  Zhaba
zhd  Dai Zhuang  Zhuang, Dai
zhi  Zhire  Zhire
zhn  Nong Zhuang  Zhuang, Nong
zho  Chinese  Chinese
zhw  Zhoa  Zhoa
zia  Zia  Zia
zib  Zimbabwe Sign Language  Zimbabwe Sign Language
zik  Zimakani  Zimakani
zil  Zialo  Zialo
zim  Mesme  Mesme
zin  Zinza  Zinza
zir  Ziriya  Ziriya
ziw  Zigula  Zigula
ziz  Zizilivakan  Zizilivakan
zka  Kaimbulawa  Kaimbulawa
zkb  Koibal  Koibal
zkd  Kadu  Kadu
zkg  Koguryo  Koguryo
zkh  Khorezmian  Khorezmian
zkk  Karankawa  Karankawa
zkn  Kanan  Kanan
zko  Kott  Kott
zkp  São Paulo Kaingáng  Kaingáng, São Paulo
zkr  Zakhring  Zakhring
zkt  Kitan  Kitan
zku  Kaurna  Kaurna
zkv  Krevinian  Krevinian
zkz  Khazar  Khazar
zlj  Liujiang Zhuang  Zhuang, Liujiang
zlm  Malay (individual language)  Malay (individual language)
zln  Lianshan Zhuang  Zhuang, Lianshan
zlq  Liuqian Zhuang  Zhuang, Liuqian
zma  Manda (Australia)  Manda (Australia)
zmb  Zimba  Zimba
zmc  Margany  Margany
zmd  Maridan  Maridan
zme  Mangerr  Mangerr
zmf  Mfinu  Mfinu
zmg  Marti Ke  Marti Ke
zmh  Makolkol  Makolkol
zmi  Negeri Sembilan Malay  Negeri Sembilan Malay
zmj  Maridjabin  Maridjabin
zmk  Mandandanyi  Mandandanyi
zml  Madngele  Madngele
zmm  Marimanindji  Marimanindji
zmn  Mbangwe  Mbangwe
zmo  Molo  Molo
zmp  Mpuono  Mpuono
zmq  Mituku  Mituku
zmr  Maranunggu  Maranunggu
zms  Mbesa  Mbesa
zmt  Maringarr  Maringarr
zmu  Muruwari  Muruwari
zmv  Mbariman-Gudhinma  Mbariman-Gudhinma
zmw  Mbo (Democratic Republic of Congo)  Mbo (Democratic Republic of Congo)
zmx  Bomitaba  Bomitaba
zmy  Mariyedi  Mariyedi
zmz  Mbandja  Mbandja
zna  Zan Gula  Zan Gula
zne  Zande (individual language)  Zande (individual language)
zng  Mang  Mang
znk  Manangkari  Manangkari
zns  Mangas  Mangas
zoc  Copainalá Zoque  Zoque, Copainalá
zoh  Chimalapa Zoque  Zoque, Chimalapa
zom  Zou  Zou
zoo  Asunción Mixtepec Zapotec  Zapotec, Asunción Mixtepec
zoq  Tabasco Zoque  Zoque, Tabasco
zor  Rayón Zoque  Zoque, Rayón
zos  Francisco León Zoque  Zoque, Francisco León
zpa  Lachiguiri Zapotec  Zapotec, Lachiguiri
zpb  Yautepec Zapotec  Zapotec, Yautepec
zpc  Choapan Zapotec  Zapotec, Choapan
zpd  Southeastern Ixtlán Zapotec  Zapotec, Southeastern Ixtlán
zpe  Petapa Zapotec  Zapotec, Petapa
zpf  San Pedro Quiatoni Zapotec  Zapotec, San Pedro Quiatoni
zpg  Guevea De Humboldt Zapotec  Zapotec, Guevea De Humboldt
zph  Totomachapan Zapotec  Zapotec, Totomachapan
zpi  Santa María Quiegolani Zapotec  Zapotec, Santa María Quiegolani
zpj  Quiavicuzas Zapotec  Zapotec, Quiavicuzas
zpk  Tlacolulita Zapotec  Zapotec, Tlacolulita
zpl  Lachixío Zapotec  Zapotec, Lachixío
zpm  Mixtepec Zapotec  Zapotec, Mixtepec
zpn  Santa Inés Yatzechi Zapotec  Zapotec, Santa Inés Yatzechi
zpo  Amatlán Zapotec  Zapotec, Amatlán
zpp  El Alto Zapotec  Zapotec, El Alto
zpq  Zoogocho Zapotec  Zapotec, Zoogocho
zpr  Santiago Xanica Zapotec  Zapotec, Santiago Xanica
zps  Coatlán Zapotec  Zapotec, Coatlán
zpt  San Vicente Coatlán Zapotec  Zapotec, San Vicente Coatlán
zpu  Yalálag Zapotec  Zapotec, Yalálag
zpv  Chichicapan Zapotec  Zapotec, Chichicapan
zpw  Zaniza Zapotec  Zapotec, Zaniza
zpx  San Baltazar Loxicha Zapotec  Zapotec, San Baltazar Loxicha
zpy  Mazaltepec Zapotec  Zapotec, Mazaltepec
zpz  Texmelucan Zapotec  Zapotec, Texmelucan
zqe  Qiubei Zhuang  Zhuang, Qiubei
zra  Kara (Korea)  Kara (Korea)
zrg  Mirgan  Mirgan
zrn  Zerenkel  Zerenkel
zro  Záparo  Záparo
zrp  Zarphatic  Zarphatic
zrs  Mairasi  Mairasi
zsa  Sarasira  Sarasira
zsk  Kaskean  Kaskean
zsl  Zambian Sign Language  Zambian Sign Language
zsm  Standard Malay  Malay, Standard
zsr  Southern Rincon Zapotec  Zapotec, Southern Rincon
zsu  Sukurum  Sukurum
zte  Elotepec Zapotec  Zapotec, Elotepec
ztg  Xanaguía Zapotec  Zapotec, Xanaguía
ztl  Lapaguía-Guivini Zapotec  Zapotec, Lapaguía-Guivini
ztm  San Agustín Mixtepec Zapotec  Zapotec, San Agustín Mixtepec
ztn  Santa Catarina Albarradas Zapotec  Zapotec, Santa Catarina Albarradas
ztp  Loxicha Zapotec  Zapotec, Loxicha
ztq  Quioquitani-Quierí Zapotec  Zapotec, Quioquitani-Quierí
zts  Tilquiapan Zapotec  Zapotec, Tilquiapan
ztt  Tejalapan Zapotec  Zapotec, Tejalapan
ztu  Güilá Zapotec  Zapotec, Güilá
ztx  Zaachila Zapotec  Zapotec, Zaachila
zty  Yatee Zapotec  Zapotec, Yatee
zua  Zeem  Zeem
zuh  Tokano  Tokano
zul  Zulu  Zulu
zum  Kumzari  Kumzari
zun  Zuni  Zuni
zuy  Zumaya  Zumaya
zwa  Zay  Zay
zxx  No linguistic content  No linguistic content
zxx  Not applicable  Not applicable
zyb  Yongbei Zhuang  Zhuang, Yongbei
zyg  Yang Zhuang  Zhuang, Yang
zyj  Youjiang Zhuang  Zhuang, Youjiang
zyn  Yongnan Zhuang  Zhuang, Yongnan
zyp  Zyphe Chin  Chin, Zyphe
zza  Dimili  Dimili
zza  Dimli (macrolanguage)  Dimli (macrolanguage)
zza  Kirdki  Kirdki
zza  Kirmanjki (macrolanguage)  Kirmanjki (macrolanguage)
zza  Zaza  Zaza
zza  Zazaki  Zazaki
zzj  Zuojiang Zhuang  Zhuang, Zuojiang"""



# from http://www-01.sil.org/iso639-3/codes.asp?order=639_3&letter=%25
#639-1 	639-2/639-5 	639-3	Language Name 	Scope 	Type
isomapping = """aa 	aar 	aar 	Afar 	Individual 	Living 	more ...
ab 	abk 	abk 	Abkhazian 	Individual 	Living 	more ...
ae 	ave 	ave 	Avestan 	Individual 	Ancient 	more ...
af 	afr 	afr 	Afrikaans 	Individual 	Living 	more ...
ak 	aka 	aka 	Akan 	Macrolanguage 	Living 	more ...
am 	amh 	amh 	Amharic 	Individual 	Living 	more ...
an 	arg 	arg 	Aragonese 	Individual 	Living 	more ...
ar 	ara 	ara 	Arabic 	Macrolanguage 	Living 	more ...
as 	asm 	asm 	Assamese 	Individual 	Living 	more ...
av 	ava 	ava 	Avaric 	Individual 	Living 	more ...
ay 	aym 	aym 	Aymara 	Macrolanguage 	Living 	more ...
az 	aze 	aze 	Azerbaijani 	Macrolanguage 	Living 	more ...
ba 	bak 	bak 	Bashkir 	Individual 	Living 	more ...
be 	bel 	bel 	Belarusian 	Individual 	Living 	more ...
bg 	bul 	bul 	Bulgarian 	Individual 	Living 	more ...
bh 	bih 	- 	Bihari languages 	Collective 		more ...
bi 	bis 	bis 	Bislama 	Individual 	Living 	more ...
bm 	bam 	bam 	Bambara 	Individual 	Living 	more ...
bn 	ben 	ben 	Bengali 	Individual 	Living 	more ...
bo 	bod / tib*  	bod 	Tibetan 	Individual 	Living 	more ...
br 	bre 	bre 	Breton 	Individual 	Living 	more ...
bs 	bos 	bos 	Bosnian 	Individual 	Living 	more ...
ca 	cat 	cat 	Catalan 	Individual 	Living 	more ...
ce 	che 	che 	Chechen 	Individual 	Living 	more ...
ch 	cha 	cha 	Chamorro 	Individual 	Living 	more ...
co 	cos 	cos 	Corsican 	Individual 	Living 	more ...
cr 	cre 	cre 	Cree 	Macrolanguage 	Living 	more ...
cs 	ces / cze*  	ces 	Czech 	Individual 	Living 	more ...
cu 	chu 	chu 	Church Slavic 	Individual 	Ancient 	more ...
cv 	chv 	chv 	Chuvash 	Individual 	Living 	more ...
cy 	cym / wel*  	cym 	Welsh 	Individual 	Living 	more ...
da 	dan 	dan 	Danish 	Individual 	Living 	more ...
de 	deu / ger*  	deu 	German 	Individual 	Living 	more ...
dv 	div 	div 	Dhivehi 	Individual 	Living 	more ...
dz 	dzo 	dzo 	Dzongkha 	Individual 	Living 	more ...
ee 	ewe 	ewe 	Ewe 	Individual 	Living 	more ...
el 	ell / gre*  	ell 	Modern Greek (1453-) 	Individual 	Living 	more ...
en 	eng 	eng 	English 	Individual 	Living 	more ...
eo 	epo 	epo 	Esperanto 	Individual 	Constructed 	more ...
es 	spa 	spa 	Spanish 	Individual 	Living 	more ...
et 	est 	est 	Estonian 	Macrolanguage 	Living 	more ...
eu 	eus / baq*  	eus 	Basque 	Individual 	Living 	more ...
fa 	fas / per*  	fas 	Persian 	Macrolanguage 	Living 	more ...
ff 	ful 	ful 	Fulah 	Macrolanguage 	Living 	more ...
fi 	fin 	fin 	Finnish 	Individual 	Living 	more ...
fj 	fij 	fij 	Fijian 	Individual 	Living 	more ...
fo 	fao 	fao 	Faroese 	Individual 	Living 	more ...
fr 	fra / fre*  	fra 	French 	Individual 	Living 	more ...
fy 	fry 	fry 	Western Frisian 	Individual 	Living 	more ...
ga 	gle 	gle 	Irish 	Individual 	Living 	more ...
gd 	gla 	gla 	Scottish Gaelic 	Individual 	Living 	more ...
gl 	glg 	glg 	Galician 	Individual 	Living 	more ...
gn 	grn 	grn 	Guarani 	Macrolanguage 	Living 	more ...
gu 	guj 	guj 	Gujarati 	Individual 	Living 	more ...
gv 	glv 	glv 	Manx 	Individual 	Living 	more ...
ha 	hau 	hau 	Hausa 	Individual 	Living 	more ...
he 	heb 	heb 	Hebrew 	Individual 	Living 	more ...
hi 	hin 	hin 	Hindi 	Individual 	Living 	more ...
ho 	hmo 	hmo 	Hiri Motu 	Individual 	Living 	more ...
hr 	hrv 	hrv 	Croatian 	Individual 	Living 	more ...
ht 	hat 	hat 	Haitian 	Individual 	Living 	more ...
hu 	hun 	hun 	Hungarian 	Individual 	Living 	more ...
hy 	hye / arm*  	hye 	Armenian 	Individual 	Living 	more ...
hz 	her 	her 	Herero 	Individual 	Living 	more ...
ia 	ina 	ina 	Interlingua (International Auxiliary Language Association) 	Individual 	Constructed 	more ...
id 	ind 	ind 	Indonesian 	Individual 	Living 	more ...
ie 	ile 	ile 	Interlingue 	Individual 	Constructed 	more ...
ig 	ibo 	ibo 	Igbo 	Individual 	Living 	more ...
ii 	iii 	iii 	Sichuan Yi 	Individual 	Living 	more ...
ik 	ipk 	ipk 	Inupiaq 	Macrolanguage 	Living 	more ...
io 	ido 	ido 	Ido 	Individual 	Constructed 	more ...
is 	isl / ice*  	isl 	Icelandic 	Individual 	Living 	more ...
it 	ita 	ita 	Italian 	Individual 	Living 	more ...
iu 	iku 	iku 	Inuktitut 	Macrolanguage 	Living 	more ...
ja 	jpn 	jpn 	Japanese 	Individual 	Living 	more ...
jv 	jav 	jav 	Javanese 	Individual 	Living 	more ...
ka 	kat / geo*  	kat 	Georgian 	Individual 	Living 	more ...
kg 	kon 	kon 	Kongo 	Macrolanguage 	Living 	more ...
ki 	kik 	kik 	Kikuyu 	Individual 	Living 	more ...
kj 	kua 	kua 	Kuanyama 	Individual 	Living 	more ...
kk 	kaz 	kaz 	Kazakh 	Individual 	Living 	more ...
kl 	kal 	kal 	Kalaallisut 	Individual 	Living 	more ...
km 	khm 	khm 	Central Khmer 	Individual 	Living 	more ...
kn 	kan 	kan 	Kannada 	Individual 	Living 	more ...
ko 	kor 	kor 	Korean 	Individual 	Living 	more ...
kr 	kau 	kau 	Kanuri 	Macrolanguage 	Living 	more ...
ks 	kas 	kas 	Kashmiri 	Individual 	Living 	more ...
ku 	kur 	kur 	Kurdish 	Macrolanguage 	Living 	more ...
kv 	kom 	kom 	Komi 	Macrolanguage 	Living 	more ...
kw 	cor 	cor 	Cornish 	Individual 	Living 	more ...
ky 	kir 	kir 	Kirghiz 	Individual 	Living 	more ...
la 	lat 	lat 	Latin 	Individual 	Ancient 	more ...
lb 	ltz 	ltz 	Luxembourgish 	Individual 	Living 	more ...
lg 	lug 	lug 	Ganda 	Individual 	Living 	more ...
li 	lim 	lim 	Limburgan 	Individual 	Living 	more ...
ln 	lin 	lin 	Lingala 	Individual 	Living 	more ...
lo 	lao 	lao 	Lao 	Individual 	Living 	more ...
lt 	lit 	lit 	Lithuanian 	Individual 	Living 	more ...
lu 	lub 	lub 	Luba-Katanga 	Individual 	Living 	more ...
lv 	lav 	lav 	Latvian 	Macrolanguage 	Living 	more ...
mg 	mlg 	mlg 	Malagasy 	Macrolanguage 	Living 	more ...
mh 	mah 	mah 	Marshallese 	Individual 	Living 	more ...
mi 	mri / mao*  	mri 	Maori 	Individual 	Living 	more ...
mk 	mkd / mac*  	mkd 	Macedonian 	Individual 	Living 	more ...
ml 	mal 	mal 	Malayalam 	Individual 	Living 	more ...
mn 	mon 	mon 	Mongolian 	Macrolanguage 	Living 	more ...
mr 	mar 	mar 	Marathi 	Individual 	Living 	more ...
ms 	msa / may*  	msa 	Malay (macrolanguage) 	Macrolanguage 	Living 	more ...
mt 	mlt 	mlt 	Maltese 	Individual 	Living 	more ...
my 	mya / bur*  	mya 	Burmese 	Individual 	Living 	more ...
na 	nau 	nau 	Nauru 	Individual 	Living 	more ...
nb 	nob 	nob 	Norwegian Bokmål 	Individual 	Living 	more ...
nd 	nde 	nde 	North Ndebele 	Individual 	Living 	more ...
ne 	nep 	nep 	Nepali (macrolanguage) 	Macrolanguage 	Living 	more ...
ng 	ndo 	ndo 	Ndonga 	Individual 	Living 	more ...
nl 	nld / dut*  	nld 	Dutch 	Individual 	Living 	more ...
nn 	nno 	nno 	Norwegian Nynorsk 	Individual 	Living 	more ...
no 	nor 	nor 	Norwegian 	Macrolanguage 	Living 	more ...
nr 	nbl 	nbl 	South Ndebele 	Individual 	Living 	more ...
nv 	nav 	nav 	Navajo 	Individual 	Living 	more ...
ny 	nya 	nya 	Nyanja 	Individual 	Living 	more ...
oc 	oci 	oci 	Occitan (post 1500) 	Individual 	Living 	more ...
oj 	oji 	oji 	Ojibwa 	Macrolanguage 	Living 	more ...
om 	orm 	orm 	Oromo 	Macrolanguage 	Living 	more ...
or 	ori 	ori 	Oriya (macrolanguage) 	Macrolanguage 	Living 	more ...
os 	oss 	oss 	Ossetian 	Individual 	Living 	more ...
pa 	pan 	pan 	Panjabi 	Individual 	Living 	more ...
pi 	pli 	pli 	Pali 	Individual 	Ancient 	more ...
pl 	pol 	pol 	Polish 	Individual 	Living 	more ...
ps 	pus 	pus 	Pushto 	Macrolanguage 	Living 	more ...
pt 	por 	por 	Portuguese 	Individual 	Living 	more ...
qu 	que 	que 	Quechua 	Macrolanguage 	Living 	more ...
rm 	roh 	roh 	Romansh 	Individual 	Living 	more ...
rn 	run 	run 	Rundi 	Individual 	Living 	more ...
ro 	ron / rum*  	ron 	Romanian 	Individual 	Living 	more ...
ru 	rus 	rus 	Russian 	Individual 	Living 	more ...
rw 	kin 	kin 	Kinyarwanda 	Individual 	Living 	more ...
sa 	san 	san 	Sanskrit 	Individual 	Ancient 	more ...
sc 	srd 	srd 	Sardinian 	Macrolanguage 	Living 	more ...
sd 	snd 	snd 	Sindhi 	Individual 	Living 	more ...
se 	sme 	sme 	Northern Sami 	Individual 	Living 	more ...
sg 	sag 	sag 	Sango 	Individual 	Living 	more ...
sh (deprecated) 	- 	hbs 	Serbo-Croatian 	Macrolanguage 	Living 	more ...
si 	sin 	sin 	Sinhala 	Individual 	Living 	more ...
sk 	slk / slo*  	slk 	Slovak 	Individual 	Living 	more ...
sl 	slv 	slv 	Slovenian 	Individual 	Living 	more ...
sm 	smo 	smo 	Samoan 	Individual 	Living 	more ...
sn 	sna 	sna 	Shona 	Individual 	Living 	more ...
so 	som 	som 	Somali 	Individual 	Living 	more ...
sq 	sqi / alb*  	sqi 	Albanian 	Macrolanguage 	Living 	more ...
sr 	srp 	srp 	Serbian 	Individual 	Living 	more ...
ss 	ssw 	ssw 	Swati 	Individual 	Living 	more ...
st 	sot 	sot 	Southern Sotho 	Individual 	Living 	more ...
su 	sun 	sun 	Sundanese 	Individual 	Living 	more ...
sv 	swe 	swe 	Swedish 	Individual 	Living 	more ...
sw 	swa 	swa 	Swahili (macrolanguage) 	Macrolanguage 	Living 	more ...
ta 	tam 	tam 	Tamil 	Individual 	Living 	more ...
te 	tel 	tel 	Telugu 	Individual 	Living 	more ...
tg 	tgk 	tgk 	Tajik 	Individual 	Living 	more ...
th 	tha 	tha 	Thai 	Individual 	Living 	more ...
ti 	tir 	tir 	Tigrinya 	Individual 	Living 	more ...
tk 	tuk 	tuk 	Turkmen 	Individual 	Living 	more ...
tl 	tgl 	tgl 	Tagalog 	Individual 	Living 	more ...
tn 	tsn 	tsn 	Tswana 	Individual 	Living 	more ...
to 	ton 	ton 	Tonga (Tonga Islands) 	Individual 	Living 	more ...
tr 	tur 	tur 	Turkish 	Individual 	Living 	more ...
ts 	tso 	tso 	Tsonga 	Individual 	Living 	more ...
tt 	tat 	tat 	Tatar 	Individual 	Living 	more ...
tw 	twi 	twi 	Twi 	Individual 	Living 	more ...
ty 	tah 	tah 	Tahitian 	Individual 	Living 	more ...
ug 	uig 	uig 	Uighur 	Individual 	Living 	more ...
uk 	ukr 	ukr 	Ukrainian 	Individual 	Living 	more ...
ur 	urd 	urd 	Urdu 	Individual 	Living 	more ...
uz 	uzb 	uzb 	Uzbek 	Macrolanguage 	Living 	more ...
ve 	ven 	ven 	Venda 	Individual 	Living 	more ...
vi 	vie 	vie 	Vietnamese 	Individual 	Living 	more ...
vo 	vol 	vol 	Volapük 	Individual 	Constructed 	more ...
wa 	wln 	wln 	Walloon 	Individual 	Living 	more ...
wo 	wol 	wol 	Wolof 	Individual 	Living 	more ...
xh 	xho 	xho 	Xhosa 	Individual 	Living 	more ...
yi 	yid 	yid 	Yiddish 	Macrolanguage 	Living 	more ...
yo 	yor 	yor 	Yoruba 	Individual 	Living 	more ...
za 	zha 	zha 	Zhuang 	Macrolanguage 	Living 	more ...
zh 	zho / chi*  	zho 	Chinese 	Macrolanguage 	Living 	more ...
zu 	zul 	zul 	Zulu 	Individual 	Living 	more ..."""

# from http://meta.wikimedia.org/wiki/Special_language_codes and http://meta.wikimedia.org/wiki/List_of_Wikipedias
wikispecialcodes = """als gsw
bat-smg sgs
bat_smg sgs
cbk-zam cbk
cbk_zam cbk
fiu-vro vro
fiu_vro vro
roa-rup rup
roa_rup rup
sh hbs
zh-classical lzh
zh_classical lzh
zh-min-nan nan
zh_min_nan nan
zh-yue yue
zh_yue yue
nrm None
no nob""" # Norwegian Bokmal instaead of general Norwegian
#simple en
#mo ron
#map-bms jv
#map_bms jv

iso6395 = """aka  Akan  fat  Fanti
   twi  Twi
ara  Arabic  aao  Algerian Saharan Arabic
   abh  Tajiki Arabic
   abv  Baharna Arabic
   acm  Mesopotamian Arabic
   acq  Ta'izzi-Adeni Arabic
   acw  Hijazi Arabic
   acx  Omani Arabic
   acy  Cypriot Arabic
   adf  Dhofari Arabic
   aeb  Tunisian Arabic
   aec  Saidi Arabic
   afb  Gulf Arabic
   ajp  South Levantine Arabic
   apc  North Levantine Arabic
   apd  Sudanese Arabic
   arb  Standard Arabic
   arq  Algerian Arabic
   ars  Najdi Arabic
   ary  Moroccan Arabic
   arz  Egyptian Arabic
   auz  Uzbeki Arabic
   avl  Eastern Egyptian Bedawi Arabic
   ayh  Hadrami Arabic
   ayl  Libyan Arabic
   ayn  Sanaani Arabic
   ayp  North Mesopotamian Arabic
   bbz  Babalia Creole Arabic
   pga  Sudanese Creole Arabic
   shu  Chadian Arabic
   ssh  Shihhi Arabic
aym  Aymara  ayc  Southern Aymara
   ayr  Central Aymara
aze  Azerbaijani  azb  South Azerbaijani
   azj  North Azerbaijani
bal  Baluchi  bcc  Southern Balochi
   bgn  Western Balochi
   bgp  Eastern Balochi
bik  Bikol  bcl  Central Bikol
   bhk  Albay Bicolano  (Retired 1/15/2010)
   bln  Southern Catanduanes Bikol
   bto  Rinconada Bikol
   cts  Northern Catanduanes Bikol
   fbl  West Albay Bikol
   lbl  Libon Bikol
   rbl  Miraya Bikol
   ubl  Buhi'non Bikol
bnc  Bontok  ebk  Eastern Bontok
   lbk  Central Bontok
   obk  Southern Bontok
   rbk  Northern Bontok
   vbk  Southwestern Bontok
bua  Buriat  bxm  Mongolia Buriat
   bxr  Russia Buriat
   bxu  China Buriat
chm  Mari (Russia)  mhr  Eastern Mari
   mrj  Western Mari
cre  Cree  crj  Southern East Cree
   crk  Plains Cree
   crl  Northern East Cree
   crm  Moose Cree
   csw  Swampy Cree
   cwd  Woods Cree
del  Delaware  umu  Munsee
   unm  Unami
den  Slave (Athapascan)  scs  North Slavey
   xsl  South Slavey
din  Dinka  dib  South Central Dinka
   dik  Southwestern Dinka
   dip  Northeastern Dinka
   diw  Northwestern Dinka
   dks  Southeastern Dinka
doi  Dogri (macrolanguage)  dgo  Dogri (individual language)
   xnr  Kangri
est  Estonian  ekk  Standard Estonian
   vro  Võro
fas  Persian  pes  Iranian Persian
   prs  Dari
ful  Fulah  ffm  Maasina Fulfulde
   fub  Adamawa Fulfulde
   fuc  Pulaar
   fue  Borgu Fulfulde
   fuf  Pular
   fuh  Western Niger Fulfulde
   fui  Bagirmi Fulfulde
   fuq  Central-Eastern Niger Fulfulde
   fuv  Nigerian Fulfulde
gba  Gbaya (Central African Republic)  bdt  Bokoto
   gbp  Gbaya-Bossangoa
   gbq  Gbaya-Bozoum
   gmm  Gbaya-Mbodomo
   gso  Southwest Gbaya
   gya  Northwest Gbaya
   mdo  Southwest Gbaya  (Retired 1/14/2008)
gon  Gondi  ggo  Southern Gondi
   gno  Northern Gondi
grb  Grebo  gbo  Northern Grebo
   gec  Gboloo Grebo
   grj  Southern Grebo
   grv  Central Grebo
   gry  Barclayville Grebo
grn  Guarani  gnw  Western Bolivian Guaraní
   gug  Paraguayan Guaraní
   gui  Eastern Bolivian Guaraní
   gun  Mbyá Guaraní
   nhd  Chiripá
hai  Haida  hax  Southern Haida
   hdn  Northern Haida
hbs  Serbo-Croatian  bos  Bosnian
   hrv  Croatian
   srp  Serbian
hmn  Hmong  blu  Hmong Njua  (Retired 1/14/2008)
   cqd  Chuanqiandian Cluster Miao
   hea  Northern Qiandong Miao
   hma  Southern Mashan Hmong
   hmc  Central Huishui Hmong
   hmd  Large Flowery Miao
   hme  Eastern Huishui Hmong
   hmg  Southwestern Guiyang Hmong
   hmh  Southwestern Huishui Hmong
   hmi  Northern Huishui Hmong
   hmj  Ge
   hml  Luopohe Hmong
   hmm  Central Mashan Hmong
   hmp  Northern Mashan Hmong
   hmq  Eastern Qiandong Miao
   hms  Southern Qiandong Miao
   hmw  Western Mashan Hmong
   hmy  Southern Guiyang Hmong
   hmz  Hmong Shua
   hnj  Hmong Njua
   hrm  Horned Miao
   huj  Northern Guiyang Hmong
   mmr  Western Xiangxi Miao
   muq  Eastern Xiangxi Miao
   mww  Hmong Daw
   sfm  Small Flowery Miao
iku  Inuktitut  ike  Eastern Canadian Inuktitut
   ikt  Inuinnaqtun
ipk  Inupiaq  esi  North Alaskan Inupiatun
   esk  Northwest Alaska Inupiatun
jrb  Judeo-Arabic  ajt  Judeo-Tunisian Arabic
   aju  Judeo-Moroccan Arabic
   jye  Judeo-Yemeni Arabic
   yhd  Judeo-Iraqi Arabic
   yud  Judeo-Tripolitanian Arabic
kau  Kanuri  kby  Manga Kanuri
   knc  Central Kanuri
   krt  Tumari Kanuri
kln  Kalenjin  enb  Markweeta
   eyo  Keiyo
   niq  Nandi
   oki  Okiek
   pko  Pökoot
   sgc  Kipsigis
   spy  Sabaot
   tec  Terik
   tuy  Tugen
kok  Konkani (macrolanguage)  gom  Goan Konkani
   knn  Konkani (individual language)
kom  Komi  koi  Komi-Permyak
   kpv  Komi-Zyrian
kon  Kongo  kng  Koongo
   kwy  San Salvador Kongo
   ldi  Laari
kpe  Kpelle  gkp  Guinea Kpelle
   xpe  Liberia Kpelle
kur  Kurdish  ckb  Central Kurdish
   kmr  Northern Kurdish
   sdh  Southern Kurdish
lah  Lahnda  hnd  Southern Hindko
   hno  Northern Hindko
   jat  Jakati
   phr  Pahari-Potwari
   pmu  Mirpur Panjabi
   pnb  Western Panjabi
   skr  Seraiki
   xhe  Khetrani
lav  Latvian  ltg  Latgalian
   lvs  Standard Latvian
luy  Luyia  bxk  Bukusu
   ida  Idakho-Isukha-Tiriki
   lkb  Kabras
   lko  Khayo
   lks  Kisa
   lri  Marachi
   lrm  Marama
   lsm  Saamia
   lto  Tsotso
   lts  Tachoni
   lwg  Wanga
   nle  East Nyala
   nyd  Nyore
   rag  Logooli
man  Mandingo  emk  Eastern Maninkakan
   mku  Konyanka Maninka
   mlq  Western Maninkakan
   mnk  Mandinka
   msc  Sankaran Maninka
   mwk  Kita Maninkakan
   myq  Forest Maninka  (Retired )
mlg  Malagasy  bhr  Bara Malagasy
   bjq  Southern Betsimisaraka Malagasy  (Retired )
   bmm  Northern Betsimisaraka Malagasy
   bzc  Southern Betsimisaraka Malagasy
   msh  Masikoro Malagasy
   plt  Plateau Malagasy
   skg  Sakalava Malagasy
   tdx  Tandroy-Mahafaly Malagasy
   tkg  Tesaka Malagasy
   txy  Tanosy Malagasy
   xmv  Antankarana Malagasy
   xmw  Tsimihety Malagasy
mon  Mongolian  khk  Halh Mongolian
   mvf  Peripheral Mongolian
msa  Malay (macrolanguage)  bjn  Banjar
   btj  Bacanese Malay
   bve  Berau Malay
   bvu  Bukit Malay
   coa  Cocos Islands Malay
   dup  Duano
   hji  Haji
   ind  Indonesian
   jak  Jakun
   jax  Jambi Malay
   kvb  Kubu
   kvr  Kerinci
   kxd  Brunei
   lce  Loncong
   lcf  Lubu
   liw  Col
   max  North Moluccan Malay
   meo  Kedah Malay
   mfa  Pattani Malay
   mfb  Bangka
   min  Minangkabau
   mly  Malay (individual language)  (Retired 2/18/2008)
   mqg  Kota Bangun Kutai Malay
   msi  Sabah Malay
   mui  Musi
   orn  Orang Kanaq
   ors  Orang Seletar
   pel  Pekal
   pse  Central Malay
   tmw  Temuan
   urk  Urak Lawoi'
   vkk  Kaur
   vkt  Tenggarong Kutai Malay
   xmm  Manado Malay
   zlm  Malay (individual language)
   zmi  Negeri Sembilan Malay
   zsm  Standard Malay
mwr  Marwari  dhd  Dhundari
   mtr  Mewari
   mve  Marwari (Pakistan)
   rwr  Marwari (India)
   swv  Shekhawati
   wry  Merwari
nep  Nepali (macrolanguage)  dty  Dotyali
   npi  Nepali (individual language)
nor  Norwegian  nno  Norwegian Nynorsk
   nob  Norwegian Bokmål
oji  Ojibwa  ciw  Chippewa
   ojb  Northwestern Ojibwa
   ojc  Central Ojibwa
   ojg  Eastern Ojibwa
   ojs  Severn Ojibwa
   ojw  Western Ojibwa
   otw  Ottawa
ori  Oriya (macrolanguage)  ory  Oriya (individual language)
   spv  Sambalpuri
orm  Oromo  gax  Borana-Arsi-Guji Oromo
   gaz  West Central Oromo
   hae  Eastern Oromo
   orc  Orma
pus  Pushto  pbt  Southern Pashto
   pbu  Northern Pashto
   pst  Central Pashto
que  Quechua  cqu  Chilean Quechua
   qub  Huallaga Huánuco Quechua
   qud  Calderón Highland Quichua
   quf  Lambayeque Quechua
   qug  Chimborazo Highland Quichua
   quh  South Bolivian Quechua
   quk  Chachapoyas Quechua
   qul  North Bolivian Quechua
   qup  Southern Pastaza Quechua
   qur  Yanahuanca Pasco Quechua
   qus  Santiago del Estero Quichua
   quw  Tena Lowland Quichua
   qux  Yauyos Quechua
   quy  Ayacucho Quechua
   quz  Cusco Quechua
   qva  Ambo-Pasco Quechua
   qvc  Cajamarca Quechua
   qve  Eastern Apurímac Quechua
   qvh  Huamalíes-Dos de Mayo Huánuco Quechua
   qvi  Imbabura Highland Quichua
   qvj  Loja Highland Quichua
   qvl  Cajatambo North Lima Quechua
   qvm  Margos-Yarowilca-Lauricocha Quechua
   qvn  North Junín Quechua
   qvo  Napo Lowland Quechua
   qvp  Pacaraos Quechua
   qvs  San Martín Quechua
   qvw  Huaylla Wanca Quechua
   qvz  Northern Pastaza Quichua
   qwa  Corongo Ancash Quechua
   qwc  Classical Quechua
   qwh  Huaylas Ancash Quechua
   qws  Sihuas Ancash Quechua
   qxa  Chiquián Ancash Quechua
   qxc  Chincha Quechua
   qxh  Panao Huánuco Quechua
   qxl  Salasaca Highland Quichua
   qxn  Northern Conchucos Ancash Quechua
   qxo  Southern Conchucos Ancash Quechua
   qxp  Puno Quechua
   qxr  Cañar Highland Quichua
   qxt  Santa Ana de Tusi Pasco Quechua
   qxu  Arequipa-La Unión Quechua
   qxw  Jauja Wanca Quechua
raj  Rajasthani  bgq  Bagri
   gda  Gade Lohar
   gju  Gujari
   hoj  Hadothi
   mup  Malvi
   wbr  Wagdi
rom  Romany  rmc  Carpathian Romani
   rmf  Kalo Finnish Romani
   rml  Baltic Romani
   rmn  Balkan Romani
   rmo  Sinte Romani
   rmw  Welsh Romani
   rmy  Vlax Romani
sqi  Albanian  aae  Arbëreshë Albanian
   aat  Arvanitika Albanian
   aln  Gheg Albanian
   als  Tosk Albanian
srd  Sardinian  sdc  Sassarese Sardinian
   sdn  Gallurese Sardinian
   src  Logudorese Sardinian
   sro  Campidanese Sardinian
swa  Swahili (macrolanguage)  swc  Congo Swahili
   swh  Swahili (individual language)
syr  Syriac  aii  Assyrian Neo-Aramaic
   cld  Chaldean Neo-Aramaic
tmh  Tamashek  taq  Tamasheq
   thv  Tahaggart Tamahaq
   thz  Tayart Tamajeq
   ttq  Tawallammat Tamajaq
uzb  Uzbek  uzn  Northern Uzbek
   uzs  Southern Uzbek
yid  Yiddish  ydd  Eastern Yiddish
   yih  Western Yiddish
zap  Zapotec  zaa  Sierra de Juárez Zapotec
   zab  San Juan Guelavía Zapotec
   zac  Ocotlán Zapotec
   zad  Cajonos Zapotec
   zae  Yareni Zapotec
   zaf  Ayoquesco Zapotec
   zai  Isthmus Zapotec
   zam  Miahuatlán Zapotec
   zao  Ozolotepec Zapotec
   zaq  Aloápam Zapotec
   zar  Rincón Zapotec
   zas  Santo Domingo Albarradas Zapotec
   zat  Tabaa Zapotec
   zav  Yatzachi Zapotec
   zaw  Mitla Zapotec
   zax  Xadani Zapotec
   zca  Coatecas Altas Zapotec
   zoo  Asunción Mixtepec Zapotec
   zpa  Lachiguiri Zapotec
   zpb  Yautepec Zapotec
   zpc  Choapan Zapotec
   zpd  Southeastern Ixtlán Zapotec
   zpe  Petapa Zapotec
   zpf  San Pedro Quiatoni Zapotec
   zpg  Guevea De Humboldt Zapotec
   zph  Totomachapan Zapotec
   zpi  Santa María Quiegolani Zapotec
   zpj  Quiavicuzas Zapotec
   zpk  Tlacolulita Zapotec
   zpl  Lachixío Zapotec
   zpm  Mixtepec Zapotec
   zpn  Santa Inés Yatzechi Zapotec
   zpo  Amatlán Zapotec
   zpp  El Alto Zapotec
   zpq  Zoogocho Zapotec
   zpr  Santiago Xanica Zapotec
   zps  Coatlán Zapotec
   zpt  San Vicente Coatlán Zapotec
   zpu  Yalálag Zapotec
   zpv  Chichicapan Zapotec
   zpw  Zaniza Zapotec
   zpx  San Baltazar Loxicha Zapotec
   zpy  Mazaltepec Zapotec
   zpz  Texmelucan Zapotec
   zsr  Southern Rincon Zapotec
   ztc  Lachirioag Zapotec  (Retired 7/18/2007)
   zte  Elotepec Zapotec
   ztg  Xanaguía Zapotec
   ztl  Lapaguía-Guivini Zapotec
   ztm  San Agustín Mixtepec Zapotec
   ztn  Santa Catarina Albarradas Zapotec
   ztp  Loxicha Zapotec
   ztq  Quioquitani-Quierí Zapotec
   zts  Tilquiapan Zapotec
   ztt  Tejalapan Zapotec
   ztu  Güilá Zapotec
   ztx  Zaachila Zapotec
   zty  Yatee Zapotec
zha  Zhuang  ccx  Northern Zhuang  (Retired 1/14/2008)
   ccy  Southern Zhuang  (Retired 7/18/2007)
   zch  Central Hongshuihe Zhuang
   zeh  Eastern Hongshuihe Zhuang
   zgb  Guibei Zhuang
   zgm  Minz Zhuang
   zgn  Guibian Zhuang
   zhd  Dai Zhuang
   zhn  Nong Zhuang
   zlj  Liujiang Zhuang
   zln  Lianshan Zhuang
   zlq  Liuqian Zhuang
   zqe  Qiubei Zhuang
   zyb  Yongbei Zhuang
   zyg  Yang Zhuang
   zyj  Youjiang Zhuang
   zyn  Yongnan Zhuang
   zzj  Zuojiang Zhuang
zho  Chinese  cdo  Min Dong Chinese
   cjy  Jinyu Chinese
   cmn  Mandarin Chinese
   cpx  Pu-Xian Chinese
   czh  Huizhou Chinese
   czo  Min Zhong Chinese
   gan  Gan Chinese
   hak  Hakka Chinese
   hsn  Xiang Chinese
   lzh  Literary Chinese
   mnp  Min Bei Chinese
   nan  Min Nan Chinese
   wuu  Wu Chinese
   yue  Yue Chinese
zza  Zaza  diq  Dimli (individual language)
   kiu  Kirmanjki (individual language)""" 

# extracted from .wpdownload from the wp-download tool (https://github.com/babilen/wp-download), manually added missing ones
listofwikicodes = """aa
ab
ace
af
ak
als
am
an
ang
ar
arc
arz
as
ast
av
ay
az
ba
bar
bat_smg
bcl
be
be_x_old
bg
bh
bi
bjn
bm
bn
bo
bpy
br
bs
bug
bxr
ca
cbk_zam
cdo
ce
ceb
ch
cho
chr
chy
ckb
co
cr
crh
cs
csb
cu
cv
cy
da
de
diq
dsb
dv
dz
ee
el
eml
en
eo
es
et
eu
ext
fa
ff
fi
fiu_vro
fj
fo
fr
frp
frr
fur
fy
ga
gag
gan
gd
gl
glk
gn
got
gu
gv
ha
hak
haw
he
hi
hif
ho
hr
hsb
ht
hu
hy
hz
ia
id
ie
ig
ii
ik
ilo
io
is
it
iu
ja
jbo
jv
ka
kaa
kab
kbd
kg
ki
kj
kk
kl
km
kn
ko
koi
kr
krc
ks
ksh
ku
kv
kw
ky
la
lad
lb
lbe
lez
lg
li
lij
lmo
ln
lo
lt
ltg
lv
map_bms
mdf
mg
mh
mhr
mi
min
mk
ml
mn
mo
mr
mrj
ms
mt
mus
mwl
my
myv
mzn
na
nah
nap
nds
nds_nl
ne
new
ng
nl
nn
no
nov
nrm
nso
nv
ny
oc
om
or
os
pa
pag
pam
pap
pcd
pdc
pfl
pi
pih
pl
pms
pnb
pnt
ps
pt
qu
rm
rmy
rn
ro
roa_rup
roa_tara
ru
rue
rw
sa
sah
sc
scn
sco
sd
se
sg
sh
si
simple
sk
sl
sm
sn
so
sq
sr
srn
ss
st
stq
su
sv
sw
szl
ta
te
tet
tg
th
ti
tk
tl
tn
to
tokipona
tpi
tr
ts
tt
tum
tw
ty
tyv
udm
ug
uk
ur
uz
ve
vec
vep
vi
vls
vo
wa
war
wo
wuu
xal
xh
xmf
yi
yo
za
zea
zh
zh_classical
zh_min_nan
zh_yue
zu"""



def isiso(code):
  '''Check whether a code is an iso-696-3 code.'''
  for line in iso6963.split('\n'):
    if code == line.split(' ')[0].strip():
        return True         
  return False


def wikicode2iso(wikicode):
    '''
    Given a wikipedia language code return its corresponding iso-6393 code.
    Check whether the code is an iso-639-1 code (see isomapping) or appears
    in the list of special codes (wikispecialcodes). Else check whether it 
    already is an iso-639-3 code.
    Note: No iso-639-3 codes are found for be-x-old, nds-nl, nah, roa-tara,
    eml and simple.
    '''
    wikicode = wikicode.split()[0]
    for i in wikispecialcodes.split('\n'):
        if wikicode == i.split(' ')[0]:
            return i.split(' ')[1]
    for i in isomapping.split('\n'):
        if wikicode == i.split(' 	')[0] and i.split(' 	')[2].lower() != '-':
            return i.split(' 	')[2].lower()
    if isiso(wikicode):
        return wikicode
    else:
        return None


WIKI2ISO = dict()
for i in listofwikicodes.split('\n'):
  wikicode = i
  WIKI2ISO[wikicode] = wikicode2iso(wikicode)


'''
# print all wikipedia language codes and their corresponding iso-6393 code
l = WIKI2ISO.keys()
l.sort()
for key in l:
  print(key + ' ' + str(WIKI2ISO[key]))
'''

#print(WIKI2ISO['aa'])
#print(wikicode2iso('aa'))

