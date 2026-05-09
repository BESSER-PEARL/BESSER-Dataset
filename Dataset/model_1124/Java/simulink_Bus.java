





import java.util.List;
import java.util.ArrayList;

public class simulink_Bus extends Element {

    private String name;





    private simulink_Line simulink_line;


    public simulink_Bus(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simulink_Line getSimulink_line() {
        return simulink_line;
    }

    public void setSimulink_line(simulink_Line simulink_line) {
        this.simulink_line = simulink_line;
    }

}