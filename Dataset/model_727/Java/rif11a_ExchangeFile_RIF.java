





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_RIF  {

    private String author;
    private String title;
    private String version;
    private String creationTime;
    private String identifier;
    private String countryCode;
    private String sourceToolId;
    private String comment;



    public rif11a_ExchangeFile_RIF(
        String author,        String title,        String version,        String creationTime,        String identifier,        String countryCode,        String sourceToolId,        String comment    ) {
        this.author = author;
        this.title = title;
        this.version = version;
        this.creationTime = creationTime;
        this.identifier = identifier;
        this.countryCode = countryCode;
        this.sourceToolId = sourceToolId;
        this.comment = comment;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getCountrycode() {
        return countryCode;
    }

    public void setCountrycode(String countryCode) {
        this.countryCode = countryCode;
    }
    public String getSourcetoolid() {
        return sourceToolId;
    }

    public void setSourcetoolid(String sourceToolId) {
        this.sourceToolId = sourceToolId;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}