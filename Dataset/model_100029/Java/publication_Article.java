





import java.util.List;
import java.util.ArrayList;

public class publication_Article extends BiblioReference {

    private String lastPage;
    private String firstPage;



    public publication_Article(
        String lastPage,        String firstPage    ) {
        super(
        );
        this.lastPage = lastPage;
        this.firstPage = firstPage;
    }


    public String getLastpage() {
        return lastPage;
    }

    public void setLastpage(String lastPage) {
        this.lastPage = lastPage;
    }
    public String getFirstpage() {
        return firstPage;
    }

    public void setFirstpage(String firstPage) {
        this.firstPage = firstPage;
    }


}