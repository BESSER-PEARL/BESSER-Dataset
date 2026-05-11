





import java.util.List;
import java.util.ArrayList;

public class smm_RescaledMeasure extends DimensionalMeasure {

    private String formula;



    public smm_RescaledMeasure(
        String formula    ) {
        super(
        );
        this.formula = formula;
    }


    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }


}