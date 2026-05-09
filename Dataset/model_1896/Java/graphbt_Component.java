





import java.util.List;
import java.util.ArrayList;

public class graphbt_Component  {

    private boolean enumerated;
    private String componentRef;
    private String componentDesc;
    private String componentName;
    private int id;





    private graphbt_Component graphbt_component;




    private graphbt_ComponentList graphbt_componentlist;


    public graphbt_Component(
        boolean enumerated,        String componentRef,        String componentDesc,        String componentName,        int id    ) {
        this.enumerated = enumerated;
        this.componentRef = componentRef;
        this.componentDesc = componentDesc;
        this.componentName = componentName;
        this.id = id;
    }


    public boolean getEnumerated() {
        return enumerated;
    }

    public void setEnumerated(boolean enumerated) {
        this.enumerated = enumerated;
    }
    public String getComponentref() {
        return componentRef;
    }

    public void setComponentref(String componentRef) {
        this.componentRef = componentRef;
    }
    public String getComponentdesc() {
        return componentDesc;
    }

    public void setComponentdesc(String componentDesc) {
        this.componentDesc = componentDesc;
    }
    public String getComponentname() {
        return componentName;
    }

    public void setComponentname(String componentName) {
        this.componentName = componentName;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }
    public graphbt_ComponentList getGraphbt_componentlist() {
        return graphbt_componentlist;
    }

    public void setGraphbt_componentlist(graphbt_ComponentList graphbt_componentlist) {
        this.graphbt_componentlist = graphbt_componentlist;
    }

}