




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalApplicationComponent extends Element, ApplicationComponent {

    private String throughputPeriod;
    private LocalDate initialLiveDate;
    private String integrityCharacteristics;
    private LocalDate dateOfLastRelease;
    private String localizationCharacteristics;
    private String portabilityCharacteristics;
    private String growthPeriod;
    private LocalDate dateOfNextRelease;
    private String extensibilityCharacteristics;
    private LocalDate retirementDate;
    private String scalabilityCharacteristics;
    private String peakProfileLongTerm;
    private String availabilityQualityCharacteristics;
    private String interoperabilityCharacteristics;
    private String credibilityCharacteristics;
    private String lifeCycleStatus;
    private String growth;
    private String throughput;
    private String servicesTimes;
    private String peakProfileShortTerm;
    private String reliabilityCharacteristics;
    private String internationalizationCharacteristics;
    private String locatabilityCharacteristics;
    private String manageabilityCharacteristics;
    private String securityCharacteristics;
    private String serviceabilityCharacteristics;
    private String privacyCharacteristics;
    private String recoverabilityCharacteristics;
    private String performanceCharacteristics;
    private String capacityCharacteristics;





    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private contentfwk_Location contentfwk_location;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private List<contentfwk_Location> contentfwk_locations;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;


    public contentfwk_PhysicalApplicationComponent(
        String throughputPeriod,        LocalDate initialLiveDate,        String integrityCharacteristics,        LocalDate dateOfLastRelease,        String localizationCharacteristics,        String portabilityCharacteristics,        String growthPeriod,        LocalDate dateOfNextRelease,        String extensibilityCharacteristics,        LocalDate retirementDate,        String scalabilityCharacteristics,        String peakProfileLongTerm,        String availabilityQualityCharacteristics,        String interoperabilityCharacteristics,        String credibilityCharacteristics,        String lifeCycleStatus,        String growth,        String throughput,        String servicesTimes,        String peakProfileShortTerm,        String reliabilityCharacteristics,        String internationalizationCharacteristics,        String locatabilityCharacteristics,        String manageabilityCharacteristics,        String securityCharacteristics,        String serviceabilityCharacteristics,        String privacyCharacteristics,        String recoverabilityCharacteristics,        String performanceCharacteristics,        String capacityCharacteristics    ) {
        super(
        );
        this.throughputPeriod = throughputPeriod;
        this.initialLiveDate = initialLiveDate;
        this.integrityCharacteristics = integrityCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.localizationCharacteristics = localizationCharacteristics;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.dateOfNextRelease = dateOfNextRelease;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.retirementDate = retirementDate;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.growth = growth;
        this.throughput = throughput;
        this.servicesTimes = servicesTimes;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.contentfwk_locations = new ArrayList<>();
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalApplicationComponent(
        String throughputPeriod,        LocalDate initialLiveDate,        String integrityCharacteristics,        LocalDate dateOfLastRelease,        String localizationCharacteristics,        String portabilityCharacteristics,        String growthPeriod,        LocalDate dateOfNextRelease,        String extensibilityCharacteristics,        LocalDate retirementDate,        String scalabilityCharacteristics,        String peakProfileLongTerm,        String availabilityQualityCharacteristics,        String interoperabilityCharacteristics,        String credibilityCharacteristics,        String lifeCycleStatus,        String growth,        String throughput,        String servicesTimes,        String peakProfileShortTerm,        String reliabilityCharacteristics,        String internationalizationCharacteristics,        String locatabilityCharacteristics,        String manageabilityCharacteristics,        String securityCharacteristics,        String serviceabilityCharacteristics,        String privacyCharacteristics,        String recoverabilityCharacteristics,        String performanceCharacteristics,        String capacityCharacteristics        ArrayList<contentfwk_Location> contentfwk_locations,        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents    ) {
        this.throughputPeriod = throughputPeriod;
        this.initialLiveDate = initialLiveDate;
        this.integrityCharacteristics = integrityCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.localizationCharacteristics = localizationCharacteristics;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.dateOfNextRelease = dateOfNextRelease;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.retirementDate = retirementDate;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.growth = growth;
        this.throughput = throughput;
        this.servicesTimes = servicesTimes;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.securityCharacteristics = securityCharacteristics;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.performanceCharacteristics = performanceCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.contentfwk_locations = contentfwk_locations;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
    }

    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public LocalDate getInitiallivedate() {
        return initialLiveDate;
    }

    public void setInitiallivedate(LocalDate initialLiveDate) {
        this.initialLiveDate = initialLiveDate;
    }
    public String getIntegritycharacteristics() {
        return integrityCharacteristics;
    }

    public void setIntegritycharacteristics(String integrityCharacteristics) {
        this.integrityCharacteristics = integrityCharacteristics;
    }
    public LocalDate getDateoflastrelease() {
        return dateOfLastRelease;
    }

    public void setDateoflastrelease(LocalDate dateOfLastRelease) {
        this.dateOfLastRelease = dateOfLastRelease;
    }
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
    }
    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
    }
    public LocalDate getDateofnextrelease() {
        return dateOfNextRelease;
    }

    public void setDateofnextrelease(LocalDate dateOfNextRelease) {
        this.dateOfNextRelease = dateOfNextRelease;
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
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
    }
    public String getAvailabilityqualitycharacteristics() {
        return availabilityQualityCharacteristics;
    }

    public void setAvailabilityqualitycharacteristics(String availabilityQualityCharacteristics) {
        this.availabilityQualityCharacteristics = availabilityQualityCharacteristics;
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
    public String getLifecyclestatus() {
        return lifeCycleStatus;
    }

    public void setLifecyclestatus(String lifeCycleStatus) {
        this.lifeCycleStatus = lifeCycleStatus;
    }
    public String getGrowth() {
        return growth;
    }

    public void setGrowth(String growth) {
        this.growth = growth;
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
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getReliabilitycharacteristics() {
        return reliabilityCharacteristics;
    }

    public void setReliabilitycharacteristics(String reliabilityCharacteristics) {
        this.reliabilityCharacteristics = reliabilityCharacteristics;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
    }
    public String getSecuritycharacteristics() {
        return securityCharacteristics;
    }

    public void setSecuritycharacteristics(String securityCharacteristics) {
        this.securityCharacteristics = securityCharacteristics;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getPrivacycharacteristics() {
        return privacyCharacteristics;
    }

    public void setPrivacycharacteristics(String privacyCharacteristics) {
        this.privacyCharacteristics = privacyCharacteristics;
    }
    public String getRecoverabilitycharacteristics() {
        return recoverabilityCharacteristics;
    }

    public void setRecoverabilitycharacteristics(String recoverabilityCharacteristics) {
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public String getCapacitycharacteristics() {
        return capacityCharacteristics;
    }

    public void setCapacitycharacteristics(String capacityCharacteristics) {
        this.capacityCharacteristics = capacityCharacteristics;
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
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_ApplicationArchitecture getContentfwk_applicationarchitecture() {
        return contentfwk_applicationarchitecture;
    }

    public void setContentfwk_applicationarchitecture(contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture) {
        this.contentfwk_applicationarchitecture = contentfwk_applicationarchitecture;
    }
    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
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
    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }

}