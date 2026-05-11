





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Limits  {

    private float lowerBound;
    private float upperBound;





    private domainmodel_Feature domainmodel_feature;


    public domainmodel_Limits(
        float lowerBound,        float upperBound    ) {
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public float getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(float lowerBound) {
        this.lowerBound = lowerBound;
    }
    public float getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(float upperBound) {
        this.upperBound = upperBound;
    }

    public domainmodel_Feature getDomainmodel_feature() {
        return domainmodel_feature;
    }

    public void setDomainmodel_feature(domainmodel_Feature domainmodel_feature) {
        this.domainmodel_feature = domainmodel_feature;
    }

}