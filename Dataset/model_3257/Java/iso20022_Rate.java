





import java.util.List;
import java.util.ArrayList;

public class iso20022_Rate extends Decimal {

    private String baseUnitCode;
    private String baseValue;



    public iso20022_Rate(
        String baseUnitCode,        String baseValue    ) {
        super(
        );
        this.baseUnitCode = baseUnitCode;
        this.baseValue = baseValue;
    }


    public String getBaseunitcode() {
        return baseUnitCode;
    }

    public void setBaseunitcode(String baseUnitCode) {
        this.baseUnitCode = baseUnitCode;
    }
    public String getBasevalue() {
        return baseValue;
    }

    public void setBasevalue(String baseValue) {
        this.baseValue = baseValue;
    }


}