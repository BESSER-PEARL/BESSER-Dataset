




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalApplicationComponent extends Element, ApplicationComponent {

    private String portabilityCharacteristics;
    private String peakProfileShortTerm;
    private LocalDate retirementDate;
    private String manageabilityCharacteristics;
    private LocalDate dateOfNextRelease;
    private String interoperabilityCharacteristics;
    private String growthPeriod;
    private String performanceCharacteristics;
    private LocalDate dateOfLastRelease;
    private String servicesTimes;
    private String reliabilityCharacteristics;
    private String integrityCharacteristics;
    private String privacyCharacteristics;
    private String credibilityCharacteristics;
    private String localizationCharacteristics;
    private String peakProfileLongTerm;
    private String recoverabilityCharacteristics;
    private String availabilityCharacteristics;
    private String throughput;
    private String scalabilityCharacteristics;
    private String growth;
    private String serviceabilityCharacteristics;
    private String extensibilityCharacteristics;
    private LocalDate initialLiveDate;
    private String locatabilityCharacteristics;
    private String internationalizationCharacteristics;
    private String lifeCycleStatus;
    private String throughputPeriod;
    private String securityCharacteristics;
    private String capacityCharacteristics;





    private contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private List<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private List<contentfwk_Location> contentfwk_locations;




    private contentfwk_Location contentfwk_location;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;


    public contentfwk_PhysicalApplicationComponent(
        String portabilityCharacteristics,        String peakProfileShortTerm,        LocalDate retirementDate,        String manageabilityCharacteristics,        LocalDate dateOfNextRelease,        String interoperabilityCharacteristics,        String growthPeriod,        String performanceCharacteristics,        LocalDate dateOfLastRelease,        String servicesTimes,        String reliabilityCharacteristics,        String integrityCharacteristics,        String privacyCharacteristics,        String credibilityCharacteristics,        String localizationCharacteristics,        String peakProfileLongTerm,        String recoverabilityCharacteristics,        String availabilityCharacteristics,        String throughput,        String scalabilityCharacteristics,        String growth,        String serviceabilityCharacteristics,        String extensibilityCharacteristics,        LocalDate initialLiveDate,        String locatabilityCharacteristics,        String internationalizationCharacteristics,        String lifeCycleStatus,        String throughputPeriod,        String securityCharacteristics,        String capacityCharacteristics    ) {
        super(
        );
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.retirementDate = retirementDate;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.performanceCharacteristics = performanceCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.servicesTimes = servicesTimes;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.availabilityCharacteristics = availabilityCharacteristics;
        this.throughput = throughput;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.growth = growth;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.throughputPeriod = throughputPeriod;
        this.securityCharacteristics = securityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_physicaldatacomponents = new ArrayList<>();
        this.contentfwk_locations = new ArrayList<>();
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalApplicationComponent(
        String portabilityCharacteristics,        String peakProfileShortTerm,        LocalDate retirementDate,        String manageabilityCharacteristics,        LocalDate dateOfNextRelease,        String interoperabilityCharacteristics,        String growthPeriod,        String performanceCharacteristics,        LocalDate dateOfLastRelease,        String servicesTimes,        String reliabilityCharacteristics,        String integrityCharacteristics,        String privacyCharacteristics,        String credibilityCharacteristics,        String localizationCharacteristics,        String peakProfileLongTerm,        String recoverabilityCharacteristics,        String availabilityCharacteristics,        String throughput,        String scalabilityCharacteristics,        String growth,        String serviceabilityCharacteristics,        String extensibilityCharacteristics,        LocalDate initialLiveDate,        String locatabilityCharacteristics,        String internationalizationCharacteristics,        String lifeCycleStatus,        String throughputPeriod,        String securityCharacteristics,        String capacityCharacteristics        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_PhysicalDataComponent> contentfwk_physicaldatacomponents,        ArrayList<contentfwk_Location> contentfwk_locations,        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents    ) {
        this.portabilityCharacteristics = portabilityCharacteristics;
        this.peakProfileShortTerm = peakProfileShortTerm;
        this.retirementDate = retirementDate;
        this.manageabilityCharacteristics = manageabilityCharacteristics;
        this.dateOfNextRelease = dateOfNextRelease;
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
        this.growthPeriod = growthPeriod;
        this.performanceCharacteristics = performanceCharacteristics;
        this.dateOfLastRelease = dateOfLastRelease;
        this.servicesTimes = servicesTimes;
        this.reliabilityCharacteristics = reliabilityCharacteristics;
        this.integrityCharacteristics = integrityCharacteristics;
        this.privacyCharacteristics = privacyCharacteristics;
        this.credibilityCharacteristics = credibilityCharacteristics;
        this.localizationCharacteristics = localizationCharacteristics;
        this.peakProfileLongTerm = peakProfileLongTerm;
        this.recoverabilityCharacteristics = recoverabilityCharacteristics;
        this.availabilityCharacteristics = availabilityCharacteristics;
        this.throughput = throughput;
        this.scalabilityCharacteristics = scalabilityCharacteristics;
        this.growth = growth;
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
        this.extensibilityCharacteristics = extensibilityCharacteristics;
        this.initialLiveDate = initialLiveDate;
        this.locatabilityCharacteristics = locatabilityCharacteristics;
        this.internationalizationCharacteristics = internationalizationCharacteristics;
        this.lifeCycleStatus = lifeCycleStatus;
        this.throughputPeriod = throughputPeriod;
        this.securityCharacteristics = securityCharacteristics;
        this.capacityCharacteristics = capacityCharacteristics;
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_physicaldatacomponents = contentfwk_physicaldatacomponents;
        this.contentfwk_locations = contentfwk_locations;
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
    }

    public String getPortabilitycharacteristics() {
        return portabilityCharacteristics;
    }

    public void setPortabilitycharacteristics(String portabilityCharacteristics) {
        this.portabilityCharacteristics = portabilityCharacteristics;
    }
    public String getPeakprofileshortterm() {
        return peakProfileShortTerm;
    }

    public void setPeakprofileshortterm(String peakProfileShortTerm) {
        this.peakProfileShortTerm = peakProfileShortTerm;
    }
    public LocalDate getRetirementdate() {
        return retirementDate;
    }

    public void setRetirementdate(LocalDate retirementDate) {
        this.retirementDate = retirementDate;
    }
    public String getManageabilitycharacteristics() {
        return manageabilityCharacteristics;
    }

    public void setManageabilitycharacteristics(String manageabilityCharacteristics) {
        this.manageabilityCharacteristics = manageabilityCharacteristics;
    }
    public LocalDate getDateofnextrelease() {
        return dateOfNextRelease;
    }

    public void setDateofnextrelease(LocalDate dateOfNextRelease) {
        this.dateOfNextRelease = dateOfNextRelease;
    }
    public String getInteroperabilitycharacteristics() {
        return interoperabilityCharacteristics;
    }

    public void setInteroperabilitycharacteristics(String interoperabilityCharacteristics) {
        this.interoperabilityCharacteristics = interoperabilityCharacteristics;
    }
    public String getGrowthperiod() {
        return growthPeriod;
    }

    public void setGrowthperiod(String growthPeriod) {
        this.growthPeriod = growthPeriod;
    }
    public String getPerformancecharacteristics() {
        return performanceCharacteristics;
    }

    public void setPerformancecharacteristics(String performanceCharacteristics) {
        this.performanceCharacteristics = performanceCharacteristics;
    }
    public LocalDate getDateoflastrelease() {
        return dateOfLastRelease;
    }

    public void setDateoflastrelease(LocalDate dateOfLastRelease) {
        this.dateOfLastRelease = dateOfLastRelease;
    }
    public String getServicestimes() {
        return servicesTimes;
    }

    public void setServicestimes(String servicesTimes) {
        this.servicesTimes = servicesTimes;
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
    public String getLocalizationcharacteristics() {
        return localizationCharacteristics;
    }

    public void setLocalizationcharacteristics(String localizationCharacteristics) {
        this.localizationCharacteristics = localizationCharacteristics;
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
    public String getAvailabilitycharacteristics() {
        return availabilityCharacteristics;
    }

    public void setAvailabilitycharacteristics(String availabilityCharacteristics) {
        this.availabilityCharacteristics = availabilityCharacteristics;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
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
    public String getServiceabilitycharacteristics() {
        return serviceabilityCharacteristics;
    }

    public void setServiceabilitycharacteristics(String serviceabilityCharacteristics) {
        this.serviceabilityCharacteristics = serviceabilityCharacteristics;
    }
    public String getExtensibilitycharacteristics() {
        return extensibilityCharacteristics;
    }

    public void setExtensibilitycharacteristics(String extensibilityCharacteristics) {
        this.extensibilityCharacteristics = extensibilityCharacteristics;
    }
    public LocalDate getInitiallivedate() {
        return initialLiveDate;
    }

    public void setInitiallivedate(LocalDate initialLiveDate) {
        this.initialLiveDate = initialLiveDate;
    }
    public String getLocatabilitycharacteristics() {
        return locatabilityCharacteristics;
    }

    public void setLocatabilitycharacteristics(String locatabilityCharacteristics) {
        this.locatabilityCharacteristics = locatabilityCharacteristics;
    }
    public String getInternationalizationcharacteristics() {
        return internationalizationCharacteristics;
    }

    public void setInternationalizationcharacteristics(String internationalizationCharacteristics) {
        this.internationalizationCharacteristics = internationalizationCharacteristics;
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

    public contentfwk_PhysicalDataComponent getContentfwk_physicaldatacomponent() {
        return contentfwk_physicaldatacomponent;
    }

    public void setContentfwk_physicaldatacomponent(contentfwk_PhysicalDataComponent contentfwk_physicaldatacomponent) {
        this.contentfwk_physicaldatacomponent = contentfwk_physicaldatacomponent;
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
    public contentfwk_ApplicationArchitecture getContentfwk_applicationarchitecture() {
        return contentfwk_applicationarchitecture;
    }

    public void setContentfwk_applicationarchitecture(contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture) {
        this.contentfwk_applicationarchitecture = contentfwk_applicationarchitecture;
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
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public List<contentfwk_PhysicalApplicationComponent> getContentfwk_physicalapplicationcomponents() {
        return contentfwk_physicalapplicationcomponents;
    }

    public void addContentfwk_physicalapplicationcomponent(Contentfwk_physicalapplicationcomponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponents.add(contentfwk_physicalapplicationcomponent);
    }

}