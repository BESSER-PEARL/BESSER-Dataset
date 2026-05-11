





import java.util.List;
import java.util.ArrayList;

public class krendering_KRoundedBendsPolyline extends KPolyline {

    private float bendRadius;



    public krendering_KRoundedBendsPolyline(
        float bendRadius    ) {
        super(
        );
        this.bendRadius = bendRadius;
    }


    public float getBendradius() {
        return bendRadius;
    }

    public void setBendradius(float bendRadius) {
        this.bendRadius = bendRadius;
    }


}