





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactFunctions  {

    private String lifecycleclass;
    private String renderclass;





    private List<myDsl_EObject> mydsl_eobjects;


    public myDsl_ReactFunctions(
        String lifecycleclass,        String renderclass    ) {
        this.lifecycleclass = lifecycleclass;
        this.renderclass = renderclass;
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_ReactFunctions(
        String lifecycleclass,        String renderclass        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.lifecycleclass = lifecycleclass;
        this.renderclass = renderclass;
        this.mydsl_eobjects = mydsl_eobjects;
    }

    public String getLifecycleclass() {
        return lifecycleclass;
    }

    public void setLifecycleclass(String lifecycleclass) {
        this.lifecycleclass = lifecycleclass;
    }
    public String getRenderclass() {
        return renderclass;
    }

    public void setRenderclass(String renderclass) {
        this.renderclass = renderclass;
    }

    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }

}