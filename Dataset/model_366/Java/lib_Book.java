





import java.util.List;
import java.util.ArrayList;

public class lib_Book  {

    private int pages;
    private String title;
    private String category;





    private lib_Writer lib_writer;




    private lib_Library lib_library;


    public lib_Book(
        int pages,        String title,        String category    ) {
        this.pages = pages;
        this.title = title;
        this.category = category;
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
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public lib_Writer getLib_writer() {
        return lib_writer;
    }

    public void setLib_writer(lib_Writer lib_writer) {
        this.lib_writer = lib_writer;
    }
    public lib_Library getLib_library() {
        return lib_library;
    }

    public void setLib_library(lib_Library lib_library) {
        this.lib_library = lib_library;
    }

}