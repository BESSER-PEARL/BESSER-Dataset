





import java.util.List;
import java.util.ArrayList;

public class website_ImageIndexUnit extends ImageUnit, InlineActionContainer {

    private String contentClass;
    private String styleClass;



    public website_ImageIndexUnit(
        String contentClass,        String styleClass    ) {
        super(
        );
        this.contentClass = contentClass;
        this.styleClass = styleClass;
    }


    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }
    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }


}