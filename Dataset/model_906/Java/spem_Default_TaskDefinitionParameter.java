





import java.util.List;
import java.util.ArrayList;

public class spem_Default_TaskDefinitionParameter extends WorkDefinitionParameter {

    private String optionality;
    private String name;





    private spem_WorkProductDefinition spem_workproductdefinition;




    private spem_TaskDefinition spem_taskdefinition;


    public spem_Default_TaskDefinitionParameter(
        String optionality,        String name    ) {
        super(
        );
        this.optionality = optionality;
        this.name = name;
    }


    public String getOptionality() {
        return optionality;
    }

    public void setOptionality(String optionality) {
        this.optionality = optionality;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public spem_WorkProductDefinition getSpem_workproductdefinition() {
        return spem_workproductdefinition;
    }

    public void setSpem_workproductdefinition(spem_WorkProductDefinition spem_workproductdefinition) {
        this.spem_workproductdefinition = spem_workproductdefinition;
    }
    public spem_TaskDefinition getSpem_taskdefinition() {
        return spem_taskdefinition;
    }

    public void setSpem_taskdefinition(spem_TaskDefinition spem_taskdefinition) {
        this.spem_taskdefinition = spem_taskdefinition;
    }

}