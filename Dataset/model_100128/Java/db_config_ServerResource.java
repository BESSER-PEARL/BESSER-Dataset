




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class db_config_ServerResource  {

    private LocalDate lastUpdated;
    private LocalDate lastModified;
    private int id;
    private String description;
    private String name;



    public db_config_ServerResource(
        LocalDate lastUpdated,        LocalDate lastModified,        int id,        String description,        String name    ) {
        this.lastUpdated = lastUpdated;
        this.lastModified = lastModified;
        this.id = id;
        this.description = description;
        this.name = name;
    }


    public LocalDate getLastupdated() {
        return lastUpdated;
    }

    public void setLastupdated(LocalDate lastUpdated) {
        this.lastUpdated = lastUpdated;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}