





import java.util.List;
import java.util.ArrayList;

public class egt_Vertex  {

    private String name;
    private String color;
    private int index;



    public egt_Vertex(
        String name,        String color,        int index    ) {
        this.name = name;
        this.color = color;
        this.index = index;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }


}