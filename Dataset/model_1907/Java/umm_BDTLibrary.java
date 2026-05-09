





import java.util.List;
import java.util.ArrayList;

public class umm_BDTLibrary extends Library {

    private String namespacePrefix;
    private String versionIdentifier;
    private String baseURN;
    private String copyright;
    private String reference;
    private String owner;
    private String uniqueIdentifier;
    private String businessTerm;





    private umm_BIELibrary umm_bielibrary;


    public umm_BDTLibrary(
        String namespacePrefix,        String versionIdentifier,        String baseURN,        String copyright,        String reference,        String owner,        String uniqueIdentifier,        String businessTerm    ) {
        super(
        );
        this.namespacePrefix = namespacePrefix;
        this.versionIdentifier = versionIdentifier;
        this.baseURN = baseURN;
        this.copyright = copyright;
        this.reference = reference;
        this.owner = owner;
        this.uniqueIdentifier = uniqueIdentifier;
        this.businessTerm = businessTerm;
    }


    public String getNamespaceprefix() {
        return namespacePrefix;
    }

    public void setNamespaceprefix(String namespacePrefix) {
        this.namespacePrefix = namespacePrefix;
    }
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }
    public String getBaseurn() {
        return baseURN;
    }

    public void setBaseurn(String baseURN) {
        this.baseURN = baseURN;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
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

    public umm_BIELibrary getUmm_bielibrary() {
        return umm_bielibrary;
    }

    public void setUmm_bielibrary(umm_BIELibrary umm_bielibrary) {
        this.umm_bielibrary = umm_bielibrary;
    }

}