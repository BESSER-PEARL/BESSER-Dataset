





import java.util.List;
import java.util.ArrayList;

public class idl_Event extends TemplateDefinition, Definition, FixedDefinition {

    private String name;
    private boolean isAbstract;



    public idl_Event(
        String name,        boolean isAbstract    ) {
        super(
        );
        this.name = name;
        this.isAbstract = isAbstract;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }


}