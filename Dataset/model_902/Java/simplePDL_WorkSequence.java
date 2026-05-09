





import java.util.List;
import java.util.ArrayList;

public class simplePDL_WorkSequence  {

    private String linkType;





    private simplePDL_Process simplepdl_process;




    private List<simplePDL_WorkDefinition> simplepdl_workdefinitions;




    private simplePDL_WorkDefinition simplepdl_workdefinition;




    private simplePDL_WorkDefinition simplepdl_workdefinition;




    private List<simplePDL_WorkDefinition> simplepdl_workdefinitions;


    public simplePDL_WorkSequence(
        String linkType    ) {
        this.linkType = linkType;
        this.simplepdl_workdefinitions = new ArrayList<>();
        this.simplepdl_workdefinitions = new ArrayList<>();
    }

    public simplePDL_WorkSequence(
        String linkType        ArrayList<simplePDL_WorkDefinition> simplepdl_workdefinitions,        ArrayList<simplePDL_WorkDefinition> simplepdl_workdefinitions    ) {
        this.linkType = linkType;
        this.simplepdl_workdefinitions = simplepdl_workdefinitions;
        this.simplepdl_workdefinitions = simplepdl_workdefinitions;
    }

    public String getLinktype() {
        return linkType;
    }

    public void setLinktype(String linkType) {
        this.linkType = linkType;
    }

    public simplePDL_Process getSimplepdl_process() {
        return simplepdl_process;
    }

    public void setSimplepdl_process(simplePDL_Process simplepdl_process) {
        this.simplepdl_process = simplepdl_process;
    }
    public List<simplePDL_WorkDefinition> getSimplepdl_workdefinitions() {
        return simplepdl_workdefinitions;
    }

    public void addSimplepdl_workdefinition(Simplepdl_workdefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinitions.add(simplepdl_workdefinition);
    }
    public simplePDL_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplePDL_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }
    public simplePDL_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplePDL_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }
    public List<simplePDL_WorkDefinition> getSimplepdl_workdefinitions() {
        return simplepdl_workdefinitions;
    }

    public void addSimplepdl_workdefinition(Simplepdl_workdefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinitions.add(simplepdl_workdefinition);
    }

}