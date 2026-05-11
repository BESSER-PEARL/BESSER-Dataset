





import java.util.List;
import java.util.ArrayList;

public class egt_Vertex  {

    private int index;
    private String color;
    private String name;





    private egt_GraphModel egt_graphmodel;


    public egt_Vertex(
        int index,        String color,        String name    ) {
        this.index = index;
        this.color = color;
        this.name = name;
    }


    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public egt_GraphModel getEgt_graphmodel() {
        return egt_graphmodel;
    }

    public void setEgt_graphmodel(egt_GraphModel egt_graphmodel) {
        this.egt_graphmodel = egt_graphmodel;
    }

}