





import java.util.List;
import java.util.ArrayList;

public class persistence_Persistence  {

    private boolean timestampCreation;
    private String databaseTechnology;
    private boolean timestampUpdates;
    private String ormTechnology;



    public persistence_Persistence(
        boolean timestampCreation,        String databaseTechnology,        boolean timestampUpdates,        String ormTechnology    ) {
        this.timestampCreation = timestampCreation;
        this.databaseTechnology = databaseTechnology;
        this.timestampUpdates = timestampUpdates;
        this.ormTechnology = ormTechnology;
    }


    public boolean getTimestampcreation() {
        return timestampCreation;
    }

    public void setTimestampcreation(boolean timestampCreation) {
        this.timestampCreation = timestampCreation;
    }
    public String getDatabasetechnology() {
        return databaseTechnology;
    }

    public void setDatabasetechnology(String databaseTechnology) {
        this.databaseTechnology = databaseTechnology;
    }
    public boolean getTimestampupdates() {
        return timestampUpdates;
    }

    public void setTimestampupdates(boolean timestampUpdates) {
        this.timestampUpdates = timestampUpdates;
    }
    public String getOrmtechnology() {
        return ormTechnology;
    }

    public void setOrmtechnology(String ormTechnology) {
        this.ormTechnology = ormTechnology;
    }


}