





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Contract extends Element {

    private String behaviorCharacteristics;
    private String qualityOfInformationRequired;
    private String interoperabilityCharacteristics;
    private String serviceabilityCharacteristics;
    private String contractControlRequirements;
    private String locatabilityCharacteristics;
    private String recoverabilityCharacteristics;
    private String manageabilityCharacteristics;
    private String reliabilityCharacteristics;
    private String performanceCharacteristics;
    private String throughput;
    private String servicesTimes;
    private String extensibilityCharacteristics;
    private String throughputPeriod;
    private String ServiceNameCaller;
    private String portabilityCharacteristics;
    private String securityCharacteristics;
    private String privacyCharacteristics;
    private String credibilityCharacteristics;
    private String ServiceNameCalled;
    private String serviceQualityCharacteristics;
    private String capacityCharacteristics;
    private String availabilityQualityCharacteristics;
    private String peakProfileLongTerm;
    private String integrityCharacteristics;
    private String growth;
    private String responseCharacteristics;
    private String localizationCharacteristics;
    private String resultControlRequirements;
    private String growthPeriod;
    private String peakProfileShortTerm;
    private String internationalizationCharacteristics;
    private String scalabilityCharacteristics;





    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Service contentfwk_service;




    private List<contentfwk_Service> contentfwk_services;


    public contentfwk_Contract(
        String behaviorCharacteristics,        String qualityOfInformationRequired,        String interoperabilityCharacteristics,        String serviceabilityCharacteristics,        String contractControlRequirements,        String locatabilityCharacteristics,        String recoverabilityCharacteristics,        String manageabilityCharacteristics,        String reliabilityCharacteristics,        String performanceCharacteristics,        String throughput,        String servicesTimes,        String extensibilityCharacteristics,        String throughputPeriod,        String ServiceNameCaller,        String portabilityCharacteristics,        String securityCharacteristics,        String privacyCharacteristics,        String credibilityCharacteristics,        String ServiceNameCalled,        String serviceQualityCharacteristics,        String capacityCharacteristics,        String availabilityQualityCharacteristics,        String peakProfileLongTerm,        String integrityCharacteristics,        String growth,        String responseCharacteristics,        String localizationCharacteristics,        String resultControlRequirements,        String growthPeriod,        String peakProfileShortTerm,        String internationalizationCharacteristics,        String scalabilityCharacteristics    ) {
        super(
        );
        this.behaviorCharacteristics = behaviorCharacteristics;
        this.qualityOfInformationRequired = qualityOfInformationRequired;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.contractControlRequirements = contractControlRequirements;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.throughput = throughput;
        this.servicesTimes = servicesTimes;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.ServiceNameCaller = ServiceNameCaller;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.ServiceNameCalled = ServiceNameCalled;
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.integrityCharacteristics = integrityCharacteristics;
        this.growth = growth;
        this.responseCharacteristics = responseCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.resultControlRequirements = resultControlRequirements;
        this.growthPeriod = growthPeriod;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.contentfwk_services = new ArrayList<>();
    }

    public contentfwk_Contract(
        String behaviorCharacteristics,        String qualityOfInformationRequired,        String interoperabilityCharacteristics,        String serviceabilityCharacteristics,        String contractControlRequirements,        String locatabilityCharacteristics,        String recoverabilityCharacteristics,        String manageabilityCharacteristics,        String reliabilityCharacteristics,        String performanceCharacteristics,        String throughput,        String servicesTimes,        String extensibilityCharacteristics,        String throughputPeriod,        String ServiceNameCaller,        String portabilityCharacteristics,        String securityCharacteristics,        String privacyCharacteristics,        String credibilityCharacteristics,        String ServiceNameCalled,        String serviceQualityCharacteristics,        String capacityCharacteristics,        String availabilityQualityCharacteristics,        String peakProfileLongTerm,        String integrityCharacteristics,        String growth,        String responseCharacteristics,        String localizationCharacteristics,        String resultControlRequirements,        String growthPeriod,        String peakProfileShortTerm,        String internationalizationCharacteristics,        String scalabilityCharacteristics        ArrayList<contentfwk_Service> contentfwk_services    ) {
        this.behaviorCharacteristics = behaviorCharacteristics;
        this.qualityOfInformationRequired = qualityOfInformationRequired;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.contractControlRequirements = contractControlRequirements;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.throughput = throughput;
        this.servicesTimes = servicesTimes;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.ServiceNameCaller = ServiceNameCaller;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.ServiceNameCalled = ServiceNameCalled;
        this.serviceQualityCharacteristics = serviceQualityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.integrityCharacteristics = integrityCharacteristics;
        this.growth = growth;
        this.responseCharacteristics = responseCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.resultControlRequirements = resultControlRequirements;
        this.growthPeriod = growthPeriod;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.contentfwk_services = contentfwk_services;
    }

    public String getBehaviorcharacteristics() {
        return behaviorCharacteristics;
    }

    public void setBehaviorcharacteristics(String behaviorCharacteristics) {
        this.behaviorCharacteristics = behaviorCharacteristics;
    }
    public String getQualityofinformationrequired() {
        return qualityOfInformationRequired;
    }

    public void setQualityofinformationrequired(String qualityOfInformationRequired) {
        this.qualityOfInformationRequired = qualityOfInformationRequired;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getContractcontrolrequirements() {
        return contractControlRequirements;
    }

    public void setContractcontrolrequirements(String contractControlRequirements) {
        this.contractControlRequirements = contractControlRequirements;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
    }
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
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
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public String getCredibilitycharacteristics() {
        return credibilityCharacteristics;
    }

    public void setCredibilitycharacteristics(String credibilityCharacteristics) {
        this.credibilityCharacteristics = credibilityCharacteristics;
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
    public String getCapacitycharacteristics() {
        return capacityCharacteristics;
    }

    public void setCapacitycharacteristics(String capacityCharacteristics) {
        this.capacityCharacteristics = capacityCharacteristics;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
    }
    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
    }
    public String getResponsecharacteristics() {
        return responseCharacteristics;
    }

    public void setResponsecharacteristics(String responseCharacteristics) {
        this.responseCharacteristics = responseCharacteristics;
    }
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public String getResultcontrolrequirements() {
        return resultControlRequirements;
    }

    public void setResultcontrolrequirements(String resultControlRequirements) {
        this.resultControlRequirements = resultControlRequirements;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
    }
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }

    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }

}