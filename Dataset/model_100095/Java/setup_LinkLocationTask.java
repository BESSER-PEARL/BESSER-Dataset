





import java.util.List;
import java.util.ArrayList;

public class setup_LinkLocationTask extends SetupTask {

    private String name;
    private String path;



    public setup_LinkLocationTask(
        String name,        String path    ) {
        super(
        );
        this.name = name;
        this.path = path;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}