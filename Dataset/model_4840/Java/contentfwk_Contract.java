





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Contract extends Element {

    private String ServiceNameCaller;
    private String interoperabilityCharacteristics;
    private String resultControlRequirements;
    private String servicesTimes;
    private String throughputPeriod;
    private String serviceabilityCharacteristics;
    private String recoverabilityCharacteristics;
    private String reliabilityCharacteristics;
    private String integrityCharacteristics;
    private String ServiceNameCalled;
    private String growth;
    private String contractControlRequirements;
    private String behaviorCharacteristics;
    private String peakProfileLongTerm;
    private String manageabilityCharacteristics;
    private String capacityCharacteristics;
    private String securityCharacteristics;
    private String locatabilityCharacteristics;
    private String credibilityCharacteristics;
    private String extensibilityCharacteristics;
    private String peakProfileShortTerm;
    private String qualityOfInformationRequired;
    private String availabilityQualityCharacteristics;
    private String throughput;
    private String internationalizationCharacteristics;
    private String growthPeriod;
    private String privacyCharacteristics;
    private String scalabilityCharacteristics;
    private String portabilityCharacteristics;
    private String localizationCharacteristics;
    private String responseCharacteristics;
    private String serviceQualityCharacteristics;
    private String performanceCharacteristics;





    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;


    public contentfwk_Contract(
        String ServiceNameCaller,        String interoperabilityCharacteristics,        String resultControlRequirements,        String servicesTimes,        String throughputPeriod,        String serviceabilityCharacteristics,        String recoverabilityCharacteristics,        String reliabilityCharacteristics,        String integrityCharacteristics,        String ServiceNameCalled,        String growth,        String contractControlRequirements,        String behaviorCharacteristics,        String peakProfileLongTerm,        String manageabilityCharacteristics,        String capacityCharacteristics,        String securityCharacteristics,        String locatabilityCharacteristics,        String credibilityCharacteristics,        String extensibilityCharacteristics,        String peakProfileShortTerm,        String qualityOfInformationRequired,        String availabilityQualityCharacteristics,        String throughput,        String internationalizationCharacteristics,        String growthPeriod,        String privacyCharacteristics,        String scalabilityCharacteristics,        String portabilityCharacteristics,        String localizationCharacteristics,        String responseCharacteristics,        String serviceQualityCharacteristics,        String performanceCharacteristics    ) {
        super(
        );
        this.ServiceNameCaller = ServiceNameCaller;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.resultControlRequirements = resultControlRequirements;
        this.servicesTimes = servicesTimes;
        this.throughputPeriod = throughputPeriod;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.ServiceNameCalled = ServiceNameCalled;
        this.growth = growth;
        this.contractControlRequirements = contractControlRequirements;
        this.behaviorCharacteristics = behaviorCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.qualityOfInformationRequired = qualityOfInformationRequired;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.throughput = throughput;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.growthPeriod = growthPeriod;
        this.privacyCharacteristics = privacyCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.responseCharacteristics = responseCharacteristics;
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
    }


    public String getServicenamecaller() {
        return ServiceNameCaller;
    }

    public void setServicenamecaller(String ServiceNameCaller) {
        this.ServiceNameCaller = ServiceNameCaller;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getResultcontrolrequirements() {
        return resultControlRequirements;
    }

    public void setResultcontrolrequirements(String resultControlRequirements) {
        this.resultControlRequirements = resultControlRequirements;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getServicenamecalled() {
        return ServiceNameCalled;
    }

    public void setServicenamecalled(String ServiceNameCalled) {
        this.ServiceNameCalled = ServiceNameCalled;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
    }
    public String getContractcontrolrequirements() {
        return contractControlRequirements;
    }

    public void setContractcontrolrequirements(String contractControlRequirements) {
        this.contractControlRequirements = contractControlRequirements;
    }
    public String getBehaviorcharacteristics() {
        return behaviorCharacteristics;
    }

    public void setBehaviorcharacteristics(String behaviorCharacteristics) {
        this.behaviorCharacteristics = behaviorCharacteristics;
    }
    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
    }
    public String getCapacitycharacteristics() {
        return capacityCharacteristics;
    }

    public void setCapacitycharacteristics(String capacityCharacteristics) {
        this.capacityCharacteristics = capacityCharacteristics;
    }
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getCredibilitycharacteristics() {
        return credibilityCharacteristics;
    }

    public void setCredibilitycharacteristics(String credibilityCharacteristics) {
        this.credibilityCharacteristics = credibilityCharacteristics;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getQualityofinformationrequired() {
        return qualityOfInformationRequired;
    }

    public void setQualityofinformationrequired(String qualityOfInformationRequired) {
        this.qualityOfInformationRequired = qualityOfInformationRequired;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
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
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public String getResponsecharacteristics() {
        return responseCharacteristics;
    }

    public void setResponsecharacteristics(String responseCharacteristics) {
        this.responseCharacteristics = responseCharacteristics;
    }
    public String getServicequalitycharacteristics() {
        return serviceQualityCharacteristics;
    }

    public void setServicequalitycharacteristics(String serviceQualityCharacteristics) {
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }

    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }

}