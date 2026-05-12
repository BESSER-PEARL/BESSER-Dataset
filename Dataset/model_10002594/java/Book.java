





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private String publisher;
    private String publisherCity;
    private int yearPublished;
    private String title;
    private String Author;





    private Library library;


    public Book(
        String publisher,        String publisherCity,        int yearPublished,        String title,        String Author    ) {
        this.publisher = publisher;
        this.publisherCity = publisherCity;
        this.yearPublished = yearPublished;
        this.title = title;
        this.Author = Author;
    }


    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getPublishercity() {
        return publisherCity;
    }

    public void setPublishercity(String publisherCity) {
        this.publisherCity = publisherCity;
    }
    public int getYearpublished() {
        return yearPublished;
    }

    public void setYearpublished(int yearPublished) {
        this.yearPublished = yearPublished;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return Author;
    }

    public void setAuthor(String Author) {
        this.Author = Author;
    }

    public Library getLibrary() {
        return library;
    }

    public void setLibrary(Library library) {
        this.library = library;
    }

}