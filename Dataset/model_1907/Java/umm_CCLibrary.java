





import java.util.List;
import java.util.ArrayList;

public class umm_CCLibrary extends Library {

    private String baseURN;
    private String reference;
    private String versionIdentifier;
    private String copyright;
    private String uniqueIdentifier;
    private String owner;
    private String namespacePrefix;
    private String businessTerm;



    public umm_CCLibrary(
        String baseURN,        String reference,        String versionIdentifier,        String copyright,        String uniqueIdentifier,        String owner,        String namespacePrefix,        String businessTerm    ) {
        super(
        );
        this.baseURN = baseURN;
        this.reference = reference;
        this.versionIdentifier = versionIdentifier;
        this.copyright = copyright;
        this.uniqueIdentifier = uniqueIdentifier;
        this.owner = owner;
        this.namespacePrefix = namespacePrefix;
        this.businessTerm = businessTerm;
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
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getUniqueidentifier() {
        return uniqueIdentifier;
    }

    public void setUniqueidentifier(String uniqueIdentifier) {
        this.uniqueIdentifier = uniqueIdentifier;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
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


}