





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Library extends Addressable {

    private String name;
    private String people;





    private List<extlibrary_Book> extlibrary_books;




    private List<extlibrary_Writer> extlibrary_writers;




    private List<extlibrary_Library> extlibrary_librarys;




    private extlibrary_Library extlibrary_library;


    public extlibrary_Library(
        String name,        String people    ) {
        super(
        );
        this.name = name;
        this.people = people;
        this.extlibrary_books = new ArrayList<>();
        this.extlibrary_writers = new ArrayList<>();
        this.extlibrary_librarys = new ArrayList<>();
    }

    public extlibrary_Library(
        String name,        String people        ArrayList<extlibrary_Book> extlibrary_books,        ArrayList<extlibrary_Writer> extlibrary_writers,        ArrayList<extlibrary_Library> extlibrary_librarys    ) {
        this.name = name;
        this.people = people;
        this.extlibrary_books = extlibrary_books;
        this.extlibrary_writers = extlibrary_writers;
        this.extlibrary_librarys = extlibrary_librarys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPeople() {
        return people;
    }

    public void setPeople(String people) {
        this.people = people;
    }

    public List<extlibrary_Book> getExtlibrary_books() {
        return extlibrary_books;
    }

    public void addExtlibrary_book(Extlibrary_book extlibrary_book) {
        this.extlibrary_books.add(extlibrary_book);
    }
    public List<extlibrary_Writer> getExtlibrary_writers() {
        return extlibrary_writers;
    }

    public void addExtlibrary_writer(Extlibrary_writer extlibrary_writer) {
        this.extlibrary_writers.add(extlibrary_writer);
    }
    public List<extlibrary_Library> getExtlibrary_librarys() {
        return extlibrary_librarys;
    }

    public void addExtlibrary_library(Extlibrary_library extlibrary_library) {
        this.extlibrary_librarys.add(extlibrary_library);
    }
    public extlibrary_Library getExtlibrary_library() {
        return extlibrary_library;
    }

    public void setExtlibrary_library(extlibrary_Library extlibrary_library) {
        this.extlibrary_library = extlibrary_library;
    }

}