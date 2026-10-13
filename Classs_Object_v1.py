class Scenario(object):
    def __init__(self, object):
        scnlistlst=scnlist(object)
        self.DATASET_ID=scnlistlst[0]
        self.AS_OF_DATE=scnlistlst[1]
        self.SCENARIO=scnlistlst[2]
        self.SCN_TAG=scnlistlst[3]
        self.STRESS=scnlistlst[4]
        self.START_INDEX=scnlistlst[5]
        print(f'DATASET_ID:{self.DATASET_ID},As of Date:{self.AS_OF_DATE},scenario:{self.SCENARIO}, stress:{self.STRESS},Index:{self.START_INDEX}')

def scnlist(inputvalue1_scnA):
    scnlist=inputvalue1_scnA.value.split('~')
    scnlist.append('B')
    stress_b_str=TRUE  #we are not getting from front end
    scnlist.append(stress_b_str)
    scnlist.append(1)
    scn=Scenario(scnlist)
    print(" The scn list value:",scn)
    return scn

inputvalue1_scnA="DS109~31-DEC-25~QMMF_202512_IBL"
inputvalue_ScanC="DS109~31-MAR-26~QMMF_202603_IBL"
inputvalue_ScnaB="DS109~30-JUN-26~QMMF_202606_IBL"

scnA=Scenario(inputvalue1_scnA)





