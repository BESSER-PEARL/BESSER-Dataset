





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExprSwitchStmt  {

    private String switch;





    private myDsl_SwitchStmt mydsl_switchstmt;




    private myDsl_Expression mydsl_expression;




    private myDsl_SimpleStmt mydsl_simplestmt;


    public myDsl_ExprSwitchStmt(
        String switch    ) {
        this.switch = switch;
    }


    public String getSwitch() {
        return switch;
    }

    public void setSwitch(String switch) {
        this.switch = switch;
    }

    public myDsl_SwitchStmt getMydsl_switchstmt() {
        return mydsl_switchstmt;
    }

    public void setMydsl_switchstmt(myDsl_SwitchStmt mydsl_switchstmt) {
        this.mydsl_switchstmt = mydsl_switchstmt;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_SimpleStmt getMydsl_simplestmt() {
        return mydsl_simplestmt;
    }

    public void setMydsl_simplestmt(myDsl_SimpleStmt mydsl_simplestmt) {
        this.mydsl_simplestmt = mydsl_simplestmt;
    }

}