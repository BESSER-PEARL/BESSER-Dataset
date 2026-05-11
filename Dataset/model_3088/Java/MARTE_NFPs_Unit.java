





import java.util.List;
import java.util.ArrayList;

public class MARTE_NFPs_Unit  {

    private String convFactor;
    private String convOffset;



    public MARTE_NFPs_Unit(
        String convFactor,        String convOffset    ) {
        this.convFactor = convFactor;
        this.convOffset = convOffset;
    }


    public String getConvfactor() {
        return convFactor;
    }

    public void setConvfactor(String convFactor) {
        this.convFactor = convFactor;
    }
    public String getConvoffset() {
        return convOffset;
    }

    public void setConvoffset(String convOffset) {
        this.convOffset = convOffset;
    }


}