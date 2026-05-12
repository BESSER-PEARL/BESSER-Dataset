





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLSimplified_Page extends IdentifiedElt, NamedElt {

    private String backPage;
    private String viewScale;
    private String associatedPage;
    private String viewCenterX;
    private String reviewerID;
    private String ViewCenterY;
    private String background;





    private List<PageElt> pageelts;




    private PagesCollection pagescollection;


    public DatadiagramMLSimplified_Page(
        String backPage,        String viewScale,        String associatedPage,        String viewCenterX,        String reviewerID,        String ViewCenterY,        String background    ) {
        super(
        );
        this.backPage = backPage;
        this.viewScale = viewScale;
        this.associatedPage = associatedPage;
        this.viewCenterX = viewCenterX;
        this.reviewerID = reviewerID;
        this.ViewCenterY = ViewCenterY;
        this.background = background;
        this.pageelts = new ArrayList<>();
    }

    public DatadiagramMLSimplified_Page(
        String backPage,        String viewScale,        String associatedPage,        String viewCenterX,        String reviewerID,        String ViewCenterY,        String background        ArrayList<PageElt> pageelts    ) {
        this.backPage = backPage;
        this.viewScale = viewScale;
        this.associatedPage = associatedPage;
        this.viewCenterX = viewCenterX;
        this.reviewerID = reviewerID;
        this.ViewCenterY = ViewCenterY;
        this.background = background;
        this.pageelts = pageelts;
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

    public List<PageElt> getPageelts() {
        return pageelts;
    }

    public void addPageelt(Pageelt pageelt) {
        this.pageelts.add(pageelt);
    }
    public PagesCollection getPagescollection() {
        return pagescollection;
    }

    public void setPagescollection(PagesCollection pagescollection) {
        this.pagescollection = pagescollection;
    }

}