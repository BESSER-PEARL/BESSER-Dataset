





import java.util.List;
import java.util.ArrayList;

public class krendering_KDecoratorPlacementData extends KPlacementData {

    private float height;
    private float relative;
    private float width;
    private boolean rotateWithLine;
    private float absolute;
    private float yOffset;
    private float xOffset;



    public krendering_KDecoratorPlacementData(
        float height,        float relative,        float width,        boolean rotateWithLine,        float absolute,        float yOffset,        float xOffset    ) {
        super(
        );
        this.height = height;
        this.relative = relative;
        this.width = width;
        this.rotateWithLine = rotateWithLine;
        this.absolute = absolute;
        this.yOffset = yOffset;
        this.xOffset = xOffset;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getRelative() {
        return relative;
    }

    public void setRelative(float relative) {
        this.relative = relative;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public boolean getRotatewithline() {
        return rotateWithLine;
    }

    public void setRotatewithline(boolean rotateWithLine) {
        this.rotateWithLine = rotateWithLine;
    }
    public float getAbsolute() {
        return absolute;
    }

    public void setAbsolute(float absolute) {
        this.absolute = absolute;
    }
    public float getYoffset() {
        return yOffset;
    }

    public void setYoffset(float yOffset) {
        this.yOffset = yOffset;
    }
    public float getXoffset() {
        return xOffset;
    }

    public void setXoffset(float xOffset) {
        this.xOffset = xOffset;
    }


}