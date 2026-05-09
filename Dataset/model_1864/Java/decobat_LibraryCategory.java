




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_LibraryCategory  {

    private String name;
    private LocalDate created;
    private String shortDescription;
    private String description;





    private decobat_Library decobat_library;


    public decobat_LibraryCategory(
        String name,        LocalDate created,        String shortDescription,        String description    ) {
        this.name = name;
        this.created = created;
        this.shortDescription = shortDescription;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
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