





import java.util.List;
import java.util.ArrayList;

public class standard_SeasonalPopulationModel extends StandardPopulationModel {

    private float modulationAmplitude;
    private float phase;
    private boolean useLatitude;
    private float period;



    public standard_SeasonalPopulationModel(
        float modulationAmplitude,        float phase,        boolean useLatitude,        float period    ) {
        super(
        );
        this.modulationAmplitude = modulationAmplitude;
        this.phase = phase;
        this.useLatitude = useLatitude;
        this.period = period;
    }


    public float getModulationamplitude() {
        return modulationAmplitude;
    }

    public void setModulationamplitude(float modulationAmplitude) {
        this.modulationAmplitude = modulationAmplitude;
    }
    public float getPhase() {
        return phase;
    }

    public void setPhase(float phase) {
        this.phase = phase;
    }
    public boolean getUselatitude() {
        return useLatitude;
    }

    public void setUselatitude(boolean useLatitude) {
        this.useLatitude = useLatitude;
    }
    public float getPeriod() {
        return period;
    }

    public void setPeriod(float period) {
        this.period = period;
    }


}