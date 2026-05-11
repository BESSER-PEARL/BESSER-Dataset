





import java.util.List;
import java.util.ArrayList;

public class base_AnnotationAttribute  {

    private boolean optional;
    private String name;



    public base_AnnotationAttribute(
        boolean optional,        String name    ) {
        this.optional = optional;
        this.name = name;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}