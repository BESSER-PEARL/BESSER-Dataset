





import java.util.List;
import java.util.ArrayList;

public class simulink_StateflowElement extends SimulinkElement {

    private String path;
    private int id;



    public simulink_StateflowElement(
        String path,        int id    ) {
        super(
        );
        this.path = path;
        this.id = id;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}