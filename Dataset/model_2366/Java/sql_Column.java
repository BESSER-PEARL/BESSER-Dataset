





import java.util.List;
import java.util.ArrayList;

public class sql_Column extends ModelElement, NamedElement {

    private String type;
    private String properties;



    public sql_Column(
        String type,        String properties    ) {
        super(
        );
        this.type = type;
        this.properties = properties;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }


}