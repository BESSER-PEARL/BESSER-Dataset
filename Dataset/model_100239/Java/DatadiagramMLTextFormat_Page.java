





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_Page extends IdentifiedElt, NamedElt {

    private String ViewCenterY;
    private String background;
    private String associatedPage;
    private String viewCenterX;
    private String viewScale;
    private String backPage;
    private String reviewerID;



    public DatadiagramMLTextFormat_Page(
        String ViewCenterY,        String background,        String associatedPage,        String viewCenterX,        String viewScale,        String backPage,        String reviewerID    ) {
        super(
        );
        this.ViewCenterY = ViewCenterY;
        this.background = background;
        this.associatedPage = associatedPage;
        this.viewCenterX = viewCenterX;
        this.viewScale = viewScale;
        this.backPage = backPage;
        this.reviewerID = reviewerID;
    }


    public String getViewcentery() {
        return ViewCenterY;
    }

    public void setViewcentery(String ViewCenterY) {
        this.ViewCenterY = ViewCenterY;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getAssociatedpage() {
        return associatedPage;
    }

    public void setAssociatedpage(String associatedPage) {
        this.associatedPage = associatedPage;
    }
    public String getViewcenterx() {
        return viewCenterX;
    }

    public void setViewcenterx(String viewCenterX) {
        this.viewCenterX = viewCenterX;
    }
    public String getViewscale() {
        return viewScale;
    }

    public void setViewscale(String viewScale) {
        this.viewScale = viewScale;
    }
    public String getBackpage() {
        return backPage;
    }

    public void setBackpage(String backPage) {
        this.backPage = backPage;
    }
    public String getReviewerid() {
        return reviewerID;
    }

    public void setReviewerid(String reviewerID) {
        this.reviewerID = reviewerID;
    }


}