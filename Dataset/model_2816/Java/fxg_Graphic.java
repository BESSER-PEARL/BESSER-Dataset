





import java.util.List;
import java.util.ArrayList;

public class fxg_Graphic  {

    private String version;
    private String scaleGridBottom;
    private String scaleGridLeft;
    private String scaleGridRight;
    private int viewHeight;
    private int viewWidth;
    private String scaleGridTop;



    public fxg_Graphic(
        String version,        String scaleGridBottom,        String scaleGridLeft,        String scaleGridRight,        int viewHeight,        int viewWidth,        String scaleGridTop    ) {
        this.version = version;
        this.scaleGridBottom = scaleGridBottom;
        this.scaleGridLeft = scaleGridLeft;
        this.scaleGridRight = scaleGridRight;
        this.viewHeight = viewHeight;
        this.viewWidth = viewWidth;
        this.scaleGridTop = scaleGridTop;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getScalegridbottom() {
        return scaleGridBottom;
    }

    public void setScalegridbottom(String scaleGridBottom) {
        this.scaleGridBottom = scaleGridBottom;
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
    public int getViewheight() {
        return viewHeight;
    }

    public void setViewheight(int viewHeight) {
        this.viewHeight = viewHeight;
    }
    public int getViewwidth() {
        return viewWidth;
    }

    public void setViewwidth(int viewWidth) {
        this.viewWidth = viewWidth;
    }
    public String getScalegridtop() {
        return scaleGridTop;
    }

    public void setScalegridtop(String scaleGridTop) {
        this.scaleGridTop = scaleGridTop;
    }


}