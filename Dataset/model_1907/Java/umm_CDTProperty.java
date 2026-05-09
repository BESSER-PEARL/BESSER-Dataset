





import java.util.List;
import java.util.ArrayList;

public class umm_CDTProperty  {

    private String multiplicity;
    private String uniqueIdentifier;
    private String dictionary;
    private String businessTerm;
    private String definition;
    private String versionIdentifier;
    private String name;





    private umm_CDT umm_cdt;




    private umm_Primitive umm_primitive;


    public umm_CDTProperty(
        String multiplicity,        String uniqueIdentifier,        String dictionary,        String businessTerm,        String definition,        String versionIdentifier,        String name    ) {
        this.multiplicity = multiplicity;
        this.uniqueIdentifier = uniqueIdentifier;
        this.dictionary = dictionary;
        this.businessTerm = businessTerm;
        this.definition = definition;
        this.versionIdentifier = versionIdentifier;
        this.name = name;
    }


    public String getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(String multiplicity) {
        this.multiplicity = multiplicity;
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
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
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

    public umm_CDT getUmm_cdt() {
        return umm_cdt;
    }

    public void setUmm_cdt(umm_CDT umm_cdt) {
        this.umm_cdt = umm_cdt;
    }
    public umm_Primitive getUmm_primitive() {
        return umm_primitive;
    }

    public void setUmm_primitive(umm_Primitive umm_primitive) {
        this.umm_primitive = umm_primitive;
    }

}