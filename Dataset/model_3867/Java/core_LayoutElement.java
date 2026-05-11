





import java.util.List;
import java.util.ArrayList;

public class core_LayoutElement  {

    private float y;
    private float x;





    private core_LayoutMap core_layoutmap;


    public core_LayoutElement(
        float y,        float x    ) {
        this.y = y;
        this.x = x;
    }


    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public core_LayoutMap getCore_layoutmap() {
        return core_layoutmap;
    }

    public void setCore_layoutmap(core_LayoutMap core_layoutmap) {
        this.core_layoutmap = core_layoutmap;
    }

}