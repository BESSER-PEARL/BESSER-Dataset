





import java.util.List;
import java.util.ArrayList;

public class KM3_Reference extends StructuralFeature {

    private String isContainer;





    private KM3_Reference km3_reference;


    public KM3_Reference(
        String isContainer    ) {
        super(
        );
        this.isContainer = isContainer;
    }


    public String getIscontainer() {
        return isContainer;
    }

    public void setIscontainer(String isContainer) {
        this.isContainer = isContainer;
    }

    public KM3_Reference getKm3_reference() {
        return km3_reference;
    }

    public void setKm3_reference(KM3_Reference km3_reference) {
        this.km3_reference = km3_reference;
    }

}