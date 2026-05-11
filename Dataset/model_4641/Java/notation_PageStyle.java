





import java.util.List;
import java.util.ArrayList;

public class notation_PageStyle extends Style {

    private int pageWidth;
    private int pageX;
    private int pageHeight;
    private int pageY;



    public notation_PageStyle(
        int pageWidth,        int pageX,        int pageHeight,        int pageY    ) {
        super(
        );
        this.pageWidth = pageWidth;
        this.pageX = pageX;
        this.pageHeight = pageHeight;
        this.pageY = pageY;
    }


    public int getPagewidth() {
        return pageWidth;
    }

    public void setPagewidth(int pageWidth) {
        this.pageWidth = pageWidth;
    }
    public int getPagex() {
        return pageX;
    }

    public void setPagex(int pageX) {
        this.pageX = pageX;
    }
    public int getPageheight() {
        return pageHeight;
    }

    public void setPageheight(int pageHeight) {
        this.pageHeight = pageHeight;
    }
    public int getPagey() {
        return pageY;
    }

    public void setPagey(int pageY) {
        this.pageY = pageY;
    }


}