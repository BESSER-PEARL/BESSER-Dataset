





import java.util.List;
import java.util.ArrayList;

public class fxg_ContainerAttributes  {

    private String paddingBottom;
    private String paddingTop;
    private String paddingLeft;
    private String paddingRight;
    private String columnCount;
    private String lineBreak;
    private String verticalAlign;
    private String blockProgression;
    private String columnWidth;
    private String columnGap;
    private String firstBaselineOffset;



    public fxg_ContainerAttributes(
        String paddingBottom,        String paddingTop,        String paddingLeft,        String paddingRight,        String columnCount,        String lineBreak,        String verticalAlign,        String blockProgression,        String columnWidth,        String columnGap,        String firstBaselineOffset    ) {
        this.paddingBottom = paddingBottom;
        this.paddingTop = paddingTop;
        this.paddingLeft = paddingLeft;
        this.paddingRight = paddingRight;
        this.columnCount = columnCount;
        this.lineBreak = lineBreak;
        this.verticalAlign = verticalAlign;
        this.blockProgression = blockProgression;
        this.columnWidth = columnWidth;
        this.columnGap = columnGap;
        this.firstBaselineOffset = firstBaselineOffset;
    }


    public String getPaddingbottom() {
        return paddingBottom;
    }

    public void setPaddingbottom(String paddingBottom) {
        this.paddingBottom = paddingBottom;
    }
    public String getPaddingtop() {
        return paddingTop;
    }

    public void setPaddingtop(String paddingTop) {
        this.paddingTop = paddingTop;
    }
    public String getPaddingleft() {
        return paddingLeft;
    }

    public void setPaddingleft(String paddingLeft) {
        this.paddingLeft = paddingLeft;
    }
    public String getPaddingright() {
        return paddingRight;
    }

    public void setPaddingright(String paddingRight) {
        this.paddingRight = paddingRight;
    }
    public String getColumncount() {
        return columnCount;
    }

    public void setColumncount(String columnCount) {
        this.columnCount = columnCount;
    }
    public String getLinebreak() {
        return lineBreak;
    }

    public void setLinebreak(String lineBreak) {
        this.lineBreak = lineBreak;
    }
    public String getVerticalalign() {
        return verticalAlign;
    }

    public void setVerticalalign(String verticalAlign) {
        this.verticalAlign = verticalAlign;
    }
    public String getBlockprogression() {
        return blockProgression;
    }

    public void setBlockprogression(String blockProgression) {
        this.blockProgression = blockProgression;
    }
    public String getColumnwidth() {
        return columnWidth;
    }

    public void setColumnwidth(String columnWidth) {
        this.columnWidth = columnWidth;
    }
    public String getColumngap() {
        return columnGap;
    }

    public void setColumngap(String columnGap) {
        this.columnGap = columnGap;
    }
    public String getFirstbaselineoffset() {
        return firstBaselineOffset;
    }

    public void setFirstbaselineoffset(String firstBaselineOffset) {
        this.firstBaselineOffset = firstBaselineOffset;
    }


}