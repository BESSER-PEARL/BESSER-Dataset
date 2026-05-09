





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_NFP_DataTxRate extends NFP_Real {

    private String precision;
    private String unit;



    public MARTE_Library_BasicNFP_Types_NFP_DataTxRate(
        String precision,        String unit    ) {
        super(
        );
        this.precision = precision;
        this.unit = unit;
    }


    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}