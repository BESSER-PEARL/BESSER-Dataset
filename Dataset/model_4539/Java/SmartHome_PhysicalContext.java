





import java.util.List;
import java.util.ArrayList;

public class SmartHome_PhysicalContext extends NamedElement {

    private float lightOut;
    private float lightIn;



    public SmartHome_PhysicalContext(
        float lightOut,        float lightIn    ) {
        super(
        );
        this.lightOut = lightOut;
        this.lightIn = lightIn;
    }


    public float getLightout() {
        return lightOut;
    }

    public void setLightout(float lightOut) {
        this.lightOut = lightOut;
    }
    public float getLightin() {
        return lightIn;
    }

    public void setLightin(float lightIn) {
        this.lightIn = lightIn;
    }


}