




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_Library  {

    private String name;
    private LocalDate created;
    private String height;
    private String depth;
    private LocalDate update;
    private String shortDescription;
    private String width;
    private String description;



    public decobat_Library(
        String name,        LocalDate created,        String height,        String depth,        LocalDate update,        String shortDescription,        String width,        String description    ) {
        this.name = name;
        this.created = created;
        this.height = height;
        this.depth = depth;
        this.update = update;
        this.shortDescription = shortDescription;
        this.width = width;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getDepth() {
        return depth;
    }

    public void setDepth(String depth) {
        this.depth = depth;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}