





import java.util.List;
import java.util.ArrayList;

public class EventAutomatonModel_FixParameter extends Parameter {

    private String value;





    private EventAutomatonModel_ConstantBinding eventautomatonmodel_constantbinding;


    public EventAutomatonModel_FixParameter(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public EventAutomatonModel_ConstantBinding getEventautomatonmodel_constantbinding() {
        return eventautomatonmodel_constantbinding;
    }

    public void setEventautomatonmodel_constantbinding(EventAutomatonModel_ConstantBinding eventautomatonmodel_constantbinding) {
        this.eventautomatonmodel_constantbinding = eventautomatonmodel_constantbinding;
    }

}