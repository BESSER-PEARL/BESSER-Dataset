





import java.util.List;
import java.util.ArrayList;

public class spem_WorkDefinitionParameter  {

    private String direction;





    private spem_WorkDefinition spem_workdefinition;


    public spem_WorkDefinitionParameter(
        String direction    ) {
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public spem_WorkDefinition getSpem_workdefinition() {
        return spem_workdefinition;
    }

    public void setSpem_workdefinition(spem_WorkDefinition spem_workdefinition) {
        this.spem_workdefinition = spem_workdefinition;
    }

}