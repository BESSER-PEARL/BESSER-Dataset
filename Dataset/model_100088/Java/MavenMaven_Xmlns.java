





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Xmlns  {

    private String value;
    private String name;





    private MavenMaven_Project mavenmaven_project;


    public MavenMaven_Xmlns(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MavenMaven_Project getMavenmaven_project() {
        return mavenmaven_project;
    }

    public void setMavenmaven_project(MavenMaven_Project mavenmaven_project) {
        this.mavenmaven_project = mavenmaven_project;
    }

}