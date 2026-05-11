





import java.util.List;
import java.util.ArrayList;

public class adb_DelayStatement extends SimpleStatement, TriggeringStatement {

    private String until;





    private adb_Expression adb_expression;


    public adb_DelayStatement(
        String until    ) {
        super(
        );
        this.until = until;
    }


    public String getUntil() {
        return until;
    }

    public void setUntil(String until) {
        this.until = until;
    }

    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }

}