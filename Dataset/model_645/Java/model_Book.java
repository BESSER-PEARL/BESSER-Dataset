





import java.util.List;
import java.util.ArrayList;

public class model_Book  {

    private String author;
    private int avgRating;
    private String name;



    public model_Book(
        String author,        int avgRating,        String name    ) {
        this.author = author;
        this.avgRating = avgRating;
        this.name = name;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public int getAvgrating() {
        return avgRating;
    }

    public void setAvgrating(int avgRating) {
        this.avgRating = avgRating;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}