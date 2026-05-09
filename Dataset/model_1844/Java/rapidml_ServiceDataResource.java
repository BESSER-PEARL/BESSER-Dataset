





import java.util.List;
import java.util.ArrayList;

public class rapidml_ServiceDataResource extends ResourceDefinition, RealizationContainer {

    private boolean default;



    public rapidml_ServiceDataResource(
        boolean default    ) {
        super(
        );
        this.default = default;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }


}