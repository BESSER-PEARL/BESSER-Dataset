





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_Layout  {

    private String centerHorizontal;
    private String orientation;
    private String startPageNumber;
    private String centerVertical;





    private PageSetup pagesetup;


    public SpreadsheetMLStyles_Layout(
        String centerHorizontal,        String orientation,        String startPageNumber,        String centerVertical    ) {
        this.centerHorizontal = centerHorizontal;
        this.orientation = orientation;
        this.startPageNumber = startPageNumber;
        this.centerVertical = centerVertical;
    }


    public String getCenterhorizontal() {
        return centerHorizontal;
    }

    public void setCenterhorizontal(String centerHorizontal) {
        this.centerHorizontal = centerHorizontal;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getStartpagenumber() {
        return startPageNumber;
    }

    public void setStartpagenumber(String startPageNumber) {
        this.startPageNumber = startPageNumber;
    }
    public String getCentervertical() {
        return centerVertical;
    }

    public void setCentervertical(String centerVertical) {
        this.centerVertical = centerVertical;
    }

    public PageSetup getPagesetup() {
        return pagesetup;
    }

    public void setPagesetup(PageSetup pagesetup) {
        this.pagesetup = pagesetup;
    }

}