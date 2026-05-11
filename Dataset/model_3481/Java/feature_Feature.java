





import java.util.List;
import java.util.ArrayList;

public class feature_Feature extends Identifiable {

    private String name;
    private String configurationState;



    public feature_Feature(
        String name,        String configurationState    ) {
        super(
        );
        this.name = name;
        this.configurationState = configurationState;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConfigurationstate() {
        return configurationState;
    }

    public void setConfigurationstate(String configurationState) {
        this.configurationState = configurationState;
    }


}