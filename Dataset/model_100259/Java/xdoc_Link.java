





import java.util.List;
import java.util.ArrayList;

public class xdoc_Link extends MarkUp {

    private String url;
    private String text;



    public xdoc_Link(
        String url,        String text    ) {
        super(
        );
        this.url = url;
        this.text = text;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}