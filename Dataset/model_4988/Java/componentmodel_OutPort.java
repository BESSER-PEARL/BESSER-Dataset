





import java.util.List;
import java.util.ArrayList;

public class componentmodel_OutPort extends Port {






    private componentmodel_OutPort componentmodel_outport;




    private List<componentmodel_InPort> componentmodel_inports;




    private componentmodel_OutPort componentmodel_outport;




    private componentmodel_InPort componentmodel_inport;


    public componentmodel_OutPort(
    ) {
        super(
        );
        this.componentmodel_inports = new ArrayList<>();
    }

    public componentmodel_OutPort(
        ArrayList<componentmodel_InPort> componentmodel_inports    ) {
        this.componentmodel_inports = componentmodel_inports;
    }


    public componentmodel_OutPort getComponentmodel_outport() {
        return componentmodel_outport;
    }

    public void setComponentmodel_outport(componentmodel_OutPort componentmodel_outport) {
        this.componentmodel_outport = componentmodel_outport;
    }
    public List<componentmodel_InPort> getComponentmodel_inports() {
        return componentmodel_inports;
    }

    public void addComponentmodel_inport(Componentmodel_inport componentmodel_inport) {
        this.componentmodel_inports.add(componentmodel_inport);
    }
    public componentmodel_OutPort getComponentmodel_outport() {
        return componentmodel_outport;
    }

    public void setComponentmodel_outport(componentmodel_OutPort componentmodel_outport) {
        this.componentmodel_outport = componentmodel_outport;
    }
    public componentmodel_InPort getComponentmodel_inport() {
        return componentmodel_inport;
    }

    public void setComponentmodel_inport(componentmodel_InPort componentmodel_inport) {
        this.componentmodel_inport = componentmodel_inport;
    }

}