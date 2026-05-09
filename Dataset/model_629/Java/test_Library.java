





import java.util.List;
import java.util.ArrayList;

public class test_Library  {

    private String name;





    private List<test_Writer> test_writers;




    private List<test_Book> test_books;




    private test_Writer test_writer;


    public test_Library(
        String name    ) {
        this.name = name;
        this.test_writers = new ArrayList<>();
        this.test_books = new ArrayList<>();
    }

    public test_Library(
        String name        ArrayList<test_Writer> test_writers,        ArrayList<test_Book> test_books    ) {
        this.name = name;
        this.test_writers = test_writers;
        this.test_books = test_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<test_Writer> getTest_writers() {
        return test_writers;
    }

    public void addTest_writer(Test_writer test_writer) {
        this.test_writers.add(test_writer);
    }
    public List<test_Book> getTest_books() {
        return test_books;
    }

    public void addTest_book(Test_book test_book) {
        this.test_books.add(test_book);
    }
    public test_Writer getTest_writer() {
        return test_writer;
    }

    public void setTest_writer(test_Writer test_writer) {
        this.test_writer = test_writer;
    }

}