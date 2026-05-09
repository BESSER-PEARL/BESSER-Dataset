





import java.util.List;
import java.util.ArrayList;

public class umm_BDT extends ContextRef {

    private String dictionary;
    private String businessTerm;
    private String definition;
    private String uniqueIdentifier;
    private String versionIdentifier;





    private umm_BDTLibrary umm_bdtlibrary;


    public umm_BDT(
        String dictionary,        String businessTerm,        String definition,        String uniqueIdentifier,        String versionIdentifier    ) {
        super(
        );
        this.dictionary = dictionary;
        this.businessTerm = businessTerm;
        this.definition = definition;
        this.uniqueIdentifier = uniqueIdentifier;
        this.versionIdentifier = versionIdentifier;
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
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }

    public umm_BDTLibrary getUmm_bdtlibrary() {
        return umm_bdtlibrary;
    }

    public void setUmm_bdtlibrary(umm_BDTLibrary umm_bdtlibrary) {
        this.umm_bdtlibrary = umm_bdtlibrary;
    }

}