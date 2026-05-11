





import java.util.List;
import java.util.ArrayList;

public class aadl2_PackageSection extends Namespace {

    private String noAnnexes;
    private String imports;
    private String aliases;
    private String noProperties;
    private String declarations;





    private List<aadl2_ComponentTypeRename> aadl2_componenttyperenames;




    private List<aadl2_FeatureGroupTypeRename> aadl2_featuregrouptyperenames;




    private List<aadl2_VirtualBusType> aadl2_virtualbustypes;




    private List<aadl2_BusImplementation> aadl2_busimplementations;




    private List<aadl2_SubprogramType> aadl2_subprogramtypes;




    private List<aadl2_Classifier> aadl2_classifiers;




    private List<aadl2_DeviceType> aadl2_devicetypes;




    private List<aadl2_SystemImplementation> aadl2_systemimplementations;




    private List<aadl2_PackageRename> aadl2_packagerenames;




    private List<aadl2_ThreadGroupType> aadl2_threadgrouptypes;




    private List<aadl2_DataImplementation> aadl2_dataimplementations;




    private List<aadl2_ProcessorImplementation> aadl2_processorimplementations;




    private List<aadl2_MemoryType> aadl2_memorytypes;




    private List<aadl2_VirtualProcessorImplementation> aadl2_virtualprocessorimplementations;




    private List<aadl2_VirtualProcessorType> aadl2_virtualprocessortypes;




    private List<aadl2_AnnexLibrary> aadl2_annexlibrarys;




    private List<aadl2_ProcessorType> aadl2_processortypes;




    private List<aadl2_PropertySet> aadl2_propertysets;




    private List<aadl2_ProcessImplementation> aadl2_processimplementations;




    private List<aadl2_AadlPackage> aadl2_aadlpackages;




    private List<aadl2_VirtualBusImplementation> aadl2_virtualbusimplementations;




    private List<aadl2_ThreadImplementation> aadl2_threadimplementations;




    private List<aadl2_MemoryImplementation> aadl2_memoryimplementations;




    private List<aadl2_SubprogramGroupImplementation> aadl2_subprogramgroupimplementations;




    private List<aadl2_DataType> aadl2_datatypes;




    private List<aadl2_ThreadGroupImplementation> aadl2_threadgroupimplementations;




    private List<aadl2_SubprogramImplementation> aadl2_subprogramimplementations;




    private List<aadl2_BusType> aadl2_bustypes;




    private List<aadl2_SystemType> aadl2_systemtypes;




    private List<aadl2_ThreadType> aadl2_threadtypes;




    private List<aadl2_AbstractType> aadl2_abstracttypes;




    private List<aadl2_ProcessType> aadl2_processtypes;




    private List<aadl2_AbstractImplementation> aadl2_abstractimplementations;




    private List<aadl2_SubprogramGroupType> aadl2_subprogramgrouptypes;




    private List<aadl2_DeviceImplementation> aadl2_deviceimplementations;


    public aadl2_PackageSection(
        String noAnnexes,        String imports,        String aliases,        String noProperties,        String declarations    ) {
        super(
        );
        this.noAnnexes = noAnnexes;
        this.imports = imports;
        this.aliases = aliases;
        this.noProperties = noProperties;
        this.declarations = declarations;
        this.aadl2_componenttyperenames = new ArrayList<>();
        this.aadl2_featuregrouptyperenames = new ArrayList<>();
        this.aadl2_virtualbustypes = new ArrayList<>();
        this.aadl2_busimplementations = new ArrayList<>();
        this.aadl2_subprogramtypes = new ArrayList<>();
        this.aadl2_classifiers = new ArrayList<>();
        this.aadl2_devicetypes = new ArrayList<>();
        this.aadl2_systemimplementations = new ArrayList<>();
        this.aadl2_packagerenames = new ArrayList<>();
        this.aadl2_threadgrouptypes = new ArrayList<>();
        this.aadl2_dataimplementations = new ArrayList<>();
        this.aadl2_processorimplementations = new ArrayList<>();
        this.aadl2_memorytypes = new ArrayList<>();
        this.aadl2_virtualprocessorimplementations = new ArrayList<>();
        this.aadl2_virtualprocessortypes = new ArrayList<>();
        this.aadl2_annexlibrarys = new ArrayList<>();
        this.aadl2_processortypes = new ArrayList<>();
        this.aadl2_propertysets = new ArrayList<>();
        this.aadl2_processimplementations = new ArrayList<>();
        this.aadl2_aadlpackages = new ArrayList<>();
        this.aadl2_virtualbusimplementations = new ArrayList<>();
        this.aadl2_threadimplementations = new ArrayList<>();
        this.aadl2_memoryimplementations = new ArrayList<>();
        this.aadl2_subprogramgroupimplementations = new ArrayList<>();
        this.aadl2_datatypes = new ArrayList<>();
        this.aadl2_threadgroupimplementations = new ArrayList<>();
        this.aadl2_subprogramimplementations = new ArrayList<>();
        this.aadl2_bustypes = new ArrayList<>();
        this.aadl2_systemtypes = new ArrayList<>();
        this.aadl2_threadtypes = new ArrayList<>();
        this.aadl2_abstracttypes = new ArrayList<>();
        this.aadl2_processtypes = new ArrayList<>();
        this.aadl2_abstractimplementations = new ArrayList<>();
        this.aadl2_subprogramgrouptypes = new ArrayList<>();
        this.aadl2_deviceimplementations = new ArrayList<>();
    }

