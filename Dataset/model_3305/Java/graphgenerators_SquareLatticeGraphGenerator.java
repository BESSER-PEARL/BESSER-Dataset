





import java.util.List;
import java.util.ArrayList;

public class graphgenerators_SquareLatticeGraphGenerator extends LatticeGraphGenerator {

    private float area;
    private int ySize;
    private int xSize;



    public graphgenerators_SquareLatticeGraphGenerator(
        float area,        int ySize,        int xSize    ) {
        super(
        );
        this.area = area;
        this.ySize = ySize;
        this.xSize = xSize;
    }


    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }
    public int getYsize() {
        return ySize;
    }

    public void setYsize(int ySize) {
        this.ySize = ySize;
    }
    public int getXsize() {
        return xSize;
    }

    public void setXsize(int xSize) {
        this.xSize = xSize;
    }


}