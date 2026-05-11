





import java.util.List;
import java.util.ArrayList;

public class html_Section  {

    private String title;
    private int id;





    private html_View html_view;


    public html_Section(
        String title,        int id    ) {
        this.title = title;
        this.id = id;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public html_View getHtml_view() {
        return html_view;
    }

    public void setHtml_view(html_View html_view) {
        this.html_view = html_view;
    }

}