





import java.util.List;
import java.util.ArrayList;

public class idl_NativeType extends FixedDefinition, Definition, TemplateDefinition {

    private String name;



    public idl_NativeType(
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