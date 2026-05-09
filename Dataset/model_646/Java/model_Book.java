





import java.util.List;
import java.util.ArrayList;

public class model_Book  {

    private String name;
    private int avgRating;
    private String author;





    private model_DataBase model_database;


    public model_Book(
        String name,        int avgRating,        String author    ) {
        this.name = name;
        this.avgRating = avgRating;
        this.author = author;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAvgrating() {
        return avgRating;
    }

    public void setAvgrating(int avgRating) {
        this.avgRating = avgRating;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public model_DataBase getModel_database() {
        return model_database;
    }

    public void setModel_database(model_DataBase model_database) {
        this.model_database = model_database;
    }

}