




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_ProjectCategory  {

    private LocalDate created;
    private String name;
    private String description;
    private String shortDescription;





    private decobat_Project decobat_project;


    public decobat_ProjectCategory(
        LocalDate created,        String name,        String description,        String shortDescription    ) {
        this.created = created;
        this.name = name;
        this.description = description;
        this.shortDescription = shortDescription;
    }


    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
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
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }

    public decobat_Project getDecobat_project() {
        return decobat_project;
    }

    public void setDecobat_project(decobat_Project decobat_project) {
        this.decobat_project = decobat_project;
    }

}