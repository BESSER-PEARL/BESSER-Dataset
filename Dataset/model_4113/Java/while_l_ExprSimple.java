





import java.util.List;
import java.util.ArrayList;

public class while_l_ExprSimple  {

    private String varSimple;
    private String str;
    private String sym;
    private String nameFunction;





    private while_l_ExprEq while_l_expreq;




    private while_l_ExprEq while_l_expreq;




    private while_l_Input while_l_input;


    public while_l_ExprSimple(
        String varSimple,        String str,        String sym,        String nameFunction    ) {
        this.varSimple = varSimple;
        this.str = str;
        this.sym = sym;
        this.nameFunction = nameFunction;
    }


    public String getVarsimple() {
        return varSimple;
    }

    public void setVarsimple(String varSimple) {
        this.varSimple = varSimple;
    }
    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }
    public String getSym() {
        return sym;
    }

    public void setSym(String sym) {
        this.sym = sym;
    }
    public String getNamefunction() {
        return nameFunction;
    }

    public void setNamefunction(String nameFunction) {
        this.nameFunction = nameFunction;
    }

    public while_l_ExprEq getWhile_l_expreq() {
        return while_l_expreq;
    }

    public void setWhile_l_expreq(while_l_ExprEq while_l_expreq) {
        this.while_l_expreq = while_l_expreq;
    }
    public while_l_ExprEq getWhile_l_expreq() {
        return while_l_expreq;
    }

    public void setWhile_l_expreq(while_l_ExprEq while_l_expreq) {
        this.while_l_expreq = while_l_expreq;
    }
    public while_l_Input getWhile_l_input() {
        return while_l_input;
    }

    public void setWhile_l_input(while_l_Input while_l_input) {
        this.while_l_input = while_l_input;
    }

}