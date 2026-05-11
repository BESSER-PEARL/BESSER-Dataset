





import java.util.List;
import java.util.ArrayList;

public class model3_NodeE  {

    private String name;





    private List<model3_NodeA> model3_nodeas;




    private model3_NodeA model3_nodea;


    public model3_NodeE(
        String name    ) {
        this.name = name;
        this.model3_nodeas = new ArrayList<>();
    }

    public model3_NodeE(
        String name        ArrayList<model3_NodeA> model3_nodeas    ) {
        this.name = name;
        this.model3_nodeas = model3_nodeas;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model3_NodeA> getModel3_nodeas() {
        return model3_nodeas;
    }

    public void addModel3_nodea(Model3_nodea model3_nodea) {
        this.model3_nodeas.add(model3_nodea);
    }
    public model3_NodeA getModel3_nodea() {
        return model3_nodea;
    }

    public void setModel3_nodea(model3_NodeA model3_nodea) {
        this.model3_nodea = model3_nodea;
    }

}