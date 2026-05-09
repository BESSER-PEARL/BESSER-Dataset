





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String title;
    private String category;
    private int pages;





    private List<library__cPfTBB9KEeeOINGRvT6ccg> library__cpftbb9keeeoingrvt6ccgs;


    public library_Book(
        String title,        String category,        int pages    ) {
        this.title = title;
        this.category = category;
        this.pages = pages;
        this.library__cpftbb9keeeoingrvt6ccgs = new ArrayList<>();
    }

    public library_Book(
        String title,        String category,        int pages        ArrayList<library__cPfTBB9KEeeOINGRvT6ccg> library__cpftbb9keeeoingrvt6ccgs    ) {
        this.title = title;
        this.category = category;
        this.pages = pages;
        this.library__cpftbb9keeeoingrvt6ccgs = library__cpftbb9keeeoingrvt6ccgs;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }

    public List<library__cPfTBB9KEeeOINGRvT6ccg> getLibrary__cpftbb9keeeoingrvt6ccgs() {
        return library__cpftbb9keeeoingrvt6ccgs;
    }

    public void addLibrary__cpftbb9keeeoingrvt6ccg(Library__cpftbb9keeeoingrvt6ccg library__cpftbb9keeeoingrvt6ccg) {
        this.library__cpftbb9keeeoingrvt6ccgs.add(library__cpftbb9keeeoingrvt6ccg);
    }

}