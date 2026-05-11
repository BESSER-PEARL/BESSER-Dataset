





import java.util.List;
import java.util.ArrayList;

public class KM3_Reference extends StructuralFeature {

    private boolean isContainer;





    private KM3_Reference km3_reference;


    public KM3_Reference(
        boolean isContainer    ) {
        super(
        );
        this.isContainer = isContainer;
    }


    public boolean getIscontainer() {
        return isContainer;
    }

    public void setIscontainer(boolean isContainer) {
        this.isContainer = isContainer;
    }

    public KM3_Reference getKm3_reference() {
        return km3_reference;
    }

    public void setKm3_reference(KM3_Reference km3_reference) {
        this.km3_reference = km3_reference;
    }

}