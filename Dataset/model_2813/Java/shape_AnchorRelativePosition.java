





import java.util.List;
import java.util.ArrayList;

public class shape_AnchorRelativePosition extends AnchorPositionPos {

    private String xoffset;
    private String yoffset;



    public shape_AnchorRelativePosition(
        String xoffset,        String yoffset    ) {
        super(
        );
        this.xoffset = xoffset;
        this.yoffset = yoffset;
    }


    public String getXoffset() {
        return xoffset;
    }

    public void setXoffset(String xoffset) {
        this.xoffset = xoffset;
    }
    public String getYoffset() {
        return yoffset;
    }

    public void setYoffset(String yoffset) {
        this.yoffset = yoffset;
    }


}