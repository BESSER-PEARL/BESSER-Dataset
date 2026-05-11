





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends HTMLElement {

    private String height;
    private String border;
    private String width;
    private String src;



    public HTML_IMG(
        String height,        String border,        String width,        String src    ) {
        super(
        );
        this.height = height;
        this.border = border;
        this.width = width;
        this.src = src;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}