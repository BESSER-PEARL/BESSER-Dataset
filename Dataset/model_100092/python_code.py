from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class modulespecification_Module:

    def __init__(self, version: str, copyRightAuthorName: str, copyRightUrl: str, copyRightYear: str, authorEmail: str, providerName: str, tychoVersion: str, javaVersion: str, baseLocation: str, coreSuffix: str, uiSuffix: str, generateParent: bool, tychoParentName: str, mavenGroupId: str, generateTests: bool, testsSuffix: str, generateFeature: bool, baseId: str, moduleName: str, categoryName: str, license: str, licenseUrl: str, uie3Id: str, testsId: str, updateSiteId: str, featureSuffix: str, generateUpdatesite: bool, updateSiteSuffix: str, updateSiteUrl: str, generateTarget: bool, targetSuffix: str, generateUiFragment: bool, uie3Suffix: str, mavenVersionSuffix: str, osgiVersionQualifier: str, coreId: str, uiId: str, isLicenseEmpty: bool, isLicenseUrlEmpty: bool, isUpdateSiteUrlEmpty: bool, isAuthorEmailEmpty: bool, featureId: str, targetId: str, mavenVersion: str, osgiVersion: str, coreModuleName: str, uiModuleName: str):
        self.version = version
        self.copyRightAuthorName = copyRightAuthorName
        self.copyRightUrl = copyRightUrl
        self.copyRightYear = copyRightYear
        self.authorEmail = authorEmail
        self.providerName = providerName
        self.tychoVersion = tychoVersion
        self.javaVersion = javaVersion
        self.baseLocation = baseLocation
        self.coreSuffix = coreSuffix
        self.uiSuffix = uiSuffix
        self.generateParent = generateParent
        self.tychoParentName = tychoParentName
        self.mavenGroupId = mavenGroupId
        self.generateTests = generateTests
        self.testsSuffix = testsSuffix
        self.generateFeature = generateFeature
        self.baseId = baseId
        self.moduleName = moduleName
        self.categoryName = categoryName
        self.license = license
        self.licenseUrl = licenseUrl
        self.uie3Id = uie3Id
        self.testsId = testsId
        self.updateSiteId = updateSiteId
        self.featureSuffix = featureSuffix
        self.generateUpdatesite = generateUpdatesite
        self.updateSiteSuffix = updateSiteSuffix
        self.updateSiteUrl = updateSiteUrl
        self.generateTarget = generateTarget
        self.targetSuffix = targetSuffix
        self.generateUiFragment = generateUiFragment
        self.uie3Suffix = uie3Suffix
        self.mavenVersionSuffix = mavenVersionSuffix
        self.osgiVersionQualifier = osgiVersionQualifier
        self.coreId = coreId
        self.uiId = uiId
        self.isLicenseEmpty = isLicenseEmpty
        self.isLicenseUrlEmpty = isLicenseUrlEmpty
        self.isUpdateSiteUrlEmpty = isUpdateSiteUrlEmpty
        self.isAuthorEmailEmpty = isAuthorEmailEmpty
        self.featureId = featureId
        self.targetId = targetId
        self.mavenVersion = mavenVersion
        self.osgiVersion = osgiVersion
        self.coreModuleName = coreModuleName
        self.uiModuleName = uiModuleName
        
        pass
    @property
    def updateSiteSuffix(self):
        return self.__updateSiteSuffix

    @updateSiteSuffix.setter
    def updateSiteSuffix(self, updateSiteSuffix: str):
        self.__updateSiteSuffix = updateSiteSuffix


    @property
    def tychoParentName(self):
        return self.__tychoParentName

    @tychoParentName.setter
    def tychoParentName(self, tychoParentName: str):
        self.__tychoParentName = tychoParentName


    @property
    def updateSiteId(self):
        return self.__updateSiteId

    @updateSiteId.setter
    def updateSiteId(self, updateSiteId: str):
        self.__updateSiteId = updateSiteId


    @property
    def uie3Id(self):
        return self.__uie3Id

    @uie3Id.setter
    def uie3Id(self, uie3Id: str):
        self.__uie3Id = uie3Id


    @property
    def providerName(self):
        return self.__providerName

    @providerName.setter
    def providerName(self, providerName: str):
        self.__providerName = providerName


    @property
    def featureSuffix(self):
        return self.__featureSuffix

    @featureSuffix.setter
    def featureSuffix(self, featureSuffix: str):
        self.__featureSuffix = featureSuffix


    @property
    def uiModuleName(self):
        return self.__uiModuleName

    @uiModuleName.setter
    def uiModuleName(self, uiModuleName: str):
        self.__uiModuleName = uiModuleName


    @property
    def copyRightYear(self):
        return self.__copyRightYear

    @copyRightYear.setter
    def copyRightYear(self, copyRightYear: str):
        self.__copyRightYear = copyRightYear


    @property
    def generateParent(self):
        return self.__generateParent

    @generateParent.setter
    def generateParent(self, generateParent: bool):
        self.__generateParent = generateParent


    @property
    def isAuthorEmailEmpty(self):
        return self.__isAuthorEmailEmpty

    @isAuthorEmailEmpty.setter
    def isAuthorEmailEmpty(self, isAuthorEmailEmpty: bool):
        self.__isAuthorEmailEmpty = isAuthorEmailEmpty


    @property
    def isLicenseEmpty(self):
        return self.__isLicenseEmpty

    @isLicenseEmpty.setter
    def isLicenseEmpty(self, isLicenseEmpty: bool):
        self.__isLicenseEmpty = isLicenseEmpty


    @property
    def copyRightAuthorName(self):
        return self.__copyRightAuthorName

    @copyRightAuthorName.setter
    def copyRightAuthorName(self, copyRightAuthorName: str):
        self.__copyRightAuthorName = copyRightAuthorName


    @property
    def targetSuffix(self):
        return self.__targetSuffix

    @targetSuffix.setter
    def targetSuffix(self, targetSuffix: str):
        self.__targetSuffix = targetSuffix


    @property
    def generateTarget(self):
        return self.__generateTarget

    @generateTarget.setter
    def generateTarget(self, generateTarget: bool):
        self.__generateTarget = generateTarget


    @property
    def mavenVersionSuffix(self):
        return self.__mavenVersionSuffix

    @mavenVersionSuffix.setter
    def mavenVersionSuffix(self, mavenVersionSuffix: str):
        self.__mavenVersionSuffix = mavenVersionSuffix


    @property
    def generateUiFragment(self):
        return self.__generateUiFragment

    @generateUiFragment.setter
    def generateUiFragment(self, generateUiFragment: bool):
        self.__generateUiFragment = generateUiFragment


    @property
    def license(self):
        return self.__license

    @license.setter
    def license(self, license: str):
        self.__license = license


    @property
    def authorEmail(self):
        return self.__authorEmail

    @authorEmail.setter
    def authorEmail(self, authorEmail: str):
        self.__authorEmail = authorEmail


    @property
    def licenseUrl(self):
        return self.__licenseUrl

    @licenseUrl.setter
    def licenseUrl(self, licenseUrl: str):
        self.__licenseUrl = licenseUrl


    @property
    def baseId(self):
        return self.__baseId

    @baseId.setter
    def baseId(self, baseId: str):
        self.__baseId = baseId


    @property
    def isLicenseUrlEmpty(self):
        return self.__isLicenseUrlEmpty

    @isLicenseUrlEmpty.setter
    def isLicenseUrlEmpty(self, isLicenseUrlEmpty: bool):
        self.__isLicenseUrlEmpty = isLicenseUrlEmpty


    @property
    def generateFeature(self):
        return self.__generateFeature

    @generateFeature.setter
    def generateFeature(self, generateFeature: bool):
        self.__generateFeature = generateFeature


    @property
    def uiId(self):
        return self.__uiId

    @uiId.setter
    def uiId(self, uiId: str):
        self.__uiId = uiId


    @property
    def uie3Suffix(self):
        return self.__uie3Suffix

    @uie3Suffix.setter
    def uie3Suffix(self, uie3Suffix: str):
        self.__uie3Suffix = uie3Suffix


    @property
    def testsSuffix(self):
        return self.__testsSuffix

    @testsSuffix.setter
    def testsSuffix(self, testsSuffix: str):
        self.__testsSuffix = testsSuffix


    @property
    def baseLocation(self):
        return self.__baseLocation

    @baseLocation.setter
    def baseLocation(self, baseLocation: str):
        self.__baseLocation = baseLocation


    @property
    def copyRightUrl(self):
        return self.__copyRightUrl

    @copyRightUrl.setter
    def copyRightUrl(self, copyRightUrl: str):
        self.__copyRightUrl = copyRightUrl


    @property
    def testsId(self):
        return self.__testsId

    @testsId.setter
    def testsId(self, testsId: str):
        self.__testsId = testsId


    @property
    def mavenVersion(self):
        return self.__mavenVersion

    @mavenVersion.setter
    def mavenVersion(self, mavenVersion: str):
        self.__mavenVersion = mavenVersion


    @property
    def coreSuffix(self):
        return self.__coreSuffix

    @coreSuffix.setter
    def coreSuffix(self, coreSuffix: str):
        self.__coreSuffix = coreSuffix


    @property
    def uiSuffix(self):
        return self.__uiSuffix

    @uiSuffix.setter
    def uiSuffix(self, uiSuffix: str):
        self.__uiSuffix = uiSuffix


    @property
    def osgiVersionQualifier(self):
        return self.__osgiVersionQualifier

    @osgiVersionQualifier.setter
    def osgiVersionQualifier(self, osgiVersionQualifier: str):
        self.__osgiVersionQualifier = osgiVersionQualifier


    @property
    def tychoVersion(self):
        return self.__tychoVersion

    @tychoVersion.setter
    def tychoVersion(self, tychoVersion: str):
        self.__tychoVersion = tychoVersion


    @property
    def targetId(self):
        return self.__targetId

    @targetId.setter
    def targetId(self, targetId: str):
        self.__targetId = targetId


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def isUpdateSiteUrlEmpty(self):
        return self.__isUpdateSiteUrlEmpty

    @isUpdateSiteUrlEmpty.setter
    def isUpdateSiteUrlEmpty(self, isUpdateSiteUrlEmpty: bool):
        self.__isUpdateSiteUrlEmpty = isUpdateSiteUrlEmpty


    @property
    def updateSiteUrl(self):
        return self.__updateSiteUrl

    @updateSiteUrl.setter
    def updateSiteUrl(self, updateSiteUrl: str):
        self.__updateSiteUrl = updateSiteUrl


    @property
    def generateUpdatesite(self):
        return self.__generateUpdatesite

    @generateUpdatesite.setter
    def generateUpdatesite(self, generateUpdatesite: bool):
        self.__generateUpdatesite = generateUpdatesite


    @property
    def coreModuleName(self):
        return self.__coreModuleName

    @coreModuleName.setter
    def coreModuleName(self, coreModuleName: str):
        self.__coreModuleName = coreModuleName


    @property
    def generateTests(self):
        return self.__generateTests

    @generateTests.setter
    def generateTests(self, generateTests: bool):
        self.__generateTests = generateTests


    @property
    def mavenGroupId(self):
        return self.__mavenGroupId

    @mavenGroupId.setter
    def mavenGroupId(self, mavenGroupId: str):
        self.__mavenGroupId = mavenGroupId


    @property
    def coreId(self):
        return self.__coreId

    @coreId.setter
    def coreId(self, coreId: str):
        self.__coreId = coreId


    @property
    def featureId(self):
        return self.__featureId

    @featureId.setter
    def featureId(self, featureId: str):
        self.__featureId = featureId


    @property
    def osgiVersion(self):
        return self.__osgiVersion

    @osgiVersion.setter
    def osgiVersion(self, osgiVersion: str):
        self.__osgiVersion = osgiVersion


    @property
    def moduleName(self):
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName


    @property
    def javaVersion(self):
        return self.__javaVersion

    @javaVersion.setter
    def javaVersion(self, javaVersion: str):
        self.__javaVersion = javaVersion


    @property
    def categoryName(self):
        return self.__categoryName

    @categoryName.setter
    def categoryName(self, categoryName: str):
        self.__categoryName = categoryName

