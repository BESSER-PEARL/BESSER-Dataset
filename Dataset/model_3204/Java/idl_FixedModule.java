





import java.util.List;
import java.util.ArrayList;

public class idl_FixedModule extends TemplateDefinition, FixedDefinition {

    private String name;



    public idl_FixedModule(
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