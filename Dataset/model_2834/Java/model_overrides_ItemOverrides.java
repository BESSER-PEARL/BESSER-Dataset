





import java.util.List;
import java.util.ArrayList;

public class model_overrides_ItemOverrides extends Reference {

    private String link;
    private String text;
    private boolean noLink;



    public model_overrides_ItemOverrides(
        String link,        String text,        boolean noLink    ) {
        super(
        );
        this.link = link;
        this.text = text;
        this.noLink = noLink;
    }


    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
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