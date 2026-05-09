





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Library extends Addressable {

    private String name;





    private extlibrary_Library extlibrary_library;




    private List<extlibrary_Book> extlibrary_books;




    private extlibrary_Library extlibrary_library;




    private List<extlibrary_Writer> extlibrary_writers;


    public extlibrary_Library(
        String name    ) {
        super(
        );
        this.name = name;
        this.extlibrary_books = new ArrayList<>();
        this.extlibrary_writers = new ArrayList<>();
    }

    public extlibrary_Library(
        String name        ArrayList<extlibrary_Book> extlibrary_books,        ArrayList<extlibrary_Writer> extlibrary_writers    ) {
        this.name = name;
        this.extlibrary_books = extlibrary_books;
        this.extlibrary_writers = extlibrary_writers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public extlibrary_Library getExtlibrary_library() {
        return extlibrary_library;
    }

    public void setExtlibrary_library(extlibrary_Library extlibrary_library) {
        this.extlibrary_library = extlibrary_library;
    }
    public List<extlibrary_Book> getExtlibrary_books() {
        return extlibrary_books;
    }

    public void addExtlibrary_book(Extlibrary_book extlibrary_book) {
        this.extlibrary_books.add(extlibrary_book);
    }
    public extlibrary_Library getExtlibrary_library() {
        return extlibrary_library;
    }

    public void setExtlibrary_library(extlibrary_Library extlibrary_library) {
        this.extlibrary_library = extlibrary_library;
    }
    public List<extlibrary_Writer> getExtlibrary_writers() {
        return extlibrary_writers;
    }

    public void addExtlibrary_writer(Extlibrary_writer extlibrary_writer) {
        this.extlibrary_writers.add(extlibrary_writer);
    }

}