    public aadl2_PackageSection(
        String noAnnexes,        String imports,        String aliases,        String noProperties,        String declarations        ArrayList<aadl2_ComponentTypeRename> aadl2_componenttyperenames,        ArrayList<aadl2_FeatureGroupTypeRename> aadl2_featuregrouptyperenames,        ArrayList<aadl2_VirtualBusType> aadl2_virtualbustypes,        ArrayList<aadl2_BusImplementation> aadl2_busimplementations,        ArrayList<aadl2_SubprogramType> aadl2_subprogramtypes,        ArrayList<aadl2_Classifier> aadl2_classifiers,        ArrayList<aadl2_DeviceType> aadl2_devicetypes,        ArrayList<aadl2_SystemImplementation> aadl2_systemimplementations,        ArrayList<aadl2_PackageRename> aadl2_packagerenames,        ArrayList<aadl2_ThreadGroupType> aadl2_threadgrouptypes,        ArrayList<aadl2_DataImplementation> aadl2_dataimplementations,        ArrayList<aadl2_ProcessorImplementation> aadl2_processorimplementations,        ArrayList<aadl2_MemoryType> aadl2_memorytypes,        ArrayList<aadl2_VirtualProcessorImplementation> aadl2_virtualprocessorimplementations,        ArrayList<aadl2_VirtualProcessorType> aadl2_virtualprocessortypes,        ArrayList<aadl2_AnnexLibrary> aadl2_annexlibrarys,        ArrayList<aadl2_ProcessorType> aadl2_processortypes,        ArrayList<aadl2_PropertySet> aadl2_propertysets,        ArrayList<aadl2_ProcessImplementation> aadl2_processimplementations,        ArrayList<aadl2_AadlPackage> aadl2_aadlpackages,        ArrayList<aadl2_VirtualBusImplementation> aadl2_virtualbusimplementations,        ArrayList<aadl2_ThreadImplementation> aadl2_threadimplementations,        ArrayList<aadl2_MemoryImplementation> aadl2_memoryimplementations,        ArrayList<aadl2_SubprogramGroupImplementation> aadl2_subprogramgroupimplementations,        ArrayList<aadl2_DataType> aadl2_datatypes,        ArrayList<aadl2_ThreadGroupImplementation> aadl2_threadgroupimplementations,        ArrayList<aadl2_SubprogramImplementation> aadl2_subprogramimplementations,        ArrayList<aadl2_BusType> aadl2_bustypes,        ArrayList<aadl2_SystemType> aadl2_systemtypes,        ArrayList<aadl2_ThreadType> aadl2_threadtypes,        ArrayList<aadl2_AbstractType> aadl2_abstracttypes,        ArrayList<aadl2_ProcessType> aadl2_processtypes,        ArrayList<aadl2_AbstractImplementation> aadl2_abstractimplementations,        ArrayList<aadl2_SubprogramGroupType> aadl2_subprogramgrouptypes,        ArrayList<aadl2_DeviceImplementation> aadl2_deviceimplementations    ) {
        this.noAnnexes = noAnnexes;
        this.imports = imports;
        this.aliases = aliases;
        this.noProperties = noProperties;
        this.declarations = declarations;
        this.aadl2_componenttyperenames = aadl2_componenttyperenames;
        this.aadl2_featuregrouptyperenames = aadl2_featuregrouptyperenames;
        this.aadl2_virtualbustypes = aadl2_virtualbustypes;
        this.aadl2_busimplementations = aadl2_busimplementations;
        this.aadl2_subprogramtypes = aadl2_subprogramtypes;
        this.aadl2_classifiers = aadl2_classifiers;
        this.aadl2_devicetypes = aadl2_devicetypes;
        this.aadl2_systemimplementations = aadl2_systemimplementations;
        this.aadl2_packagerenames = aadl2_packagerenames;
        this.aadl2_threadgrouptypes = aadl2_threadgrouptypes;
        this.aadl2_dataimplementations = aadl2_dataimplementations;
        this.aadl2_processorimplementations = aadl2_processorimplementations;
        this.aadl2_memorytypes = aadl2_memorytypes;
        this.aadl2_virtualprocessorimplementations = aadl2_virtualprocessorimplementations;
        this.aadl2_virtualprocessortypes = aadl2_virtualprocessortypes;
        this.aadl2_annexlibrarys = aadl2_annexlibrarys;
        this.aadl2_processortypes = aadl2_processortypes;
        this.aadl2_propertysets = aadl2_propertysets;
        this.aadl2_processimplementations = aadl2_processimplementations;
        this.aadl2_aadlpackages = aadl2_aadlpackages;
        this.aadl2_virtualbusimplementations = aadl2_virtualbusimplementations;
        this.aadl2_threadimplementations = aadl2_threadimplementations;
        this.aadl2_memoryimplementations = aadl2_memoryimplementations;
        this.aadl2_subprogramgroupimplementations = aadl2_subprogramgroupimplementations;
        this.aadl2_datatypes = aadl2_datatypes;
        this.aadl2_threadgroupimplementations = aadl2_threadgroupimplementations;
        this.aadl2_subprogramimplementations = aadl2_subprogramimplementations;
        this.aadl2_bustypes = aadl2_bustypes;
        this.aadl2_systemtypes = aadl2_systemtypes;
        this.aadl2_threadtypes = aadl2_threadtypes;
        this.aadl2_abstracttypes = aadl2_abstracttypes;
        this.aadl2_processtypes = aadl2_processtypes;
        this.aadl2_abstractimplementations = aadl2_abstractimplementations;
        this.aadl2_subprogramgrouptypes = aadl2_subprogramgrouptypes;
        this.aadl2_deviceimplementations = aadl2_deviceimplementations;
    }

