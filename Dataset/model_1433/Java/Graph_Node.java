





import java.util.List;
import java.util.ArrayList;

public class Graph_Node  {

    private String name;
    private String type;
    private float size;



    public Graph_Node(
        String name,        String type,        float size    ) {
        this.name = name;
        this.type = type;
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
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }


}