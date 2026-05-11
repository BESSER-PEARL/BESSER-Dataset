





import java.util.List;
import java.util.ArrayList;

public class krendering_KDecoratorPlacementData extends KPlacementData {

    private float absolute;
    private float width;
    private float xOffset;
    private float height;
    private float yOffset;
    private float relative;
    private boolean rotateWithLine;



    public krendering_KDecoratorPlacementData(
        float absolute,        float width,        float xOffset,        float height,        float yOffset,        float relative,        boolean rotateWithLine    ) {
        super(
        );
        this.absolute = absolute;
        this.width = width;
        this.xOffset = xOffset;
        this.height = height;
        this.yOffset = yOffset;
        this.relative = relative;
        this.rotateWithLine = rotateWithLine;
    }


    public float getAbsolute() {
        return absolute;
    }

    public void setAbsolute(float absolute) {
        this.absolute = absolute;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getXoffset() {
        return xOffset;
    }

    public void setXoffset(float xOffset) {
        this.xOffset = xOffset;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getYoffset() {
        return yOffset;
    }

    public void setYoffset(float yOffset) {
        this.yOffset = yOffset;
    }
    public float getRelative() {
        return relative;
    }

    public void setRelative(float relative) {
        this.relative = relative;
    }
    public boolean getRotatewithline() {
        return rotateWithLine;
    }

    public void setRotatewithline(boolean rotateWithLine) {
        this.rotateWithLine = rotateWithLine;
    }


}