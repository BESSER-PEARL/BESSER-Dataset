





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Book extends CirculatingItem {

    private String title;
    private int pages;
    private String category;





    private extlibrary_Writer extlibrary_writer;




    private extlibrary_Writer extlibrary_writer;


    public extlibrary_Book(
        String title,        int pages,        String category    ) {
        super(
        );
        this.title = title;
        this.pages = pages;
        this.category = category;
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
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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