





import java.util.List;
import java.util.ArrayList;

public class umm_ENUM  {

    private String definition;
    private String versionIdentifier;
    private String codeListName;
    private String codeListAgencyIdentifier;
    private String businessTerm;
    private String codeListIdentifier;
    private String uniqueIdentifier;
    private String name;
    private String dictionary;





    private umm_ENUMLibrary umm_enumlibrary;


    public umm_ENUM(
        String definition,        String versionIdentifier,        String codeListName,        String codeListAgencyIdentifier,        String businessTerm,        String codeListIdentifier,        String uniqueIdentifier,        String name,        String dictionary    ) {
        this.definition = definition;
        this.versionIdentifier = versionIdentifier;
        this.codeListName = codeListName;
        this.codeListAgencyIdentifier = codeListAgencyIdentifier;
        this.businessTerm = businessTerm;
        this.codeListIdentifier = codeListIdentifier;
        this.uniqueIdentifier = uniqueIdentifier;
        this.name = name;
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
    public String getCodelistname() {
        return codeListName;
    }

    public void setCodelistname(String codeListName) {
        this.codeListName = codeListName;
    }
    public String getCodelistagencyidentifier() {
        return codeListAgencyIdentifier;
    }

    public void setCodelistagencyidentifier(String codeListAgencyIdentifier) {
        this.codeListAgencyIdentifier = codeListAgencyIdentifier;
    }
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
    }
    public String getCodelistidentifier() {
        return codeListIdentifier;
    }

    public void setCodelistidentifier(String codeListIdentifier) {
        this.codeListIdentifier = codeListIdentifier;
    }
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDictionary() {
        return dictionary;
    }

    public void setDictionary(String dictionary) {
        this.dictionary = dictionary;
    }

    public umm_ENUMLibrary getUmm_enumlibrary() {
        return umm_enumlibrary;
    }

    public void setUmm_enumlibrary(umm_ENUMLibrary umm_enumlibrary) {
        this.umm_enumlibrary = umm_enumlibrary;
    }

}