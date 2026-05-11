





import java.util.List;
import java.util.ArrayList;

public class pyrep_Robot extends Entity {

    private int port;
    private String name;





    private List<pyrep_Wheel> pyrep_wheels;




    private pyrep_Environment pyrep_environment;


    public pyrep_Robot(
        int port,        String name    ) {
        super(
        );
        this.port = port;
        this.name = name;
        this.pyrep_wheels = new ArrayList<>();
    }

    public pyrep_Robot(
        int port,        String name        ArrayList<pyrep_Wheel> pyrep_wheels    ) {
        this.port = port;
        this.name = name;
        this.pyrep_wheels = pyrep_wheels;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<pyrep_Wheel> getPyrep_wheels() {
        return pyrep_wheels;
    }

    public void addPyrep_wheel(Pyrep_wheel pyrep_wheel) {
        this.pyrep_wheels.add(pyrep_wheel);
    }
    public pyrep_Environment getPyrep_environment() {
        return pyrep_environment;
    }

    public void setPyrep_environment(pyrep_Environment pyrep_environment) {
        this.pyrep_environment = pyrep_environment;
    }

}