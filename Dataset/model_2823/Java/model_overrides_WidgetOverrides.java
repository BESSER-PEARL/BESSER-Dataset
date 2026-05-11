





import java.util.List;
import java.util.ArrayList;

public class model_overrides_WidgetOverrides extends overrides_WidgetContainerOverrides, overrides_Reference {

    private String text;
    private String link;
    private String src;
    private String y;
    private String width;
    private boolean noLink;
    private String height;
    private String x;
    private boolean noText;



    public model_overrides_WidgetOverrides(
        String text,        String link,        String src,        String y,        String width,        boolean noLink,        String height,        String x,        boolean noText    ) {
        super(
        );
        this.text = text;
        this.link = link;
        this.src = src;
        this.y = y;
        this.width = width;
        this.noLink = noLink;
        this.height = height;
        this.x = x;
        this.noText = noText;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
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
    public boolean getNolink() {
        return noLink;
    }

    public void setNolink(boolean noLink) {
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
    public boolean getNotext() {
        return noText;
    }

    public void setNotext(boolean noText) {
        this.noText = noText;
    }


}