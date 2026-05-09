





import java.util.List;
import java.util.ArrayList;

public class eavlibrary_Writer  {

    private String name;
    private String abstract;
    private String image;





    private List<eavlibrary_Book> eavlibrary_books;




    private eavlibrary_Book eavlibrary_book;


    public eavlibrary_Writer(
        String name,        String abstract,        String image    ) {
        this.name = name;
        this.abstract = abstract;
        this.image = image;
        this.eavlibrary_books = new ArrayList<>();
    }

    public eavlibrary_Writer(
        String name,        String abstract,        String image        ArrayList<eavlibrary_Book> eavlibrary_books    ) {
        this.name = name;
        this.abstract = abstract;
        this.image = image;
        this.eavlibrary_books = eavlibrary_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
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

}