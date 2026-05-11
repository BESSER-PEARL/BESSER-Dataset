





import java.util.List;
import java.util.ArrayList;

public class rcl_Loop extends Statement {






    private rcl_RoverExpression rcl_roverexpression;




    private rcl_RclBlock rcl_rclblock;


    public rcl_Loop(
    ) {
        super(
        );
    }



    public rcl_RoverExpression getRcl_roverexpression() {
        return rcl_roverexpression;
    }

    public void setRcl_roverexpression(rcl_RoverExpression rcl_roverexpression) {
        this.rcl_roverexpression = rcl_roverexpression;
    }
    public rcl_RclBlock getRcl_rclblock() {
        return rcl_rclblock;
    }

    public void setRcl_rclblock(rcl_RclBlock rcl_rclblock) {
        this.rcl_rclblock = rcl_rclblock;
    }

}