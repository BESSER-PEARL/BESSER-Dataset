





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Quantity extends XSDDecimal {

    private String unitCode;



    public ISO20022_Quantity(
        String unitCode    ) {
        super(
        );
        this.unitCode = unitCode;
    }


    public String getUnitcode() {
        return unitCode;
    }

    public void setUnitcode(String unitCode) {
        this.unitCode = unitCode;
    }


}