





import java.util.List;
import java.util.ArrayList;

public class emftest_Book  {

    private int pages;
    private String title;





    private emftest_BookCollection emftest_bookcollection;


    public emftest_Book(
        int pages,        String title    ) {
        this.pages = pages;
        this.title = title;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public emftest_BookCollection getEmftest_bookcollection() {
        return emftest_bookcollection;
    }

    public void setEmftest_bookcollection(emftest_BookCollection emftest_bookcollection) {
        this.emftest_bookcollection = emftest_bookcollection;
    }

}