





import java.util.List;
import java.util.ArrayList;

public class SmartHome_Light extends Activator {

    private boolean stateInit;
    private float intensity;



    public SmartHome_Light(
        boolean stateInit,        float intensity    ) {
        super(
        );
        this.stateInit = stateInit;
        this.intensity = intensity;
    }


    public boolean getStateinit() {
        return stateInit;
    }

    public void setStateinit(boolean stateInit) {
        this.stateInit = stateInit;
    }
    public float getIntensity() {
        return intensity;
    }

    public void setIntensity(float intensity) {
        this.intensity = intensity;
    }


}