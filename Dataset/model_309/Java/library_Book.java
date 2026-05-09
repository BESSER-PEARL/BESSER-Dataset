





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String title;
    private boolean borrowed;
    private String category;
    private int pages;



    public library_Book(
        String title,        boolean borrowed,        String category,        int pages    ) {
        this.title = title;
        this.borrowed = borrowed;
        this.category = category;
        this.pages = pages;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getBorrowed() {
        return borrowed;
    }

    public void setBorrowed(boolean borrowed) {
        this.borrowed = borrowed;
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


}