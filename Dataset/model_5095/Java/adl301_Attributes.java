





import java.util.List;
import java.util.ArrayList;

public class adl301_Attributes  {

    private String signature;





    private adl301_AbstractComponent adl301_abstractcomponent;


    public adl301_Attributes(
        String signature    ) {
        this.signature = signature;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public adl301_AbstractComponent getAdl301_abstractcomponent() {
        return adl301_abstractcomponent;
    }

    public void setAdl301_abstractcomponent(adl301_AbstractComponent adl301_abstractcomponent) {
        this.adl301_abstractcomponent = adl301_abstractcomponent;
    }

}