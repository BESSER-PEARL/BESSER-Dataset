





import java.util.List;
import java.util.ArrayList;

public class spem_ProcessParameter extends WorkDefinitionParameter, BreakdownElement {

    private String optionality;



    public spem_ProcessParameter(
        String optionality    ) {
        super(
        );
        this.optionality = optionality;
    }


    public String getOptionality() {
        return optionality;
    }

    public void setOptionality(String optionality) {
        this.optionality = optionality;
    }


}