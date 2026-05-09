





import java.util.List;
import java.util.ArrayList;

public class umm_CDT  {

    private String uniqueIdentifier;
    private String businessTerm;
    private String definition;
    private String name;
    private String versionIdentifier;
    private String dictionary;





    private umm_CDTLibrary umm_cdtlibrary;




    private umm_BCC umm_bcc;


    public umm_CDT(
        String uniqueIdentifier,        String businessTerm,        String definition,        String name,        String versionIdentifier,        String dictionary    ) {
        this.uniqueIdentifier = uniqueIdentifier;
        this.businessTerm = businessTerm;
        this.definition = definition;
        this.name = name;
        this.versionIdentifier = versionIdentifier;
        this.dictionary = dictionary;
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
    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }
    public String getDictionary() {
        return dictionary;
    }

    public void setDictionary(String dictionary) {
        this.dictionary = dictionary;
    }

    public umm_CDTLibrary getUmm_cdtlibrary() {
        return umm_cdtlibrary;
    }

    public void setUmm_cdtlibrary(umm_CDTLibrary umm_cdtlibrary) {
        this.umm_cdtlibrary = umm_cdtlibrary;
    }
    public umm_BCC getUmm_bcc() {
        return umm_bcc;
    }

    public void setUmm_bcc(umm_BCC umm_bcc) {
        this.umm_bcc = umm_bcc;
    }

}