





import java.util.List;
import java.util.ArrayList;

public class model_Movie  {

    private int id;
    private String title;



    public model_Movie(
        int id,        String title    ) {
        this.id = id;
        this.title = title;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}