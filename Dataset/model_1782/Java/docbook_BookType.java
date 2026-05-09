





import java.util.List;
import java.util.ArrayList;

public class docbook_BookType  {

    private String title;
    private String info;



    public docbook_BookType(
        String title,        String info    ) {
        this.title = title;
        this.info = info;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }


}