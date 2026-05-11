





import java.util.List;
import java.util.ArrayList;

public class cs_CSNode extends CSElement {

    private String heightRatioToParent;
    private String widthRatioToParent;
    private String maxHeight;
    private String horizontalAlign;
    private String maxWidth;
    private String x;
    private String height;
    private String y;
    private String minWidth;
    private String minHeight;
    private String verticalAlign;
    private String width;



    public cs_CSNode(
        String heightRatioToParent,        String widthRatioToParent,        String maxHeight,        String horizontalAlign,        String maxWidth,        String x,        String height,        String y,        String minWidth,        String minHeight,        String verticalAlign,        String width    ) {
        super(
        );
        this.heightRatioToParent = heightRatioToParent;
        this.widthRatioToParent = widthRatioToParent;
        this.maxHeight = maxHeight;
        this.horizontalAlign = horizontalAlign;
        this.maxWidth = maxWidth;
        this.x = x;
        this.height = height;
        this.y = y;
        this.minWidth = minWidth;
        this.minHeight = minHeight;
        this.verticalAlign = verticalAlign;
        this.width = width;
    }


    public String getHeightratiotoparent() {
        return heightRatioToParent;
    }

    public void setHeightratiotoparent(String heightRatioToParent) {
        this.heightRatioToParent = heightRatioToParent;
    }
    public String getWidthratiotoparent() {
        return widthRatioToParent;
    }

    public void setWidthratiotoparent(String widthRatioToParent) {
        this.widthRatioToParent = widthRatioToParent;
    }
    public String getMaxheight() {
        return maxHeight;
    }

    public void setMaxheight(String maxHeight) {
        this.maxHeight = maxHeight;
    }
    public String getHorizontalalign() {
        return horizontalAlign;
    }

    public void setHorizontalalign(String horizontalAlign) {
        this.horizontalAlign = horizontalAlign;
    }
    public String getMaxwidth() {
        return maxWidth;
    }

    public void setMaxwidth(String maxWidth) {
        this.maxWidth = maxWidth;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getMinwidth() {
        return minWidth;
    }

    public void setMinwidth(String minWidth) {
        this.minWidth = minWidth;
    }
    public String getMinheight() {
        return minHeight;
    }

    public void setMinheight(String minHeight) {
        this.minHeight = minHeight;
    }
    public String getVerticalalign() {
        return verticalAlign;
    }

    public void setVerticalalign(String verticalAlign) {
        this.verticalAlign = verticalAlign;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}