





import java.util.List;
import java.util.ArrayList;

public class db_config_SafletProject extends ServerResource {

    private boolean enabled;



    public db_config_SafletProject(
        boolean enabled    ) {
        super(
        );
        this.enabled = enabled;
    }


    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }


}