





import java.util.List;
import java.util.ArrayList;

public class jsonldConverter_Type  {

    private String name;





    private jsonldConverter_Model jsonldconverter_model;


    public jsonldConverter_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jsonldConverter_Model getJsonldconverter_model() {
        return jsonldconverter_model;
    }

    public void setJsonldconverter_model(jsonldConverter_Model jsonldconverter_model) {
        this.jsonldconverter_model = jsonldconverter_model;
    }

}