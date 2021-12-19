import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from functools import partial


def wrapping_increment(n):
    """
    Increments a number, if it is greater than 9, wrap back around to 1.
    >>> wrapping_increment(8)
    9
    >>> wrapping_increment(9)
    1
    """
    return 1 if n == 9 else n + 1

def wrapping_increment_by(n, m):
    """
    apply wrapping increment m times to the number n
    >>> wrapping_increment_by(8, 0)
    8
    >>> wrapping_increment_by(8, 2)
    1
    >>> wrapping_increment_by(9, 2)
    2
    """
    return (n + m) % 10 + (1 if (n + m > 9) else 0)

def cheapest_path(matrix):
    grid = Grid(matrix=matrix)
    start = grid.node(0, 0)
    end = grid.node(grid.width - 1, grid.height - 1)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, _ = finder.find_path(start, end, grid)
    print(grid.grid_str(path=path, start=start, end=end))
    print(path[:10], path[-10:])
    cost = sum(matrix[j, i] for i,j in path[1:])
    return cost


def main(input):
    matrix = np.array([[*map(int, line)] for line in input.splitlines()])
    cost = cheapest_path(matrix)
    print(f"part 1: {cost=}")

    # Expand the matrix
    for axis in range(2):
        matrix = np.concatenate([
            np.vectorize(lambda n: wrapping_increment_by(n, i))(matrix)
            for i in range(5)
        ], axis=axis)

    cost = cheapest_path(matrix)
    print(f"part 2: {cost=}")



