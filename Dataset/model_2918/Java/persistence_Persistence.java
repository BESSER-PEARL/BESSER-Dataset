





import java.util.List;
import java.util.ArrayList;

public class persistence_Persistence  {

    private String ormTechnology;
    private boolean timestampUpdates;
    private String databaseTechnology;
    private boolean timestampCreation;



    public persistence_Persistence(
        String ormTechnology,        boolean timestampUpdates,        String databaseTechnology,        boolean timestampCreation    ) {
        this.ormTechnology = ormTechnology;
        this.timestampUpdates = timestampUpdates;
        this.databaseTechnology = databaseTechnology;
        this.timestampCreation = timestampCreation;
    }


    public String getOrmtechnology() {
        return ormTechnology;
    }

    public void setOrmtechnology(String ormTechnology) {
        this.ormTechnology = ormTechnology;
    }
    public boolean getTimestampupdates() {
        return timestampUpdates;
    }

    public void setTimestampupdates(boolean timestampUpdates) {
        this.timestampUpdates = timestampUpdates;
    }
    public String getDatabasetechnology() {
        return databaseTechnology;
    }

    public void setDatabasetechnology(String databaseTechnology) {
        this.databaseTechnology = databaseTechnology;
    }
    public boolean getTimestampcreation() {
        return timestampCreation;
    }

    public void setTimestampcreation(boolean timestampCreation) {
        this.timestampCreation = timestampCreation;
    }


}