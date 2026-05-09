





import java.util.List;
import java.util.ArrayList;

public class extralazy_Book  {

    private String subTitles;
    private String title;



    public extralazy_Book(
        String subTitles,        String title    ) {
        this.subTitles = subTitles;
        this.title = title;
    }


    public String getSubtitles() {
        return subTitles;
    }

    public void setSubtitles(String subTitles) {
        this.subTitles = subTitles;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}