    public String getNoannexes() {
        return noAnnexes;
    }

    public void setNoannexes(String noAnnexes) {
        this.noAnnexes = noAnnexes;
    }
    public String getImports() {
        return imports;
    }

    public void setImports(String imports) {
        this.imports = imports;
    }
    public String getAliases() {
        return aliases;
    }

    public void setAliases(String aliases) {
        this.aliases = aliases;
    }
    public String getNoproperties() {
        return noProperties;
    }

    public void setNoproperties(String noProperties) {
        this.noProperties = noProperties;
    }
    public String getDeclarations() {
        return declarations;
    }

    public void setDeclarations(String declarations) {
        this.declarations = declarations;
    }

    public List<aadl2_ComponentTypeRename> getAadl2_componenttyperenames() {
        return aadl2_componenttyperenames;
    }

    public void addAadl2_componenttyperename(Aadl2_componenttyperename aadl2_componenttyperename) {
        this.aadl2_componenttyperenames.add(aadl2_componenttyperename);
    }
    public List<aadl2_FeatureGroupTypeRename> getAadl2_featuregrouptyperenames() {
        return aadl2_featuregrouptyperenames;
    }

    public void addAadl2_featuregrouptyperename(Aadl2_featuregrouptyperename aadl2_featuregrouptyperename) {
        this.aadl2_featuregrouptyperenames.add(aadl2_featuregrouptyperename);
    }
    public List<aadl2_VirtualBusType> getAadl2_virtualbustypes() {
        return aadl2_virtualbustypes;
    }

    public void addAadl2_virtualbustype(Aadl2_virtualbustype aadl2_virtualbustype) {
        this.aadl2_virtualbustypes.add(aadl2_virtualbustype);
    }
    public List<aadl2_BusImplementation> getAadl2_busimplementations() {
        return aadl2_busimplementations;
    }

    public void addAadl2_busimplementation(Aadl2_busimplementation aadl2_busimplementation) {
        this.aadl2_busimplementations.add(aadl2_busimplementation);
    }
    public List<aadl2_SubprogramType> getAadl2_subprogramtypes() {
        return aadl2_subprogramtypes;
    }

    public void addAadl2_subprogramtype(Aadl2_subprogramtype aadl2_subprogramtype) {
        this.aadl2_subprogramtypes.add(aadl2_subprogramtype);
    }
    public List<aadl2_Classifier> getAadl2_classifiers() {
        return aadl2_classifiers;
    }

