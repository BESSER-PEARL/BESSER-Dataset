





import java.util.List;
import java.util.ArrayList;

public class afpText_TilePosition extends triplet {

    private String XOFFSET;
    private String YOFFSET;



    public afpText_TilePosition(
        String XOFFSET,        String YOFFSET    ) {
        super(
        );
        this.XOFFSET = XOFFSET;
        this.YOFFSET = YOFFSET;
    }


    public String getXoffset() {
        return XOFFSET;
    }

    public void setXoffset(String XOFFSET) {
        this.XOFFSET = XOFFSET;
    }
    public String getYoffset() {
        return YOFFSET;
    }

    public void setYoffset(String YOFFSET) {
        this.YOFFSET = YOFFSET;
    }


}