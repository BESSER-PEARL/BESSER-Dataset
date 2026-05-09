





import java.util.List;
import java.util.ArrayList;

public class graphbt_Layout  {

    private int height;
    private int y;
    private int x;
    private int z;
    private int width;
    private String cRef;





    private graphbt_LayoutList graphbt_layoutlist;


    public graphbt_Layout(
        int height,        int y,        int x,        int z,        int width,        String cRef    ) {
        this.height = height;
        this.y = y;
        this.x = x;
        this.z = z;
        this.width = width;
        this.cRef = cRef;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getZ() {
        return z;
    }

    public void setZ(int z) {
        this.z = z;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getCref() {
        return cRef;
    }

    public void setCref(String cRef) {
        this.cRef = cRef;
    }

    public graphbt_LayoutList getGraphbt_layoutlist() {
        return graphbt_layoutlist;
    }

    public void setGraphbt_layoutlist(graphbt_LayoutList graphbt_layoutlist) {
        this.graphbt_layoutlist = graphbt_layoutlist;
    }

}