





import java.util.List;
import java.util.ArrayList;

public class table_description_TableVariable extends tool_VariableContainer, description_AbstractVariable {

    private String documentation;



    public table_description_TableVariable(
        String documentation    ) {
        super(
        );
        this.documentation = documentation;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }


}