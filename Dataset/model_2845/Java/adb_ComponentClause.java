





import java.util.List;
import java.util.ArrayList;

public class adb_ComponentClause  {

    private String localName;





    private adb_AspectClause adb_aspectclause;




    private adb_SimpleExpression adb_simpleexpression;




    private adb_SimpleExpression adb_simpleexpression;


    public adb_ComponentClause(
        String localName    ) {
        this.localName = localName;
    }


    public String getLocalname() {
        return localName;
    }

    public void setLocalname(String localName) {
        this.localName = localName;
    }

    public adb_AspectClause getAdb_aspectclause() {
        return adb_aspectclause;
    }

    public void setAdb_aspectclause(adb_AspectClause adb_aspectclause) {
        this.adb_aspectclause = adb_aspectclause;
    }
    public adb_SimpleExpression getAdb_simpleexpression() {
        return adb_simpleexpression;
    }

    public void setAdb_simpleexpression(adb_SimpleExpression adb_simpleexpression) {
        this.adb_simpleexpression = adb_simpleexpression;
    }
    public adb_SimpleExpression getAdb_simpleexpression() {
        return adb_simpleexpression;
    }

    public void setAdb_simpleexpression(adb_SimpleExpression adb_simpleexpression) {
        this.adb_simpleexpression = adb_simpleexpression;
    }

}