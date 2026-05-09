





import java.util.List;
import java.util.ArrayList;

public class umm_ABIE extends ContextRef {

    private String definition;
    private String versionIdentifier;
    private String uniqueIdentifier;
    private String businessTerm;
    private String dictionary;





    private umm_BIELibrary umm_bielibrary;


    public umm_ABIE(
        String definition,        String versionIdentifier,        String uniqueIdentifier,        String businessTerm,        String dictionary    ) {
        super(
        );
        this.definition = definition;
        this.versionIdentifier = versionIdentifier;
        this.uniqueIdentifier = uniqueIdentifier;
        this.businessTerm = businessTerm;
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
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
    }
    public String getDictionary() {
        return dictionary;
    }

    public void setDictionary(String dictionary) {
        this.dictionary = dictionary;
    }

    public umm_BIELibrary getUmm_bielibrary() {
        return umm_bielibrary;
    }

    public void setUmm_bielibrary(umm_BIELibrary umm_bielibrary) {
        this.umm_bielibrary = umm_bielibrary;
    }

}