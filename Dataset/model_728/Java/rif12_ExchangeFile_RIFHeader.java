





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_RIFHeader  {

    private String creationTime;
    private String author;
    private String title;
    private String comment;
    private String sourceToolId;
    private String identifier;



    public rif12_ExchangeFile_RIFHeader(
        String creationTime,        String author,        String title,        String comment,        String sourceToolId,        String identifier    ) {
        this.creationTime = creationTime;
        this.author = author;
        this.title = title;
        this.comment = comment;
        this.sourceToolId = sourceToolId;
        this.identifier = identifier;
    }


    public String getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(String creationTime) {
        this.creationTime = creationTime;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getSourcetoolid() {
        return sourceToolId;
    }

    public void setSourcetoolid(String sourceToolId) {
        this.sourceToolId = sourceToolId;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}