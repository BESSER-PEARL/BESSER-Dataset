





import java.util.List;
import java.util.ArrayList;

public class pivot_VariableExp extends OCLExpression, ReferringElement {

    private String isImplicit;



    public pivot_VariableExp(
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


}