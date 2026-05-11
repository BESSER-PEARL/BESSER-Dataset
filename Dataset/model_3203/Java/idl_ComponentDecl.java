





import java.util.List;
import java.util.ArrayList;

public class idl_ComponentDecl extends TemplateDefinition, Definition, FixedDefinition {

    private String name;



    public idl_ComponentDecl(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}