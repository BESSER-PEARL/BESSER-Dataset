





import java.util.List;
import java.util.ArrayList;

public class WT_Architecture  {

    private String name;





    private WT_Subsystem wt_subsystem;




    private List<WT_Component> wt_components;


    public WT_Architecture(
        String name    ) {
        this.name = name;
        this.wt_components = new ArrayList<>();
    }

    public WT_Architecture(
        String name        ArrayList<WT_Component> wt_components    ) {
        this.name = name;
        this.wt_components = wt_components;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public WT_Subsystem getWt_subsystem() {
        return wt_subsystem;
    }

    public void setWt_subsystem(WT_Subsystem wt_subsystem) {
        this.wt_subsystem = wt_subsystem;
    }
    public List<WT_Component> getWt_components() {
        return wt_components;
    }

    public void addWt_component(Wt_component wt_component) {
        this.wt_components.add(wt_component);
    }

}