





import java.util.List;
import java.util.ArrayList;

public class simplepdl_GuidanceLink extends ProcessElement {






    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_Guidance simplepdl_guidance;


    public simplepdl_GuidanceLink(
    ) {
        super(
        );
    }



    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }
    public simplepdl_Guidance getSimplepdl_guidance() {
        return simplepdl_guidance;
    }

    public void setSimplepdl_guidance(simplepdl_Guidance simplepdl_guidance) {
        this.simplepdl_guidance = simplepdl_guidance;
    }

}