





import java.util.List;
import java.util.ArrayList;

public class Flightlist  {

    private String id;
    private String name;





    private System system;


    public Flightlist(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}