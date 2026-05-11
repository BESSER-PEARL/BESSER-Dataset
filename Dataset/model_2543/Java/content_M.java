





import java.util.List;
import java.util.ArrayList;

public class content_M  {






    private List<content_A> content_as;


    public content_M(
    ) {
        this.content_as = new ArrayList<>();
    }

    public content_M(
        ArrayList<content_A> content_as    ) {
        this.content_as = content_as;
    }


    public List<content_A> getContent_as() {
        return content_as;
    }

    public void addContent_a(Content_a content_a) {
        this.content_as.add(content_a);
    }

}