





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Rate extends XSDDecimal {

    private String baseUnitCode;
    private String baseValue;



    public ISO20022_Rate(
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