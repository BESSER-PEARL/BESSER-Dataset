





import java.util.List;
import java.util.ArrayList;

public class umm_BIELibrary extends Library {

    private String versionIdentifier;
    private String uniqueIdentifier;
    private String namespacePrefix;
    private String businessTerm;
    private String copyright;
    private String owner;
    private String baseURN;
    private String reference;



    public umm_BIELibrary(
        String versionIdentifier,        String uniqueIdentifier,        String namespacePrefix,        String businessTerm,        String copyright,        String owner,        String baseURN,        String reference    ) {
        super(
        );
        this.versionIdentifier = versionIdentifier;
        this.uniqueIdentifier = uniqueIdentifier;
        this.namespacePrefix = namespacePrefix;
        this.businessTerm = businessTerm;
        this.copyright = copyright;
        this.owner = owner;
        this.baseURN = baseURN;
        this.reference = reference;
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
    public String getNamespaceprefix() {
        return namespacePrefix;
    }

    public void setNamespaceprefix(String namespacePrefix) {
        this.namespacePrefix = namespacePrefix;
    }
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }
    public String getBaseurn() {
        return baseURN;
    }

    public void setBaseurn(String baseURN) {
        this.baseURN = baseURN;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }


}