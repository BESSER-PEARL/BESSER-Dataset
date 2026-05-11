




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalApplicationComponent extends ApplicationComponent, Element {

    private String locatabilityCharacteristics;
    private String peakProfileShortTerm;
    private String growth;
    private String credibilityCharacteristics;
    private String peakProfileLongTerm;
    private String throughputPeriod;
    private String portabilityCharacteristics;
    private String interoperabilityCharacteristics;
    private String manageabilityCharacteristics;
    private String localizationCharacteristics;
    private String privacyCharacteristics;
    private String availabilityQualityCharacteristics;
    private String reliabilityCharacteristics;
    private String capacityCharacteristics;
    private String scalabilityCharacteristics;
    private String securityCharacteristics;
    private LocalDate initialLiveDate;
    private String extensibilityCharacteristics;
    private String integrityCharacteristics;
    private String servicesTimes;
    private String throughput;
    private String performanceCharacteristics;
    private String lifeCycleStatus;
    private String growthPeriod;
    private String recoverabilityCharacteristics;
    private LocalDate dateOfLastRelease;
    private LocalDate retirementDate;
    private String serviceabilityCharacteristics;
    private LocalDate dateOfNextRelease;
    private String internationalizationCharacteristics;





    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;




    private List<contentfwk_Location> contentfwk_locations;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private contentfwk_Location contentfwk_location;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;


    public contentfwk_PhysicalApplicationComponent(
        String locatabilityCharacteristics,        String peakProfileShortTerm,        String growth,        String credibilityCharacteristics,        String peakProfileLongTerm,        String throughputPeriod,        String portabilityCharacteristics,        String interoperabilityCharacteristics,        String manageabilityCharacteristics,        String localizationCharacteristics,        String privacyCharacteristics,        String availabilityQualityCharacteristics,        String reliabilityCharacteristics,        String capacityCharacteristics,        String scalabilityCharacteristics,        String securityCharacteristics,        LocalDate initialLiveDate,        String extensibilityCharacteristics,        String integrityCharacteristics,        String servicesTimes,        String throughput,        String performanceCharacteristics,        String lifeCycleStatus,        String growthPeriod,        String recoverabilityCharacteristics,        LocalDate dateOfLastRelease,        LocalDate retirementDate,        String serviceabilityCharacteristics,        LocalDate dateOfNextRelease,        String internationalizationCharacteristics    ) {
        super(
        );
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.growth = growth;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.throughputPeriod = throughputPeriod;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.servicesTimes = servicesTimes;
        this.throughput = throughput;
        this.performanceCharacteristics = performanceCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.growthPeriod = growthPeriod;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.retirementDate = retirementDate;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
        this.contentfwk_locations = new ArrayList<>();
    }

    public contentfwk_PhysicalApplicationComponent(
        String locatabilityCharacteristics,        String peakProfileShortTerm,        String growth,        String credibilityCharacteristics,        String peakProfileLongTerm,        String throughputPeriod,        String portabilityCharacteristics,        String interoperabilityCharacteristics,        String manageabilityCharacteristics,        String localizationCharacteristics,        String privacyCharacteristics,        String availabilityQualityCharacteristics,        String reliabilityCharacteristics,        String capacityCharacteristics,        String scalabilityCharacteristics,        String securityCharacteristics,        LocalDate initialLiveDate,        String extensibilityCharacteristics,        String integrityCharacteristics,        String servicesTimes,        String throughput,        String performanceCharacteristics,        String lifeCycleStatus,        String growthPeriod,        String recoverabilityCharacteristics,        LocalDate dateOfLastRelease,        LocalDate retirementDate,        String serviceabilityCharacteristics,        LocalDate dateOfNextRelease,        String internationalizationCharacteristics        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents,        ArrayList<contentfwk_Location> contentfwk_locations    ) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.growth = growth;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.throughputPeriod = throughputPeriod;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.servicesTimes = servicesTimes;
        this.throughput = throughput;
        this.performanceCharacteristics = performanceCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.growthPeriod = growthPeriod;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.retirementDate = retirementDate;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
        this.contentfwk_locations = contentfwk_locations;
    }

    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
    }
    public String getCredibilitycharacteristics() {
        return credibilityCharacteristics;
    }

    public void setCredibilitycharacteristics(String credibilityCharacteristics) {
        this.credibilityCharacteristics = credibilityCharacteristics;
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
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
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
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
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
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public LocalDate getInitiallivedate() {
        return initialLiveDate;
    }

    public void setInitiallivedate(LocalDate initialLiveDate) {
        this.initialLiveDate = initialLiveDate;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public String getLifecyclestatus() {
        return lifeCycleStatus;
    }

    public void setLifecyclestatus(String lifeCycleStatus) {
        this.lifeCycleStatus = lifeCycleStatus;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public LocalDate getDateoflastrelease() {
        return dateOfLastRelease;
    }

    public void setDateoflastrelease(LocalDate dateOfLastRelease) {
        this.dateOfLastRelease = dateOfLastRelease;
    }
    public LocalDate getRetirementdate() {
        return retirementDate;
    }

    public void setRetirementdate(LocalDate retirementDate) {
        this.retirementDate = retirementDate;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public LocalDate getDateofnextrelease() {
        return dateOfNextRelease;
    }

    public void setDateofnextrelease(LocalDate dateOfNextRelease) {
        this.dateOfNextRelease = dateOfNextRelease;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
    }

    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }
    public List<contentfwk_PhysicalDataComponent> getContentfwk_physicaldatacomponents() {
        return contentfwk_physicaldatacomponents;
    }

    public void addContentfwk_physicaldatacomponent(Contentfwk_physicaldatacomponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponents.add(contentfwk_physicaldatacomponent);
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
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
    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }

}