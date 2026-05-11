





import java.util.List;
import java.util.ArrayList;

public class ioT_Config  {

    private String name;





    private List<ioT_Declaration> iot_declarations;




    private ioT_Model iot_model;


    public ioT_Config(
        String name    ) {
        this.name = name;
        this.iot_declarations = new ArrayList<>();
    }

    public ioT_Config(
        String name        ArrayList<ioT_Declaration> iot_declarations    ) {
        this.name = name;
        this.iot_declarations = iot_declarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ioT_Declaration> getIot_declarations() {
        return iot_declarations;
    }

    public void addIot_declaration(Iot_declaration iot_declaration) {
        this.iot_declarations.add(iot_declaration);
    }
    public ioT_Model getIot_model() {
        return iot_model;
    }

    public void setIot_model(ioT_Model iot_model) {
        this.iot_model = iot_model;
    }

}