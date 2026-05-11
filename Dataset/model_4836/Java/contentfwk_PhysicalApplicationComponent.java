




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalApplicationComponent extends Element, ApplicationComponent {

    private String recoverabilityCharacteristics;
    private String growth;
    private String performanceCharacteristics;
    private LocalDate initialLiveDate;
    private String lifeCycleStatus;
    private String localizationCharacteristics;
    private LocalDate dateOfLastRelease;
    private String peakProfileLongTerm;
    private String manageabilityCharacteristics;
    private String integrityCharacteristics;
    private String serviceabilityCharacteristics;
    private String peakProfileShortTerm;
    private String securityCharacteristics;
    private String growthPeriod;
    private String portabilityCharacteristics;
    private String extensibilityCharacteristics;
    private String credibilityCharacteristics;
    private String reliabilityCharacteristics;
    private String capacityCharacteristics;
    private String throughputPeriod;
    private LocalDate dateOfNextRelease;
    private String servicesTimes;
    private String locatabilityCharacteristics;
    private String interoperabilityCharacteristics;
    private String internationalizationCharacteristics;
    private String throughput;
    private String privacyCharacteristics;
    private LocalDate retirementDate;
    private String scalabilityCharacteristics;
    private String availabilityQualityCharacteristics;





    private List<contentfwk_Location> contentfwk_locations;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_Location contentfwk_location;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;


    public contentfwk_PhysicalApplicationComponent(
        String recoverabilityCharacteristics,        String growth,        String performanceCharacteristics,        LocalDate initialLiveDate,        String lifeCycleStatus,        String localizationCharacteristics,        LocalDate dateOfLastRelease,        String peakProfileLongTerm,        String manageabilityCharacteristics,        String integrityCharacteristics,        String serviceabilityCharacteristics,        String peakProfileShortTerm,        String securityCharacteristics,        String growthPeriod,        String portabilityCharacteristics,        String extensibilityCharacteristics,        String credibilityCharacteristics,        String reliabilityCharacteristics,        String capacityCharacteristics,        String throughputPeriod,        LocalDate dateOfNextRelease,        String servicesTimes,        String locatabilityCharacteristics,        String interoperabilityCharacteristics,        String internationalizationCharacteristics,        String throughput,        String privacyCharacteristics,        LocalDate retirementDate,        String scalabilityCharacteristics,        String availabilityQualityCharacteristics    ) {
        super(
        );
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.growth = growth;
        this.performanceCharacteristics = performanceCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.lifeCycleStatus = lifeCycleStatus;
        this.localizationCharacteristics = localizationCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.securityCharacteristics = securityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.dateOfNextRelease = dateOfNextRelease;
        this.servicesTimes = servicesTimes;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.throughput = throughput;
        this.privacyCharacteristics = privacyCharacteristics;
        this.retirementDate = retirementDate;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.contentfwk_locations = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalApplicationComponent(
        String recoverabilityCharacteristics,        String growth,        String performanceCharacteristics,        LocalDate initialLiveDate,        String lifeCycleStatus,        String localizationCharacteristics,        LocalDate dateOfLastRelease,        String peakProfileLongTerm,        String manageabilityCharacteristics,        String integrityCharacteristics,        String serviceabilityCharacteristics,        String peakProfileShortTerm,        String securityCharacteristics,        String growthPeriod,        String portabilityCharacteristics,        String extensibilityCharacteristics,        String credibilityCharacteristics,        String reliabilityCharacteristics,        String capacityCharacteristics,        String throughputPeriod,        LocalDate dateOfNextRelease,        String servicesTimes,        String locatabilityCharacteristics,        String interoperabilityCharacteristics,        String internationalizationCharacteristics,        String throughput,        String privacyCharacteristics,        LocalDate retirementDate,        String scalabilityCharacteristics,        String availabilityQualityCharacteristics        ArrayList<contentfwk_Location> contentfwk_locations,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents    ) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.growth = growth;
        this.performanceCharacteristics = performanceCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.lifeCycleStatus = lifeCycleStatus;
        this.localizationCharacteristics = localizationCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.securityCharacteristics = securityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.dateOfNextRelease = dateOfNextRelease;
        this.servicesTimes = servicesTimes;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.throughput = throughput;
        this.privacyCharacteristics = privacyCharacteristics;
        this.retirementDate = retirementDate;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.contentfwk_locations = contentfwk_locations;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
    }

    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
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
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public LocalDate getDateoflastrelease() {
        return dateOfLastRelease;
    }

    public void setDateoflastrelease(LocalDate dateOfLastRelease) {
        this.dateOfLastRelease = dateOfLastRelease;
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
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
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
    public String getCredibilitycharacteristics() {
        return credibilityCharacteristics;
    }

    public void setCredibilitycharacteristics(String credibilityCharacteristics) {
        this.credibilityCharacteristics = credibilityCharacteristics;
    }
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getCapacitycharacteristics() {
        return capacityCharacteristics;
    }

    public void setCapacitycharacteristics(String capacityCharacteristics) {
        this.capacityCharacteristics = capacityCharacteristics;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public LocalDate getDateofnextrelease() {
        return dateOfNextRelease;
    }

    public void setDateofnextrelease(LocalDate dateOfNextRelease) {
        this.dateOfNextRelease = dateOfNextRelease;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public LocalDate getRetirementdate() {
        return retirementDate;
    }

    public void setRetirementdate(LocalDate retirementDate) {
        this.retirementDate = retirementDate;
    }
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
    }

    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
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
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
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
    public List<contentfwk_PhysicalDataComponent> getContentfwk_physicaldatacomponents() {
        return contentfwk_physicaldatacomponents;
    }

    public void addContentfwk_physicaldatacomponent(Contentfwk_physicaldatacomponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponents.add(contentfwk_physicaldatacomponent);
    }
    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
    }
    public List<contentfwk_LogicalApplicationComponent> getContentfwk_logicalapplicationcomponents() {
        return contentfwk_logicalapplicationcomponents;
    }

    public void addContentfwk_logicalapplicationcomponent(Contentfwk_logicalapplicationcomponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponents.add(contentfwk_logicalapplicationcomponent);
    }
    public contentfwk_LogicalApplicationComponent getContentfwk_logicalapplicationcomponent() {
        return contentfwk_logicalapplicationcomponent;
    }

    public void setContentfwk_logicalapplicationcomponent(contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponent = contentfwk_logicalapplicationcomponent;
    }

}