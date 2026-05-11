





import java.util.List;
import java.util.ArrayList;

public class fragdial_Attributes  {

    private String signature;





    private fragdial_AbstractComponent fragdial_abstractcomponent;


    public fragdial_Attributes(
        String signature    ) {
        this.signature = signature;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public fragdial_AbstractComponent getFragdial_abstractcomponent() {
        return fragdial_abstractcomponent;
    }

    public void setFragdial_abstractcomponent(fragdial_AbstractComponent fragdial_abstractcomponent) {
        this.fragdial_abstractcomponent = fragdial_abstractcomponent;
    }

}