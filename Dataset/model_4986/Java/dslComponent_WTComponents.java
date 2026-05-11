





import java.util.List;
import java.util.ArrayList;

public class dslComponent_WTComponents  {

    private String author;
    private String id;



    public dslComponent_WTComponents(
        String author,        String id    ) {
        this.author = author;
        this.id = id;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}