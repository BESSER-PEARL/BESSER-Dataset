





import java.util.List;
import java.util.ArrayList;

public class model_overrides_WidgetOverrides extends overrides_WidgetContainerOverrides, overrides_Reference {

    private String height;
    private String x;
    private String src;
    private String link;
    private boolean noText;
    private String y;
    private String width;
    private String text;
    private boolean noLink;



    public model_overrides_WidgetOverrides(
        String height,        String x,        String src,        String link,        boolean noText,        String y,        String width,        String text,        boolean noLink    ) {
        super(
        );
        this.height = height;
        this.x = x;
        this.src = src;
        this.link = link;
        this.noText = noText;
        this.y = y;
        this.width = width;
        this.text = text;
        this.noLink = noLink;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public boolean getNotext() {
        return noText;
    }

    public void setNotext(boolean noText) {
        this.noText = noText;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public boolean getNolink() {
        return noLink;
    }

    public void setNolink(boolean noLink) {
        this.noLink = noLink;
    }


}