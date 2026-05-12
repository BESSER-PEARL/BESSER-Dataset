





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_InBook extends Book {

    private String type;
    private String chapter;



    public BIBTEXML_InBook(
        String type,        String chapter    ) {
        super(
        );
        this.type = type;
        this.chapter = chapter;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }


}