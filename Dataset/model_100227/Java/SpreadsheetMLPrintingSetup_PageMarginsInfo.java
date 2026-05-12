





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_PageMarginsInfo  {

    private String top;
    private String left;
    private String bottom;
    private String right;





    private PageSetup pagesetup;


    public SpreadsheetMLPrintingSetup_PageMarginsInfo(
        String top,        String left,        String bottom,        String right    ) {
        this.top = top;
        this.left = left;
        this.bottom = bottom;
        this.right = right;
    }


    public String getTop() {
        return top;
    }

    public void setTop(String top) {
        this.top = top;
    }
    public String getLeft() {
        return left;
    }

    public void setLeft(String left) {
        this.left = left;
    }
    public String getBottom() {
        return bottom;
    }

    public void setBottom(String bottom) {
        this.bottom = bottom;
    }
    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }

    public PageSetup getPagesetup() {
        return pagesetup;
    }

    public void setPagesetup(PageSetup pagesetup) {
        this.pagesetup = pagesetup;
    }

}