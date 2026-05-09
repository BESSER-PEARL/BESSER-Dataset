





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_NFP_Price extends NFP_Real {

    private String unit;



    public MARTE_Library_BasicNFP_Types_NFP_Price(
        String unit    ) {
        super(
        );
        this.unit = unit;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}