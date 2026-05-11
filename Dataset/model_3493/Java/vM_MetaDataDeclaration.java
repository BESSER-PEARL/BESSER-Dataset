





import java.util.List;
import java.util.ArrayList;

public class vM_MetaDataDeclaration extends VmBlock {

    private String date;
    private String organization;
    private String author;
    private String publication;
    private String name;
    private String description;



    public vM_MetaDataDeclaration(
        String date,        String organization,        String author,        String publication,        String name,        String description    ) {
        super(
        );
        this.date = date;
        this.organization = organization;
        this.author = author;
        this.publication = publication;
        this.name = name;
        this.description = description;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getPublication() {
        return publication;
    }

    public void setPublication(String publication) {
        this.publication = publication;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}