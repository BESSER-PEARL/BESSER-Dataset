





import java.util.List;
import java.util.ArrayList;

public class urml_TimerPort  {

    private String name;





    private urml_Capsule urml_capsule;


    public urml_TimerPort(
        String name    ) {
        this.name = name;
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

}