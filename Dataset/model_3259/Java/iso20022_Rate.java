





import java.util.List;
import java.util.ArrayList;

public class iso20022_Rate extends Decimal {

    private String baseValue;
    private String baseUnitCode;



    public iso20022_Rate(
        String baseValue,        String baseUnitCode    ) {
        super(
        );
        this.baseValue = baseValue;
        this.baseUnitCode = baseUnitCode;
    }


    public String getBasevalue() {
        return baseValue;
    }

    public void setBasevalue(String baseValue) {
        this.baseValue = baseValue;
    }
    public String getBaseunitcode() {
        return baseUnitCode;
    }

    public void setBaseunitcode(String baseUnitCode) {
        this.baseUnitCode = baseUnitCode;
    }


}