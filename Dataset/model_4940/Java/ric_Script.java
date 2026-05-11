





import java.util.List;
import java.util.ArrayList;

public class ric_Script  {

    private String implementation;
    private String type;
    private String name;





    private ric_Event ric_event;


    public ric_Script(
        String implementation,        String type,        String name    ) {
        this.implementation = implementation;
        this.type = type;
        this.name = name;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ric_Event getRic_event() {
        return ric_event;
    }

    public void setRic_event(ric_Event ric_event) {
        this.ric_event = ric_event;
    }

}