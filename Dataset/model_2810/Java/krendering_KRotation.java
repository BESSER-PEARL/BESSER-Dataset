





import java.util.List;
import java.util.ArrayList;

public class krendering_KRotation extends KStyle {

    private float rotation;





    private krendering_KPosition krendering_kposition;


    public krendering_KRotation(
        float rotation    ) {
        super(
        );
        this.rotation = rotation;
    }


    public float getRotation() {
        return rotation;
    }

    public void setRotation(float rotation) {
        this.rotation = rotation;
    }

    public krendering_KPosition getKrendering_kposition() {
        return krendering_kposition;
    }

    public void setKrendering_kposition(krendering_KPosition krendering_kposition) {
        this.krendering_kposition = krendering_kposition;
    }

}