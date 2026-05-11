





import java.util.List;
import java.util.ArrayList;

public class idl_Event extends TemplateDefinition, Definition, FixedDefinition {

    private boolean isAbstract;
    private String name;



    public idl_Event(
        boolean isAbstract,        String name    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.name = name;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}