





import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeSwitchStmt  {

    private String switch;





    private myDsl_SwitchStmt mydsl_switchstmt;




    private myDsl_SimpleStmt mydsl_simplestmt;


    public myDsl_TypeSwitchStmt(
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
    public myDsl_SimpleStmt getMydsl_simplestmt() {
        return mydsl_simplestmt;
    }

    public void setMydsl_simplestmt(myDsl_SimpleStmt mydsl_simplestmt) {
        this.mydsl_simplestmt = mydsl_simplestmt;
    }

}