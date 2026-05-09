




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_ProjectRevision  {

    private String description;
    private LocalDate update;
    private String shortDescription;
    private String comment;





    private decobat_Project decobat_project;


    public decobat_ProjectRevision(
        String description,        LocalDate update,        String shortDescription,        String comment    ) {
        this.description = description;
        this.update = update;
        this.shortDescription = shortDescription;
        this.comment = comment;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getUpdate() {
        return update;
    }

    public void setUpdate(LocalDate update) {
        this.update = update;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public decobat_Project getDecobat_project() {
        return decobat_project;
    }

    public void setDecobat_project(decobat_Project decobat_project) {
        this.decobat_project = decobat_project;
    }

}