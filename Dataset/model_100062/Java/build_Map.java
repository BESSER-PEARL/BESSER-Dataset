





import java.util.List;
import java.util.ArrayList;

public class build_Map  {

    private String repo;
    private String root;
    private String tag;



    public build_Map(
        String repo,        String root,        String tag    ) {
        this.repo = repo;
        this.root = root;
        this.tag = tag;
    }


    public String getRepo() {
        return repo;
    }

    public void setRepo(String repo) {
        this.repo = repo;
    }
    public String getRoot() {
        return root;
    }

    public void setRoot(String root) {
        this.root = root;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }


}