





import java.util.List;
import java.util.ArrayList;

public class core_LayoutElement  {

    private float x;
    private float y;





    private core_LayoutMap core_layoutmap;


    public core_LayoutElement(
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

    public core_LayoutMap getCore_layoutmap() {
        return core_layoutmap;
    }

    public void setCore_layoutmap(core_LayoutMap core_layoutmap) {
        this.core_layoutmap = core_layoutmap;
    }

}