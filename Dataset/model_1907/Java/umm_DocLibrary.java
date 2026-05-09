





import java.util.List;
import java.util.ArrayList;

public class umm_DocLibrary extends Library {

    private String namespacePrefix;
    private String baseURN;
    private String copyright;
    private String versionIdentifier;
    private String businessTerm;
    private String owner;
    private String uniqueIdentifier;
    private String reference;





    private List<umm_InfEnvelope> umm_infenvelopes;




    private umm_BDTLibrary umm_bdtlibrary;




    private umm_BIELibrary umm_bielibrary;


    public umm_DocLibrary(
        String namespacePrefix,        String baseURN,        String copyright,        String versionIdentifier,        String businessTerm,        String owner,        String uniqueIdentifier,        String reference    ) {
        super(
        );
        this.namespacePrefix = namespacePrefix;
        this.baseURN = baseURN;
        this.copyright = copyright;
        this.versionIdentifier = versionIdentifier;
        this.businessTerm = businessTerm;
        this.owner = owner;
        this.uniqueIdentifier = uniqueIdentifier;
        this.reference = reference;
        this.umm_infenvelopes = new ArrayList<>();
    }

    public umm_DocLibrary(
        String namespacePrefix,        String baseURN,        String copyright,        String versionIdentifier,        String businessTerm,        String owner,        String uniqueIdentifier,        String reference        ArrayList<umm_InfEnvelope> umm_infenvelopes    ) {
        this.namespacePrefix = namespacePrefix;
        this.baseURN = baseURN;
        this.copyright = copyright;
        this.versionIdentifier = versionIdentifier;
        this.businessTerm = businessTerm;
        this.owner = owner;
        this.uniqueIdentifier = uniqueIdentifier;
        this.reference = reference;
        this.umm_infenvelopes = umm_infenvelopes;
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
    public String getVersionidentifier() {
        return versionIdentifier;
    }

    public void setVersionidentifier(String versionIdentifier) {
        this.versionIdentifier = versionIdentifier;
    }
    public String getBusinessterm() {
        return businessTerm;
    }

    public void setBusinessterm(String businessTerm) {
        this.businessTerm = businessTerm;
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
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }

    public List<umm_InfEnvelope> getUmm_infenvelopes() {
        return umm_infenvelopes;
    }

    public void addUmm_infenvelope(Umm_infenvelope umm_infenvelope) {
        this.umm_infenvelopes.add(umm_infenvelope);
    }
    public umm_BDTLibrary getUmm_bdtlibrary() {
        return umm_bdtlibrary;
    }

    public void setUmm_bdtlibrary(umm_BDTLibrary umm_bdtlibrary) {
        this.umm_bdtlibrary = umm_bdtlibrary;
    }
    public umm_BIELibrary getUmm_bielibrary() {
        return umm_bielibrary;
    }

    public void setUmm_bielibrary(umm_BIELibrary umm_bielibrary) {
        this.umm_bielibrary = umm_bielibrary;
    }

}