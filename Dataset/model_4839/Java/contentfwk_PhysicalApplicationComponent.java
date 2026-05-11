




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalApplicationComponent extends Element, ApplicationComponent {

    private String availabilityQualityCharacteristics;
    private String peakProfileShortTerm;
    private String peakProfileLongTerm;
    private String securityCharacteristics;
    private String integrityCharacteristics;
    private String capacityCharacteristics;
    private String recoverabilityCharacteristics;
    private String serviceabilityCharacteristics;
    private String interoperabilityCharacteristics;
    private String privacyCharacteristics;
    private String localizationCharacteristics;
    private String servicesTimes;
    private String throughputPeriod;
    private String scalabilityCharacteristics;
    private String locatabilityCharacteristics;
    private LocalDate dateOfLastRelease;
    private String manageabilityCharacteristics;
    private String internationalizationCharacteristics;
    private String growthPeriod;
    private String credibilityCharacteristics;
    private String growth;
    private String performanceCharacteristics;
    private LocalDate initialLiveDate;
    private String lifeCycleStatus;
    private String portabilityCharacteristics;
    private String extensibilityCharacteristics;
    private LocalDate retirementDate;
    private String reliabilityCharacteristics;
    private LocalDate dateOfNextRelease;
    private String throughput;





    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;


    public contentfwk_PhysicalApplicationComponent(
        String availabilityQualityCharacteristics,        String peakProfileShortTerm,        String peakProfileLongTerm,        String securityCharacteristics,        String integrityCharacteristics,        String capacityCharacteristics,        String recoverabilityCharacteristics,        String serviceabilityCharacteristics,        String interoperabilityCharacteristics,        String privacyCharacteristics,        String localizationCharacteristics,        String servicesTimes,        String throughputPeriod,        String scalabilityCharacteristics,        String locatabilityCharacteristics,        LocalDate dateOfLastRelease,        String manageabilityCharacteristics,        String internationalizationCharacteristics,        String growthPeriod,        String credibilityCharacteristics,        String growth,        String performanceCharacteristics,        LocalDate initialLiveDate,        String lifeCycleStatus,        String portabilityCharacteristics,        String extensibilityCharacteristics,        LocalDate retirementDate,        String reliabilityCharacteristics,        LocalDate dateOfNextRelease,        String throughput    ) {
        super(
        );
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.securityCharacteristics = securityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.servicesTimes = servicesTimes;
        this.throughputPeriod = throughputPeriod;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.growthPeriod = growthPeriod;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.growth = growth;
        this.performanceCharacteristics = performanceCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.lifeCycleStatus = lifeCycleStatus;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.retirementDate = retirementDate;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.throughput = throughput;
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalApplicationComponent(
        String availabilityQualityCharacteristics,        String peakProfileShortTerm,        String peakProfileLongTerm,        String securityCharacteristics,        String integrityCharacteristics,        String capacityCharacteristics,        String recoverabilityCharacteristics,        String serviceabilityCharacteristics,        String interoperabilityCharacteristics,        String privacyCharacteristics,        String localizationCharacteristics,        String servicesTimes,        String throughputPeriod,        String scalabilityCharacteristics,        String locatabilityCharacteristics,        LocalDate dateOfLastRelease,        String manageabilityCharacteristics,        String internationalizationCharacteristics,        String growthPeriod,        String credibilityCharacteristics,        String growth,        String performanceCharacteristics,        LocalDate initialLiveDate,        String lifeCycleStatus,        String portabilityCharacteristics,        String extensibilityCharacteristics,        LocalDate retirementDate,        String reliabilityCharacteristics,        LocalDate dateOfNextRelease,        String throughput        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents    ) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.securityCharacteristics = securityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.servicesTimes = servicesTimes;
        this.throughputPeriod = throughputPeriod;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.growthPeriod = growthPeriod;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.growth = growth;
        this.performanceCharacteristics = performanceCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.lifeCycleStatus = lifeCycleStatus;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.retirementDate = retirementDate;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.throughput = throughput;
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
    }

    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
    }
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getCapacitycharacteristics() {
        return capacityCharacteristics;
    }

    public void setCapacitycharacteristics(String capacityCharacteristics) {
        this.capacityCharacteristics = capacityCharacteristics;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
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
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public LocalDate getDateoflastrelease() {
        return dateOfLastRelease;
    }

    public void setDateoflastrelease(LocalDate dateOfLastRelease) {
        this.dateOfLastRelease = dateOfLastRelease;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
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
    public String getCredibilitycharacteristics() {
        return credibilityCharacteristics;
    }

    public void setCredibilitycharacteristics(String credibilityCharacteristics) {
        this.credibilityCharacteristics = credibilityCharacteristics;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public LocalDate getInitiallivedate() {
        return initialLiveDate;
    }

    public void setInitiallivedate(LocalDate initialLiveDate) {
        this.initialLiveDate = initialLiveDate;
    }
    public String getLifecyclestatus() {
        return lifeCycleStatus;
    }

    public void setLifecyclestatus(String lifeCycleStatus) {
        this.lifeCycleStatus = lifeCycleStatus;
    }
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public LocalDate getRetirementdate() {
        return retirementDate;
    }

    public void setRetirementdate(LocalDate retirementDate) {
        this.retirementDate = retirementDate;
    }
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public LocalDate getDateofnextrelease() {
        return dateOfNextRelease;
    }

    public void setDateofnextrelease(LocalDate dateOfNextRelease) {
        this.dateOfNextRelease = dateOfNextRelease;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }

    public contentfwk_LogicalApplicationComponent getContentfwk_logicalapplicationcomponent() {
        return contentfwk_logicalapplicationcomponent;
    }

    public void setContentfwk_logicalapplicationcomponent(contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponent = contentfwk_logicalapplicationcomponent;
    }
    public List<contentfwk_PhysicalApplicationComponent> getContentfwk_physicalapplicationcomponents() {
        return contentfwk_physicalapplicationcomponents;
    }

    public void addContentfwk_physicalapplicationcomponent(Contentfwk_physicalapplicationcomponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponents.add(contentfwk_physicalapplicationcomponent);
    }
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }
    public List<contentfwk_LogicalApplicationComponent> getContentfwk_logicalapplicationcomponents() {
        return contentfwk_logicalapplicationcomponents;
    }

    public void addContentfwk_logicalapplicationcomponent(Contentfwk_logicalapplicationcomponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponents.add(contentfwk_logicalapplicationcomponent);
    }

}