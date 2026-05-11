





import java.util.List;
import java.util.ArrayList;

public class Activities_BasicActivities_Parameter  {

    private String effect;
    private boolean isException;
    private boolean isStream;





    private List<ParameterSet> parametersets;


    public Activities_BasicActivities_Parameter(
        String effect,        boolean isException,        boolean isStream    ) {
        this.effect = effect;
        this.isException = isException;
        this.isStream = isStream;
        this.parametersets = new ArrayList<>();
    }

    public Activities_BasicActivities_Parameter(
        String effect,        boolean isException,        boolean isStream        ArrayList<ParameterSet> parametersets    ) {
        this.effect = effect;
        this.isException = isException;
        this.isStream = isStream;
        this.parametersets = parametersets;
    }

    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public boolean getIsexception() {
        return isException;
    }

    public void setIsexception(boolean isException) {
        this.isException = isException;
    }
    public boolean getIsstream() {
        return isStream;
    }

    public void setIsstream(boolean isStream) {
        this.isStream = isStream;
    }

    public List<ParameterSet> getParametersets() {
        return parametersets;
    }

    public void addParameterset(Parameterset parameterset) {
        this.parametersets.add(parameterset);
    }

}