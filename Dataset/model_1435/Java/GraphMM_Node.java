





import java.util.List;
import java.util.ArrayList;

public class GraphMM_Node  {

    private String type;
    private String name;
    private float size;



    public GraphMM_Node(
        String type,        String name,        float size    ) {
        this.type = type;
        this.name = name;
        this.size = size;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }


}