





import java.util.List;
import java.util.ArrayList;

public class express_Rule  {

    private String name;





    private express_Schema express_schema;


    public express_Rule(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public express_Schema getExpress_schema() {
        return express_schema;
    }

    public void setExpress_schema(express_Schema express_schema) {
        this.express_schema = express_schema;
    }

}