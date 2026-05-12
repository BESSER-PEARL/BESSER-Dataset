





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_Page extends NamedElt, IdentifiedElt {

    private String backPage;
    private String viewScale;
    private String associatedPage;
    private String ViewCenterY;
    private String viewCenterX;
    private String reviewerID;
    private String background;



    public DatadiagramMLXForm_Page(
        String backPage,        String viewScale,        String associatedPage,        String ViewCenterY,        String viewCenterX,        String reviewerID,        String background    ) {
        super(
        );
        this.backPage = backPage;
        this.viewScale = viewScale;
        this.associatedPage = associatedPage;
        this.ViewCenterY = ViewCenterY;
        this.viewCenterX = viewCenterX;
        this.reviewerID = reviewerID;
        this.background = background;
    }


    public String getBackpage() {
        return backPage;
    }

    public void setBackpage(String backPage) {
        this.backPage = backPage;
    }
    public String getViewscale() {
        return viewScale;
    }

    public void setViewscale(String viewScale) {
        this.viewScale = viewScale;
    }
    public String getAssociatedpage() {
        return associatedPage;
    }

    public void setAssociatedpage(String associatedPage) {
        this.associatedPage = associatedPage;
    }
    public String getViewcentery() {
        return ViewCenterY;
    }

    public void setViewcentery(String ViewCenterY) {
        this.ViewCenterY = ViewCenterY;
    }
    public String getViewcenterx() {
        return viewCenterX;
    }

    public void setViewcenterx(String viewCenterX) {
        this.viewCenterX = viewCenterX;
    }
    public String getReviewerid() {
        return reviewerID;
    }

    public void setReviewerid(String reviewerID) {
        this.reviewerID = reviewerID;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }


}