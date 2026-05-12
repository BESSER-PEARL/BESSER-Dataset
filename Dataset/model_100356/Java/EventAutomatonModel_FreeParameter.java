





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_FreeParameter extends Parameter {

    private String excludedValues;



    public EventAutomatonModel_FreeParameter(
        String excludedValues    ) {
        super(
        );
        this.excludedValues = excludedValues;
    }


    public String getExcludedvalues() {
        return excludedValues;
    }

    public void setExcludedvalues(String excludedValues) {
        this.excludedValues = excludedValues;
    }


}