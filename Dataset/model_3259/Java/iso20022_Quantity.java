





import java.util.List;
import java.util.ArrayList;

public class iso20022_Quantity extends Decimal {

    private String unitCode;



    public iso20022_Quantity(
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