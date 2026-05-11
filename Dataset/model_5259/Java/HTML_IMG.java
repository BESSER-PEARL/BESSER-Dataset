





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends HTMLElement {

    private String width;
    private String border;
    private String height;
    private String src;



    public HTML_IMG(
        String width,        String border,        String height,        String src    ) {
        super(
        );
        this.width = width;
        this.border = border;
        this.height = height;
        this.src = src;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}