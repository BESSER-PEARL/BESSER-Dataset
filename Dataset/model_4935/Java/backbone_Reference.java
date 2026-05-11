





import java.util.List;
import java.util.ArrayList;

public class backbone_Reference extends NamedElement {

    private String cardinality;



    public backbone_Reference(
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