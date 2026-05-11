





import java.util.List;
import java.util.ArrayList;

public class component_CorbaConfigurationSet extends ConfigurationSet {

    private String sDOConfigurationSet;



    public component_CorbaConfigurationSet(
        String sDOConfigurationSet    ) {
        super(
        );
        this.sDOConfigurationSet = sDOConfigurationSet;
    }


    public String getSdoconfigurationset() {
        return sDOConfigurationSet;
    }

    public void setSdoconfigurationset(String sDOConfigurationSet) {
        this.sDOConfigurationSet = sDOConfigurationSet;
    }


}