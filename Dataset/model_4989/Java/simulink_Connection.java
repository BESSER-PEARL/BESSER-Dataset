





import java.util.List;
import java.util.ArrayList;

public class simulink_Connection extends SimulinkElement {

    private String lineName;



    public simulink_Connection(
        String lineName    ) {
        super(
        );
        this.lineName = lineName;
    }


    public String getLinename() {
        return lineName;
    }

    public void setLinename(String lineName) {
        this.lineName = lineName;
    }


}