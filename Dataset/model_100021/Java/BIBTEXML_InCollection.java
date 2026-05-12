





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_InCollection extends Book, BookTitledEntry {

    private String chapter;
    private String type;



    public BIBTEXML_InCollection(
        String chapter,        String type    ) {
        super(
        );
        this.chapter = chapter;
        this.type = type;
    }


    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}