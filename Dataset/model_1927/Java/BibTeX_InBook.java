





import java.util.List;
import java.util.ArrayList;

public class BibTeX_InBook extends Book {

    private int chapter;



    public BibTeX_InBook(
        int chapter    ) {
        super(
        );
        this.chapter = chapter;
    }


    public int getChapter() {
        return chapter;
    }

    public void setChapter(int chapter) {
        this.chapter = chapter;
    }


}