





import java.util.List;
import java.util.ArrayList;

public class properties_DatabasePropertiesListType  {






    private List<properties_DatabaseProperties> properties_databasepropertiess;




    private List<properties_DatabaseAlias> properties_databasealiass;


    public properties_DatabasePropertiesListType(
    ) {
        this.properties_databasepropertiess = new ArrayList<>();
        this.properties_databasealiass = new ArrayList<>();
    }

    public properties_DatabasePropertiesListType(
        ArrayList<properties_DatabaseProperties> properties_databasepropertiess,        ArrayList<properties_DatabaseAlias> properties_databasealiass    ) {
        this.properties_databasepropertiess = properties_databasepropertiess;
        this.properties_databasealiass = properties_databasealiass;
    }


    public List<properties_DatabaseProperties> getProperties_databasepropertiess() {
        return properties_databasepropertiess;
    }

    public void addProperties_databaseproperties(Properties_databaseproperties properties_databaseproperties) {
        this.properties_databasepropertiess.add(properties_databaseproperties);
    }
    public List<properties_DatabaseAlias> getProperties_databasealiass() {
        return properties_databasealiass;
    }

    public void addProperties_databasealias(Properties_databasealias properties_databasealias) {
        this.properties_databasealiass.add(properties_databasealias);
    }

}