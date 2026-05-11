





import java.util.List;
import java.util.ArrayList;

public class article_Snippet extends EmbeddableElement {

    private String titleImage;
    private String title;



    public article_Snippet(
        String titleImage,        String title    ) {
        super(
        );
        this.titleImage = titleImage;
        this.title = title;
    }


    public String getTitleimage() {
        return titleImage;
    }

    public void setTitleimage(String titleImage) {
        this.titleImage = titleImage;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}