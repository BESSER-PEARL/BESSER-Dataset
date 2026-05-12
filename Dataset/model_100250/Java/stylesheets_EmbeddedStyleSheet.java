





import java.util.List;
import java.util.ArrayList;

public class stylesheets_EmbeddedStyleSheet extends StyleSheet {

    private String label;
    private String content;



    public stylesheets_EmbeddedStyleSheet(
        String label,        String content    ) {
        super(
        );
        this.label = label;
        this.content = content;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}