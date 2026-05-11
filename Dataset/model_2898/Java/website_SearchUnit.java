





import java.util.List;
import java.util.ArrayList;

public class website_SearchUnit extends ControlUnit {

    private String styleClass;





    private website_IndexUnit website_indexunit;


    public website_SearchUnit(
        String styleClass    ) {
        super(
        );
        this.styleClass = styleClass;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }

    public website_IndexUnit getWebsite_indexunit() {
        return website_indexunit;
    }

    public void setWebsite_indexunit(website_IndexUnit website_indexunit) {
        this.website_indexunit = website_indexunit;
    }

}