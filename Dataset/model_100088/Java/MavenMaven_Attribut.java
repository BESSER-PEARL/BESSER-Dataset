





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Attribut  {

    private String name;
    private String value;





    private MavenMaven_NewTask mavenmaven_newtask;


    public MavenMaven_Attribut(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public MavenMaven_NewTask getMavenmaven_newtask() {
        return mavenmaven_newtask;
    }

    public void setMavenmaven_newtask(MavenMaven_NewTask mavenmaven_newtask) {
        this.mavenmaven_newtask = mavenmaven_newtask;
    }

}