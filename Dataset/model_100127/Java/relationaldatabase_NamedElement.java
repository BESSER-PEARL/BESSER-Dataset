





import java.util.List;
import java.util.ArrayList;

public class relationaldatabase_NamedElement extends Taggable {

    private String documentation;
    private String name;



    public relationaldatabase_NamedElement(
        String documentation,        String name    ) {
        super(
        );
        this.documentation = documentation;
        this.name = name;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}