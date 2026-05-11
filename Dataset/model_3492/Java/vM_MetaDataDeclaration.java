





import java.util.List;
import java.util.ArrayList;

public class vM_MetaDataDeclaration extends VmBlock {

    private String name;
    private String date;
    private String description;
    private String publication;
    private String organization;
    private String author;



    public vM_MetaDataDeclaration(
        String name,        String date,        String description,        String publication,        String organization,        String author    ) {
        super(
        );
        this.name = name;
        this.date = date;
        this.description = description;
        this.publication = publication;
        this.organization = organization;
        this.author = author;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPublication() {
        return publication;
    }

    public void setPublication(String publication) {
        this.publication = publication;
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


}