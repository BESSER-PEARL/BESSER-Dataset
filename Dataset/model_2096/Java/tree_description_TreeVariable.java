





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeVariable extends tool_VariableContainer, description_AbstractVariable {

    private String documentation;



    public tree_description_TreeVariable(
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