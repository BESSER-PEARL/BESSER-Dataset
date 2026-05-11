





import java.util.List;
import java.util.ArrayList;

public class adb_ArrayComponentAssociation  {

    private boolean box;





    private adb_Expression adb_expression;




    private adb_NamedArrayAggregate adb_namedarrayaggregate;


    public adb_ArrayComponentAssociation(
        boolean box    ) {
        this.box = box;
    }


    public boolean getBox() {
        return box;
    }

    public void setBox(boolean box) {
        this.box = box;
    }

    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }
    public adb_NamedArrayAggregate getAdb_namedarrayaggregate() {
        return adb_namedarrayaggregate;
    }

    public void setAdb_namedarrayaggregate(adb_NamedArrayAggregate adb_namedarrayaggregate) {
        this.adb_namedarrayaggregate = adb_namedarrayaggregate;
    }

}