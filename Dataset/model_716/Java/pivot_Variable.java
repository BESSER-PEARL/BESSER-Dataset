





import java.util.List;
import java.util.ArrayList;

public class pivot_Variable extends VariableDeclaration {

    private String isImplicit;





    private pivot_Parameter pivot_parameter;


    public pivot_Variable(
        String isImplicit    ) {
        super(
        );
        this.isImplicit = isImplicit;
    }


    public String getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(String isImplicit) {
        this.isImplicit = isImplicit;
    }

    public pivot_Parameter getPivot_parameter() {
        return pivot_parameter;
    }

    public void setPivot_parameter(pivot_Parameter pivot_parameter) {
        this.pivot_parameter = pivot_parameter;
    }

}