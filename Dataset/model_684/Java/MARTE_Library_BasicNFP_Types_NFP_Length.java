





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_NFP_Length extends NFP_Real {

    private String unit;
    private String precision;



    public MARTE_Library_BasicNFP_Types_NFP_Length(
        String unit,        String precision    ) {
        super(
        );
        this.unit = unit;
        this.precision = precision;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }


}