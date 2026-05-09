





import java.util.List;
import java.util.ArrayList;

public class ccsl_method_Method extends method_SimpleMethod, namedElements_NamedElement {

    private String abstract;
    private String inheritance;
    private String static;
    private String final;



    public ccsl_method_Method(
        String abstract,        String inheritance,        String static,        String final    ) {
        super(
        );
        this.abstract = abstract;
        this.inheritance = inheritance;
        this.static = static;
        this.final = final;
    }


    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }


}