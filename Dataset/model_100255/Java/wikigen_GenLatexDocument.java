





import java.util.List;
import java.util.ArrayList;

public class wikigen_GenLatexDocument  {

    private String authors;
    private String filename;
    private String title;





    private List<wikigen_Container> wikigen_containers;


    public wikigen_GenLatexDocument(
        String authors,        String filename,        String title    ) {
        this.authors = authors;
        this.filename = filename;
        this.title = title;
        this.wikigen_containers = new ArrayList<>();
    }

    public wikigen_GenLatexDocument(
        String authors,        String filename,        String title        ArrayList<wikigen_Container> wikigen_containers    ) {
        this.authors = authors;
        this.filename = filename;
        this.title = title;
        this.wikigen_containers = wikigen_containers;
    }

    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<wikigen_Container> getWikigen_containers() {
        return wikigen_containers;
    }

    public void addWikigen_container(Wikigen_container wikigen_container) {
        this.wikigen_containers.add(wikigen_container);
    }

}