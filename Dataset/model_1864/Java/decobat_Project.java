




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_Project  {

    private String shortDescription;
    private String description;
    private LocalDate closed;
    private LocalDate created;
    private String name;





    private List<decobat_ProjectRevision> decobat_projectrevisions;


    public decobat_Project(
        String shortDescription,        String description,        LocalDate closed,        LocalDate created,        String name    ) {
        this.shortDescription = shortDescription;
        this.description = description;
        this.closed = closed;
        this.created = created;
        this.name = name;
        this.decobat_projectrevisions = new ArrayList<>();
    }

    public decobat_Project(
        String shortDescription,        String description,        LocalDate closed,        LocalDate created,        String name        ArrayList<decobat_ProjectRevision> decobat_projectrevisions    ) {
        this.shortDescription = shortDescription;
        this.description = description;
        this.closed = closed;
        this.created = created;
        this.name = name;
        this.decobat_projectrevisions = decobat_projectrevisions;
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
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
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

    public List<decobat_ProjectRevision> getDecobat_projectrevisions() {
        return decobat_projectrevisions;
    }

    public void addDecobat_projectrevision(Decobat_projectrevision decobat_projectrevision) {
        this.decobat_projectrevisions.add(decobat_projectrevision);
    }

}