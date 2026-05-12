





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_CellType  {

    private String formula;
    private String unit;
    private String err;
    private String value;



    public DatadiagramMLBasicDef_CellType(
        String formula,        String unit,        String err,        String value    ) {
        this.formula = formula;
        this.unit = unit;
        this.err = err;
        this.value = value;
    }


    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getErr() {
        return err;
    }

    public void setErr(String err) {
        this.err = err;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}