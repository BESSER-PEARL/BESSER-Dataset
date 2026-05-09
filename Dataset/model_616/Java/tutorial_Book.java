





import java.util.List;
import java.util.ArrayList;

public class tutorial_Book  {

    private String copies;
    private String name;



    public tutorial_Book(
        String copies,        String name    ) {
        this.copies = copies;
        this.name = name;
    }


    public String getCopies() {
        return copies;
    }

    public void setCopies(String copies) {
        this.copies = copies;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}