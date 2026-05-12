





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_Layout  {

    private String orientation;
    private String centerHorizontal;
    private String centerVertical;
    private String startPageNumber;





    private PageSetup pagesetup;


    public SpreadsheetMLPrintingSetup_Layout(
        String orientation,        String centerHorizontal,        String centerVertical,        String startPageNumber    ) {
        this.orientation = orientation;
        this.centerHorizontal = centerHorizontal;
        this.centerVertical = centerVertical;
        this.startPageNumber = startPageNumber;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getCenterhorizontal() {
        return centerHorizontal;
    }

    public void setCenterhorizontal(String centerHorizontal) {
        this.centerHorizontal = centerHorizontal;
    }
    public String getCentervertical() {
        return centerVertical;
    }

    public void setCentervertical(String centerVertical) {
        this.centerVertical = centerVertical;
    }
    public String getStartpagenumber() {
        return startPageNumber;
    }

    public void setStartpagenumber(String startPageNumber) {
        this.startPageNumber = startPageNumber;
    }

    public PageSetup getPagesetup() {
        return pagesetup;
    }

    public void setPagesetup(PageSetup pagesetup) {
        this.pagesetup = pagesetup;
    }

}