





import java.util.List;
import java.util.ArrayList;

public class robot_Protocol extends NamedElement {

    private String version;
    private int remainingBuffer;
    private int bufferSize;





    private robot_Roboid robot_roboid;


    public robot_Protocol(
        String version,        int remainingBuffer,        int bufferSize    ) {
        super(
        );
        this.version = version;
        this.remainingBuffer = remainingBuffer;
        this.bufferSize = bufferSize;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public int getRemainingbuffer() {
        return remainingBuffer;
    }

    public void setRemainingbuffer(int remainingBuffer) {
        this.remainingBuffer = remainingBuffer;
    }
    public int getBuffersize() {
        return bufferSize;
    }

    public void setBuffersize(int bufferSize) {
        this.bufferSize = bufferSize;
    }

    public robot_Roboid getRobot_roboid() {
        return robot_roboid;
    }

    public void setRobot_roboid(robot_Roboid robot_roboid) {
        this.robot_roboid = robot_roboid;
    }

}