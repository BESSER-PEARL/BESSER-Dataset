





import java.util.List;
import java.util.ArrayList;

public class edd_Model  {

    private String name;





    private edd_Diagram edd_diagram;


    public edd_Model(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public edd_Diagram getEdd_diagram() {
        return edd_diagram;
    }

    public void setEdd_diagram(edd_Diagram edd_diagram) {
        this.edd_diagram = edd_diagram;
    }

}