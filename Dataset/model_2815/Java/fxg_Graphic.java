





import java.util.List;
import java.util.ArrayList;

public class fxg_Graphic  {

    private String version;
    private int viewHeight;
    private String scaleGridTop;
    private String scaleGridLeft;
    private String scaleGridRight;
    private int viewWidth;
    private String scaleGridBottom;



    public fxg_Graphic(
        String version,        int viewHeight,        String scaleGridTop,        String scaleGridLeft,        String scaleGridRight,        int viewWidth,        String scaleGridBottom    ) {
        this.version = version;
        this.viewHeight = viewHeight;
        this.scaleGridTop = scaleGridTop;
        this.scaleGridLeft = scaleGridLeft;
        this.scaleGridRight = scaleGridRight;
        this.viewWidth = viewWidth;
        this.scaleGridBottom = scaleGridBottom;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public int getViewheight() {
        return viewHeight;
    }

    public void setViewheight(int viewHeight) {
        this.viewHeight = viewHeight;
    }
    public String getScalegridtop() {
        return scaleGridTop;
    }

    public void setScalegridtop(String scaleGridTop) {
        this.scaleGridTop = scaleGridTop;
    }
    public String getScalegridleft() {
        return scaleGridLeft;
    }

    public void setScalegridleft(String scaleGridLeft) {
        this.scaleGridLeft = scaleGridLeft;
    }
    public String getScalegridright() {
        return scaleGridRight;
    }

    public void setScalegridright(String scaleGridRight) {
        this.scaleGridRight = scaleGridRight;
    }
    public int getViewwidth() {
        return viewWidth;
    }

    public void setViewwidth(int viewWidth) {
        this.viewWidth = viewWidth;
    }
    public String getScalegridbottom() {
        return scaleGridBottom;
    }

    public void setScalegridbottom(String scaleGridBottom) {
        this.scaleGridBottom = scaleGridBottom;
    }


}