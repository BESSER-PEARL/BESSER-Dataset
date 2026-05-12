





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_System  {

    private String system;
    private String name;





    private reqLanguage_StateEvent reqlanguage_stateevent;


    public reqLanguage_System(
        String system,        String name    ) {
        this.system = system;
        this.name = name;
    }


    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public reqLanguage_StateEvent getReqlanguage_stateevent() {
        return reqlanguage_stateevent;
    }

    public void setReqlanguage_stateevent(reqLanguage_StateEvent reqlanguage_stateevent) {
        this.reqlanguage_stateevent = reqlanguage_stateevent;
    }

}