    public void addAadl2_classifier(Aadl2_classifier aadl2_classifier) {
        this.aadl2_classifiers.add(aadl2_classifier);
    }
    public List<aadl2_DeviceType> getAadl2_devicetypes() {
        return aadl2_devicetypes;
    }

    public void addAadl2_devicetype(Aadl2_devicetype aadl2_devicetype) {
        this.aadl2_devicetypes.add(aadl2_devicetype);
    }
    public List<aadl2_SystemImplementation> getAadl2_systemimplementations() {
        return aadl2_systemimplementations;
    }

    public void addAadl2_systemimplementation(Aadl2_systemimplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementations.add(aadl2_systemimplementation);
    }
    public List<aadl2_PackageRename> getAadl2_packagerenames() {
        return aadl2_packagerenames;
    }

    public void addAadl2_packagerename(Aadl2_packagerename aadl2_packagerename) {
        this.aadl2_packagerenames.add(aadl2_packagerename);
    }
    public List<aadl2_ThreadGroupType> getAadl2_threadgrouptypes() {
        return aadl2_threadgrouptypes;
    }

    public void addAadl2_threadgrouptype(Aadl2_threadgrouptype aadl2_threadgrouptype) {
        this.aadl2_threadgrouptypes.add(aadl2_threadgrouptype);
    }
    public List<aadl2_DataImplementation> getAadl2_dataimplementations() {
        return aadl2_dataimplementations;
    }

    public void addAadl2_dataimplementation(Aadl2_dataimplementation aadl2_dataimplementation) {
        this.aadl2_dataimplementations.add(aadl2_dataimplementation);
    }
    public List<aadl2_ProcessorImplementation> getAadl2_processorimplementations() {
        return aadl2_processorimplementations;
    }

    public void addAadl2_processorimplementation(Aadl2_processorimplementation aadl2_processorimplementation) {
        this.aadl2_processorimplementations.add(aadl2_processorimplementation);
    }
    public List<aadl2_MemoryType> getAadl2_memorytypes() {
        return aadl2_memorytypes;
    }

    public void addAadl2_memorytype(Aadl2_memorytype aadl2_memorytype) {
        this.aadl2_memorytypes.add(aadl2_memorytype);
    }
    public List<aadl2_VirtualProcessorImplementation> getAadl2_virtualprocessorimplementations() {
        return aadl2_virtualprocessorimplementations;
    }

    public void addAadl2_virtualprocessorimplementation(Aadl2_virtualprocessorimplementation aadl2_virtualprocessorimplementation) {
        this.aadl2_virtualprocessorimplementations.add(aadl2_virtualprocessorimplementation);
    }
    public List<aadl2_VirtualProcessorType> getAadl2_virtualprocessortypes() {
        return aadl2_virtualprocessortypes;
    }

    public void addAadl2_virtualprocessortype(Aadl2_virtualprocessortype aadl2_virtualprocessortype) {
        this.aadl2_virtualprocessortypes.add(aadl2_virtualprocessortype);
    }
    public List<aadl2_AnnexLibrary> getAadl2_annexlibrarys() {
        return aadl2_annexlibrarys;
    }

    public void addAadl2_annexlibrary(Aadl2_annexlibrary aadl2_annexlibrary) {
        this.aadl2_annexlibrarys.add(aadl2_annexlibrary);
    }
    public List<aadl2_ProcessorType> getAadl2_processortypes() {
        return aadl2_processortypes;
    }

    public void addAadl2_processortype(Aadl2_processortype aadl2_processortype) {
        this.aadl2_processortypes.add(aadl2_processortype);
    }
    public List<aadl2_PropertySet> getAadl2_propertysets() {
        return aadl2_propertysets;
    }

    public void addAadl2_propertyset(Aadl2_propertyset aadl2_propertyset) {
        this.aadl2_propertysets.add(aadl2_propertyset);
    }
    public List<aadl2_ProcessImplementation> getAadl2_processimplementations() {
        return aadl2_processimplementations;
    }

    public void addAadl2_processimplementation(Aadl2_processimplementation aadl2_processimplementation) {
        this.aadl2_processimplementations.add(aadl2_processimplementation);
    }
    public List<aadl2_AadlPackage> getAadl2_aadlpackages() {
        return aadl2_aadlpackages;
    }

    public void addAadl2_aadlpackage(Aadl2_aadlpackage aadl2_aadlpackage) {
        this.aadl2_aadlpackages.add(aadl2_aadlpackage);
    }
    public List<aadl2_VirtualBusImplementation> getAadl2_virtualbusimplementations() {
        return aadl2_virtualbusimplementations;
    }

