





import java.util.List;
import java.util.ArrayList;

public class urml_Port  {

    private boolean conjugated;
    private String name;





    private urml_Capsule urml_capsule;




    private urml_Protocol urml_protocol;




    private urml_Capsule urml_capsule;


    public urml_Port(
        boolean conjugated,        String name    ) {
        this.conjugated = conjugated;
        this.name = name;
    }


    public boolean getConjugated() {
        return conjugated;
    }

    public void setConjugated(boolean conjugated) {
        this.conjugated = conjugated;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public urml_Capsule getUrml_capsule() {
        return urml_capsule;
    }

    public void setUrml_capsule(urml_Capsule urml_capsule) {
        this.urml_capsule = urml_capsule;
    }
    public urml_Protocol getUrml_protocol() {
        return urml_protocol;
    }

    public void setUrml_protocol(urml_Protocol urml_protocol) {
        this.urml_protocol = urml_protocol;
    }
    public urml_Capsule getUrml_capsule() {
        return urml_capsule;
    }

    public void setUrml_capsule(urml_Capsule urml_capsule) {
        this.urml_capsule = urml_capsule;
    }

}