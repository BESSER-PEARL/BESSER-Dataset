





import java.util.List;
import java.util.ArrayList;

public class library_t_library  {

    private String tagName;
    private String text;



    public library_t_library(
        String tagName,        String text    ) {
        this.tagName = tagName;
        this.text = text;
    }


    public String getTagname() {
        return tagName;
    }

    public void setTagname(String tagName) {
        this.tagName = tagName;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}