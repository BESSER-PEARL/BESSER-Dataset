





import java.util.List;
import java.util.ArrayList;

public class adb_PragmaArgumentAssociation  {

    private String name;





    private adb_Pragma adb_pragma;




    private adb_Expression adb_expression;


    public adb_PragmaArgumentAssociation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adb_Pragma getAdb_pragma() {
        return adb_pragma;
    }

    public void setAdb_pragma(adb_Pragma adb_pragma) {
        this.adb_pragma = adb_pragma;
    }
    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }

}