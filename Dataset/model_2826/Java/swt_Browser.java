





import java.util.List;
import java.util.ArrayList;

public class swt_Browser extends Control {

    private boolean javascriptEnabled;
    private String text;
    private String url;



    public swt_Browser(
        boolean javascriptEnabled,        String text,        String url    ) {
        super(
        );
        this.javascriptEnabled = javascriptEnabled;
        this.text = text;
        this.url = url;
    }


    public boolean getJavascriptenabled() {
        return javascriptEnabled;
    }

    public void setJavascriptenabled(boolean javascriptEnabled) {
        this.javascriptEnabled = javascriptEnabled;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}