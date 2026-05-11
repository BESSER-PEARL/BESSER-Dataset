




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class db_DBResource  {

    private LocalDate lastUpdated;
    private String name;
    private LocalDate lastModified;
    private int id;



    public db_DBResource(
        LocalDate lastUpdated,        String name,        LocalDate lastModified,        int id    ) {
        this.lastUpdated = lastUpdated;
        this.name = name;
        this.lastModified = lastModified;
        this.id = id;
    }


    public LocalDate getLastupdated() {
        return lastUpdated;
    }

    public void setLastupdated(LocalDate lastUpdated) {
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}