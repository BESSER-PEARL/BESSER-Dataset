





import java.util.List;
import java.util.ArrayList;

public class db_config_Prompt extends ServerResource {

    private String extension;
    private boolean system;



    public db_config_Prompt(
        String extension,        boolean system    ) {
        super(
        );
        this.extension = extension;
        this.system = system;
    }


    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public boolean getSystem() {
        return system;
    }

    public void setSystem(boolean system) {
        this.system = system;
    }


}