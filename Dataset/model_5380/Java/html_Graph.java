





import java.util.List;
import java.util.ArrayList;

public class html_Graph  {

    private String type;
    private String title;





    private html_View html_view;


    public html_Graph(
        String type,        String title    ) {
        this.type = type;
        this.title = title;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public html_View getHtml_view() {
        return html_view;
    }

    public void setHtml_view(html_View html_view) {
        this.html_view = html_view;
    }

}