





import java.util.List;
import java.util.ArrayList;

public class Sample_Library  {

    private String name;





    private List<Sample_Book> sample_books;


    public Sample_Library(
        String name    ) {
        this.name = name;
        this.sample_books = new ArrayList<>();
    }

    public Sample_Library(
        String name        ArrayList<Sample_Book> sample_books    ) {
        this.name = name;
        this.sample_books = sample_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Sample_Book> getSample_books() {
        return sample_books;
    }

    public void addSample_book(Sample_book sample_book) {
        this.sample_books.add(sample_book);
    }

}