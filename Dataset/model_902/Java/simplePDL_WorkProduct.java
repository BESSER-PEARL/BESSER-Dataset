





import java.util.List;
import java.util.ArrayList;

public class simplePDL_WorkProduct  {

    private String name;





    private simplePDL_WorkDefinitionParameter simplepdl_workdefinitionparameter;


    public simplePDL_WorkProduct(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplePDL_WorkDefinitionParameter getSimplepdl_workdefinitionparameter() {
        return simplepdl_workdefinitionparameter;
    }

    public void setSimplepdl_workdefinitionparameter(simplePDL_WorkDefinitionParameter simplepdl_workdefinitionparameter) {
        this.simplepdl_workdefinitionparameter = simplepdl_workdefinitionparameter;
    }

}