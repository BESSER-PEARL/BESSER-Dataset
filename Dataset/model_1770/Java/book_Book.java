





import java.util.List;
import java.util.ArrayList;

public class book_Book  {

    private String title;





    private book_DocBook book_docbook;




    private book_Person book_person;




    private book_Person book_person;




    private List<book_Person> book_persons;




    private book_Article book_article;




    private List<book_Article> book_articles;




    private book_DocBook book_docbook;




    private List<book_Person> book_persons;


    public book_Book(
        String title    ) {
        this.title = title;
        this.book_persons = new ArrayList<>();
        this.book_articles = new ArrayList<>();
        this.book_persons = new ArrayList<>();
    }

    public book_Book(
        String title        ArrayList<book_Person> book_persons,        ArrayList<book_Article> book_articles,        ArrayList<book_Person> book_persons    ) {
        this.title = title;
        this.book_persons = book_persons;
        this.book_articles = book_articles;
        this.book_persons = book_persons;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public book_DocBook getBook_docbook() {
        return book_docbook;
    }

    public void setBook_docbook(book_DocBook book_docbook) {
        this.book_docbook = book_docbook;
    }
    public book_Person getBook_person() {
        return book_person;
    }

    public void setBook_person(book_Person book_person) {
        this.book_person = book_person;
    }
    public book_Person getBook_person() {
        return book_person;
    }

    public void setBook_person(book_Person book_person) {
        this.book_person = book_person;
    }
    public List<book_Person> getBook_persons() {
        return book_persons;
    }

    public void addBook_person(Book_person book_person) {
        this.book_persons.add(book_person);
    }
    public book_Article getBook_article() {
        return book_article;
    }

    public void setBook_article(book_Article book_article) {
        this.book_article = book_article;
    }
    public List<book_Article> getBook_articles() {
        return book_articles;
    }

    public void addBook_article(Book_article book_article) {
        this.book_articles.add(book_article);
    }
    public book_DocBook getBook_docbook() {
        return book_docbook;
    }

    public void setBook_docbook(book_DocBook book_docbook) {
        this.book_docbook = book_docbook;
    }
    public List<book_Person> getBook_persons() {
        return book_persons;
    }

    public void addBook_person(Book_person book_person) {
        this.book_persons.add(book_person);
    }

}