





import java.util.List;
import java.util.ArrayList;

public class robot_Roboid extends Simulacra, Findable, NamedElement, Storable {

    private String provider;
    private String id;
    private String address;
    private String version;
    private String uid;





    private robot_Roboid robot_roboid;




    private robot_Roboid robot_roboid;


    public robot_Roboid(
        String provider,        String id,        String address,        String version,        String uid    ) {
        super(
        );
        this.provider = provider;
        this.id = id;
        this.address = address;
        this.version = version;
        this.uid = uid;
    }


    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public robot_Roboid getRobot_roboid() {
        return robot_roboid;
    }

    public void setRobot_roboid(robot_Roboid robot_roboid) {
        this.robot_roboid = robot_roboid;
    }
    public robot_Roboid getRobot_roboid() {
        return robot_roboid;
    }

    public void setRobot_roboid(robot_Roboid robot_roboid) {
        this.robot_roboid = robot_roboid;
    }

}