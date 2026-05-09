




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_LibraryCategory  {

    private String name;
    private String shortDescription;
    private LocalDate created;
    private String description;





    private decobat_Library decobat_library;


    public decobat_LibraryCategory(
        String name,        String shortDescription,        LocalDate created,        String description    ) {
        this.name = name;
        this.shortDescription = shortDescription;
        this.created = created;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public decobat_Library getDecobat_library() {
        return decobat_library;
    }

    public void setDecobat_library(decobat_Library decobat_library) {
        this.decobat_library = decobat_library;
    }

}