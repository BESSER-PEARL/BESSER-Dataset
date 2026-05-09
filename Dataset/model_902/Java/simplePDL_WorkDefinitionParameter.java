





import java.util.List;
import java.util.ArrayList;

public class simplePDL_WorkDefinitionParameter  {

    private String parameterKind;





    private simplePDL_WorkDefinition simplepdl_workdefinition;


    public simplePDL_WorkDefinitionParameter(
        String parameterKind    ) {
        this.parameterKind = parameterKind;
    }


    public String getParameterkind() {
        return parameterKind;
    }

    public void setParameterkind(String parameterKind) {
        this.parameterKind = parameterKind;
    }

    public simplePDL_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplePDL_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }

}