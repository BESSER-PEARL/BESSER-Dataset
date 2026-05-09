





import java.util.List;
import java.util.ArrayList;

public class graphbt_Component  {

    private String componentRef;
    private boolean enumerated;
    private int id;
    private String componentName;
    private String componentDesc;





    private List<graphbt_Component> graphbt_components;




    private graphbt_ComponentList graphbt_componentlist;


    public graphbt_Component(
        String componentRef,        boolean enumerated,        int id,        String componentName,        String componentDesc    ) {
        this.componentRef = componentRef;
        this.enumerated = enumerated;
        this.id = id;
        this.componentName = componentName;
        this.componentDesc = componentDesc;
        this.graphbt_components = new ArrayList<>();
    }

    public graphbt_Component(
        String componentRef,        boolean enumerated,        int id,        String componentName,        String componentDesc        ArrayList<graphbt_Component> graphbt_components    ) {
        this.componentRef = componentRef;
        this.enumerated = enumerated;
        this.id = id;
        this.componentName = componentName;
        this.componentDesc = componentDesc;
        this.graphbt_components = graphbt_components;
    }

    public String getComponentref() {
        return componentRef;
    }

    public void setComponentref(String componentRef) {
        this.componentRef = componentRef;
    }
    public boolean getEnumerated() {
        return enumerated;
    }

    public void setEnumerated(boolean enumerated) {
        this.enumerated = enumerated;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getComponentname() {
        return componentName;
    }

    public void setComponentname(String componentName) {
        this.componentName = componentName;
    }
    public String getComponentdesc() {
        return componentDesc;
    }

    public void setComponentdesc(String componentDesc) {
        this.componentDesc = componentDesc;
    }

    public List<graphbt_Component> getGraphbt_components() {
        return graphbt_components;
    }

    public void addGraphbt_component(Graphbt_component graphbt_component) {
        this.graphbt_components.add(graphbt_component);
    }
    public graphbt_ComponentList getGraphbt_componentlist() {
        return graphbt_componentlist;
    }

    public void setGraphbt_componentlist(graphbt_ComponentList graphbt_componentlist) {
        this.graphbt_componentlist = graphbt_componentlist;
    }

}