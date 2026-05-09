





import java.util.List;
import java.util.ArrayList;

public class rapidml_RealizationContainer extends Extensible {

    private String effectiveRealization;
    private boolean withDefaultRealization;
    private String realizationName;



    public rapidml_RealizationContainer(
        String effectiveRealization,        boolean withDefaultRealization,        String realizationName    ) {
        super(
        );
        this.effectiveRealization = effectiveRealization;
        this.withDefaultRealization = withDefaultRealization;
        this.realizationName = realizationName;
    }


    public String getEffectiverealization() {
        return effectiveRealization;
    }

    public void setEffectiverealization(String effectiveRealization) {
        this.effectiveRealization = effectiveRealization;
    }
    public boolean getWithdefaultrealization() {
        return withDefaultRealization;
    }

    public void setWithdefaultrealization(boolean withDefaultRealization) {
        this.withDefaultRealization = withDefaultRealization;
    }
    public String getRealizationname() {
        return realizationName;
    }

    public void setRealizationname(String realizationName) {
        this.realizationName = realizationName;
    }


}