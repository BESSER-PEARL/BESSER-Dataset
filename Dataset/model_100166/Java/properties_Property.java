





import java.util.List;
import java.util.ArrayList;

public class properties_Property  {

    private String value;
    private String key;





    private properties_DatabaseProperties properties_databaseproperties;


    public properties_Property(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public properties_DatabaseProperties getProperties_databaseproperties() {
        return properties_databaseproperties;
    }

    public void setProperties_databaseproperties(properties_DatabaseProperties properties_databaseproperties) {
        this.properties_databaseproperties = properties_databaseproperties;
    }

}