





import java.util.List;
import java.util.ArrayList;

public class pivot_VariableExp extends ReferringElement, OCLExpression {

    private String isImplicit;





    private pivot_VariableDeclaration pivot_variabledeclaration;


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

    public pivot_VariableDeclaration getPivot_variabledeclaration() {
        return pivot_variabledeclaration;
    }

    public void setPivot_variabledeclaration(pivot_VariableDeclaration pivot_variabledeclaration) {
        this.pivot_variabledeclaration = pivot_variabledeclaration;
    }

}