





import java.util.List;
import java.util.ArrayList;

public class model3_NodeD  {

    private String name;





    private model3_NodeD model3_noded;




    private model3_NodeD model3_noded;




    private model3_NodeD model3_noded;




    private List<model3_NodeD> model3_nodeds;


    public model3_NodeD(
        String name    ) {
        this.name = name;
        this.model3_nodeds = new ArrayList<>();
    }

    public model3_NodeD(
        String name        ArrayList<model3_NodeD> model3_nodeds    ) {
        this.name = name;
        this.model3_nodeds = model3_nodeds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model3_NodeD getModel3_noded() {
        return model3_noded;
    }

    public void setModel3_noded(model3_NodeD model3_noded) {
        this.model3_noded = model3_noded;
    }
    public model3_NodeD getModel3_noded() {
        return model3_noded;
    }

    public void setModel3_noded(model3_NodeD model3_noded) {
        this.model3_noded = model3_noded;
    }
    public model3_NodeD getModel3_noded() {
        return model3_noded;
    }

    public void setModel3_noded(model3_NodeD model3_noded) {
        this.model3_noded = model3_noded;
    }
    public List<model3_NodeD> getModel3_nodeds() {
        return model3_nodeds;
    }

    public void addModel3_noded(Model3_noded model3_noded) {
        this.model3_nodeds.add(model3_noded);
    }

}