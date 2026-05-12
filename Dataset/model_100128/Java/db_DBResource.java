




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class db_DBResource  {

    private String name;
    private LocalDate lastModified;
    private LocalDate lastUpdated;
    private int id;



    public db_DBResource(
        String name,        LocalDate lastModified,        LocalDate lastUpdated,        int id    ) {
        this.name = name;
        this.lastModified = lastModified;
        this.lastUpdated = lastUpdated;
        this.id = id;
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
    public LocalDate getLastupdated() {
        return lastUpdated;
    }

    public void setLastupdated(LocalDate lastUpdated) {
        this.lastUpdated = lastUpdated;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}