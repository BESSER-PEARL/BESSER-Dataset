





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_AccessPolicy extends Identifiable {

    private String accessMode;





    private List<ExchangeFile_SpecHierarchy> exchangefile_spechierarchys;




    private List<ExchangeFile_SpecObject> exchangefile_specobjects;




    private List<ExchangeFile_RelationGroup> exchangefile_relationgroups;




    private List<ExchangeFile_SpecRelation> exchangefile_specrelations;


    public rif11a_ExchangeFile_AccessPolicy(
        String accessMode    ) {
        super(
        );
        this.accessMode = accessMode;
        this.exchangefile_spechierarchys = new ArrayList<>();
        this.exchangefile_specobjects = new ArrayList<>();
        this.exchangefile_relationgroups = new ArrayList<>();
        this.exchangefile_specrelations = new ArrayList<>();
    }

    public rif11a_ExchangeFile_AccessPolicy(
        String accessMode        ArrayList<ExchangeFile_SpecHierarchy> exchangefile_spechierarchys,        ArrayList<ExchangeFile_SpecObject> exchangefile_specobjects,        ArrayList<ExchangeFile_RelationGroup> exchangefile_relationgroups,        ArrayList<ExchangeFile_SpecRelation> exchangefile_specrelations    ) {
        this.accessMode = accessMode;
        this.exchangefile_spechierarchys = exchangefile_spechierarchys;
        this.exchangefile_specobjects = exchangefile_specobjects;
        this.exchangefile_relationgroups = exchangefile_relationgroups;
        this.exchangefile_specrelations = exchangefile_specrelations;
    }

    public String getAccessmode() {
        return accessMode;
    }

    public void setAccessmode(String accessMode) {
        this.accessMode = accessMode;
    }

    public List<ExchangeFile_SpecHierarchy> getExchangefile_spechierarchys() {
        return exchangefile_spechierarchys;
    }

    public void addExchangefile_spechierarchy(Exchangefile_spechierarchy exchangefile_spechierarchy) {
        this.exchangefile_spechierarchys.add(exchangefile_spechierarchy);
    }
    public List<ExchangeFile_SpecObject> getExchangefile_specobjects() {
        return exchangefile_specobjects;
    }

    public void addExchangefile_specobject(Exchangefile_specobject exchangefile_specobject) {
        this.exchangefile_specobjects.add(exchangefile_specobject);
    }
    public List<ExchangeFile_RelationGroup> getExchangefile_relationgroups() {
        return exchangefile_relationgroups;
    }

    public void addExchangefile_relationgroup(Exchangefile_relationgroup exchangefile_relationgroup) {
        this.exchangefile_relationgroups.add(exchangefile_relationgroup);
    }
    public List<ExchangeFile_SpecRelation> getExchangefile_specrelations() {
        return exchangefile_specrelations;
    }

    public void addExchangefile_specrelation(Exchangefile_specrelation exchangefile_specrelation) {
        this.exchangefile_specrelations.add(exchangefile_specrelation);
    }

}