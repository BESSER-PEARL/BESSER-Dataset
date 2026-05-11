





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Contract extends Element {

    private String ServiceNameCalled;
    private String growth;
    private String serviceabilityCharacteristics;
    private String performanceCharacteristics;
    private String interoperabilityCharacteristics;
    private String throughputPeriod;
    private String internationalizationCharacteristics;
    private String localizationCharacteristics;
    private String availabilityQualityCharacteristics;
    private String locatabilityCharacteristics;
    private String credibilityCharacteristics;
    private String serviceQualityCharacteristics;
    private String portabilityCharacteristics;
    private String manageabilityCharacteristics;
    private String behaviorCharacteristics;
    private String peakProfileLongTerm;
    private String ServiceNameCaller;
    private String peakProfileShortTerm;
    private String contractControlRequirements;
    private String extensibilityCharacteristics;
    private String servicesTimes;
    private String responseCharacteristics;
    private String integrityCharacteristics;
    private String qualityOfInformationRequired;
    private String recoverabilityCharacteristics;
    private String throughput;
    private String securityCharacteristics;
    private String capacityCharacteristics;
    private String growthPeriod;
    private String scalabilityCharacteristics;
    private String reliabilityCharacteristics;
    private String privacyCharacteristics;
    private String resultControlRequirements;





    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;


    public contentfwk_Contract(
        String ServiceNameCalled,        String growth,        String serviceabilityCharacteristics,        String performanceCharacteristics,        String interoperabilityCharacteristics,        String throughputPeriod,        String internationalizationCharacteristics,        String localizationCharacteristics,        String availabilityQualityCharacteristics,        String locatabilityCharacteristics,        String credibilityCharacteristics,        String serviceQualityCharacteristics,        String portabilityCharacteristics,        String manageabilityCharacteristics,        String behaviorCharacteristics,        String peakProfileLongTerm,        String ServiceNameCaller,        String peakProfileShortTerm,        String contractControlRequirements,        String extensibilityCharacteristics,        String servicesTimes,        String responseCharacteristics,        String integrityCharacteristics,        String qualityOfInformationRequired,        String recoverabilityCharacteristics,        String throughput,        String securityCharacteristics,        String capacityCharacteristics,        String growthPeriod,        String scalabilityCharacteristics,        String reliabilityCharacteristics,        String privacyCharacteristics,        String resultControlRequirements    ) {
        super(
        );
        this.ServiceNameCalled = ServiceNameCalled;
        this.growth = growth;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.behaviorCharacteristics = behaviorCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.ServiceNameCaller = ServiceNameCaller;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.contractControlRequirements = contractControlRequirements;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.servicesTimes = servicesTimes;
        this.responseCharacteristics = responseCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.qualityOfInformationRequired = qualityOfInformationRequired;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.throughput = throughput;
        this.securityCharacteristics = securityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.resultControlRequirements = resultControlRequirements;
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
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
    }
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
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
    public String getServicequalitycharacteristics() {
        return serviceQualityCharacteristics;
    }

    public void setServicequalitycharacteristics(String serviceQualityCharacteristics) {
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
    }
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
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
    public String getServicenamecaller() {
        return ServiceNameCaller;
    }

    public void setServicenamecaller(String ServiceNameCaller) {
        this.ServiceNameCaller = ServiceNameCaller;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getContractcontrolrequirements() {
        return contractControlRequirements;
    }

    public void setContractcontrolrequirements(String contractControlRequirements) {
        this.contractControlRequirements = contractControlRequirements;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getResponsecharacteristics() {
        return responseCharacteristics;
    }

    public void setResponsecharacteristics(String responseCharacteristics) {
        this.responseCharacteristics = responseCharacteristics;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getQualityofinformationrequired() {
        return qualityOfInformationRequired;
    }

    public void setQualityofinformationrequired(String qualityOfInformationRequired) {
        this.qualityOfInformationRequired = qualityOfInformationRequired;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
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
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public String getResultcontrolrequirements() {
        return resultControlRequirements;
    }

    public void setResultcontrolrequirements(String resultControlRequirements) {
        this.resultControlRequirements = resultControlRequirements;
    }

    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }

}