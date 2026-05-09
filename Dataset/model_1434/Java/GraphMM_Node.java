





import java.util.List;
import java.util.ArrayList;

public class GraphMM_Node  {

    private float size;
    private String name;
    private String type;



    public GraphMM_Node(
        float size,        String name,        String type    ) {
        this.size = size;
        this.name = name;
        this.type = type;
    }


    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}