





import java.util.List;
import java.util.ArrayList;

public class bibTeX_InBook extends Book {

    private String chapter;



    public bibTeX_InBook(
        String chapter    ) {
        super(
        );
        this.chapter = chapter;
    }


    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }


}