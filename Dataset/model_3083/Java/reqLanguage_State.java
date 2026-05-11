





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_State  {

    private String name;
    private String state;





    private reqLanguage_StateEvent reqlanguage_stateevent;


    public reqLanguage_State(
        String name,        String state    ) {
        this.name = name;
        this.state = state;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public reqLanguage_StateEvent getReqlanguage_stateevent() {
        return reqlanguage_stateevent;
    }

    public void setReqlanguage_stateevent(reqLanguage_StateEvent reqlanguage_stateevent) {
        this.reqlanguage_stateevent = reqlanguage_stateevent;
    }

}