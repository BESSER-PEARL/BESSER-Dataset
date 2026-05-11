





import java.util.List;
import java.util.ArrayList;

public class transport_LoadUnloadEdgeLabel extends MigrationEdgeLabel, DynamicLabel {

    private float activatedRate;



    public transport_LoadUnloadEdgeLabel(
        float activatedRate    ) {
        super(
        );
        this.activatedRate = activatedRate;
    }


    public float getActivatedrate() {
        return activatedRate;
    }

    public void setActivatedrate(float activatedRate) {
        this.activatedRate = activatedRate;
    }


}