





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_ContentProvider extends ModelElement {

    private boolean many;





    private applauseDsl_ScalarExpression applausedsl_scalarexpression;




    private applauseDsl_ScalarExpression applausedsl_scalarexpression;




    private applauseDsl_Type applausedsl_type;




    private applauseDsl_Parameter applausedsl_parameter;


    public applauseDsl_ContentProvider(
        boolean many    ) {
        super(
        );
        this.many = many;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public applauseDsl_ScalarExpression getApplausedsl_scalarexpression() {
        return applausedsl_scalarexpression;
    }

    public void setApplausedsl_scalarexpression(applauseDsl_ScalarExpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpression = applausedsl_scalarexpression;
    }
    public applauseDsl_ScalarExpression getApplausedsl_scalarexpression() {
        return applausedsl_scalarexpression;
    }

    public void setApplausedsl_scalarexpression(applauseDsl_ScalarExpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpression = applausedsl_scalarexpression;
    }
    public applauseDsl_Type getApplausedsl_type() {
        return applausedsl_type;
    }

    public void setApplausedsl_type(applauseDsl_Type applausedsl_type) {
        this.applausedsl_type = applausedsl_type;
    }
    public applauseDsl_Parameter getApplausedsl_parameter() {
        return applausedsl_parameter;
    }

    public void setApplausedsl_parameter(applauseDsl_Parameter applausedsl_parameter) {
        this.applausedsl_parameter = applausedsl_parameter;
    }

}