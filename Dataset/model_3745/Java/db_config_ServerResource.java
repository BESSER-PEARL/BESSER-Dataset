




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class db_config_ServerResource  {

    private String name;
    private LocalDate lastModified;
    private String description;
    private int id;
    private LocalDate lastUpdated;



    public db_config_ServerResource(
        String name,        LocalDate lastModified,        String description,        int id,        LocalDate lastUpdated    ) {
        this.name = name;
        this.lastModified = lastModified;
        this.description = description;
        this.id = id;
        this.lastUpdated = lastUpdated;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getLastupdated() {
        return lastUpdated;
    }

    public void setLastupdated(LocalDate lastUpdated) {
        this.lastUpdated = lastUpdated;
    }


}