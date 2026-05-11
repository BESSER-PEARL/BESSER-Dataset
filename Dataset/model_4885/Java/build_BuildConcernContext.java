





import java.util.List;
import java.util.ArrayList;

public class build_BuildConcernContext extends BConcernContext, IProvidedCapabilityContainer {

    private String defaultPropertiesRemovals;



    public build_BuildConcernContext(
        String defaultPropertiesRemovals    ) {
        super(
        );
        this.defaultPropertiesRemovals = defaultPropertiesRemovals;
    }


    public String getDefaultpropertiesremovals() {
        return defaultPropertiesRemovals;
    }

    public void setDefaultpropertiesremovals(String defaultPropertiesRemovals) {
        this.defaultPropertiesRemovals = defaultPropertiesRemovals;
    }


}