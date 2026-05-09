





import java.util.List;
import java.util.ArrayList;

public class eavlibrary_Writer  {

    private String name;
    private String image;
    private String abstract;





    private eavlibrary_Library eavlibrary_library;




    private List<eavlibrary_Book> eavlibrary_books;




    private eavlibrary_Book eavlibrary_book;




    private eavlibrary_City eavlibrary_city;


    public eavlibrary_Writer(
        String name,        String image,        String abstract    ) {
        this.name = name;
        this.image = image;
        this.abstract = abstract;
        this.eavlibrary_books = new ArrayList<>();
    }

    public eavlibrary_Writer(
        String name,        String image,        String abstract        ArrayList<eavlibrary_Book> eavlibrary_books    ) {
        this.name = name;
        this.image = image;
        this.abstract = abstract;
        this.eavlibrary_books = eavlibrary_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }

    public eavlibrary_Library getEavlibrary_library() {
        return eavlibrary_library;
    }

    public void setEavlibrary_library(eavlibrary_Library eavlibrary_library) {
        this.eavlibrary_library = eavlibrary_library;
    }
    public List<eavlibrary_Book> getEavlibrary_books() {
        return eavlibrary_books;
    }

    public void addEavlibrary_book(Eavlibrary_book eavlibrary_book) {
        this.eavlibrary_books.add(eavlibrary_book);
    }
    public eavlibrary_Book getEavlibrary_book() {
        return eavlibrary_book;
    }

    public void setEavlibrary_book(eavlibrary_Book eavlibrary_book) {
        this.eavlibrary_book = eavlibrary_book;
    }
    public eavlibrary_City getEavlibrary_city() {
        return eavlibrary_city;
    }

    public void setEavlibrary_city(eavlibrary_City eavlibrary_city) {
        this.eavlibrary_city = eavlibrary_city;
    }

}