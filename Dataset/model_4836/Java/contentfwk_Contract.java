





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Contract extends Element {

    private String qualityOfInformationRequired;
    private String serviceabilityCharacteristics;
    private String reliabilityCharacteristics;
    private String servicesTimes;
    private String behaviorCharacteristics;
    private String interoperabilityCharacteristics;
    private String capacityCharacteristics;
    private String growthPeriod;
    private String privacyCharacteristics;
    private String ServiceNameCaller;
    private String localizationCharacteristics;
    private String throughput;
    private String portabilityCharacteristics;
    private String credibilityCharacteristics;
    private String peakProfileShortTerm;
    private String extensibilityCharacteristics;
    private String recoverabilityCharacteristics;
    private String ServiceNameCalled;
    private String internationalizationCharacteristics;
    private String serviceQualityCharacteristics;
    private String peakProfileLongTerm;
    private String throughputPeriod;
    private String contractControlRequirements;
    private String availabilityQualityCharacteristics;
    private String resultControlRequirements;
    private String securityCharacteristics;
    private String scalabilityCharacteristics;
    private String performanceCharacteristics;
    private String locatabilityCharacteristics;
    private String integrityCharacteristics;
    private String responseCharacteristics;
    private String growth;
    private String manageabilityCharacteristics;





    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;


    public contentfwk_Contract(
        String qualityOfInformationRequired,        String serviceabilityCharacteristics,        String reliabilityCharacteristics,        String servicesTimes,        String behaviorCharacteristics,        String interoperabilityCharacteristics,        String capacityCharacteristics,        String growthPeriod,        String privacyCharacteristics,        String ServiceNameCaller,        String localizationCharacteristics,        String throughput,        String portabilityCharacteristics,        String credibilityCharacteristics,        String peakProfileShortTerm,        String extensibilityCharacteristics,        String recoverabilityCharacteristics,        String ServiceNameCalled,        String internationalizationCharacteristics,        String serviceQualityCharacteristics,        String peakProfileLongTerm,        String throughputPeriod,        String contractControlRequirements,        String availabilityQualityCharacteristics,        String resultControlRequirements,        String securityCharacteristics,        String scalabilityCharacteristics,        String performanceCharacteristics,        String locatabilityCharacteristics,        String integrityCharacteristics,        String responseCharacteristics,        String growth,        String manageabilityCharacteristics    ) {
        super(
        );
        this.qualityOfInformationRequired = qualityOfInformationRequired;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.servicesTimes = servicesTimes;
        this.behaviorCharacteristics = behaviorCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.privacyCharacteristics = privacyCharacteristics;
        this.ServiceNameCaller = ServiceNameCaller;
        this.localizationCharacteristics = localizationCharacteristics;
        this.throughput = throughput;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.ServiceNameCalled = ServiceNameCalled;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.throughputPeriod = throughputPeriod;
        this.contractControlRequirements = contractControlRequirements;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.resultControlRequirements = resultControlRequirements;
        this.securityCharacteristics = securityCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.responseCharacteristics = responseCharacteristics;
        this.growth = growth;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
    }


    public String getQualityofinformationrequired() {
        return qualityOfInformationRequired;
    }

    public void setQualityofinformationrequired(String qualityOfInformationRequired) {
        this.qualityOfInformationRequired = qualityOfInformationRequired;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getBehaviorcharacteristics() {
        return behaviorCharacteristics;
    }

    public void setBehaviorcharacteristics(String behaviorCharacteristics) {
        this.behaviorCharacteristics = behaviorCharacteristics;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getCapacitycharacteristics() {
        return capacityCharacteristics;
    }

    public void setCapacitycharacteristics(String capacityCharacteristics) {
        this.capacityCharacteristics = capacityCharacteristics;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public String getServicenamecaller() {
        return ServiceNameCaller;
    }

    public void setServicenamecaller(String ServiceNameCaller) {
        this.ServiceNameCaller = ServiceNameCaller;
    }
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getCredibilitycharacteristics() {
        return credibilityCharacteristics;
    }

    public void setCredibilitycharacteristics(String credibilityCharacteristics) {
        this.credibilityCharacteristics = credibilityCharacteristics;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public String getServicenamecalled() {
        return ServiceNameCalled;
    }

    public void setServicenamecalled(String ServiceNameCalled) {
        this.ServiceNameCalled = ServiceNameCalled;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
    }
    public String getServicequalitycharacteristics() {
        return serviceQualityCharacteristics;
    }

    public void setServicequalitycharacteristics(String serviceQualityCharacteristics) {
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
    }
    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public String getContractcontrolrequirements() {
        return contractControlRequirements;
    }

    public void setContractcontrolrequirements(String contractControlRequirements) {
        this.contractControlRequirements = contractControlRequirements;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
    }
    public String getResultcontrolrequirements() {
        return resultControlRequirements;
    }

    public void setResultcontrolrequirements(String resultControlRequirements) {
        this.resultControlRequirements = resultControlRequirements;
    }
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getResponsecharacteristics() {
        return responseCharacteristics;
    }

    public void setResponsecharacteristics(String responseCharacteristics) {
        this.responseCharacteristics = responseCharacteristics;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
    }

    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }

}