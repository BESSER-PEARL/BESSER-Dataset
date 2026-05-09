





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_RIFHeader  {

    private String comment;
    private String author;
    private String identifier;
    private String sourceToolId;
    private String title;
    private String creationTime;



    public rif12_ExchangeFile_RIFHeader(
        String comment,        String author,        String identifier,        String sourceToolId,        String title,        String creationTime    ) {
        this.comment = comment;
        this.author = author;
        this.identifier = identifier;
        this.sourceToolId = sourceToolId;
        this.title = title;
        this.creationTime = creationTime;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
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
    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
    }


}