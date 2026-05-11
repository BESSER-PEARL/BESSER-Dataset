





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Type extends ModelElement {

    private String name;





    private applauseDsl_TypeDescription applausedsl_typedescription;


    public applauseDsl_Type(
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

    public applauseDsl_TypeDescription getApplausedsl_typedescription() {
        return applausedsl_typedescription;
    }

    public void setApplausedsl_typedescription(applauseDsl_TypeDescription applausedsl_typedescription) {
        this.applausedsl_typedescription = applausedsl_typedescription;
    }

}