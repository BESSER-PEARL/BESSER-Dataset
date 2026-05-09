





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ConnectionPointReference extends Vertex {

    private String exit;
    private String entry;
    private String state;



    public UMLModel_ConnectionPointReference(
        String exit,        String entry,        String state    ) {
        super(
        );
        this.exit = exit;
        this.entry = entry;
        this.state = state;
    }


    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }
    public String getEntry() {
        return entry;
    }

    public void setEntry(String entry) {
        this.entry = entry;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}