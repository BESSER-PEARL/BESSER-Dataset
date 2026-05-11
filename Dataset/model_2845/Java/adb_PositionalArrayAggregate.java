





import java.util.List;
import java.util.ArrayList;

public class adb_PositionalArrayAggregate extends ArrayAggregate {

    private boolean othersBox;





    private List<adb_Expression> adb_expressions;




    private adb_Expression adb_expression;


    public adb_PositionalArrayAggregate(
        boolean othersBox    ) {
        super(
        );
        this.othersBox = othersBox;
        this.adb_expressions = new ArrayList<>();
    }

    public adb_PositionalArrayAggregate(
        boolean othersBox        ArrayList<adb_Expression> adb_expressions    ) {
        this.othersBox = othersBox;
        this.adb_expressions = adb_expressions;
    }

    public boolean getOthersbox() {
        return othersBox;
    }

    public void setOthersbox(boolean othersBox) {
        this.othersBox = othersBox;
    }

    public List<adb_Expression> getAdb_expressions() {
        return adb_expressions;
    }

    public void addAdb_expression(Adb_expression adb_expression) {
        this.adb_expressions.add(adb_expression);
    }
    public adb_Expression getAdb_expression() {
        return adb_expression;
    }

    public void setAdb_expression(adb_Expression adb_expression) {
        this.adb_expression = adb_expression;
    }

}