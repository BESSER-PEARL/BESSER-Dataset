





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_RIF  {

    private String version;
    private String identifier;
    private String creationTime;
    private String sourceToolId;
    private String title;
    private String author;
    private String countryCode;
    private String comment;





    private List<ExchangeFile_SpecGroup> exchangefile_specgroups;




    private List<ExchangeFile_SpecHierarchyRoot> exchangefile_spechierarchyroots;




    private List<ExchangeFile_SpecType> exchangefile_spectypes;




    private List<ExchangeFile_SpecObject> exchangefile_specobjects;




    private List<ExchangeFile_SpecRelation> exchangefile_specrelations;




    private List<ExchangeFile_DatatypeDefinition> exchangefile_datatypedefinitions;


    public rif11a_ExchangeFile_RIF(
        String version,        String identifier,        String creationTime,        String sourceToolId,        String title,        String author,        String countryCode,        String comment    ) {
        this.version = version;
        this.identifier = identifier;
        this.creationTime = creationTime;
        this.sourceToolId = sourceToolId;
        this.title = title;
        this.author = author;
        this.countryCode = countryCode;
        this.comment = comment;
        this.exchangefile_specgroups = new ArrayList<>();
        this.exchangefile_spechierarchyroots = new ArrayList<>();
        this.exchangefile_spectypes = new ArrayList<>();
        this.exchangefile_specobjects = new ArrayList<>();
        this.exchangefile_specrelations = new ArrayList<>();
        this.exchangefile_datatypedefinitions = new ArrayList<>();
    }

    public rif11a_ExchangeFile_RIF(
        String version,        String identifier,        String creationTime,        String sourceToolId,        String title,        String author,        String countryCode,        String comment        ArrayList<ExchangeFile_SpecGroup> exchangefile_specgroups,        ArrayList<ExchangeFile_SpecHierarchyRoot> exchangefile_spechierarchyroots,        ArrayList<ExchangeFile_SpecType> exchangefile_spectypes,        ArrayList<ExchangeFile_SpecObject> exchangefile_specobjects,        ArrayList<ExchangeFile_SpecRelation> exchangefile_specrelations,        ArrayList<ExchangeFile_DatatypeDefinition> exchangefile_datatypedefinitions    ) {
        this.version = version;
        this.identifier = identifier;
        this.creationTime = creationTime;
        this.sourceToolId = sourceToolId;
        this.title = title;
        this.author = author;
        this.countryCode = countryCode;
        this.comment = comment;
        this.exchangefile_specgroups = exchangefile_specgroups;
        this.exchangefile_spechierarchyroots = exchangefile_spechierarchyroots;
        this.exchangefile_spectypes = exchangefile_spectypes;
        this.exchangefile_specobjects = exchangefile_specobjects;
        this.exchangefile_specrelations = exchangefile_specrelations;
        this.exchangefile_datatypedefinitions = exchangefile_datatypedefinitions;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
    }
    public String getSourcetoolid() {
        return sourceToolId;
    }

    public void setSourcetoolid(String sourceToolId) {
        this.sourceToolId = sourceToolId;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getCountrycode() {
        return countryCode;
    }

    public void setCountrycode(String countryCode) {
        this.countryCode = countryCode;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public List<ExchangeFile_SpecGroup> getExchangefile_specgroups() {
        return exchangefile_specgroups;
    }

    public void addExchangefile_specgroup(Exchangefile_specgroup exchangefile_specgroup) {
        this.exchangefile_specgroups.add(exchangefile_specgroup);
    }
    public List<ExchangeFile_SpecHierarchyRoot> getExchangefile_spechierarchyroots() {
        return exchangefile_spechierarchyroots;
    }

    public void addExchangefile_spechierarchyroot(Exchangefile_spechierarchyroot exchangefile_spechierarchyroot) {
        this.exchangefile_spechierarchyroots.add(exchangefile_spechierarchyroot);
    }
    public List<ExchangeFile_SpecType> getExchangefile_spectypes() {
        return exchangefile_spectypes;
    }

    public void addExchangefile_spectype(Exchangefile_spectype exchangefile_spectype) {
        this.exchangefile_spectypes.add(exchangefile_spectype);
    }
    public List<ExchangeFile_SpecObject> getExchangefile_specobjects() {
        return exchangefile_specobjects;
    }

    public void addExchangefile_specobject(Exchangefile_specobject exchangefile_specobject) {
        this.exchangefile_specobjects.add(exchangefile_specobject);
    }
    public List<ExchangeFile_SpecRelation> getExchangefile_specrelations() {
        return exchangefile_specrelations;
    }

    public void addExchangefile_specrelation(Exchangefile_specrelation exchangefile_specrelation) {
        this.exchangefile_specrelations.add(exchangefile_specrelation);
    }
    public List<ExchangeFile_DatatypeDefinition> getExchangefile_datatypedefinitions() {
        return exchangefile_datatypedefinitions;
    }

    public void addExchangefile_datatypedefinition(Exchangefile_datatypedefinition exchangefile_datatypedefinition) {
        this.exchangefile_datatypedefinitions.add(exchangefile_datatypedefinition);
    }

}