    public void addAadl2_virtualbusimplementation(Aadl2_virtualbusimplementation aadl2_virtualbusimplementation) {
        this.aadl2_virtualbusimplementations.add(aadl2_virtualbusimplementation);
    }
    public List<aadl2_ThreadImplementation> getAadl2_threadimplementations() {
        return aadl2_threadimplementations;
    }

    public void addAadl2_threadimplementation(Aadl2_threadimplementation aadl2_threadimplementation) {
        this.aadl2_threadimplementations.add(aadl2_threadimplementation);
    }
    public List<aadl2_MemoryImplementation> getAadl2_memoryimplementations() {
        return aadl2_memoryimplementations;
    }

    public void addAadl2_memoryimplementation(Aadl2_memoryimplementation aadl2_memoryimplementation) {
        this.aadl2_memoryimplementations.add(aadl2_memoryimplementation);
    }
    public List<aadl2_SubprogramGroupImplementation> getAadl2_subprogramgroupimplementations() {
        return aadl2_subprogramgroupimplementations;
    }

    public void addAadl2_subprogramgroupimplementation(Aadl2_subprogramgroupimplementation aadl2_subprogramgroupimplementation) {
        this.aadl2_subprogramgroupimplementations.add(aadl2_subprogramgroupimplementation);
    }
    public List<aadl2_DataType> getAadl2_datatypes() {
        return aadl2_datatypes;
    }

    public void addAadl2_datatype(Aadl2_datatype aadl2_datatype) {
        this.aadl2_datatypes.add(aadl2_datatype);
    }
    public List<aadl2_ThreadGroupImplementation> getAadl2_threadgroupimplementations() {
        return aadl2_threadgroupimplementations;
    }

    public void addAadl2_threadgroupimplementation(Aadl2_threadgroupimplementation aadl2_threadgroupimplementation) {
        this.aadl2_threadgroupimplementations.add(aadl2_threadgroupimplementation);
    }
    public List<aadl2_SubprogramImplementation> getAadl2_subprogramimplementations() {
        return aadl2_subprogramimplementations;
    }

    public void addAadl2_subprogramimplementation(Aadl2_subprogramimplementation aadl2_subprogramimplementation) {
        this.aadl2_subprogramimplementations.add(aadl2_subprogramimplementation);
    }
    public List<aadl2_BusType> getAadl2_bustypes() {
        return aadl2_bustypes;
    }

    public void addAadl2_bustype(Aadl2_bustype aadl2_bustype) {
        this.aadl2_bustypes.add(aadl2_bustype);
    }
    public List<aadl2_SystemType> getAadl2_systemtypes() {
        return aadl2_systemtypes;
    }

    public void addAadl2_systemtype(Aadl2_systemtype aadl2_systemtype) {
        this.aadl2_systemtypes.add(aadl2_systemtype);
    }
    public List<aadl2_ThreadType> getAadl2_threadtypes() {
        return aadl2_threadtypes;
    }

    public void addAadl2_threadtype(Aadl2_threadtype aadl2_threadtype) {
        this.aadl2_threadtypes.add(aadl2_threadtype);
    }
    public List<aadl2_AbstractType> getAadl2_abstracttypes() {
        return aadl2_abstracttypes;
    }

    public void addAadl2_abstracttype(Aadl2_abstracttype aadl2_abstracttype) {
        this.aadl2_abstracttypes.add(aadl2_abstracttype);
    }
    public List<aadl2_ProcessType> getAadl2_processtypes() {
        return aadl2_processtypes;
    }

    public void addAadl2_processtype(Aadl2_processtype aadl2_processtype) {
        this.aadl2_processtypes.add(aadl2_processtype);
    }
    public List<aadl2_AbstractImplementation> getAadl2_abstractimplementations() {
        return aadl2_abstractimplementations;
    }

    public void addAadl2_abstractimplementation(Aadl2_abstractimplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementations.add(aadl2_abstractimplementation);
    }
    public List<aadl2_SubprogramGroupType> getAadl2_subprogramgrouptypes() {
        return aadl2_subprogramgrouptypes;
    }

    public void addAadl2_subprogramgrouptype(Aadl2_subprogramgrouptype aadl2_subprogramgrouptype) {
        this.aadl2_subprogramgrouptypes.add(aadl2_subprogramgrouptype);
    }
    public List<aadl2_DeviceImplementation> getAadl2_deviceimplementations() {
        return aadl2_deviceimplementations;
    }

    public void addAadl2_deviceimplementation(Aadl2_deviceimplementation aadl2_deviceimplementation) {
        this.aadl2_deviceimplementations.add(aadl2_deviceimplementation);
    }

}