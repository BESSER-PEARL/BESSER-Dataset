





import java.util.List;
import java.util.ArrayList;

public class dsml_web_Page  {

    private String name;
    private String title;



    public dsml_web_Page(
        String name,        String title    ) {
        this.name = name;
        this.title = title;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}