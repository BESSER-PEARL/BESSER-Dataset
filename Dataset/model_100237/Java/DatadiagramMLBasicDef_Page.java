





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_Page extends NamedElt, IdentifiedElt {

    private String associatedPage;
    private String backPage;
    private String reviewerID;
    private String background;
    private String viewScale;
    private String viewCenterX;
    private String ViewCenterY;





    private PagesCollection pagescollection;


    public DatadiagramMLBasicDef_Page(
        String associatedPage,        String backPage,        String reviewerID,        String background,        String viewScale,        String viewCenterX,        String ViewCenterY    ) {
        super(
        );
        this.associatedPage = associatedPage;
        this.backPage = backPage;
        this.reviewerID = reviewerID;
        this.background = background;
        this.viewScale = viewScale;
        this.viewCenterX = viewCenterX;
        this.ViewCenterY = ViewCenterY;
    }


    public String getAssociatedpage() {
        return associatedPage;
    }

    public void setAssociatedpage(String associatedPage) {
        this.associatedPage = associatedPage;
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
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getViewscale() {
        return viewScale;
    }

    public void setViewscale(String viewScale) {
        this.viewScale = viewScale;
    }
    public String getViewcenterx() {
        return viewCenterX;
    }

    public void setViewcenterx(String viewCenterX) {
        this.viewCenterX = viewCenterX;
    }
    public String getViewcentery() {
        return ViewCenterY;
    }

    public void setViewcentery(String ViewCenterY) {
        this.ViewCenterY = ViewCenterY;
    }

    public PagesCollection getPagescollection() {
        return pagescollection;
    }

    public void setPagescollection(PagesCollection pagescollection) {
        this.pagescollection = pagescollection;
    }

}