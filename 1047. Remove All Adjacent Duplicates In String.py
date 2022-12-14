class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 0:
            return ""

        ans = []
        for i in s:
            if len(ans) > 0:
                if i == ans[-1]:
                    ans.pop()
                else: 
                    ans.append(i)
            else:
                ans.append(i)
        
        out = ""
        for i in ans:
            out = out + i
        return out
        
"""
        s_split = [*s]
        i = 1
        while s_split:
            dupe = False
            if len(s_split)==1:
                return s_split[0]

            if len(s_split)<=2:
                if s_split[0] == s_split[1]:
                    return ""
                else:
                    return s_split[0]+s_split[1]

            
            if len(s_split)-1>i:
                if s_split[i] == s_split[i+1]:
                    s_split = s_split[0:i] + s_split[i+2:]
                    dupe = True
            else:
                ans = ""
                for i in s_split:
                    ans += i
                return ans
            
            if not dupe:
                i+=1
            else: i = 0


        ans = ""
        for i in s_split:
            ans += i
        return ans
"""

"""class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        i = 0
        for i in s:
            if len(ans) > 0:
                if i == ans[-1]:
                    ans.pop()
                else:
                    ans.append(i)
            else:
                ans.append(i)
        return ''.join(ans)"""


tester = Solution()

