





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Primitive  {

    private String name;





    private VisualInterface_Symbol visualinterface_symbol;


    public VisualInterface_Primitive(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public VisualInterface_Symbol getVisualinterface_symbol() {
        return visualinterface_symbol;
    }

    public void setVisualinterface_symbol(VisualInterface_Symbol visualinterface_symbol) {
        this.visualinterface_symbol = visualinterface_symbol;
    }

}