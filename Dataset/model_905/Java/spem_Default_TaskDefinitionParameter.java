





import java.util.List;
import java.util.ArrayList;

public class spem_Default_TaskDefinitionParameter extends WorkDefinitionParameter {

    private String name;
    private String optionality;





    private spem_TaskDefinition spem_taskdefinition;


    public spem_Default_TaskDefinitionParameter(
        String name,        String optionality    ) {
        super(
        );
        this.name = name;
        this.optionality = optionality;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOptionality() {
        return optionality;
    }

    public void setOptionality(String optionality) {
        this.optionality = optionality;
    }

    public spem_TaskDefinition getSpem_taskdefinition() {
        return spem_taskdefinition;
    }

    public void setSpem_taskdefinition(spem_TaskDefinition spem_taskdefinition) {
        this.spem_taskdefinition = spem_taskdefinition;
    }

}