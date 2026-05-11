





import java.util.List;
import java.util.ArrayList;

public class DOT_Shape extends GraphElement {

    private int height;
    private int width;
    private int peripheries;



    public DOT_Shape(
        int height,        int width,        int peripheries    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.peripheries = peripheries;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getPeripheries() {
        return peripheries;
    }

    public void setPeripheries(int peripheries) {
        this.peripheries = peripheries;
    }


}