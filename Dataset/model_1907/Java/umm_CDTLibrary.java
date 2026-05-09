





import java.util.List;
import java.util.ArrayList;

public class umm_CDTLibrary extends Library {

    private String businessTerm;
    private String baseURN;
    private String uniqueIdentifier;
    private String namespacePrefix;
    private String copyright;
    private String owner;
    private String versionIdentifier;
    private String reference;



    public umm_CDTLibrary(
        String businessTerm,        String baseURN,        String uniqueIdentifier,        String namespacePrefix,        String copyright,        String owner,        String versionIdentifier,        String reference    ) {
        super(
        );
        this.businessTerm = businessTerm;
        this.baseURN = baseURN;
        this.uniqueIdentifier = uniqueIdentifier;
        this.namespacePrefix = namespacePrefix;
        this.copyright = copyright;
        this.owner = owner;
        this.versionIdentifier = versionIdentifier;
        this.reference = reference;
    }


    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
    }
    public String getBaseurn() {
        return baseURN;
    }

    public void setBaseurn(String baseURN) {
        this.baseURN = baseURN;
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
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }


}