





import java.util.List;
import java.util.ArrayList;

public class ConfParam extends AssessmentElement {

    private String param_type;
    private String value;





    private Configuration configuration;


    public ConfParam(
        String param_type,        String value    ) {
        super(
            String,            name,            String,            description        );
        this.param_type = param_type;
        this.value = value;
    }


    public String getParam_type() {
        return param_type;
    }

    public void setParam_type(String param_type) {
        this.param_type = param_type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Configuration getConfiguration() {
        return configuration;
    }

    public void setConfiguration(Configuration configuration) {
        this.configuration = configuration;
    }

}