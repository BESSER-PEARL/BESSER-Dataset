





import java.util.List;
import java.util.ArrayList;

public class website_StaticUnit extends ContentUnit {

    private String content;
    private String contentClass;
    private String styleClass;



    public website_StaticUnit(
        String content,        String contentClass,        String styleClass    ) {
        super(
        );
        this.content = content;
        this.contentClass = contentClass;
        this.styleClass = styleClass;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
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