





import java.util.List;
import java.util.ArrayList;

public class requirements_BasicElement extends ModelElement {

    private String name;
    private String id;
    private String documentation;



    public requirements_BasicElement(
        String name,        String id,        String documentation    ) {
        super(
        );
        this.name = name;
        this.id = id;
        this.documentation = documentation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }


}