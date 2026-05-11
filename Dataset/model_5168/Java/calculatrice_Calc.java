





import java.util.List;
import java.util.ArrayList;

public class calculatrice_Calc  {

    private boolean decl;
    private String varName;
    private String boolName;





    private calculatrice_BoolExpr calculatrice_boolexpr;




    private calculatrice_Calculatrice calculatrice_calculatrice;




    private calculatrice_BoolExpr calculatrice_boolexpr;




    private calculatrice_BoolExpr calculatrice_boolexpr;


    public calculatrice_Calc(
        boolean decl,        String varName,        String boolName    ) {
        this.decl = decl;
        this.varName = varName;
        this.boolName = boolName;
    }


    public boolean getDecl() {
        return decl;
    }

    public void setDecl(boolean decl) {
        this.decl = decl;
    }
    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }
    public String getBoolname() {
        return boolName;
    }

    public void setBoolname(String boolName) {
        this.boolName = boolName;
    }

    public calculatrice_BoolExpr getCalculatrice_boolexpr() {
        return calculatrice_boolexpr;
    }

    public void setCalculatrice_boolexpr(calculatrice_BoolExpr calculatrice_boolexpr) {
        this.calculatrice_boolexpr = calculatrice_boolexpr;
    }
    public calculatrice_Calculatrice getCalculatrice_calculatrice() {
        return calculatrice_calculatrice;
    }

    public void setCalculatrice_calculatrice(calculatrice_Calculatrice calculatrice_calculatrice) {
        this.calculatrice_calculatrice = calculatrice_calculatrice;
    }
    public calculatrice_BoolExpr getCalculatrice_boolexpr() {
        return calculatrice_boolexpr;
    }

    public void setCalculatrice_boolexpr(calculatrice_BoolExpr calculatrice_boolexpr) {
        this.calculatrice_boolexpr = calculatrice_boolexpr;
    }
    public calculatrice_BoolExpr getCalculatrice_boolexpr() {
        return calculatrice_boolexpr;
    }

    public void setCalculatrice_boolexpr(calculatrice_BoolExpr calculatrice_boolexpr) {
        this.calculatrice_boolexpr = calculatrice_boolexpr;
    }

}