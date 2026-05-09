





import java.util.List;
import java.util.ArrayList;

public class umm_ACCProperty  {

    private String uniqueIdentifier;
    private String multiplicity;
    private String name;
    private String sequencingKey;
    private String dictionary;
    private String definition;
    private String versionIdentifier;
    private String businessTerm;





    private umm_ACC umm_acc;


    public umm_ACCProperty(
        String uniqueIdentifier,        String multiplicity,        String name,        String sequencingKey,        String dictionary,        String definition,        String versionIdentifier,        String businessTerm    ) {
        this.uniqueIdentifier = uniqueIdentifier;
        this.multiplicity = multiplicity;
        this.name = name;
        this.sequencingKey = sequencingKey;
        this.dictionary = dictionary;
        this.definition = definition;
        this.versionIdentifier = versionIdentifier;
        this.businessTerm = businessTerm;
    }


    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(String multiplicity) {
        this.multiplicity = multiplicity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSequencingkey() {
        return sequencingKey;
    }

    public void setSequencingkey(String sequencingKey) {
        this.sequencingKey = sequencingKey;
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
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
    }

    public umm_ACC getUmm_acc() {
        return umm_acc;
    }

    public void setUmm_acc(umm_ACC umm_acc) {
        this.umm_acc = umm_acc;
    }

}