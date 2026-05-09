





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_extPHP_Text extends HTMLElement {

    private String content;
    private String language;



    public PHPMVC_extPHP_Text(
        String content,        String language    ) {
        super(
        );
        this.content = content;
        this.language = language;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}