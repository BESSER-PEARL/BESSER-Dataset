





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_RIFContent  {






    private List<SpecGroupHierarchyRoot> specgrouphierarchyroots;




    private List<DatatypeDefinition> datatypedefinitions;




    private List<SpecHierarchyRoot> spechierarchyroots;




    private List<SpecType> spectypes;




    private List<SpecObject> specobjects;




    private List<SpecGroup> specgroups;




    private List<SpecRelation> specrelations;


    public rif12_ExchangeFile_RIFContent(
    ) {
        this.specgrouphierarchyroots = new ArrayList<>();
        this.datatypedefinitions = new ArrayList<>();
        this.spechierarchyroots = new ArrayList<>();
        this.spectypes = new ArrayList<>();
        this.specobjects = new ArrayList<>();
        this.specgroups = new ArrayList<>();
        this.specrelations = new ArrayList<>();
    }

    public rif12_ExchangeFile_RIFContent(
        ArrayList<SpecGroupHierarchyRoot> specgrouphierarchyroots,        ArrayList<DatatypeDefinition> datatypedefinitions,        ArrayList<SpecHierarchyRoot> spechierarchyroots,        ArrayList<SpecType> spectypes,        ArrayList<SpecObject> specobjects,        ArrayList<SpecGroup> specgroups,        ArrayList<SpecRelation> specrelations    ) {
        this.specgrouphierarchyroots = specgrouphierarchyroots;
        this.datatypedefinitions = datatypedefinitions;
        this.spechierarchyroots = spechierarchyroots;
        this.spectypes = spectypes;
        this.specobjects = specobjects;
        this.specgroups = specgroups;
        this.specrelations = specrelations;
    }


    public List<SpecGroupHierarchyRoot> getSpecgrouphierarchyroots() {
        return specgrouphierarchyroots;
    }

    public void addSpecgrouphierarchyroot(Specgrouphierarchyroot specgrouphierarchyroot) {
        this.specgrouphierarchyroots.add(specgrouphierarchyroot);
    }
    public List<DatatypeDefinition> getDatatypedefinitions() {
        return datatypedefinitions;
    }

    public void addDatatypedefinition(Datatypedefinition datatypedefinition) {
        this.datatypedefinitions.add(datatypedefinition);
    }
    public List<SpecHierarchyRoot> getSpechierarchyroots() {
        return spechierarchyroots;
    }

    public void addSpechierarchyroot(Spechierarchyroot spechierarchyroot) {
        this.spechierarchyroots.add(spechierarchyroot);
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
    public List<SpecGroup> getSpecgroups() {
        return specgroups;
    }

    public void addSpecgroup(Specgroup specgroup) {
        this.specgroups.add(specgroup);
    }
    public List<SpecRelation> getSpecrelations() {
        return specrelations;
    }

    public void addSpecrelation(Specrelation specrelation) {
        this.specrelations.add(specrelation);
    }

}