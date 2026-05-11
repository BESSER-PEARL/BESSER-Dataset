





import java.util.List;
import java.util.ArrayList;

public class scxml_Datamodel extends DescriptionContainer {

    private String schema;



    public scxml_Datamodel(
        String schema    ) {
        super(
        );
        this.schema = schema;
    }


    public String getSchema() {
        return schema;
    }

    public void setSchema(String schema) {
        this.schema = schema;
    }


}