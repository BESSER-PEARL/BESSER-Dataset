





import java.util.List;
import java.util.ArrayList;

public class limp_Expr  {






    private limp_Postcondition limp_postcondition;




    private limp_ConstantDeclaration limp_constantdeclaration;




    private limp_Precondition limp_precondition;


    public limp_Expr(
    ) {
    }



    public limp_Postcondition getLimp_postcondition() {
        return limp_postcondition;
    }

    public void setLimp_postcondition(limp_Postcondition limp_postcondition) {
        this.limp_postcondition = limp_postcondition;
    }
    public limp_ConstantDeclaration getLimp_constantdeclaration() {
        return limp_constantdeclaration;
    }

    public void setLimp_constantdeclaration(limp_ConstantDeclaration limp_constantdeclaration) {
        this.limp_constantdeclaration = limp_constantdeclaration;
    }
    public limp_Precondition getLimp_precondition() {
        return limp_precondition;
    }

    public void setLimp_precondition(limp_Precondition limp_precondition) {
        this.limp_precondition = limp_precondition;
    }

}