





import java.util.List;
import java.util.ArrayList;

public class smm_GradeInterval extends Interval {

    private String symbol;





    private smm_GradeMeasure smm_grademeasure;


    public smm_GradeInterval(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public smm_GradeMeasure getSmm_grademeasure() {
        return smm_grademeasure;
    }

    public void setSmm_grademeasure(smm_GradeMeasure smm_grademeasure) {
        this.smm_grademeasure = smm_grademeasure;
    }

}