





import java.util.List;
import java.util.ArrayList;

public class simplepdl_NeedSet extends ProcessElement {

    private String name;





    private simplepdl_Need simplepdl_need;




    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private List<simplepdl_Need> simplepdl_needs;




    private simplepdl_WorkDefinition simplepdl_workdefinition;


    public simplepdl_NeedSet(
        String name    ) {
        super(
        );
        this.name = name;
        this.simplepdl_needs = new ArrayList<>();
    }

    public simplepdl_NeedSet(
        String name        ArrayList<simplepdl_Need> simplepdl_needs    ) {
        this.name = name;
        this.simplepdl_needs = simplepdl_needs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplepdl_Need getSimplepdl_need() {
        return simplepdl_need;
    }

    public void setSimplepdl_need(simplepdl_Need simplepdl_need) {
        this.simplepdl_need = simplepdl_need;
    }
    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }
    public List<simplepdl_Need> getSimplepdl_needs() {
        return simplepdl_needs;
    }

    public void addSimplepdl_need(Simplepdl_need simplepdl_need) {
        this.simplepdl_needs.add(simplepdl_need);
    }
    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }

}