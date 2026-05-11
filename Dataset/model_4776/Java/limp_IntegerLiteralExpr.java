





import java.util.List;
import java.util.ArrayList;

public class limp_IntegerLiteralExpr extends Expr {

    private String intVal;



    public limp_IntegerLiteralExpr(
        String intVal    ) {
        super(
        );
        this.intVal = intVal;
    }


    public String getIntval() {
        return intVal;
    }

    public void setIntval(String intVal) {
        this.intVal = intVal;
    }


}