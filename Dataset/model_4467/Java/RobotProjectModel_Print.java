





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_Print extends Instruction {

    private String string;



    public RobotProjectModel_Print(
        String string    ) {
        super(
        );
        this.string = string;
    }


    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }


}