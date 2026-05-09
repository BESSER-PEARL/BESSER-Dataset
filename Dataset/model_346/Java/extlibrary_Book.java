





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Book extends CirculatingItem {

    private String title;
    private String category;
    private int pages;





    private extlibrary_Writer extlibrary_writer;




    private extlibrary_Writer extlibrary_writer;


    public extlibrary_Book(
        String title,        String category,        int pages    ) {
        super(
        );
        this.title = title;
        this.category = category;
        this.pages = pages;
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

    public extlibrary_Writer getExtlibrary_writer() {
        return extlibrary_writer;
    }

    public void setExtlibrary_writer(extlibrary_Writer extlibrary_writer) {
        this.extlibrary_writer = extlibrary_writer;
    }
    public extlibrary_Writer getExtlibrary_writer() {
        return extlibrary_writer;
    }

    public void setExtlibrary_writer(extlibrary_Writer extlibrary_writer) {
        this.extlibrary_writer = extlibrary_writer;
    }

}