





import java.util.List;
import java.util.ArrayList;

public class avm_eda_CircuitLayout extends DomainModel_ {

    private String BoundingBoxes;



    public avm_eda_CircuitLayout(
        String BoundingBoxes    ) {
        super(
        );
        this.BoundingBoxes = BoundingBoxes;
    }


    public String getBoundingboxes() {
        return BoundingBoxes;
    }

    public void setBoundingboxes(String BoundingBoxes) {
        this.BoundingBoxes = BoundingBoxes;
    }


}