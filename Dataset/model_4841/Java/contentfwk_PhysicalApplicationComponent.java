




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalApplicationComponent extends ApplicationComponent, Element {

    private String peakProfileShortTerm;
    private String growthPeriod;
    private String peakProfileLongTerm;
    private String extensibilityCharacteristics;
    private LocalDate dateOfNextRelease;
    private String reliabilityCharacteristics;
    private String integrityCharacteristics;
    private String growth;
    private String performanceCharacteristics;
    private String interoperabilityCharacteristics;
    private LocalDate retirementDate;
    private String locatabilityCharacteristics;
    private String throughputPeriod;
    private LocalDate dateOfLastRelease;
    private String portabilityCharacteristics;
    private String credibilityCharacteristics;
    private String servicesTimes;
    private String securityCharacteristics;
    private LocalDate initialLiveDate;
    private String manageabilityCharacteristics;
    private String localizationCharacteristics;
    private String privacyCharacteristics;
    private String availabilityCharacteristics;
    private String capacityCharacteristics;
    private String recoverabilityCharacteristics;
    private String throughput;
    private String serviceabilityCharacteristics;
    private String lifeCycleStatus;
    private String scalabilityCharacteristics;
    private String internationalizationCharacteristics;





    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;




    private contentfwk_Location contentfwk_location;




    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;




    private List<contentfwk_Location> contentfwk_locations;


    public contentfwk_PhysicalApplicationComponent(
        String peakProfileShortTerm,        String growthPeriod,        String peakProfileLongTerm,        String extensibilityCharacteristics,        LocalDate dateOfNextRelease,        String reliabilityCharacteristics,        String integrityCharacteristics,        String growth,        String performanceCharacteristics,        String interoperabilityCharacteristics,        LocalDate retirementDate,        String locatabilityCharacteristics,        String throughputPeriod,        LocalDate dateOfLastRelease,        String portabilityCharacteristics,        String credibilityCharacteristics,        String servicesTimes,        String securityCharacteristics,        LocalDate initialLiveDate,        String manageabilityCharacteristics,        String localizationCharacteristics,        String privacyCharacteristics,        String availabilityCharacteristics,        String capacityCharacteristics,        String recoverabilityCharacteristics,        String throughput,        String serviceabilityCharacteristics,        String lifeCycleStatus,        String scalabilityCharacteristics,        String internationalizationCharacteristics    ) {
        super(
        );
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.growthPeriod = growthPeriod;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.growth = growth;
        this.performanceCharacteristics = performanceCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.retirementDate = retirementDate;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.dateOfLastRelease = dateOfLastRelease;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.servicesTimes = servicesTimes;
        this.securityCharacteristics = securityCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.availabilityCharacteristics = availabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.throughput = throughput;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_locations = new ArrayList<>();
    }

    public contentfwk_PhysicalApplicationComponent(
        String peakProfileShortTerm,        String growthPeriod,        String peakProfileLongTerm,        String extensibilityCharacteristics,        LocalDate dateOfNextRelease,        String reliabilityCharacteristics,        String integrityCharacteristics,        String growth,        String performanceCharacteristics,        String interoperabilityCharacteristics,        LocalDate retirementDate,        String locatabilityCharacteristics,        String throughputPeriod,        LocalDate dateOfLastRelease,        String portabilityCharacteristics,        String credibilityCharacteristics,        String servicesTimes,        String securityCharacteristics,        LocalDate initialLiveDate,        String manageabilityCharacteristics,        String localizationCharacteristics,        String privacyCharacteristics,        String availabilityCharacteristics,        String capacityCharacteristics,        String recoverabilityCharacteristics,        String throughput,        String serviceabilityCharacteristics,        String lifeCycleStatus,        String scalabilityCharacteristics,        String internationalizationCharacteristics        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents,        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents,        ArrayList<contentfwk_Location> contentfwk_locations    ) {
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.growthPeriod = growthPeriod;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.growth = growth;
        this.performanceCharacteristics = performanceCharacteristics;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.retirementDate = retirementDate;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.throughputPeriod = throughputPeriod;
        this.dateOfLastRelease = dateOfLastRelease;
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.servicesTimes = servicesTimes;
        this.securityCharacteristics = securityCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.availabilityCharacteristics = availabilityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.throughput = throughput;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
        this.contentfwk_locations = contentfwk_locations;
    }

    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
    }
    public String getPeakprofilelongterm() {
        return peakProfileLongTerm;
    }

    public void setPeakprofilelongterm(String peakProfileLongTerm) {
        this.peakProfileLongTerm = peakProfileLongTerm;
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
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public LocalDate getRetirementdate() {
        return retirementDate;
    }

    public void setRetirementdate(LocalDate retirementDate) {
        this.retirementDate = retirementDate;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getThroughputperiod() {
        return throughputPeriod;
    }

    public void setThroughputperiod(String throughputPeriod) {
        this.throughputPeriod = throughputPeriod;
    }
    public LocalDate getDateoflastrelease() {
        return dateOfLastRelease;
    }

    public void setDateoflastrelease(LocalDate dateOfLastRelease) {
        this.dateOfLastRelease = dateOfLastRelease;
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
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
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
    public String getAvailabilitycharacteristics() {
        return availabilityCharacteristics;
    }

    public void setAvailabilitycharacteristics(String availabilityCharacteristics) {
        this.availabilityCharacteristics = availabilityCharacteristics;
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
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getLifecyclestatus() {
        return lifeCycleStatus;
    }

    public void setLifecyclestatus(String lifeCycleStatus) {
        this.lifeCycleStatus = lifeCycleStatus;
    }
    public String getScalabilitycharacteristics() {
        return scalabilityCharacteristics;
    }

    public void setScalabilitycharacteristics(String scalabilityCharacteristics) {
        this.scalabilityCharacteristics = scalabilityCharacteristics;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
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
    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
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
    public contentfwk_ApplicationArchitecture getContentfwk_applicationarchitecture() {
        return contentfwk_applicationarchitecture;
    }

    public void setContentfwk_applicationarchitecture(contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture) {
        this.contentfwk_applicationarchitecture = contentfwk_applicationarchitecture;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public List<contentfwk_PhysicalDataComponent> getContentfwk_physicaldatacomponents() {
        return contentfwk_physicaldatacomponents;
    }

    public void addContentfwk_physicaldatacomponent(Contentfwk_physicaldatacomponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponents.add(contentfwk_physicaldatacomponent);
    }
    public List<contentfwk_PhysicalApplicationComponent> getContentfwk_physicalapplicationcomponents() {
        return contentfwk_physicalapplicationcomponents;
    }

    public void addContentfwk_physicalapplicationcomponent(Contentfwk_physicalapplicationcomponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponents.add(contentfwk_physicalapplicationcomponent);
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }

}