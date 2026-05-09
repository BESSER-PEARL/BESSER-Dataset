





import java.util.List;
import java.util.ArrayList;

public class libsys_Book extends Medium {

    private String publisher;
    private String ISBN;
    private String placeOfPublication;
    private String editor;



    public libsys_Book(
        String publisher,        String ISBN,        String placeOfPublication,        String editor    ) {
        super(
        );
        this.publisher = publisher;
        this.ISBN = ISBN;
        this.placeOfPublication = placeOfPublication;
        this.editor = editor;
    }


    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getIsbn() {
        return ISBN;
    }

    public void setIsbn(String ISBN) {
        this.ISBN = ISBN;
    }
    public String getPlaceofpublication() {
        return placeOfPublication;
    }

    public void setPlaceofpublication(String placeOfPublication) {
        this.placeOfPublication = placeOfPublication;
    }
    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }


}