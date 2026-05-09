





import java.util.List;
import java.util.ArrayList;

public class robotmodel_System  {

    private String description;
    private String depends;
    private String author;
    private String author_email;
    private String name;



    public robotmodel_System(
        String description,        String depends,        String author,        String author_email,        String name    ) {
        this.description = description;
        this.depends = depends;
        this.author = author;
        this.author_email = author_email;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDepends() {
        return depends;
    }

    public void setDepends(String depends) {
        this.depends = depends;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getAuthor_email() {
        return author_email;
    }

    public void setAuthor_email(String author_email) {
        this.author_email = author_email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}