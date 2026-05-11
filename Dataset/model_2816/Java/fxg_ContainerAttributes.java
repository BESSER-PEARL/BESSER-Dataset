





import java.util.List;
import java.util.ArrayList;

public class fxg_ContainerAttributes  {

    private String columnCount;
    private String paddingTop;
    private String verticalAlign;
    private String paddingLeft;
    private String paddingRight;
    private String blockProgression;
    private String columnWidth;
    private String columnGap;
    private String paddingBottom;
    private String lineBreak;
    private String firstBaselineOffset;



    public fxg_ContainerAttributes(
        String columnCount,        String paddingTop,        String verticalAlign,        String paddingLeft,        String paddingRight,        String blockProgression,        String columnWidth,        String columnGap,        String paddingBottom,        String lineBreak,        String firstBaselineOffset    ) {
        this.columnCount = columnCount;
        this.paddingTop = paddingTop;
        this.verticalAlign = verticalAlign;
        this.paddingLeft = paddingLeft;
        this.paddingRight = paddingRight;
        this.blockProgression = blockProgression;
        this.columnWidth = columnWidth;
        this.columnGap = columnGap;
        this.paddingBottom = paddingBottom;
        this.lineBreak = lineBreak;
        this.firstBaselineOffset = firstBaselineOffset;
    }


    public String getColumncount() {
        return columnCount;
    }

    public void setColumncount(String columnCount) {
        this.columnCount = columnCount;
    }
    public String getPaddingtop() {
        return paddingTop;
    }

    public void setPaddingtop(String paddingTop) {
        this.paddingTop = paddingTop;
    }
    public String getVerticalalign() {
        return verticalAlign;
    }

    public void setVerticalalign(String verticalAlign) {
        this.verticalAlign = verticalAlign;
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
    public String getPaddingbottom() {
        return paddingBottom;
    }

    public void setPaddingbottom(String paddingBottom) {
        this.paddingBottom = paddingBottom;
    }
    public String getLinebreak() {
        return lineBreak;
    }

    public void setLinebreak(String lineBreak) {
        this.lineBreak = lineBreak;
    }
    public String getFirstbaselineoffset() {
        return firstBaselineOffset;
    }

    public void setFirstbaselineoffset(String firstBaselineOffset) {
        this.firstBaselineOffset = firstBaselineOffset;
    }


}