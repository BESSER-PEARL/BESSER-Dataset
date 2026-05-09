





import java.util.List;
import java.util.ArrayList;

public class libraryModel_Book  {

    private String title;
    private int pages;
    private String category;





    private libraryModel_Library librarymodel_library;




    private libraryModel_Writer librarymodel_writer;




    private libraryModel_Writer librarymodel_writer;


    public libraryModel_Book(
        String title,        int pages,        String category    ) {
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

    public libraryModel_Library getLibrarymodel_library() {
        return librarymodel_library;
    }

    public void setLibrarymodel_library(libraryModel_Library librarymodel_library) {
        this.librarymodel_library = librarymodel_library;
    }
    public libraryModel_Writer getLibrarymodel_writer() {
        return librarymodel_writer;
    }

    public void setLibrarymodel_writer(libraryModel_Writer librarymodel_writer) {
        this.librarymodel_writer = librarymodel_writer;
    }
    public libraryModel_Writer getLibrarymodel_writer() {
        return librarymodel_writer;
    }

    public void setLibrarymodel_writer(libraryModel_Writer librarymodel_writer) {
        this.librarymodel_writer = librarymodel_writer;
    }

}