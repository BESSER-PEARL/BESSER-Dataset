





import java.util.List;
import java.util.ArrayList;

public class aadl2_PortSpecification extends FeaturePrototypeActual {

    private String direction;
    private String category;



    public aadl2_PortSpecification(
        String direction,        String category    ) {
        super(
        );
        this.direction = direction;
        this.category = category;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}