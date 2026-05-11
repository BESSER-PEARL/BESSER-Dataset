





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeatureGroup extends CallContext, Context, DirectedFeature, FeatureGroupConnectionEnd {

    private String inverse;



    public aadl2_FeatureGroup(
        String inverse    ) {
        super(
        );
        this.inverse = inverse;
    }


    public String getInverse() {
        return inverse;
    }

    public void setInverse(String inverse) {
        this.inverse = inverse;
    }


}