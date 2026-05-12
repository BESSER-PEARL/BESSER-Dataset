





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_CustomProperty  {

    private String dataType;
    private String name;



    public DatadiagramMLXForm_CustomProperty(
        String dataType,        String name    ) {
        this.dataType = dataType;
        this.name = name;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}