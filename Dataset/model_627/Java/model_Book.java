





import java.util.List;
import java.util.ArrayList;

public class model_Book  {

    private int pages;
    private String title;





    private model_Writer model_writer;




    private model_Writer model_writer;




    private model_Library model_library;


    public model_Book(
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

    public model_Writer getModel_writer() {
        return model_writer;
    }

    public void setModel_writer(model_Writer model_writer) {
        this.model_writer = model_writer;
    }
    public model_Writer getModel_writer() {
        return model_writer;
    }

    public void setModel_writer(model_Writer model_writer) {
        this.model_writer = model_writer;
    }
    public model_Library getModel_library() {
        return model_library;
    }

    public void setModel_library(model_Library model_library) {
        this.model_library = model_library;
    }

}