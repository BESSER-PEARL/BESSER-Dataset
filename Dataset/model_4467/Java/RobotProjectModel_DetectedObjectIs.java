





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_DetectedObjectIs extends Condition {

    private String rightOperand;



    public RobotProjectModel_DetectedObjectIs(
        String rightOperand    ) {
        super(
        );
        this.rightOperand = rightOperand;
    }


    public String getRightoperand() {
        return rightOperand;
    }

    public void setRightoperand(String rightOperand) {
        this.rightOperand = rightOperand;
    }


}