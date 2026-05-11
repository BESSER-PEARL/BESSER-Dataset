





import java.util.List;
import java.util.ArrayList;

public class adb_RaiseStatement extends SimpleStatement {






    private adb_Name adb_name;




    private adb_Expression adb_expression;


    public adb_RaiseStatement(
    ) {
        super(
        );
    }



    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }
    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }

}