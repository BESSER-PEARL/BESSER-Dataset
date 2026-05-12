





import java.util.List;
import java.util.ArrayList;

public class HTML_Website  {






    private List<HTML> htmls;


    public HTML_Website(
    ) {
        this.htmls = new ArrayList<>();
    }

    public HTML_Website(
        ArrayList<HTML> htmls    ) {
        this.htmls = htmls;
    }


    public List<HTML> getHtmls() {
        return htmls;
    }

    public void addHtml(Html html) {
        this.htmls.add(html);
    }

}