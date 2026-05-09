





import java.util.List;
import java.util.ArrayList;

public class umm_ENUMLibrary extends Library {

    private String versionIdentifier;
    private String owner;
    private String uniqueIdentifier;
    private String businessTerm;
    private String reference;
    private String namespacePrefix;
    private String baseURN;
    private String copyright;



    public umm_ENUMLibrary(
        String versionIdentifier,        String owner,        String uniqueIdentifier,        String businessTerm,        String reference,        String namespacePrefix,        String baseURN,        String copyright    ) {
        super(
        );
        this.versionIdentifier = versionIdentifier;
        this.owner = owner;
        this.uniqueIdentifier = uniqueIdentifier;
        this.businessTerm = businessTerm;
        this.reference = reference;
        this.namespacePrefix = namespacePrefix;
        this.baseURN = baseURN;
        this.copyright = copyright;
    }


    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
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
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getNamespaceprefix() {
        return namespacePrefix;
    }

    public void setNamespaceprefix(String namespacePrefix) {
        this.namespacePrefix = namespacePrefix;
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


}