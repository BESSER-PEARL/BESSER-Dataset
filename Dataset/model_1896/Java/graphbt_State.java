





import java.util.List;
import java.util.ArrayList;

public class graphbt_State  {

    private String name;
    private String ref;
    private String desc;





    private graphbt_Component graphbt_component;




    private graphbt_MapInformation graphbt_mapinformation;




    private graphbt_Component graphbt_component;


    public graphbt_State(
        String name,        String ref,        String desc    ) {
        this.name = name;
        this.ref = ref;
        this.desc = desc;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }
    public graphbt_MapInformation getGraphbt_mapinformation() {
        return graphbt_mapinformation;
    }

    public void setGraphbt_mapinformation(graphbt_MapInformation graphbt_mapinformation) {
        this.graphbt_mapinformation = graphbt_mapinformation;
    }
    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }

}