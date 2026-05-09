





import java.util.List;
import java.util.ArrayList;

public class spem_WorkDefinitionParameter  {

    private String name;
    private String direction;
    private String optionality;





    private spem_WorkDefinition spem_workdefinition;


    public spem_WorkDefinitionParameter(
        String name,        String direction,        String optionality    ) {
        this.name = name;
        this.direction = direction;
        this.optionality = optionality;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getOptionality() {
        return optionality;
    }

    public void setOptionality(String optionality) {
        this.optionality = optionality;
    }

    public spem_WorkDefinition getSpem_workdefinition() {
        return spem_workdefinition;
    }

    public void setSpem_workdefinition(spem_WorkDefinition spem_workdefinition) {
        this.spem_workdefinition = spem_workdefinition;
    }

}