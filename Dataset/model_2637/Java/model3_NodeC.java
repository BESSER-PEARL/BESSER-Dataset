





import java.util.List;
import java.util.ArrayList;

public class model3_NodeC  {

    private String name;





    private model3_NodeC model3_nodec;




    private List<model3_NodeC> model3_nodecs;




    private model3_NodeC model3_nodec;




    private model3_NodeC model3_nodec;


    public model3_NodeC(
        String name    ) {
        this.name = name;
        this.model3_nodecs = new ArrayList<>();
    }

    public model3_NodeC(
        String name        ArrayList<model3_NodeC> model3_nodecs    ) {
        this.name = name;
        this.model3_nodecs = model3_nodecs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model3_NodeC getModel3_nodec() {
        return model3_nodec;
    }

    public void setModel3_nodec(model3_NodeC model3_nodec) {
        this.model3_nodec = model3_nodec;
    }
    public List<model3_NodeC> getModel3_nodecs() {
        return model3_nodecs;
    }

    public void addModel3_nodec(Model3_nodec model3_nodec) {
        this.model3_nodecs.add(model3_nodec);
    }
    public model3_NodeC getModel3_nodec() {
        return model3_nodec;
    }

    public void setModel3_nodec(model3_NodeC model3_nodec) {
        this.model3_nodec = model3_nodec;
    }
    public model3_NodeC getModel3_nodec() {
        return model3_nodec;
    }

    public void setModel3_nodec(model3_NodeC model3_nodec) {
        this.model3_nodec = model3_nodec;
    }

}