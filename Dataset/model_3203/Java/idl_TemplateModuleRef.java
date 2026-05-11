





import java.util.List;
import java.util.ArrayList;

public class idl_TemplateModuleRef extends TemplateDefinition {

    private String name;
    private String id;



    public idl_TemplateModuleRef(
        String name,        String id    ) {
        super(
        );
        this.name = name;
        this.id = id;
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


}