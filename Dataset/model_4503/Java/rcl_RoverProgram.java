





import java.util.List;
import java.util.ArrayList;

public class rcl_RoverProgram  {

    private String name;





    private rcl_RclBlock rcl_rclblock;


    public rcl_RoverProgram(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rcl_RclBlock getRcl_rclblock() {
        return rcl_rclblock;
    }

    public void setRcl_rclblock(rcl_RclBlock rcl_rclblock) {
        this.rcl_rclblock = rcl_rclblock;
    }

}