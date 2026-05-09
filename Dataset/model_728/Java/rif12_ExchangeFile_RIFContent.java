





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_RIFContent  {






    private List<SpecHierarchyRoot> spechierarchyroots;




    private List<SpecRelation> specrelations;




    private List<DatatypeDefinition> datatypedefinitions;




    private List<SpecGroup> specgroups;




    private List<SpecType> spectypes;




    private List<SpecObject> specobjects;




    private List<SpecGroupHierarchyRoot> specgrouphierarchyroots;


    public rif12_ExchangeFile_RIFContent(
    ) {
        this.spechierarchyroots = new ArrayList<>();
        this.specrelations = new ArrayList<>();
        this.datatypedefinitions = new ArrayList<>();
        this.specgroups = new ArrayList<>();
        this.spectypes = new ArrayList<>();
        this.specobjects = new ArrayList<>();
        this.specgrouphierarchyroots = new ArrayList<>();
    }

    public rif12_ExchangeFile_RIFContent(
        ArrayList<SpecHierarchyRoot> spechierarchyroots,        ArrayList<SpecRelation> specrelations,        ArrayList<DatatypeDefinition> datatypedefinitions,        ArrayList<SpecGroup> specgroups,        ArrayList<SpecType> spectypes,        ArrayList<SpecObject> specobjects,        ArrayList<SpecGroupHierarchyRoot> specgrouphierarchyroots    ) {
        this.spechierarchyroots = spechierarchyroots;
        this.specrelations = specrelations;
        this.datatypedefinitions = datatypedefinitions;
        this.specgroups = specgroups;
        this.spectypes = spectypes;
        this.specobjects = specobjects;
        this.specgrouphierarchyroots = specgrouphierarchyroots;
    }


    public List<SpecHierarchyRoot> getSpechierarchyroots() {
        return spechierarchyroots;
    }

    public void addSpechierarchyroot(Spechierarchyroot spechierarchyroot) {
        this.spechierarchyroots.add(spechierarchyroot);
    }
    public List<SpecRelation> getSpecrelations() {
        return specrelations;
    }

    public void addSpecrelation(Specrelation specrelation) {
        this.specrelations.add(specrelation);
    }
    public List<DatatypeDefinition> getDatatypedefinitions() {
        return datatypedefinitions;
    }

    public void addDatatypedefinition(Datatypedefinition datatypedefinition) {
        this.datatypedefinitions.add(datatypedefinition);
    }
    public List<SpecGroup> getSpecgroups() {
        return specgroups;
    }

    public void addSpecgroup(Specgroup specgroup) {
        this.specgroups.add(specgroup);
    }
    public List<SpecType> getSpectypes() {
        return spectypes;
    }

    public void addSpectype(Spectype spectype) {
        this.spectypes.add(spectype);
    }
    public List<SpecObject> getSpecobjects() {
        return specobjects;
    }

    public void addSpecobject(Specobject specobject) {
        this.specobjects.add(specobject);
    }
    public List<SpecGroupHierarchyRoot> getSpecgrouphierarchyroots() {
        return specgrouphierarchyroots;
    }

    public void addSpecgrouphierarchyroot(Specgrouphierarchyroot specgrouphierarchyroot) {
        this.specgrouphierarchyroots.add(specgrouphierarchyroot);
    }

}