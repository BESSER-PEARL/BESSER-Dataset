





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends HTMLElement {

    private String src;
    private String border;
    private String height;
    private String width;



    public HTML_IMG(
        String src,        String border,        String height,        String width    ) {
        super(
        );
        this.src = src;
        this.border = border;
        this.height = height;
        this.width = width;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}