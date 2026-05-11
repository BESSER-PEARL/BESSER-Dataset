





import java.util.List;
import java.util.ArrayList;

public class scxml_Validate  {

    private String schema;
    private String location;





    private scxml_ExecutableContent scxml_executablecontent;


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

    public scxml_ExecutableContent getScxml_executablecontent() {
        return scxml_executablecontent;
    }

    public void setScxml_executablecontent(scxml_ExecutableContent scxml_executablecontent) {
        this.scxml_executablecontent = scxml_executablecontent;
    }

}