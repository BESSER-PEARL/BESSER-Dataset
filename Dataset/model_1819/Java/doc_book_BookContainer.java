





import java.util.List;
import java.util.ArrayList;

public class doc_book_BookContainer  {

    private String numberingStyle;





    private List<Content> contents;


    public doc_book_BookContainer(
        String numberingStyle    ) {
        this.numberingStyle = numberingStyle;
        this.contents = new ArrayList<>();
    }

    public doc_book_BookContainer(
        String numberingStyle        ArrayList<Content> contents    ) {
        this.numberingStyle = numberingStyle;
        this.contents = contents;
    }

    public String getNumberingstyle() {
        return numberingStyle;
    }

    public void setNumberingstyle(String numberingStyle) {
        this.numberingStyle = numberingStyle;
    }

    public List<Content> getContents() {
        return contents;
    }

    public void addContent(Content content) {
        this.contents.add(content);
    }

}