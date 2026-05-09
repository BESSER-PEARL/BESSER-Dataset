





import java.util.List;
import java.util.ArrayList;

public class umm_ABIEProperty extends OclRef {

    private String definition;
    private String dictionary;
    private String businessTerm;
    private String uniqueIdentifier;
    private String sequencingKey;
    private String versionIdentifier;





    private umm_ABIEProperty umm_abieproperty;




    private umm_ABIE umm_abie;


    public umm_ABIEProperty(
        String definition,        String dictionary,        String businessTerm,        String uniqueIdentifier,        String sequencingKey,        String versionIdentifier    ) {
        super(
        );
        this.definition = definition;
        this.dictionary = dictionary;
        this.businessTerm = businessTerm;
        this.uniqueIdentifier = uniqueIdentifier;
        this.sequencingKey = sequencingKey;
        this.versionIdentifier = versionIdentifier;
    }


    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
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
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getSequencingkey() {
        return sequencingKey;
    }

    public void setSequencingkey(String sequencingKey) {
        this.sequencingKey = sequencingKey;
    }
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }

    public umm_ABIEProperty getUmm_abieproperty() {
        return umm_abieproperty;
    }

    public void setUmm_abieproperty(umm_ABIEProperty umm_abieproperty) {
        this.umm_abieproperty = umm_abieproperty;
    }
    public umm_ABIE getUmm_abie() {
        return umm_abie;
    }

    public void setUmm_abie(umm_ABIE umm_abie) {
        this.umm_abie = umm_abie;
    }

}