





import java.util.List;
import java.util.ArrayList;

public class nuSMV_AssignBody  {

    private String array;
    private boolean semicolon;





    private nuSMV_SimpleExpression nusmv_simpleexpression;




    private nuSMV_AssignConstraintElement nusmv_assignconstraintelement;


    public nuSMV_AssignBody(
        String array,        boolean semicolon    ) {
        this.array = array;
        this.semicolon = semicolon;
    }


    public String getArray() {
        return array;
    }

    public void setArray(String array) {
        this.array = array;
    }
    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }

    public nuSMV_SimpleExpression getNusmv_simpleexpression() {
        return nusmv_simpleexpression;
    }

    public void setNusmv_simpleexpression(nuSMV_SimpleExpression nusmv_simpleexpression) {
        this.nusmv_simpleexpression = nusmv_simpleexpression;
    }
    public nuSMV_AssignConstraintElement getNusmv_assignconstraintelement() {
        return nusmv_assignconstraintelement;
    }

    public void setNusmv_assignconstraintelement(nuSMV_AssignConstraintElement nusmv_assignconstraintelement) {
        this.nusmv_assignconstraintelement = nusmv_assignconstraintelement;
    }

}