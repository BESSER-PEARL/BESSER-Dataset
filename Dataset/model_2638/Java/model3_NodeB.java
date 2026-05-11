





import java.util.List;
import java.util.ArrayList;

public class model3_NodeB  {

    private String name;





    private model3_NodeB model3_nodeb;




    private List<model3_NodeB> model3_nodebs;


    public model3_NodeB(
        String name    ) {
        this.name = name;
        this.model3_nodebs = new ArrayList<>();
    }

    public model3_NodeB(
        String name        ArrayList<model3_NodeB> model3_nodebs    ) {
        this.name = name;
        this.model3_nodebs = model3_nodebs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model3_NodeB getModel3_nodeb() {
        return model3_nodeb;
    }

    public void setModel3_nodeb(model3_NodeB model3_nodeb) {
        this.model3_nodeb = model3_nodeb;
    }
    public List<model3_NodeB> getModel3_nodebs() {
        return model3_nodebs;
    }

    public void addModel3_nodeb(Model3_nodeb model3_nodeb) {
        this.model3_nodebs.add(model3_nodeb);
    }

}