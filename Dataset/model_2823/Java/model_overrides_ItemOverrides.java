





import java.util.List;
import java.util.ArrayList;

public class model_overrides_ItemOverrides extends Reference {

    private boolean noLink;
    private String link;
    private String text;



    public model_overrides_ItemOverrides(
        boolean noLink,        String link,        String text    ) {
        super(
        );
        this.noLink = noLink;
        this.link = link;
        this.text = text;
    }


    public boolean getNolink() {
        return noLink;
    }

    public void setNolink(boolean noLink) {
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


}