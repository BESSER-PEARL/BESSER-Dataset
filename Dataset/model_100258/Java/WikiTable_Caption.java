





import java.util.List;
import java.util.ArrayList;

public class WikiTable_Caption extends LocatedElement {

    private String content;



    public WikiTable_Caption(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}