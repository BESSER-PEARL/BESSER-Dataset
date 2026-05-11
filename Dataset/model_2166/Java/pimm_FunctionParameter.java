





import java.util.List;
import java.util.ArrayList;

public class pimm_FunctionParameter extends PiMMVisitable {

    private String type;
    private String direction;
    private boolean isConfigurationParameter;
    private String name;



    public pimm_FunctionParameter(
        String type,        String direction,        boolean isConfigurationParameter,        String name    ) {
        super(
        );
        this.type = type;
        this.direction = direction;
        this.isConfigurationParameter = isConfigurationParameter;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public boolean getIsconfigurationparameter() {
        return isConfigurationParameter;
    }

    public void setIsconfigurationparameter(boolean isConfigurationParameter) {
        this.isConfigurationParameter = isConfigurationParameter;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}