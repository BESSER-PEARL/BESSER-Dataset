





import java.util.List;
import java.util.ArrayList;

public class simpleany_BookType  {

    private String name;
    private String author;
    private String title;



    public simpleany_BookType(
        String name,        String author,        String title    ) {
        this.name = name;
        this.author = author;
        this.title = title;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}