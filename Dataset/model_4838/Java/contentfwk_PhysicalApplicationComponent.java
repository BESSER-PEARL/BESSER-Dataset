




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalApplicationComponent extends ApplicationComponent, Element {

    private String integrityCharacteristics;
    private String securityCharacteristics;
    private String locatabilityCharacteristics;
    private String reliabilityCharacteristics;
    private String scalabilityCharacteristics;
    private String growth;
    private String extensibilityCharacteristics;
    private LocalDate dateOfNextRelease;
    private String manageabilityCharacteristics;
    private String internationalizationCharacteristics;
    private String localizationCharacteristics;
    private String privacyCharacteristics;
    private String peakProfileLongTerm;
    private String recoverabilityCharacteristics;
    private String portabilityCharacteristics;
    private String lifeCycleStatus;
    private String throughputPeriod;
    private String servicesTimes;
    private String capacityCharacteristics;
    private String serviceabilityCharacteristics;
    private String performanceCharacteristics;
    private LocalDate initialLiveDate;
    private String throughput;
    private String growthPeriod;
    private String availabilityQualityCharacteristics;
    private LocalDate retirementDate;
    private String interoperabilityCharacteristics;
    private String credibilityCharacteristics;
    private String peakProfileShortTerm;
    private LocalDate dateOfLastRelease;





    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;




    private List<contentfwk_Location> contentfwk_locations;




    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;




    private contentfwk_Location contentfwk_location;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;


    public contentfwk_PhysicalApplicationComponent(
        String integrityCharacteristics,        String securityCharacteristics,        String locatabilityCharacteristics,        String reliabilityCharacteristics,        String scalabilityCharacteristics,        String growth,        String extensibilityCharacteristics,        LocalDate dateOfNextRelease,        String manageabilityCharacteristics,        String internationalizationCharacteristics,        String localizationCharacteristics,        String privacyCharacteristics,        String peakProfileLongTerm,        String recoverabilityCharacteristics,        String portabilityCharacteristics,        String lifeCycleStatus,        String throughputPeriod,        String servicesTimes,        String capacityCharacteristics,        String serviceabilityCharacteristics,        String performanceCharacteristics,        LocalDate initialLiveDate,        String throughput,        String growthPeriod,        String availabilityQualityCharacteristics,        LocalDate retirementDate,        String interoperabilityCharacteristics,        String credibilityCharacteristics,        String peakProfileShortTerm,        LocalDate dateOfLastRelease    ) {
        super(
        );
        this.integrityCharacteristics = integrityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.growth = growth;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.throughputPeriod = throughputPeriod;
        this.servicesTimes = servicesTimes;
        this.capacityCharacteristics = capacityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.throughput = throughput;
        this.growthPeriod = growthPeriod;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.retirementDate = retirementDate;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.dateOfLastRelease = dateOfLastRelease;
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_locations = new ArrayList<>();
    }

    public contentfwk_PhysicalApplicationComponent(
        String integrityCharacteristics,        String securityCharacteristics,        String locatabilityCharacteristics,        String reliabilityCharacteristics,        String scalabilityCharacteristics,        String growth,        String extensibilityCharacteristics,        LocalDate dateOfNextRelease,        String manageabilityCharacteristics,        String internationalizationCharacteristics,        String localizationCharacteristics,        String privacyCharacteristics,        String peakProfileLongTerm,        String recoverabilityCharacteristics,        String portabilityCharacteristics,        String lifeCycleStatus,        String throughputPeriod,        String servicesTimes,        String capacityCharacteristics,        String serviceabilityCharacteristics,        String performanceCharacteristics,        LocalDate initialLiveDate,        String throughput,        String growthPeriod,        String availabilityQualityCharacteristics,        LocalDate retirementDate,        String interoperabilityCharacteristics,        String credibilityCharacteristics,        String peakProfileShortTerm,        LocalDate dateOfLastRelease        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_Location> contentfwk_locations    ) {
        this.integrityCharacteristics = integrityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.growth = growth;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.throughputPeriod = throughputPeriod;
        this.servicesTimes = servicesTimes;
        this.capacityCharacteristics = capacityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.throughput = throughput;
        this.growthPeriod = growthPeriod;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.retirementDate = retirementDate;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.dateOfLastRelease = dateOfLastRelease;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_locations = contentfwk_locations;
    }

    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
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
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public LocalDate getDateofnextrelease() {
        return dateOfNextRelease;
    }

    public void setDateofnextrelease(LocalDate dateOfNextRelease) {
        this.dateOfNextRelease = dateOfNextRelease;
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
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getLifecyclestatus() {
        return lifeCycleStatus;
    }

    public void setLifecyclestatus(String lifeCycleStatus) {
        this.lifeCycleStatus = lifeCycleStatus;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getCapacitycharacteristics() {
        return capacityCharacteristics;
    }

    public void setCapacitycharacteristics(String capacityCharacteristics) {
        this.capacityCharacteristics = capacityCharacteristics;
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
    public LocalDate getInitiallivedate() {
        return initialLiveDate;
    }

    public void setInitiallivedate(LocalDate initialLiveDate) {
        this.initialLiveDate = initialLiveDate;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
    }
    public LocalDate getRetirementdate() {
        return retirementDate;
    }

    public void setRetirementdate(LocalDate retirementDate) {
        this.retirementDate = retirementDate;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
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
    public LocalDate getDateoflastrelease() {
        return dateOfLastRelease;
    }

    public void setDateoflastrelease(LocalDate dateOfLastRelease) {
        this.dateOfLastRelease = dateOfLastRelease;
    }

    public List<contentfwk_PhysicalDataComponent> getContentfwk_physicaldatacomponents() {
        return contentfwk_physicaldatacomponents;
    }

    public void addContentfwk_physicaldatacomponent(Contentfwk_physicaldatacomponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponents.add(contentfwk_physicaldatacomponent);
    }
    public List<contentfwk_LogicalApplicationComponent> getContentfwk_logicalapplicationcomponents() {
        return contentfwk_logicalapplicationcomponents;
    }

    public void addContentfwk_logicalapplicationcomponent(Contentfwk_logicalapplicationcomponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponents.add(contentfwk_logicalapplicationcomponent);
    }
    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }
    public contentfwk_ApplicationArchitecture getContentfwk_applicationarchitecture() {
        return contentfwk_applicationarchitecture;
    }

    public void setContentfwk_applicationarchitecture(contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture) {
        this.contentfwk_applicationarchitecture = contentfwk_applicationarchitecture;
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }
    public contentfwk_LogicalApplicationComponent getContentfwk_logicalapplicationcomponent() {
        return contentfwk_logicalapplicationcomponent;
    }

    public void setContentfwk_logicalapplicationcomponent(contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponent = contentfwk_logicalapplicationcomponent;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
    }
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }

}