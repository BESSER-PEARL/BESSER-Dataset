





import java.util.List;
import java.util.ArrayList;

public class Paper_Paper  {

    private String title;





    private Paper_Papers paper_papers;




    private List<Paper_Author> paper_authors;


    public Paper_Paper(
        String title    ) {
        this.title = title;
        this.paper_authors = new ArrayList<>();
    }

    public Paper_Paper(
        String title        ArrayList<Paper_Author> paper_authors    ) {
        this.title = title;
        this.paper_authors = paper_authors;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Paper_Papers getPaper_papers() {
        return paper_papers;
    }

    public void setPaper_papers(Paper_Papers paper_papers) {
        this.paper_papers = paper_papers;
    }
    public List<Paper_Author> getPaper_authors() {
        return paper_authors;
    }

    public void addPaper_author(Paper_author paper_author) {
        this.paper_authors.add(paper_author);
    }

}