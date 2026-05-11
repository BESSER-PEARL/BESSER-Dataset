





import java.util.List;
import java.util.ArrayList;

public class ioT_ExternalDeclaration  {

    private String name;





    private ioT_Model iot_model;


    public ioT_ExternalDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioT_Model getIot_model() {
        return iot_model;
    }

    public void setIot_model(ioT_Model iot_model) {
        this.iot_model = iot_model;
    }

}