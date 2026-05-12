





import java.util.List;
import java.util.ArrayList;

public class db_config_Prompt extends ServerResource {

    private boolean system;
    private String extension;



    public db_config_Prompt(
        boolean system,        String extension    ) {
        super(
        );
        this.system = system;
        this.extension = extension;
    }


    public boolean getSystem() {
        return system;
    }

    public void setSystem(boolean system) {
        this.system = system;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }


}