test = "azxxzy"
#test = "jtiddfcbmreobbnjocmbtmjrngkmomorrscfbsboqtfmljrdnqkmjehfoejdtmhimbpsihsdlcdgarqpnraepdbhcjociljjoaakrjbhtbmndefpkqqbabgplmrgljpflhqslpgmlocanmoeierinmlbphpbgqpahhtjaofqhabiorfstpqekhrqqnhknntbdgktgfcmihmmsalieqqooqkoqsrnotqcnfamnrqpmphhajntjtnecedjcocdhphjticnpnrlficibpbteteickaoofchaigtmmpjosdscstimdmqmsnrjgfqfpqfdqoeapqjclhrtbtfgaogrdgaarsrreqfghotdsddmrsmqrmkhcdihonikpslaesinoibnghjeishjkjqstcdlhkfflphfplrrapldbsccdifomhfaendlsihkgpnerheckpgpnedncqpedfljmtqjhdtapaabsbgqahfhajhosorotqrjihkaoambhqgigfosjbgsickehkptmgqptoqatkcofqjgjlebohtmlkaqmtmncgddpfhnkgfcgbcrmmamkgonpkgobtkiokgpiohmplstknidjidrrslkhnlsmmdggsbflkqdsfmomnfdbgqknpmjcaldoqqapkjbdfjahfhsaadbegthdbteosoksfepgtmrjhhkdcablelbtnnbcqjccdjkfajcjbndresjafkijefemcbqtmgdfmdisnnfjgblghcblffofhbibfldrnslnemmganmliohmchsesbqtpclehdescqtberfijfdbppnrqeaeflkikjmgpkaofojndrrsmadjsqncqcinbstikgpeklkoastrbqnqrisrjcnrlbfrdoiojrqrpcareamrhketqpgljqkkkbtgkmbherpehhtqkoirmiatiksbjopmlrgrkpgcdmnlqtcdmotjffrllmgjcqsqtsolmdoqcaienjsflrbrrnfphhofdhergilgdififccjtotctthrbbsefnlpncfealgiqdrhhncrjmiphqtrpqqkfhtokfqbahsispmbspatijoibidnoknmebaonnssedojrqgafsnbgqjeassrdphdeorodnsoheabodjddphggcaqhlefeqgcrigqofjhakigiddifsqkroqlqtnrfqajbbhlkbdrbnekqiahessbcinknjskrdhktcmlgsqbmebqfgjbsipkomgmqlrkibhlhgcactdhsfiieckomagtadisplacldbqipdglmnktcmoatdbgcttqlplpokofancihnnasfhlajbjjdtmgtchhoimihhknpqbplnndmjcclhemdhnheqeecbketppqgpidbghnsiecgpenpjtpirmahjilomeptondlqjipknglnnpkdbeorckmqmnnmtgggackligoqjtafipfggccmssgtfgtigdctbrqltjhnpndtjdtjmhmhffassotfneqemmhiljqorpptcfnnrbqmcseenilcpahobhscletgbcajnqdncclmsrqneosgmdqiebbndmqtaskfkjbthldtisqsmsfdjohgmemkiqnnplrpmdsdmdsrmsrtbmkhreantglpbaerersptsdsfbpptaphhghebrobhihbcbsseptsmotlkaopqmsdcgobefcbfndqiccnhlccotldhbhgqhjccrrrobtcshgftprcqlsioodciahfgtrrpplsmmoteqoofmkenphmtshtiimstkbtnmbljstnardjbkterfklraghjdaggmgrphjmsmfmkkheqicjldjtnperrlggdhahdbffknfpckdjmcthfosfchlfjbcqcfkltohsffdghpqcijihnolkbefbkqqonggqncfceqksllfnneprepgercposcitrijqdbsdshqkfpbmolqmomorksidcftcmrktkccmmfotqkpragaratidnpnjkkhjnalksonrnsljncakkclttocmfsklkfssffmntnqsbtrtnrrfjgntgcsgtookfkdhtbhtjdgpfdmksqtjlkjfmsspgpkbnmotidkrlpgnikknrheodpmmbtandngomeagthkoptoclqficrsdkarmictkeijbesltescdenrpjorfjeqskbkktbprebaptkeeqghlfsamphljcscchgarmebfadlatemasrjopbffitttmajdmecgbrpaopbtctspkplshaspipbqnopffggrisprodhmbeonbkcbpjfqifelmtgmlajnsmamtraailaopirhqfqrpdncqabmjtshllfbbqcddingliorklscnfqfgblrlgsgtlfdnnsarcpbjhpofnpepfentktlcfjscdbeslhiakilnaeprjqrqbcbrtksrmpnmqstfspopmhmetpebmplrrrkjdfgnmliqgbeagdlbmmmcermpgcqbhhaddfpnenoqffdkmhgqgltglbhbpqsnjoshhafoehbkebijpsigbqrifjobkrdekoiidaadqtjarphftbaikasqbcjberjgoqdediiqfktmktaoaddkrfdliitgfqkmkmpogbcokpoletpblreaonknjobbbkenffdrbjamplhjgbfodtqkilarljgiqmoktjmhifdonsrcotmpiblqapbdjmhirrpcebjopoljthngsdbplcicprcaiqtinnnrfahlnprrflhjtaahpshikcnpsbtcaahqjajcdetmicshnkonapbniihqsdgnosrgqoqtrnhnktddtnjrgdcddjreffbbodcednpktsprbpbplkgfspjmeefcjmlfbqiffktpiqrgnfirddoepclnpnfdmtjcphgfsniccrdimtchmgddfrllqipobdcjacmfcrjslltjetmdbsoejqsihffibetqqaseglgberdqabmompidgotjdnceljqagratflefmpjkfscqdfpcmqtcjkrgdtqftksflmtabjprjccbdjnahcrsrkapjsappbasrtkirihfojobifagedktkqogcrdkoesdcqrgnomqigjislcosenasmsdrbjctcqpcsksbrrnbgfsqskerjdedcglskdoagcdjgcafqirdbgkhgtlcnlbshrofefqptbsqmpeipikbgbohlddmrgrlbhslsgkaodistjopkbqagnaibbflbabnctbdadgnibgpqlccbhokiirjjamliqokndtrltsqghaipglnjsijflstfkmrphkmcshkddhlgniptgthasdebmjtposegeserefjmojikqmkbfabqggatdhckeriidsjhjccnrahngerfcqmqijqftilsasfgfnrsjjopmmoirpccdrfatfaqnmmaoqalsfgmahpkgjdjlfhjiqtaejapeodkfaebrjbaotlrpchnfparsbinnojmrmgoljgrdqgstfcfmjcjqqtmnaobhtsitnbshlqclaeologsfbaikfcdibcckndgpmsinpmocljepfblrjekfqibpmtdkdfpegdhfmfklcljrdobaghhtafqheaqdrodhertetqntnddsdgpenfdstknqpirniejtmifitqjsiqaorlskqcdfrctbaqsflhsflihoqrdthatjclsiekrpobllgmenknobnipsthcocbimoslkripcttbbgeccgeqcsreahgeenipntoqltfafenraidhfhhrmktgmmdgnqrjklfcqnbaehsghnobiptraegjplslmceijsoemnitglcftlnlrbdlkcgjdirqbreklhbpmgrfjjsbpteockhentcdnssnbtksnkhladntahflaapmiqhanghbcjqbijsibedeloaqtnldgejlateomijjajtsfhiqnmfjfropgcaaisdsfneptsmobtqjjspshkskdftkjsbhcfbqgfosrcdahdfrlirprhanacknejfmnpdtfqlbhrptleqeegmjggsioeakhemgfkatqefnileegsbohhqsnebmolfgklhoftrojrlrbqgjpohfnfhbqalactbcbnnajlcglnrpjtneftshnhdssdcnkqtbagstcidjfhiagomesjkmmqorkabhjfelhhsqqdanfagaiiejebtoscslsprraariglolsqmngofsiqftfcktsldorjmqsllmfsbtromnebfpkmlkifcdqqpepfjaaindjfpnidqklironsolnnedfcqiqiaarfrkilfrekeshdfanljelhgprpdceesrcdfahbncqchpdpjbptfhqnottqqchqsloksjlsfjffhhjdjblgglpgloqelnbgqrgspfctnclbkaqhspmmdqelgbdnlbccaifttmrtlmqpmsqitldnsgdpsaiccecqleerjkbgnehmdpjbjtdfnkelhkbtobjjmqdqcimbhrgcjaatkrnarglbfmhltmlndbjpgmilpenkmkhbakaboeimjbrpdnilnkoijqlmdjjtsllacrjsdllngtiaeqalfelfcdtrkmsptbitbthnjhqleppilopkplmiofskeqhbfpksmehpjmlhleiaibjddpqpjocrgknmocbophameoaemqpithtgshihddbftntctegcsjpbrolccmnidllqhmtapkjdpccnqcpsksamddegbhreoboekbkcpnfbsbnljffpbjgsfmphssqaofjpqaqbrlmcbcncjafjgtfcelbcajotqqgeegsfseeplmfhrhbgcqsoeqactqklpigpscprjmipmtggbccjphfjmjnlpcrprdkjgcatemmprblhfjbtafjorhfcblgkqeejnhqfromcnmrkfficfskpitogirfnjpomsiqbbaqfijtheqrgtfcscejmmsmihaojnsqfinqckhcrhmsnjtsqkodpcleqihobcbdosjdempoksanodtrrlrshrledsbmdcmfacilqjrgmjmjsrhefifqnbdnroagtinppnklmbaobpafdabsmgsdaslsamohsnnbttqhafjhpffpjdjncbnrbfgadecophdkaaimtaiblhfkooandaqidnbscfirkeroktiincilfbsjrokptffkokqommiletppbndaglscbppslkpgnctsdjcmlftejbpcesrqqikrpmqmsckthqsdsnqfnqlltrdbnkseeelnhjjpkgaslcdhjcgjdjoontdicbdaatcnrgstsdqclcerkedlbdpaehrcakoftkdkahimcelhjkpmnqqhtpsjcspatgnjclnholfbtjnoghlcjjqkjfhnccnkpfpjmebfjqtiitotkbmcktfetftajsfpipqkrrgtlqranajffmoqfgjergicstjlciiksakckahntgobpdnmntqtlnilspnhnhpohpsohlrhbfdgalrckjhimcghebgsjngposncopqpehgjhmdsffsmonkgafmjbktlotrglsopdsajcskeonjktgqaleditjqaieppkbjatkihtncqplhpfamjmfcgbaiekatfllaohbpkqmhkdsnssqhkmegmrrdnplmhnslnlnrppmrgppcalkhncrsjbjsnastocqcfafffffqinrdeiskhljqjgqpoiatbisftjnqfgcbqqmitjdtqbdkkqjqlmbjqnafjgoohcncsraffckobltijhktpdbrjdofiatognqbttfrfdldaospilrgejrcrtlerhibgtmbjpafhtchcmollilqrheodfrmksflmensjmriaidiqbftkbtckicgnbomajddehsjpogpiefimatflqhkdnarltkjamjobkfimsfksrjgqbtknpnbhffrgdtfaqlaatmbgdnmlblcgnabkasaeerhbndsorgeqaigsscgkntqahbiobskfdesnfhkenjpnhffnkfeirrmeltishqhcfhlgcphmhmjrrcnfhqfqbepmkaeotkdlpfohopirqhfboqhegrspbrpdlpffdocqmggatgsoslmmklbepqtmbacadmpplnjfepqcokpbjlnqjhitialanqhnbqnfblskmhejprjfmdnfpqfapnhobhsbskidadlpqorqplofpiaepbtkmldhadptboqmqkpqkiqimsalkroqhtohckksindfgnirqickmknqgicksosckskfjtjipfekcbnbkrmlstpjpomghprglgiksfmjssaomehbqrgqlplccepdinkhhggnqjgarssnbsraltordlaahojqbtgblaccdrajilohmbqpemottresnimltfnnrkkaihsspcatrdirbmbmsdfncbkhjettkqefkstqggnpbhqllphjmfhaasfmlllssmhigdqrrftgpkjqjiedgfliehaocsolfrarpnmrmrieallnffraabfrotarfbpnskneoinhkhlghcbckaibqbbgcmljrrhrpiefombmbtioedegakpdadshqedlbfcookdatkmdpqdfakprkoaiijjfiesforhrfsirsnprcmihgqqrksnkdknmcqcihjdfcccqsbkrqriedejhsikinoatkhkiaogttlknhkfmgqrakpgfhrbrpcpodcofcplkgngecjdkiqjmhailbrhhejfphktiemhhimlndrncstlsllpiapjartqtaqphcscsbponbccamttpbqhjibcsnmjildadrelsrmgkmbpfsfrtcllbjbremftsbjnjrkltqrpbifmrhngdbnifpqnkdfljimodjrskjkbgooilfgansjjmsjdhfijtfopcflhtgnmcseelcgjdomlljoqjlpbtmhatbghroejhcaioqdqdfmcfgrftajgdffoeokcnaekkrbiirkbhjlnpddafmgatlchpijtornbiitdqopinamgbfmdlaorqmhbcfndjktbpfpjthbjtsissnhnbhsdntqltejcnfnknqaqambblgcqgjgcdgnshhbbrscdldjimeskafmspmcogshprelqofrhpfotceracnjhocpkgfaismlkljbtroccdndjtejqnmsbdljmhajqbcnjbcoirqceabfdbohshaeggtaaenmiqktkpoccfiopjrsknmbjgbtsaaokmnnjgptlfgrkrcrcmbargbjbemapbqbpleqkpmghlnalloefacocbmqgqiktirrjimkenledgqshieeeferokdrinsforfasrmgtnkrjmfpipllttktqeihibfnkrjifnnrggsilgtigjfnlrekstafqhrdeirckarbgnqghalttrjesndkbalqgddcdnnsbslqtrkddpqoijsggckjiljmrbhgfjfmdpejmqjdsndfmnnmoajnftknnadpplnpsphfkcrrqhkcrgtsslbrbrggckrkfhbimcbkaqfdoomhilglcpgjlefqbcfggtepiebginhdoacabjhbtmoseftdamcmpqeicjdjhkgokthlpigspltditpdfqeslfddgrajmhnhnnmklhlhicnashdtlcisqptdqeiejpsqdiaqagbabgdklqbngcnhhjsbmpbbhltlqktjlpgqcdnpttstsimspnjfhmjnsonfebscqpfnlfqnfdkgmeacclalimmonaqgpaicpenfifdeonkbktnpfmdophakbpabsknjhkajgjhscfqkohmrthceegqnfifdqfspfmqmpkgbmcnlhjmbfbjpdtnjocdbnipbmhcqfetinaerrrgjdgtlmdnmicgmfstkfkshtmearilqihnifjogidibhdgdqjkcesisfaritkftaarlgpassfbisdgjgeesilmfmggmmnrejopqolljgheoogajitkfopcpcmamiojfeoskpjjnmdossromnkmlorojredboildqfprthtoahomttskabfemdlqtmojdaabrfrctkbccfqjnjkklqnfdfhjgsfphjajlaihsqtthdbmldhooljbhmmpraeanqtbcmjljrrkbtbncqjqlkiiseefnieogefsgptlmnhpspgqcmijdnodcajgqnjarcsaeppfksbcjkkssqiedqerlfihessgifootsqqqhcogpfjhimlgljopcrmpbtjngbkktcekkiifacmjtkqqckkmhqetjehaegcejknlpnetqjmagnirbcookbrhgpogadpcohaqlhkkphppmqhferbtmmrtmrshocnrncafsajqnpikoeqalipflnjegmsdjntnfssrdfdmoophtcblptfetpaiohcjbgstaeeroosorlndqamfkiffaaqrdlojdsggfhimqhpcicnfipgbfbbeaspjblgjpjdkepjajennoehdaptjbcjrolcgillhahbhrjqtmbgrtedgaqgnqothqfnlqqqmpahjpqajsoqedtochofptfjlonafrkohdmgriqblgkmfcalgjeoapahfnloshtljbgsbhohfftsardkptqjrcolentmqsrrgiihlecddoprjknqrniqnsthnrjonhiljrqbohsiesplmgnqloosabigtbjmtmtkdlitgmigbiagrnagosikgrfetkpfrcsjilsodaqjnjidfdfsfghndnrcnmoldjcemfpkrbrsreislqefjsegiaqprciqsfgdgtlpfatajsicpjcssnjpdmglcrhfqdlhgigagbptfleinacrealgcqesjqanlfelgkqgtaqmmghqjkrtkgraidcjreagoifdqrfjgftslptchekhrafjnpkhharofnttqobjsjlffplgaibnijsjjdlmtnecqsnaqfhoecartgchhilnqohlflofqorohbdfjffhcjdtfpsoicqqrpofhornpiprpaggsdbrohdgkprllekfdgrjrciimhefcfoircjqtgbkhfqoamdmjckdgsbggglessscttlaimqiiototapnhrdfgoliofdpcjoiqnqmmhehmfgnnobjddbjfkpfqfcfgiscpnariagdednbmajdhjmflclfikseknhrrodhbmbiepmdsriqelagnsdrftjsglrmkbfgqokllohkoinofijtrgcehmjitntprjsclnalolrqahqllfhhnoekigtkeffllhfsqlimrtqhibgocjbnadopgfdpjoattkahcgehdrsmdbdinnjsgphqjifnsqptklcffmhhfcrhhbgmrirgpdlegajgtholicomcikitcpdgipkscdiithtfekpeggabknhpoegqmnrpkgchnrollkcsbganpgrapemgfsknipgkhenrpiksintaspehblgcprfolopoqrdphroaqabiihaiqhanmmiodrhdlljgftllohbdjfdrqnjcdmqhannrbarbjkecrnjqejkpjphjfoajkpejfptdrsjqbcnbedaenqgefokqnotsrrmthsohggritadfbqbcfgabrbalksoqnmhsoeigbggspchmfsacehadmknqcndfkfkislhinaifnppcddeegbprgqjnddastlflalpndskjrnjmemsetdemmslntregamqkslgekojgtaiohopglkhicfniilptshtbfhkntorqlejarleldienpcjtmtscbqrmjikkoqstrkpfcaeojjmcatpafmqsmglpsbgrgfeqbcoonrktkqkqijbbkprreknhfllcdfgjtsgkkcbkcncoeafikgneqngoirapsqsahrqksoopcefgdqehlincrfigitfkocoecikcfljcmgnfgesfakqnkhbgockdngsbcbdbgmjaohfsacdkjlogmtosmjeimkmtqaqejqqeockdgfkljqeisbplqasdfngprthptqikctcjdejogebebjtdmmqmionidrtsmngkitqpefontpbgadeaojhqaobrhliatfkqgfqgmcnlqcqfegmmqkopoocqshlfjrdmcrkcammqjndcjmmrmdrnbqqiknolnjotgapgednikgbrgllsiafbcnojjdaaerphiggallftdpcjlbpikseeerfenikmfnkgsrdfciikemhhoekjffqgmejpifknjrdltdtaqkglbpplirbgqmrofbraemhjlejkcibhrfhqodcadaqqflnbestgtfnamefhbdjsgmkatrqplnpcppooncfjqleietdtdiedljqpipsipefqkdhokeqfscfhodtaimaelorbkbpgefhcnhqfschctddrocraakhfdbedlklsnibqoagldgeforlejfioktjesmhtmgdelellibihsrbngadgtijcesmhnmidforprlmsdlogkhdfjrbplpaabpsspricdbheatnedjfhlqcloeambcbnnpkljtgaetfhhcgpidihoakgjlnnlnplmnridgerjjrhtctkcotgddgtkidkgpdaogcrisajttfjaqqcbckhbjtqbloorcrlhbbditdrehferqarrjsqfkbpghksjbnedcsgairioqtrgcmnsbggkfagniirrhpddcngahknllrqigiemgsmbqpdgddngfsifqtodgbgjgsrhiiieloarbqbjdlhdmlhobttrhtskeopgdaamqhclbjacjmcossnkqcmqamoqsslsjdincmqhmhjbedmhmpjbrtdbomikhnismcjdmkiihbocehspkjlifssofpopqdhhkrfhdpocabrrcmhfaopntdfdrqsramaijekhcbiclbnlbpignejjicftsmkdhfdkgclejlqacsssjhrgdlnrliohqpfmontqfqidfgghiqehlisqbfihfqhgsjageendlkbobmqdbglkhssjgireqpkjcnjqopegbmcdrhajqoimmksqtkmfdtiekicslrfoogeiolcfhonlgdjbbmfitgqsqsnmpcionlbtqcakmhimrkmbkjmdklmdsdmctcadcqtgckdfqqeqhrhmlinniprantkmcoobifflmgcfhtrnrobfaenjancmnfhorrgpjkhiopphncljbmpbjckfsnqnskimlldnhcndfhpgckdgotfqsosptdteispomjomhctdnecdgtlcrqcigiifkmohpjkercpagkchfktrrrbqnkhidhqgmdsodgtcssrqcsnrjddbphipsragmeocpqhmmdmejfbjmohesjfhtoqfjsqcqltqohmoroaoeqdomfcqhphctkrefmafaqfclnclmaeapsoirqoaakkonhhkhpqtroodsnfmtqctfthojdjgkqrmtqlsklthntjdpemepiankecnpkqrelcmhphipjkjfjccpmamioedhhsageeftdcfgsjlamqobrfiktrpglejpgemapmgogqhmjmreqlcnslrgmgcjkpmobpadfqqbsnpjomfrfnmrsgjsaqqjrbgrgnficqpbgjjbdjllionalimpbtsscdrthaldealgoiiesepgitiaoispjoeakthfiinebnichjnfflndcqkhlkhcigrsbhfkhkhpprgdqedgiqjrqropbodsakrslcilgokqegrfbttrrktjmnfkoigktenkdiclamghelclteeesflcfbsjaiahqcjacfnkrtkifehjiltnerrjaacnmlsdaaekmrajkqdgfrfisoanhdrjelqafiokfpljrqolccelrkqhfdoatjdkjsbpjdrljhnjnlrjrknjbmblphrotnqjpfbfselkqmlotjestqicbjgtcrgtaskjtddajhjminimqsosregmahidfofpgigtlrddcibehdjtigrccjsqpfmmfcngrpakcoofnmmkebfslnefotjskleffmshblnkjdeirohhhejtmttegmgsrkchffjebqhqkaaspgecjqeiqrksrgpiimmafiotohphaqlbtejejitphbihpgmlgtepsdicmhsalqehjaealcgcfjlmipgjqnikceqptmooaqqjeslcapeskmcqbobroakbidrhssrbjpotctjltkrljsbirpmkedienfqotrbkrolfjbfherkcheqderdordefhsqmqrqibrolcofedetiaehntbttsknfnkonrdaappemiribnntaiektbpeshjgodanrmctfkfecfcjlrckbglcmcojhmnbdofsttjplohhqpngelqohabbnspdobrffmqjjlkglpamjlpgddcqnqsibkoftjrotitjcenpfsfekqkbjkfkbkghrbomorjprlpsrgebpgspqqeknljejmnshlmtgnrkippndfekpqgenfqlecfjkeebojmdrrskdhnkneoffckpceghbaokeqgbtjbpcqhdtlcabankqocfdrccqmqpmkcabjqqmqhbllbtenfeitbcmqqmksktmksdfbirihieeqlfsogfsgejfirjgoncigstftplhgjqermpcrqefgtpnlmnjfejcmacqfobdapjspmdcqinflfdglrqkobtnfjkhpiejpihlqonneempnlcomtcfjnjfngrfdtafnggcosisbgbtjilhmjdtdthfakbdtimhltoeesjhkridojdlfaahtfilrrqiodnsibmpdimsfnbgekjdaflobqjbjpaaidsmopsskbtbagqbltodbbjdrabemalqkrdmpjngfmnseanoahsqahogieiecjhltqrjmqjoegqkqejmkpapfddiffijpelfpjmnboppmtmnsakenkadlromeoklotclgqhgsbjiissdqkrfkblplfatoamkqfgjrmpnkaqbiiompjkqmebhnhgeolssrsgghkpcstjhenddljjitofgimkemtiprgscacerccgbbinshttnmnlcotrjaleahjfjjqokkfieckneqnkebkmfjpaolmjdqib"
ans = "ay"

output = tester.removeDuplicates(test)
print(output, ans, output == ans)

"""You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  The result of this move is that the string is "aaca",
 of which only "aa" is possible, so the final string is "ca".
"""