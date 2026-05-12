





import java.util.List;
import java.util.ArrayList;

public class properties_DocumentRoot  {

    private String mixed;





    private List<properties_SqlProperties> properties_sqlpropertiess;




    private List<properties_DatabasePropertiesListType> properties_databasepropertieslisttypes;


    public properties_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.properties_sqlpropertiess = new ArrayList<>();
        this.properties_databasepropertieslisttypes = new ArrayList<>();
    }

    public properties_DocumentRoot(
        String mixed        ArrayList<properties_SqlProperties> properties_sqlpropertiess,        ArrayList<properties_DatabasePropertiesListType> properties_databasepropertieslisttypes    ) {
        this.mixed = mixed;
        this.properties_sqlpropertiess = properties_sqlpropertiess;
        this.properties_databasepropertieslisttypes = properties_databasepropertieslisttypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<properties_SqlProperties> getProperties_sqlpropertiess() {
        return properties_sqlpropertiess;
    }

    public void addProperties_sqlproperties(Properties_sqlproperties properties_sqlproperties) {
        this.properties_sqlpropertiess.add(properties_sqlproperties);
    }
    public List<properties_DatabasePropertiesListType> getProperties_databasepropertieslisttypes() {
        return properties_databasepropertieslisttypes;
    }

    public void addProperties_databasepropertieslisttype(Properties_databasepropertieslisttype properties_databasepropertieslisttype) {
        this.properties_databasepropertieslisttypes.add(properties_databasepropertieslisttype);
    }

}