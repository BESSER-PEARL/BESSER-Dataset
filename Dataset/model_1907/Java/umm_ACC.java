





import java.util.List;
import java.util.ArrayList;

public class umm_ACC  {

    private String uniqueIdentifier;
    private String dictionary;
    private String definition;
    private String versionIdentifier;
    private String name;
    private String businessTerm;





    private umm_CCLibrary umm_cclibrary;




    private List<umm_Constraint> umm_constraints;


    public umm_ACC(
        String uniqueIdentifier,        String dictionary,        String definition,        String versionIdentifier,        String name,        String businessTerm    ) {
        this.uniqueIdentifier = uniqueIdentifier;
        this.dictionary = dictionary;
        this.definition = definition;
        this.versionIdentifier = versionIdentifier;
        this.name = name;
        this.businessTerm = businessTerm;
        this.umm_constraints = new ArrayList<>();
    }

    public umm_ACC(
        String uniqueIdentifier,        String dictionary,        String definition,        String versionIdentifier,        String name,        String businessTerm        ArrayList<umm_Constraint> umm_constraints    ) {
        this.uniqueIdentifier = uniqueIdentifier;
        this.dictionary = dictionary;
        this.definition = definition;
        this.versionIdentifier = versionIdentifier;
        this.name = name;
        this.businessTerm = businessTerm;
        this.umm_constraints = umm_constraints;
    }

    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getDictionary() {
        return dictionary;
    }

    public void setDictionary(String dictionary) {
        this.dictionary = dictionary;
    }
    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
    }

    public umm_CCLibrary getUmm_cclibrary() {
        return umm_cclibrary;
    }

    public void setUmm_cclibrary(umm_CCLibrary umm_cclibrary) {
        this.umm_cclibrary = umm_cclibrary;
    }
    public List<umm_Constraint> getUmm_constraints() {
        return umm_constraints;
    }

    public void addUmm_constraint(Umm_constraint umm_constraint) {
        this.umm_constraints.add(umm_constraint);
    }

}