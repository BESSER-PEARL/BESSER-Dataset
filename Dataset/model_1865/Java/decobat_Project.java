




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_Project  {

    private LocalDate closed;
    private String name;
    private LocalDate created;
    private String shortDescription;
    private String description;



    public decobat_Project(
        LocalDate closed,        String name,        LocalDate created,        String shortDescription,        String description    ) {
        this.closed = closed;
        this.name = name;
        this.created = created;
        this.shortDescription = shortDescription;
        this.description = description;
    }


    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
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


}