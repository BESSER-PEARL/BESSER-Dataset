





import java.util.List;
import java.util.ArrayList;

public class website_ViewAssociation extends ViewFeature, NamedDisplayElement, Association {

    private String cardinality;



    public website_ViewAssociation(
        String cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }


}