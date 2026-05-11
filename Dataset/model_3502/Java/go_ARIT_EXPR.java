





import java.util.List;
import java.util.ArrayList;

public class go_ARIT_EXPR  {

    private String num;
    private String num1;
    private String num2;
    private String atr;
    private String op;





    private go_VarCall go_varcall;




    private go_VarCall go_varcall;




    private go_VarCall go_varcall;




    private go_PostStmt go_poststmt;


    public go_ARIT_EXPR(
        String num,        String num1,        String num2,        String atr,        String op    ) {
        this.num = num;
        this.num1 = num1;
        this.num2 = num2;
        this.atr = atr;
        this.op = op;
    }


    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }
    public String getNum1() {
        return num1;
    }

    public void setNum1(String num1) {
        this.num1 = num1;
    }
    public String getNum2() {
        return num2;
    }

    public void setNum2(String num2) {
        this.num2 = num2;
    }
    public String getAtr() {
        return atr;
    }

    public void setAtr(String atr) {
        this.atr = atr;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public go_VarCall getGo_varcall() {
        return go_varcall;
    }

    public void setGo_varcall(go_VarCall go_varcall) {
        this.go_varcall = go_varcall;
    }
    public go_VarCall getGo_varcall() {
        return go_varcall;
    }

    public void setGo_varcall(go_VarCall go_varcall) {
        this.go_varcall = go_varcall;
    }
    public go_VarCall getGo_varcall() {
        return go_varcall;
    }

    public void setGo_varcall(go_VarCall go_varcall) {
        this.go_varcall = go_varcall;
    }
    public go_PostStmt getGo_poststmt() {
        return go_poststmt;
    }

    public void setGo_poststmt(go_PostStmt go_poststmt) {
        this.go_poststmt = go_poststmt;
    }

}