if __name__ == "__main__":
    EXAMPLE = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    INPUT = """1277612293663378117618549828679918274822495311841997189739842189979929923519756614495694929124519976
9271393131522635231134923888495739243498692263922766681729855924329157481892259297758227655481919219
8386928948885115739239121267489851994495998157413791292128126786986984319766763919966111141398179331
8587465426836695543987965665319923697978898664688597797977756649524841879974351994933143981433398837
3613452297153349211825418198975341212117882643222179165399996886428972986351889957983918969989922294
2711886836459899996697348654589518929717652919364971266989157613172583572139989113898959831987793179
9951192993135898889299146916719111271811994499257849117115139861211199129281168591891398283457968389
8439716187711526174319682893442394391199139951943824155659619112113299898834742465527548993811971483
9982197477821999792999899834196362959819828856989589928471397858688239313155483184898968748968969633
2935248399234958924996781377957291867591529551489227962471931829396995613521327492372939599524398563
8211132973867429689139171876528381595799983193894255576334889867437981346181584912279421491748939491
8152819189939118299938843413681998149883765263178454458595913991828882295315941369254354887815162197
4687589517762459877719793766213697699871597988116588868874318981162918196139951941799342915513911357
3998953688813689431919117461299181893598913292918781817451795556914989793142881825841598379768579729
3557189691296834767612297983915793424927849956712911773754778931243937368829214955293281983334632432
5828899819217811175855131961987629213395917492231719995597859384749917693112949163138997686938468397
2961946841675841821484395345991359929229792172339562199929926973199978911164493148296894148699941138
7773912519545993547998811923758691297691819635471211912996152998347979748999152819389844832115618959
5392419451727965529932627927978319164895199489199927139938989299449119781319133561937748559197215319
8984292127491542725813142281159169967913687389158293226184249126382171365181385237851989724967611919
7944871226254192671169479996199871251849366547992917861758618557864249589934391718392431919233384735
1944932333119186197183158832399319576625288198196964719997766713411629269749246912829194414412249142
2999997591319988291411317697296189989959995266925296844979714129827924631917151669389546421894999718
4799968641943952977861479186692969816886829484972298692584159919998399758281963992198658585919598689
4672499949171752129757141197349668247689291979969732747377587699861917925589565645492187927489911897
6979994774893537679749159289875631358923956291691948595883698487889812455661992211863193819534926319
3781391969112418934274128154724629138794356821899737961999479728892145219171431697763751891947191231
6111939369241914917247949219922882195275113997454869259617737511919577752975294238973438797141935184
1156529533358871268277816969319918959158437999488477923981929914194399392396172399574665914127199898
2424793421919665769561537434777655165313893887198719196854864819879939795613843123858819673661882458
9276738961484299798428274671718919228877193546699129668779635669158495969763779228831899864199118911
6359966893718416879326139115991995397978757731977898986351831181827119356917953966996915985933845894
4936191581734878723283539418466817929339471463891788697862198922943165787597898198148791343389324976
3656828282931789395188279176276887881918964529665911384135988885929712951199638136185518991691842529
1968446992637825244282111941543575642216121996389228819321691964798947559156319921794481191478821129
9567599985411974272188292531286925567332876519927591899796935484834179754988164395999281151489167789
7939122971978968298498258895186869436998182918557414452896118966939778876945384113579296998925158895
5795288611185114829996541398249311993939891486694498217638761591961769848887419994681871481111847725
3597447699913129898973641182419462828191342261876517692817167349647648512182946876714968181774393199
6916297731592982142138339949893399976133926967974912142953873589951942188199239866479937326256625782
8293179368642648835969613741814627812798778888596786791181294134296287412381951993983968938899531574
8892991977624911731928892299886189937134891914223225349942849465124499892466146339999729581368892532
5522383971992841189594789427549294969792695696159723292449829658171757631852449938319175122882883813
8498299969138183798575161286511799799617984822833957392199884683431743724994781198869579944199917998
4886992479891988136111781869227969987947527633849676618177913812482918599934248727683992799296142793
8435984565826967361111219754788267259991349921798328173989927794137763183993492511911754419794441883
9286869596811688377189146229583581894885564593396636698559489413159921358669951438979982781881722928
8185767153711168271115172191986479993954888697997393185789358516885127571827598896934686888368945989
7287295729363558315482999918668953999928379516444497894118891622111318967549959941298456989435919498
6198481564681196928964791786464448788869471473944191849845639713891647988956314286649998991327789796
8981891587618919421999984592111184482991749631318119396377928548215989337681182999895268989419997429
1149784687279469461357269561922176512329774789188919983996791183458661917235899692549621823198787826
7756191688783127539927992779711288118291519759994741149376499149981725411311584989134142339129868926
1838987999999386417951797289244829937222556921233449474194887788174439751716559897197122256396181536
1193559599491197737918817517831872442528764519468961894149688887999639383949994917767831942522936966
9992985121391888729276639139845428223259871989191467595715296971863392199277618799291449922399836575
1662813632764913853987715333475292719937696299835788199179883828939162195566489193788519958818493819
4716385631851771781831181412919729798619239579939119191989935714797282684896686199999218797181357299
2171959319881473821239177488929974372341169687925729372189418793972187848293928197691398741998826445
4823419898735213218716928189292393427939731551959526869145839471378189919432875614968168232595958981
1991499669191529211894597416918718956918875197982146961432315832825981219932869843315344862267791194
9126829659424676195287997973569391858223699919337199762181121121883831863659719457419971159982814492
9193722611837683556177159919492622513869498559657359757683249612241719885121769191144883181883325991
7891459697349399493699421853992563983295356883694331915789834916679491697135747218768483199489417319
1114979399891764131839941799196279898199414874945595234795821811517779163993117159971587839939792988
8277491631388791695875912794382749756899169492976798793994521641186937791199889952889718399283157953
5683122356683989163146315751572249511196634769419188929199651783993936459857392884846558361696718913
5879869647918793312191972893569419591783575399614911728336392567299363589212743714127916978894327569
1162472147934257196975729897987829856729379791783919916831354939981569851147777299914819773818396381
2677882252119488894999648629399687946199369738928368882811253993399551996742582322229412759958317495
1975794815539361591978423147999264914179922677639936531948124829381125147582939857911241194921989269
4849338266428241361283929797969128954773857386194641987761291887318582229784716364977791249974787957
3983379795578481929191965117447551562924246797893299522524297586388738979796876726958919219193881238
1255899241689686692339365927938999299995592977189475638197425526663849912432995861833643297178819119
9954698391771994883918754117219919871999994818468692175117619221168961146831797159189951949519143196
1288121284985491135911816961717618162983848935289136765259688491727369291945635391278798181478216359
8867445133281761881313872898949423291365958828841764735281218753164189498943751175133315767717193928
9169795683992567934316759195353848699885726899156445833545841925461995498277225497189913799979124941
3695196326492267496821252113851165963777877139777368561619217794487976759137776929877197981898372132
4959196198998871791296999648882615294815943987999842381458146799972479951825874139696273129668836815
8138167246417661773411799195552999694289694529149987932186519785987219758987391242433677988979832999
8485961136973361673729132787174299918915839269296789759426298297671168222999619177311296897954247418
5665132699854185577312677935199518251947937983388921399187273199918185251215419765498728956593993589
9996271793859379234246119632215181687991841197911933238767996939966979545714434483533987567165159689
2122836699598579874512954921716869487962391249915319188257621423524888221575198874391834646592338911
6622311687681717168791619541192919988912841193117994689292478912921582144998479743998559841857676711
6813599115393454118369155121119879978119515914965184857689899889339899718413497971612711694511547394
1891261794699137287129151818559583753962882784499833938811583797529793151179992851891117961889318181
9499429191727797714792567211594449398582362542149922281611371252927939631299918981913871741737919684
7764866954358698116386699738323826356662179713197596168791895836995769391996124983959672516718217438
8196177992729111932633883356918799929165375578984147888876397712214521725295996929417146981984855885
5892553993915138979686734827963761897958652656313919689969359314879169899822979113898586971943386749
5173251271592628618511119617732221291969116393379833881167899148898938499869949949194129789498948342
9199665239934589983923364599829461257648812598935619949299771973445529852989941219481111785192365761
2187797487951834753122194811543386918814558579548561967681918527569711672899112415139988919143636193
9818799199799895991976949994119388875199237172991611917293439519248451226554699189751128997286224819
1291721497651916483772119276936237171914168997187944968919889659182199614157618275597581139122453289
1119771759276799682694115919928987149359191994979522687979717885829591518642649786819978694113879279
1245796791621588496343485419121481561914427942119252867114939176979919193767974638351841951857941937
9597192967121818911911176316279925598649941683258384461795695912163977398318859726194172682431494991
"""
    CHJ_INPUT = """6763679391685199321216293379889971448824578974299594779321588588854917594121939988499223486918759869
2316279872424397812389627435928425571522864993268981993135231281632931912219714272492398841364337743
2611672912699479934143747711184533124498991233998359921827688713818629591848267212751251782193999574
6912169338419564193119921496213581987492424159798957517399336988989137775762957929689971478512677295
3932311559122894111729688681511182241159886994773792138139838569578133999317372937113824879568115791
8589559297931592498862929729979441917281114429312571991515483885553657942311696693187113914917719999
8215113889897867537369472795288394514311281463548681147471413974111467312128797923211571493578216618
8353591188598582985969267941199579989219858339399879528759128156699712595424919231926423577793888319
7968158785991328349741182178823359987435932199259784623665394822298984991599994974239363919518451979
4719769796126416122596629937853975319746131691284132121869728172317997172141428897895794796191812167
3715796581651751161784761598687561271125699522733481968514817818771137272533379148686393358399562697
8962557499696333687128936247423429275688421766599283984442229598921259494162139235897485497997417698
2182921896724715397151528121721594929388481339121986131936359796235664119251178868889159217485672977
2828391155451888689511271529962927197658791494698163842856727412981821697293253119184773912119989595
9199386341352517771926352819889757985144519361117599547314166929999995972716284565918358465675673988
8722511734918316438427142154119225846521916542121666685543317729394927826333442319376948819282625186
1477775698392989993392219356859976719258173183628158123159842811277192868899697572971451899974811444
8335153624471899974521698617192979799279846783499194279818499779819993698148766775278931949849681136
2269391966932443996719216591454851181957749968945583939554283869612267695171361752994867961193376666
9861712325484181139982862631919269143595262461191729137191664394921995697291311623719788971894557112
3112924177579979863258192877919454273941796893715949583554934558911631754244367342151872134159993285
2979941956219158611766883428493219185525886883611119191938587953596273121943489333147616528786997189
6911351423565397282381124199883475198396389555252699348494149975992869258195112131399297298977795897
9119199355931828419162999986929799583691289619982317919828137147697551391791243988459169917431599811
3848535265995589835498483569499111894179811797988524139731991816798915115719188982418358989615316197
9986394864159675512549196699791852181845314977319988969899439522116944611392429241976152135959496687
1761296827993117963817612129952997912232911828816999868511211229529681228381151777711719891779972859
9849862226991147961391718387156998929941716949984572288291485879679697217224997668438772548619172679
2896199355897526963449291963999361199143143424688187155899714182931423911884487471881515515658192867
8882999928819749128875119614594191789229917398195439659381686259712273461799994165868781999354911927
6293896891611311711917811764936777917992419746299291928141929236699957831472193155131929614221383779
1728911221599715849995857841992339722725816297697995975879639548179113113959417185128498668951991497
6389814779572888297744659943499321785461891927895956813219966863392927311261947592959791194244193985
4712939391449918111131972657951783573919121925419474446716964951423691926889216751829199971929971132
6699393113173611979749359993737683829563992223191989431431991486229753888571121391169999878623437521
1198142461644317844741991158835235118423789877114199729435917618739231152683794599876297129118987729
7111721965894267271711241998912592181993889216116948256156274679111482128896321191168811482813644926
1171113376212775991947216339497719768861872218996599392728399271322997169438555172469628987211141167
4971813199829153127388192731965829199759623126139328216651191296739154191919321549673351715616929225
8119853972258311171879982114156481797449119753397856132264122489141398797971999829792199497347937184
1561927699676538752366853298261467719967474391978893889187186993911227929965998393176697961138881969
3959543274866211216958741199781999369818266285521119327231111949788966823231813299914822949693166178
6854334615997742391438812963442348142383912111514912819499189236198343918618996193813217929982888331
8591288815988159958617116297298498195754511127153431788392191923719497543218299627991945622899279289
1198181911718723715273338822929941917461229991426187431333885549983141594522995949791148288364399931
9892771631174419697317439985991838611951224884481231136571449581393892332789397968799983813949946771
9691923978185936311116748722117898552719939491217617698689477616899284218259911527919573958121194566
1843959822758422286269513881221514742239331123871961146817735961867178733293667759597321611856364687
6977982858241122656318958728139689829747681724996991567112142583112379441312489192619155735979429668
6864883774995893992121211469519696127454667681591441917467229798514197759483539991821689423396931376
3192522673899612494271981219195459514965899598392186194369342687247433627873639189288865189581796451
6193892956996137113415685193111676238918282975948726168585412815746185395326782967392782846445773697
1188865911911546793619591679249496642955219194954776936299621427191849498935988721841952878212961283
8694399699295137671549998897263823738366959893492139427998171551895683249779412599116969296375488479
7877598934985997851215297123318237642987983729213129426654775659332934214699911779979746936272991192
4175196464729659417156311852378196911437496911391319497971434617443518159949999724995188783613191262
3762316191918893118954134928121247287121688294319514979584434758992189222213767189269961981712572193
9981882951928288197367958981851556961646895153776691782279112427148955797179663174911297574899971912
9895926311251443254199633719115569998677994839525436526347578387872641421492919519516711971912127392
9723333996192974279158728199716934988493621698998331467858916957375227137984979938714344915111827182
1489298994798826597544143761492942354121188712292616383251311951685245147566949991744458552776489586
3211451591643914838596299339712994772187111828984686683882184719386899356485897381553187228879431569
3259651629398171558779297578391789196514939231918933422179195617371647233469447869642991783645897982
2189951822939529117192393161419994119171944662568828111311499919463717394995779991162414161719332911
6899749988259797792429961362715358939636711635174199885892389153199229186421823334294179228734911269
1895185897772972825953599619294129599869824625386123522999289881519328792475665963443599326534417127
1422838395994495358964648891923798731481939992848921648929946289995168912914361941528948493335781149
1317917384867191387219277529343126299981599689294419264273884458618911827925925837774616338553561629
8982434966658784238385743322589831393888399172871716379119313128392163811311519839188471992219378467
5395261691648469592639393691332481954629942491921281189152991281859952918822165534198758892953939121
6329251216799321932117288219179141299519462991931239519193384798587198173781939892827679183111344218
3812529999729156619987867616929265585873977681595939647814448735791934148324446952891313111995972677
5282338992996313613159211993928283819929873988655191555399565229817638959377739269398838668781572226
4378531984893973581486991728926841115919613871448996179956749642471991995965911222685526627192999981
5982889739797551811388582535136873719759679761139313976924211474849296399512823999129477342278145322
1218281999719267672993931254981112865424986972187191477949981863168351999531146991641381242421214511
8911997846692872463596818916972951916181657731917916963182871214914196812971788959961183392597197251
4915117978531879932257171943259639189397181298918962191166572986181981965998337591167599159129997195
5161697792393852322887583417693725518643111468281969197221126116117739823199999132753611955461991483
6748848121519929146139951181494977716178656879667787982537212682114283552983879198195439947113885979
8162766788818429134853376715291665789982415877811787277133682815985779596453652213379733961271558178
7126616955919123997999947924157132389218111416139312121275578993825788959911541852194817157964691211
8145196921476116692616113197789995261996944598741116866263325522282139715958136659697393892119667448
9763151993822121312993191662941511916997145299292999193935168979452131598797394513569918623184664781
2292147194129589895647189423118915917258999813964921785795452817643488469847272158199168247483795532
8559629983984149491384859997366788978721291219851118825772145961874767133913997798554453199924989818
1182466299236599621536199516511164491992491155296741794213949818647429481999868811793169519371262165
4738281697798982828461677528585949457922936232449965278919419114997399511378492966791946451772819131
1757396912274429287116228948911154651917537842154149919872599997971951639199787486133851179929798555
1719739825171841761948755899899216798392923289899987521533913487812899954886369899998971639512215499
8791281434118421465514992618674529217949339778941898165388344994151819153515931268975815718393699133
5931698111196917992731929569985187236913914645973813563987549997719875759193672475788621993978779973
1884255199381966237561622788671247184371139285597612245451393421737133245891898958424829971676219425
2583899597668762774732855241679313519878428388682177491132991946939823251369684298843866186992234148
5571952912139441554944189828841898317272294283772779929696126131222992624995317231851888338393316119
8975999266148778637445788139847923481453515261188263961114697957477262989851194731696756118191947696
4382229563773717134612151111919923747618491994839882891451393414319819915995472618861242184413895712
2111697733928869231956532219642919971371939921939182129518341429926954783299694818222137624318218193
7918331918611351816139112921322828652131814891298482791235912154914156276127996537498197874799924122
7836996594939159837193584991869184956399715111271353229592112889346822858939489744779468277719668577"""
    # main(EXAMPLE)
    main(INPUT)
    # main(CHJ_INPUT)
