





import java.util.List;
import java.util.ArrayList;

public class notation_StringToPropertyValueMapEntry  {

    private String key;





    private notation_PropertiesSetStyle notation_propertiessetstyle;




    private notation_PropertyValue notation_propertyvalue;


    public notation_StringToPropertyValueMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public notation_PropertiesSetStyle getNotation_propertiessetstyle() {
        return notation_propertiessetstyle;
    }

    public void setNotation_propertiessetstyle(notation_PropertiesSetStyle notation_propertiessetstyle) {
        this.notation_propertiessetstyle = notation_propertiessetstyle;
    }
    public notation_PropertyValue getNotation_propertyvalue() {
        return notation_propertyvalue;
    }

    public void setNotation_propertyvalue(notation_PropertyValue notation_propertyvalue) {
        this.notation_propertyvalue = notation_propertyvalue;
    }

}