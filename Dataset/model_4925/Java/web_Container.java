





import java.util.List;
import java.util.ArrayList;

public class web_Container  {






    private List<web_Content> web_contents;


    public web_Container(
    ) {
        this.web_contents = new ArrayList<>();
    }

    public web_Container(
        ArrayList<web_Content> web_contents    ) {
        this.web_contents = web_contents;
    }


    public List<web_Content> getWeb_contents() {
        return web_contents;
    }

    public void addWeb_content(Web_content web_content) {
        this.web_contents.add(web_content);
    }

}