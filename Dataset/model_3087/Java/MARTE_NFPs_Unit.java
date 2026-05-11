





import java.util.List;
import java.util.ArrayList;

public class MARTE_NFPs_Unit  {

    private String offsetFactor;
    private String convFactor;



    public MARTE_NFPs_Unit(
        String offsetFactor,        String convFactor    ) {
        this.offsetFactor = offsetFactor;
        this.convFactor = convFactor;
    }


    public String getOffsetfactor() {
        return offsetFactor;
    }

    public void setOffsetfactor(String offsetFactor) {
        this.offsetFactor = offsetFactor;
    }
    public String getConvfactor() {
        return convFactor;
    }

    public void setConvfactor(String convFactor) {
        this.convFactor = convFactor;
    }


}