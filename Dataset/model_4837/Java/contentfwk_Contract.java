





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Contract extends Element {

    private String peakProfileLongTerm;
    private String internationalizationCharacteristics;
    private String privacyCharacteristics;
    private String throughput;
    private String securityCharacteristics;
    private String contractControlRequirements;
    private String serviceabilityCharacteristics;
    private String availabilityQualityCharacteristics;
    private String recoverabilityCharacteristics;
    private String peakProfileShortTerm;
    private String credibilityCharacteristics;
    private String resultControlRequirements;
    private String qualityOfInformationRequired;
    private String extensibilityCharacteristics;
    private String capacityCharacteristics;
    private String growthPeriod;
    private String reliabilityCharacteristics;
    private String locatabilityCharacteristics;
    private String scalabilityCharacteristics;
    private String behaviorCharacteristics;
    private String localizationCharacteristics;
    private String growth;
    private String servicesTimes;
    private String manageabilityCharacteristics;
    private String ServiceNameCalled;
    private String serviceQualityCharacteristics;
    private String throughputPeriod;
    private String interoperabilityCharacteristics;
    private String integrityCharacteristics;
    private String performanceCharacteristics;
    private String ServiceNameCaller;
    private String portabilityCharacteristics;
    private String responseCharacteristics;





    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;


    public contentfwk_Contract(
        String peakProfileLongTerm,        String internationalizationCharacteristics,        String privacyCharacteristics,        String throughput,        String securityCharacteristics,        String contractControlRequirements,        String serviceabilityCharacteristics,        String availabilityQualityCharacteristics,        String recoverabilityCharacteristics,        String peakProfileShortTerm,        String credibilityCharacteristics,        String resultControlRequirements,        String qualityOfInformationRequired,        String extensibilityCharacteristics,        String capacityCharacteristics,        String growthPeriod,        String reliabilityCharacteristics,        String locatabilityCharacteristics,        String scalabilityCharacteristics,        String behaviorCharacteristics,        String localizationCharacteristics,        String growth,        String servicesTimes,        String manageabilityCharacteristics,        String ServiceNameCalled,        String serviceQualityCharacteristics,        String throughputPeriod,        String interoperabilityCharacteristics,        String integrityCharacteristics,        String performanceCharacteristics,        String ServiceNameCaller,        String portabilityCharacteristics,        String responseCharacteristics    ) {
        super(
        );
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.throughput = throughput;
        this.securityCharacteristics = securityCharacteristics;
        this.contractControlRequirements = contractControlRequirements;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.resultControlRequirements = resultControlRequirements;
        this.qualityOfInformationRequired = qualityOfInformationRequired;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.behaviorCharacteristics = behaviorCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.growth = growth;
        this.servicesTimes = servicesTimes;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.ServiceNameCalled = ServiceNameCalled;
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.ServiceNameCaller = ServiceNameCaller;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.responseCharacteristics = responseCharacteristics;
    }


    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public String getContractcontrolrequirements() {
        return contractControlRequirements;
    }

    public void setContractcontrolrequirements(String contractControlRequirements) {
        this.contractControlRequirements = contractControlRequirements;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getCredibilitycharacteristics() {
        return credibilityCharacteristics;
    }

    public void setCredibilitycharacteristics(String credibilityCharacteristics) {
        this.credibilityCharacteristics = credibilityCharacteristics;
    }
    public String getResultcontrolrequirements() {
        return resultControlRequirements;
    }

    public void setResultcontrolrequirements(String resultControlRequirements) {
        this.resultControlRequirements = resultControlRequirements;
    }
    public String getQualityofinformationrequired() {
        return qualityOfInformationRequired;
    }

    public void setQualityofinformationrequired(String qualityOfInformationRequired) {
        this.qualityOfInformationRequired = qualityOfInformationRequired;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
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
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getBehaviorcharacteristics() {
        return behaviorCharacteristics;
    }

    public void setBehaviorcharacteristics(String behaviorCharacteristics) {
        this.behaviorCharacteristics = behaviorCharacteristics;
    }
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
    }
    public String getServicenamecalled() {
        return ServiceNameCalled;
    }

    public void setServicenamecalled(String ServiceNameCalled) {
        this.ServiceNameCalled = ServiceNameCalled;
    }
    public String getServicequalitycharacteristics() {
        return serviceQualityCharacteristics;
    }

    public void setServicequalitycharacteristics(String serviceQualityCharacteristics) {
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public String getServicenamecaller() {
        return ServiceNameCaller;
    }

    public void setServicenamecaller(String ServiceNameCaller) {
        this.ServiceNameCaller = ServiceNameCaller;
    }
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getResponsecharacteristics() {
        return responseCharacteristics;
    }

    public void setResponsecharacteristics(String responseCharacteristics) {
        this.responseCharacteristics = responseCharacteristics;
    }

    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }

}