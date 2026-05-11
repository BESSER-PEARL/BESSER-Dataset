





import java.util.List;
import java.util.ArrayList;

public class scxml_Validate  {

    private String schema;
    private String location;





    private scxml_If scxml_if;


    public scxml_Validate(
        String schema,        String location    ) {
        this.schema = schema;
        this.location = location;
    }


    public String getSchema() {
        return schema;
    }

    public void setSchema(String schema) {
        this.schema = schema;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public scxml_If getScxml_if() {
        return scxml_if;
    }

    public void setScxml_if(scxml_If scxml_if) {
        this.scxml_if = scxml_if;
    }

}