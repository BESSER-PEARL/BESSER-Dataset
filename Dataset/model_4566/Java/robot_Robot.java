





import java.util.List;
import java.util.ArrayList;

public class robot_Robot extends Findable, NamedElement, Storable {

    private String version;
    private String standard;
    private String provider;





    private List<robot_Roboid> robot_roboids;




    private List<robot_Control> robot_controls;


    public robot_Robot(
        String version,        String standard,        String provider    ) {
        super(
        );
        this.version = version;
        this.standard = standard;
        this.provider = provider;
        this.robot_roboids = new ArrayList<>();
        this.robot_controls = new ArrayList<>();
    }

    public robot_Robot(
        String version,        String standard,        String provider        ArrayList<robot_Roboid> robot_roboids,        ArrayList<robot_Control> robot_controls    ) {
        this.version = version;
        this.standard = standard;
        this.provider = provider;
        this.robot_roboids = robot_roboids;
        this.robot_controls = robot_controls;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getStandard() {
        return standard;
    }

    public void setStandard(String standard) {
        this.standard = standard;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }

    public List<robot_Roboid> getRobot_roboids() {
        return robot_roboids;
    }

    public void addRobot_roboid(Robot_roboid robot_roboid) {
        this.robot_roboids.add(robot_roboid);
    }
    public List<robot_Control> getRobot_controls() {
        return robot_controls;
    }

    public void addRobot_control(Robot_control robot_control) {
        this.robot_controls.add(robot_control);
    }

}