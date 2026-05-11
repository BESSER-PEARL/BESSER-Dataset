





import java.util.List;
import java.util.ArrayList;

public class fxg_Group  {

    private String scaleX;
    private String scaleGridTop;
    private String scaleGridRight;
    private String transformY;
    private String alpha;
    private String transformX;
    private String scaleGridLeft;
    private String scaleGridBottom;
    private String id;
    private String scaleY;
    private String blendMode;
    private String visible;
    private String rotation;
    private String y;
    private String maskType;
    private String x;





    private fxg_Group fxg_group;




    private fxg_Graphic fxg_graphic;


    public fxg_Group(
        String scaleX,        String scaleGridTop,        String scaleGridRight,        String transformY,        String alpha,        String transformX,        String scaleGridLeft,        String scaleGridBottom,        String id,        String scaleY,        String blendMode,        String visible,        String rotation,        String y,        String maskType,        String x    ) {
        this.scaleX = scaleX;
        this.scaleGridTop = scaleGridTop;
        this.scaleGridRight = scaleGridRight;
        this.transformY = transformY;
        this.alpha = alpha;
        this.transformX = transformX;
        this.scaleGridLeft = scaleGridLeft;
        this.scaleGridBottom = scaleGridBottom;
        this.id = id;
        this.scaleY = scaleY;
        this.blendMode = blendMode;
        this.visible = visible;
        this.rotation = rotation;
        this.y = y;
        this.maskType = maskType;
        this.x = x;
    }


    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getScalegridtop() {
        return scaleGridTop;
    }

    public void setScalegridtop(String scaleGridTop) {
        this.scaleGridTop = scaleGridTop;
    }
    public String getScalegridright() {
        return scaleGridRight;
    }

    public void setScalegridright(String scaleGridRight) {
        this.scaleGridRight = scaleGridRight;
    }
    public String getTransformy() {
        return transformY;
    }

    public void setTransformy(String transformY) {
        this.transformY = transformY;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getTransformx() {
        return transformX;
    }

    public void setTransformx(String transformX) {
        this.transformX = transformX;
    }
    public String getScalegridleft() {
        return scaleGridLeft;
    }

    public void setScalegridleft(String scaleGridLeft) {
        this.scaleGridLeft = scaleGridLeft;
    }
    public String getScalegridbottom() {
        return scaleGridBottom;
    }

    public void setScalegridbottom(String scaleGridBottom) {
        this.scaleGridBottom = scaleGridBottom;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getMasktype() {
        return maskType;
    }

    public void setMasktype(String maskType) {
        this.maskType = maskType;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }
    public fxg_Graphic getFxg_graphic() {
        return fxg_graphic;
    }

    public void setFxg_graphic(fxg_Graphic fxg_graphic) {
        this.fxg_graphic = fxg_graphic;
    }

}