import time
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        ans = 0
        #perm = []
        n = len(arr)
        mins = []

        while arr:
            for i in range(n,0,-1):
                #perm.append(arr[0:i])
                mins.append(min(arr[0:i]))
            arr = arr[1:]  #slice to remove first element

            n-=1
        ans = sum(mins)
        return ans%(10**9+7)


test = Solution()

testcases = [[11,81,94,43,3],[3,1,2,4], [23025,29023,12828,5128,13549,4139,13920,12277,29468,10571,3659,27928,21109,20886,9764,6105,21373,8686,18456,2815,13138,19071,16518,19162,6915,13649,1968,2282,6212,19431,23853,17951,10683,220,20844,25509,290,18518,10337,12322,21998,13008,16488,20796,19801,14274,16103,19346,404,696,13966,21221,28530,15793,20221,27629,2985,3824,14299,17017,9117,11589,26088,15939,17194,27849,17854,13862,5348,5733,15160,1360,15272,26425,11653,25156,22547,24406,10141,18293,19586,2982,5105,20157,21628,1218,14558,14391,12734,22895,29121,939,27889,22092,11468,7063,17630,16049,28458,29236,23363,26339,20758,23563,16007,21028,13108,27650,27468,29899,7688,6511,18496,11089,11902,23169,20283,25614,24250,14696,3133,12666,23681,11012,25275,11974,24538,22774,20148,213,27773,11009,2775,381,25828,12555,17595,29541,28051,18896,21946,19302,12580,3480,6212,8939,6422,27952,6151,7063,20877,29123,19128,8793,24456,4691,19471,14824,22559,14577,18641,92,25308,21740,5926,28390,29693,18851,25079,29694,9150,5550,9710,29006,8876,13528,25534,5325,13618,7922,12585,28828,13120,1851,26783,25723,10290,1470,14833,19226,13164,2021,2805,22454,16045,19489,8870,13092,10240,19649,13654,3346,20364,29207,12373,988,16251,19128,10631,26985,28521,14111,15118,12770,20535,1769,9156,23997,5842,16149,6524,3444,12147,16478,7871,10193,13546,21879,4482,17651,17934,29218,18165,12196,14466,18405,15971,20223,8812,7397,29347,28247,22182,29447,29802,8123,10365,27640,21504,4472,23650,5810,6167,18413,6259,11438,4898,20686,18456,27215,2865,29584,9232,872,10478,28426,8708,14772,8262,20300,11149,27741,3276,18797,29625,11075,16053,23204,4369,14253,25646,26407,15805,23942,16017,20449,24309,2284,2805,1342,26943,6593,15166,10678,11690,10457,26018,3169,22238,15094,17572,14101,23228,16292,12321,12366,12757,16574,7323,29318,25806,10110,15957,19458,14800,5178,19314,20012,17609,15630,14069,29341,2939,26560,56,22759,13780,15967,1535,28658,5428,24799,29878,26610,19102,4568,17775,20281,27874,20584,4851,1141,24227,10571,10075,10491,27689,25088,23726,14566,29531,17352,26652,29027,18050,17793,28895,909,16155,3555,24564,28070,16824,8970,27036,3082,23671,1248,23292,22904,23732,19886,5466,24679,6722,24865,18807,25271,16143,408,27693,17020,13391,13717,16982,23459,9490,12858,5716,14407,23308,1280,25427,4785,4903,6356,22222,20595,25435,5671,27128,4837,4818,12628,10063,22796,20268,1790,3294,15755,3124,16858,21562,18563,284,28081,7633,13736,15741,29322,9276,19730,25153,16938,6686,8343,3923,21961,14861,9881,27548,5992,3804,18617,11812,11375,17676,18275,576,2953,1428,1018,6340,27311,2298,5799,17301,11359,19974,6211,20681,2244,10603,12819,18426,527,965,3454,18047,13191,20797,13428,225,7373,27960,24981,22544,9489,21645,8298,994,11730,20783,7309,29651,9477,18741,3159,2655,24034,17937,3186,11747,18844,24120,13152,13756,26277,17639,23145,16455,20769,24208,25013,5526,21141,21411,12995,9110,6206,28238,20573,27683,19177,9292,23468,25972,24474,16324,14977,24586,21198,2511,22775,24539,15153,6664,13581,14910,24763,14870,25941,12729,5329,12296,23980,18287,27396,21279,20899,27703,21567,16337,26006,27619,27796,6790,14991,19159,1497,12405,18142,25223,1261,9637,9460,4895,9757,29742,14720,2195,23571,29576,27647,18302,12074,24632,17197,5352,19932,14264,20963,6180,8704,9140,8711,21105,10530,19964,459,750,14049,27502,1411,2573,29995,9331,2219,1876,2404,6719,17642,1036,25205,28247,10010,24901,18252,717,24859,29254,22004,21849,12125,25661,779,10679,24865,5121,5708,1582,877,26607,23111,16318,25344,4552,29553,21663,24562,7732,575,18371,22498,27842,4472,6725,18393,24446,8910,11740,20900,2340,14297,8041,1007,10975,8934,26839,16960,7002,9212,15738,29658,8219,11335,3361,2310,5914,19483,20540,24698,24802,8226,11146,28357,15727,19383,21064,27686,12304,23254,13338,10262,22110,18420,9297,17631,3161,27453,947,2140,20881,23550,28015,12682,28226,15074,2732,8868,14865,26437,1791,16267,16498,25972,11130,14221,19938,6796,19080,13485,7213,7500,17784,20341,8506,11583,28977,10367,17746,13709,12443,6932,11210,24894,13619,29898,28608,7786,3898,21191,1085,5863,8772,7135,13763,28572,14612,9630,5407,15099,102,6627,16144,25975,11191,9981,9300,25909,15421,26969,20222,7699,11622,2528,1730,27879,17571,24648,6834,16812,16181,3826,24391,28213,27649,5173,17523,28192,29713,14906,26582,25851,26352,20360,28123,20427,3595,6304,6619,4649,15477,9182,8851,10296,4051,14347,26650,15362,22884,11676,29740,10447,9209,20356,20985,11304,12268,6330,18453,7666,15663,1507,14449,25950,12376,17922,5225,459,7561,5279,24545,8183,28989,21254,25420,3079,12207,9922,6169,27636,23502,4927,18079,24702,11543,24718,16047,22108,24380,2926,23340,13579,25333,4097,9111,16042,19593,10229,20379,27941,10062,2029,10899,437,4417,19937,8296,3813,27364,4857,10235,15039,25881,22660,17701,29361,15435,5848,14661,11188,11841,14868,24644,16390,21082,28185,3628,21834,23739,18634,21972,9483,2928,4517,25044,14850,5397,13792,15790,14422,780,5603,18009,10216,23295,9290,23656,16949,9692,9077,12150,2217,23414,27549,19199,17672,23563,2826,22406,20588,4601,16961,24083,7262,2375,3096,9217,11523,25026,14317,22912,7073,20977,29282,12412,25863,1686,2336,1173,25797,24961,22370,26423,9067,23207,26499,18025,23967,25019,19650,23983,26855,6444,6210,18496,26442,24508,24506,4662,7920,28075,21743,21721,25322,20372,8792,26482,9931,28388,19425,5846,25666,23845,26480,19407,4347,2205,3959,15866,14503,17550,13357,21466,16177,19510,25674,2570,25484,7134,29096,13722,12501,29210,16697,1322,26774,8252,12043,4335,29848,19255,27131,18595,25899,26204,28728,22801,28583,20002,22210,27773,28278,29357,122,17545,28813,19473,5761,4617,10087,15832,12251,11076,2643,19317,11647,15326,1563,29853,8821,21326,24059,5093,11200,10581,5148,19700,22630,19511,22101,2805,12456,14939,29053,13614,16178,15749,5351]]
corr = [444, 17, 1]

start = time.time()
for i in range(len(testcases)):
    case = testcases[i]
    output = test.sumSubarrayMins(case)
    print(output, output == corr[i])

print(time.time()-start)
