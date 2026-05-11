





import java.util.List;
import java.util.ArrayList;

public class content_I  {






    private List<content_P> content_ps;


    public content_I(
    ) {
        this.content_ps = new ArrayList<>();
    }

    public content_I(
        ArrayList<content_P> content_ps    ) {
        this.content_ps = content_ps;
    }


    public List<content_P> getContent_ps() {
        return content_ps;
    }

    public void addContent_p(Content_p content_p) {
        this.content_ps.add(content_p);
    }

}