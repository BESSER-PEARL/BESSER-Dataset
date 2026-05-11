





import java.util.List;
import java.util.ArrayList;

public class cal_RegExpUnary extends RegExp {

    private String unaryOperator;





    private cal_RegExp cal_regexp;


    public cal_RegExpUnary(
        String unaryOperator    ) {
        super(
        );
        this.unaryOperator = unaryOperator;
    }


    public String getUnaryoperator() {
        return unaryOperator;
    }

    public void setUnaryoperator(String unaryOperator) {
        this.unaryOperator = unaryOperator;
    }

    public cal_RegExp getCal_regexp() {
        return cal_regexp;
    }

    public void setCal_regexp(cal_RegExp cal_regexp) {
        this.cal_regexp = cal_regexp;
    }

}