





import java.util.List;
import java.util.ArrayList;

public class DOT_Node extends Nodelike {

    private int height;
    private int width;
    private int fontsize;
    private boolean fixedSize;
    private String fontname;



    public DOT_Node(
        int height,        int width,        int fontsize,        boolean fixedSize,        String fontname    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.fontsize = fontsize;
        this.fixedSize = fixedSize;
        this.fontname = fontname;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getFontsize() {
        return fontsize;
    }

    public void setFontsize(int fontsize) {
        this.fontsize = fontsize;
    }
    public boolean getFixedsize() {
        return fixedSize;
    }

    public void setFixedsize(boolean fixedSize) {
        this.fixedSize = fixedSize;
    }
    public String getFontname() {
        return fontname;
    }

    public void setFontname(String fontname) {
        this.fontname = fontname;
    }


}