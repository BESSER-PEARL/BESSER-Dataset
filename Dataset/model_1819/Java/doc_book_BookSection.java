





import java.util.List;
import java.util.ArrayList;

public class doc_book_BookSection extends BookContainer {

    private int number;
    private String fullNumber;
    private String id;
    private String title;



    public doc_book_BookSection(
        int number,        String fullNumber,        String id,        String title    ) {
        super(
        );
        this.number = number;
        this.fullNumber = fullNumber;
        this.id = id;
        this.title = title;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getFullnumber() {
        return fullNumber;
    }

    public void setFullnumber(String fullNumber) {
        this.fullNumber = fullNumber;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}