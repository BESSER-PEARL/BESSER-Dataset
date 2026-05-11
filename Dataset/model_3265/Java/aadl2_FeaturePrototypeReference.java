





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeaturePrototypeReference extends FeaturePrototypeActual {

    private String direction;





    private aadl2_FeaturePrototype aadl2_featureprototype;


    public aadl2_FeaturePrototypeReference(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public aadl2_FeaturePrototype getAadl2_featureprototype() {
        return aadl2_featureprototype;
    }

    public void setAadl2_featureprototype(aadl2_FeaturePrototype aadl2_featureprototype) {
        this.aadl2_featureprototype = aadl2_featureprototype;
    }

}