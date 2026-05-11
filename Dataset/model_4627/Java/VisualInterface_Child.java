





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Child  {

    private String name;





    private VisualInterface_Primitive visualinterface_primitive;


    public VisualInterface_Child(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public VisualInterface_Primitive getVisualinterface_primitive() {
        return visualinterface_primitive;
    }

    public void setVisualinterface_primitive(VisualInterface_Primitive visualinterface_primitive) {
        this.visualinterface_primitive = visualinterface_primitive;
    }

}