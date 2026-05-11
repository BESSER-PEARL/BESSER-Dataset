





import java.util.List;
import java.util.ArrayList;

public class model_overrides_WidgetOverrides extends overrides_Reference, overrides_WidgetContainerOverrides {

    private String height;
    private String src;
    private String width;
    private String text;
    private String y;
    private String link;
    private boolean noText;
    private String x;
    private boolean noLink;



    public model_overrides_WidgetOverrides(
        String height,        String src,        String width,        String text,        String y,        String link,        boolean noText,        String x,        boolean noLink    ) {
        super(
        );
        this.height = height;
        this.src = src;
        this.width = width;
        this.text = text;
        this.y = y;
        this.link = link;
        this.noText = noText;
        this.x = x;
        this.noLink = noLink;
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
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public boolean getNolink() {
        return noLink;
    }

    public void setNolink(boolean noLink) {
        this.noLink = noLink;
    }


}