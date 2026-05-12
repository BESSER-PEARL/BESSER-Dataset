





import java.util.List;
import java.util.ArrayList;

public class requirements_BasicElement extends ModelElement {

    private String name;
    private String documentation;
    private String id;



    public requirements_BasicElement(
        String name,        String documentation,        String id    ) {
        super(
        );
        this.name = name;
        this.documentation = documentation;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}