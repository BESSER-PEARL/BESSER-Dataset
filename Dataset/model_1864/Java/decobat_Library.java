




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class decobat_Library  {

    private String width;
    private String shortDescription;
    private String description;
    private String height;
    private LocalDate created;
    private String name;
    private String depth;
    private LocalDate update;



    public decobat_Library(
        String width,        String shortDescription,        String description,        String height,        LocalDate created,        String name,        String depth,        LocalDate update    ) {
        this.width = width;
        this.shortDescription = shortDescription;
        this.description = description;
        this.height = height;
        this.created = created;
        this.name = name;
        this.depth = depth;
        this.update = update;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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


}