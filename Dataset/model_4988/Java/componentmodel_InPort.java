





import java.util.List;
import java.util.ArrayList;

public class componentmodel_InPort extends Port {






    private List<componentmodel_InPort> componentmodel_inports;




    private componentmodel_InPort componentmodel_inport;


    public componentmodel_InPort(
    ) {
        super(
        );
        this.componentmodel_inports = new ArrayList<>();
    }

    public componentmodel_InPort(
        ArrayList<componentmodel_InPort> componentmodel_inports    ) {
        this.componentmodel_inports = componentmodel_inports;
    }


    public List<componentmodel_InPort> getComponentmodel_inports() {
        return componentmodel_inports;
    }

    public void addComponentmodel_inport(Componentmodel_inport componentmodel_inport) {
        this.componentmodel_inports.add(componentmodel_inport);
    }
    public componentmodel_InPort getComponentmodel_inport() {
        return componentmodel_inport;
    }

    public void setComponentmodel_inport(componentmodel_InPort componentmodel_inport) {
        this.componentmodel_inport = componentmodel_inport;
    }

}