





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_ContentProvider extends ModelElement {

    private boolean many;
    private boolean storing;





    private applauseDsl_Parameter applausedsl_parameter;




    private applauseDsl_Type applausedsl_type;


    public applauseDsl_ContentProvider(
        boolean many,        boolean storing    ) {
        super(
        );
        this.many = many;
        this.storing = storing;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public boolean getStoring() {
        return storing;
    }

    public void setStoring(boolean storing) {
        this.storing = storing;
    }

    public applauseDsl_Parameter getApplausedsl_parameter() {
        return applausedsl_parameter;
    }

    public void setApplausedsl_parameter(applauseDsl_Parameter applausedsl_parameter) {
        this.applausedsl_parameter = applausedsl_parameter;
    }
    public applauseDsl_Type getApplausedsl_type() {
        return applausedsl_type;
    }

    public void setApplausedsl_type(applauseDsl_Type applausedsl_type) {
        this.applausedsl_type = applausedsl_type;
    }

}