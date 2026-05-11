





import java.util.List;
import java.util.ArrayList;

public class urml_Signal  {

    private String name;





    private urml_Protocol urml_protocol;




    private urml_Protocol urml_protocol;




    private List<urml_LocalVar> urml_localvars;


    public urml_Signal(
        String name    ) {
        this.name = name;
        this.urml_localvars = new ArrayList<>();
    }

    public urml_Signal(
        String name        ArrayList<urml_LocalVar> urml_localvars    ) {
        this.name = name;
        this.urml_localvars = urml_localvars;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public urml_Protocol getUrml_protocol() {
        return urml_protocol;
    }

    public void setUrml_protocol(urml_Protocol urml_protocol) {
        this.urml_protocol = urml_protocol;
    }
    public urml_Protocol getUrml_protocol() {
        return urml_protocol;
    }

    public void setUrml_protocol(urml_Protocol urml_protocol) {
        this.urml_protocol = urml_protocol;
    }
    public List<urml_LocalVar> getUrml_localvars() {
        return urml_localvars;
    }

    public void addUrml_localvar(Urml_localvar urml_localvar) {
        this.urml_localvars.add(urml_localvar);
    }

}