





import java.util.List;
import java.util.ArrayList;

public class arduinoML_App extends NamedElement {

    private boolean monitoring;



    public arduinoML_App(
        boolean monitoring    ) {
        super(
        );
        this.monitoring = monitoring;
    }


    public boolean getMonitoring() {
        return monitoring;
    }

    public void setMonitoring(boolean monitoring) {
        this.monitoring = monitoring;
    }


}