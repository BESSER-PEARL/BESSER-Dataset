





import java.util.List;
import java.util.ArrayList;

public class website_SliderUnit extends ImageUnit {

    private String styleClass;
    private String contentClass;



    public website_SliderUnit(
        String styleClass,        String contentClass    ) {
        super(
        );
        this.styleClass = styleClass;
        this.contentClass = contentClass;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }


}