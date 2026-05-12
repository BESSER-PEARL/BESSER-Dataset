





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_CustomProperty  {

    private String name;
    private String dataType;





    private CustomPropertiesCollection custompropertiescollection;


    public DatadiagramMLBasicDef_CustomProperty(
        String name,        String dataType    ) {
        this.name = name;
        this.dataType = dataType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public CustomPropertiesCollection getCustompropertiescollection() {
        return custompropertiescollection;
    }

    public void setCustompropertiescollection(CustomPropertiesCollection custompropertiescollection) {
        this.custompropertiescollection = custompropertiescollection;
    }

}