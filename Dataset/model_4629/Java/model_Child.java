





import java.util.List;
import java.util.ArrayList;

public class model_Child  {

    private String name;





    private model_Primitive model_primitive;


    public model_Child(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Primitive getModel_primitive() {
        return model_primitive;
    }

    public void setModel_primitive(model_Primitive model_primitive) {
        this.model_primitive = model_primitive;
    }

}