





import java.util.List;
import java.util.ArrayList;

public class robot_Device extends Simulacra, NamedElement, Storable {

    private int dataSize;
    private String access;
    private String default;
    private String min;
    private String max;
    private boolean proxy;
    private String dataType;





    private robot_Roboid robot_roboid;


    public robot_Device(
        int dataSize,        String access,        String default,        String min,        String max,        boolean proxy,        String dataType    ) {
        super(
        );
        this.dataSize = dataSize;
        this.access = access;
        this.default = default;
        this.min = min;
        this.max = max;
        this.proxy = proxy;
        this.dataType = dataType;
    }


    public int getDatasize() {
        return dataSize;
    }

    public void setDatasize(int dataSize) {
        this.dataSize = dataSize;
    }
    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
        this.proxy = proxy;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public robot_Roboid getRobot_roboid() {
        return robot_roboid;
    }

    public void setRobot_roboid(robot_Roboid robot_roboid) {
        this.robot_roboid = robot_roboid;
    }

}