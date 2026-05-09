





import java.util.List;
import java.util.ArrayList;

public class doc_book_BookSection extends BookContainer {

    private String title;
    private int number;
    private String id;
    private String fullNumber;



    public doc_book_BookSection(
        String title,        int number,        String id,        String fullNumber    ) {
        super(
        );
        this.title = title;
        this.number = number;
        this.id = id;
        this.fullNumber = fullNumber;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFullnumber() {
        return fullNumber;
    }

    public void setFullnumber(String fullNumber) {
        this.fullNumber = fullNumber;
    }


}