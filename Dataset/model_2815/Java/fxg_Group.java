





import java.util.List;
import java.util.ArrayList;

public class fxg_Group  {

    private String x;
    private String scaleGridLeft;
    private String scaleY;
    private String scaleX;
    private String scaleGridBottom;
    private String y;
    private String alpha;
    private String maskType;
    private String id;
    private String transformY;
    private String rotation;
    private String scaleGridTop;
    private String scaleGridRight;
    private String blendMode;
    private String transformX;
    private String visible;





    private fxg_Group fxg_group;




    private fxg_Graphic fxg_graphic;


    public fxg_Group(
        String x,        String scaleGridLeft,        String scaleY,        String scaleX,        String scaleGridBottom,        String y,        String alpha,        String maskType,        String id,        String transformY,        String rotation,        String scaleGridTop,        String scaleGridRight,        String blendMode,        String transformX,        String visible    ) {
        this.x = x;
        this.scaleGridLeft = scaleGridLeft;
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.scaleGridBottom = scaleGridBottom;
        this.y = y;
        this.alpha = alpha;
        this.maskType = maskType;
        this.id = id;
        this.transformY = transformY;
        this.rotation = rotation;
        this.scaleGridTop = scaleGridTop;
        this.scaleGridRight = scaleGridRight;
        this.blendMode = blendMode;
        this.transformX = transformX;
        this.visible = visible;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getScalegridleft() {
        return scaleGridLeft;
    }

    public void setScalegridleft(String scaleGridLeft) {
        this.scaleGridLeft = scaleGridLeft;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getScalegridbottom() {
        return scaleGridBottom;
    }

    public void setScalegridbottom(String scaleGridBottom) {
        this.scaleGridBottom = scaleGridBottom;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getMasktype() {
        return maskType;
    }

    public void setMasktype(String maskType) {
        this.maskType = maskType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTransformy() {
        return transformY;
    }

    public void setTransformy(String transformY) {
        this.transformY = transformY;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
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
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String getTransformx() {
        return transformX;
    }

    public void setTransformx(String transformX) {
        this.transformX = transformX;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
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