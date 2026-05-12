





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_PageMarginsInfo  {

    private String bottom;
    private String left;
    private String right;
    private String top;





    private PageSetup pagesetup;


    public SpreadsheetMLStyles_PageMarginsInfo(
        String bottom,        String left,        String right,        String top    ) {
        this.bottom = bottom;
        this.left = left;
        this.right = right;
        this.top = top;
    }


    public String getBottom() {
        return bottom;
    }

    public void setBottom(String bottom) {
        this.bottom = bottom;
    }
    public String getLeft() {
        return left;
    }

    public void setLeft(String left) {
        this.left = left;
    }
    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }
    public String getTop() {
        return top;
    }

    public void setTop(String top) {
        this.top = top;
    }

    public PageSetup getPagesetup() {
        return pagesetup;
    }

    public void setPagesetup(PageSetup pagesetup) {
        this.pagesetup = pagesetup;
    }

}