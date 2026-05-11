





import java.util.List;
import java.util.ArrayList;

public class common_DublinCore  {

    private String identifier;
    private String relation;
    private String created;
    private String license;
    private String publisher;
    private String language;
    private String type;
    private String valid;
    private String title;
    private String spatial;
    private String bibliographicCitation;
    private String source;
    private String description;
    private String date;
    private String rights;
    private String subject;
    private String creator;
    private String required;
    private String format;
    private String contributor;
    private String coverage;



    public common_DublinCore(
        String identifier,        String relation,        String created,        String license,        String publisher,        String language,        String type,        String valid,        String title,        String spatial,        String bibliographicCitation,        String source,        String description,        String date,        String rights,        String subject,        String creator,        String required,        String format,        String contributor,        String coverage    ) {
        this.identifier = identifier;
        this.relation = relation;
        this.created = created;
        this.license = license;
        this.publisher = publisher;
        this.language = language;
        this.type = type;
        this.valid = valid;
        this.title = title;
        this.spatial = spatial;
        this.bibliographicCitation = bibliographicCitation;
        this.source = source;
        this.description = description;
        this.date = date;
        this.rights = rights;
        this.subject = subject;
        this.creator = creator;
        this.required = required;
        this.format = format;
        this.contributor = contributor;
        this.coverage = coverage;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getRelation() {
        return relation;
    }

    public void setRelation(String relation) {
        this.relation = relation;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValid() {
        return valid;
    }

    public void setValid(String valid) {
        this.valid = valid;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getSpatial() {
        return spatial;
    }

    public void setSpatial(String spatial) {
        this.spatial = spatial;
    }
    public String getBibliographiccitation() {
        return bibliographicCitation;
    }

    public void setBibliographiccitation(String bibliographicCitation) {
        this.bibliographicCitation = bibliographicCitation;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getRights() {
        return rights;
    }

    public void setRights(String rights) {
        this.rights = rights;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getContributor() {
        return contributor;
    }

    public void setContributor(String contributor) {
        this.contributor = contributor;
    }
    public String getCoverage() {
        return coverage;
    }

    public void setCoverage(String coverage) {
        this.coverage = coverage;
    }


}