





import java.util.List;
import java.util.ArrayList;

public class statemachine_NamedElement  {

    private String name;
    private String displayname;



    public statemachine_NamedElement(
        String name,        String displayname    ) {
        this.name = name;
        this.displayname = displayname;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDisplayname() {
        return displayname;
    }

    public void setDisplayname(String displayname) {
        this.displayname = displayname;
    }


}