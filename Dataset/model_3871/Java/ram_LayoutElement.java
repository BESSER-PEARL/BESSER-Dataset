





import java.util.List;
import java.util.ArrayList;

public class ram_LayoutElement  {

    private float x;
    private float y;





    private ram_ElementMap ram_elementmap;


    public ram_LayoutElement(
        float x,        float y    ) {
        this.x = x;
        this.y = y;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public ram_ElementMap getRam_elementmap() {
        return ram_elementmap;
    }

    public void setRam_elementmap(ram_ElementMap ram_elementmap) {
        this.ram_elementmap = ram_elementmap;
    }

}