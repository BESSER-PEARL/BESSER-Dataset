





import java.util.List;
import java.util.ArrayList;

public class Wires_Library extends WiresElement {

    private String path;
    private String name;



    public Wires_Library(
        String path,        String name    ) {
        super(
        );
        this.path = path;
        this.name = name;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}