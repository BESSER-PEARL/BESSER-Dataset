





import java.util.List;
import java.util.ArrayList;

public class notation_Bounds extends Location {

    private int width;
    private int height;





    private notation_Node notation_node;


    public notation_Bounds(
        int width,        int height    ) {
        super(
        );
        this.width = width;
        this.height = height;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public notation_Node getNotation_node() {
        return notation_node;
    }

    public void setNotation_node(notation_Node notation_node) {
        this.notation_node = notation_node;
    }

}