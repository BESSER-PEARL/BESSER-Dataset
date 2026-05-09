





import java.util.List;
import java.util.ArrayList;

public class library_IncBook extends CirculatingItem {

    private String title;
    private int pages;





    private library_Writer library_writer;




    private List<library_Writer> library_writers;


    public library_IncBook(
        String title,        int pages    ) {
        super(
        );
        this.title = title;
        this.pages = pages;
        this.library_writers = new ArrayList<>();
    }

    public library_IncBook(
        String title,        int pages        ArrayList<library_Writer> library_writers    ) {
        this.title = title;
        this.pages = pages;
        this.library_writers = library_writers;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }

    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }
    public List<library_Writer> getLibrary_writers() {
        return library_writers;
    }

    public void addLibrary_writer(Library_writer library_writer) {
        this.library_writers.add(library_writer);
    }

}