





import java.util.List;
import java.util.ArrayList;

public class documentation_TermEntry extends NamedElement {

    private String description;





    private documentation_Documentation documentation_documentation;


    public documentation_TermEntry(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public documentation_Documentation getDocumentation_documentation() {
        return documentation_documentation;
    }

    public void setDocumentation_documentation(documentation_Documentation documentation_documentation) {
        this.documentation_documentation = documentation_documentation;
    }

}