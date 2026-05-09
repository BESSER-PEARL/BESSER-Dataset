





import java.util.List;
import java.util.ArrayList;

public class Book_Summary  {

    private int nbWords;
    private String content;





    private Book_Chapter book_chapter;


    public Book_Summary(
        int nbWords,        String content    ) {
        this.nbWords = nbWords;
        this.content = content;
    }


    public int getNbwords() {
        return nbWords;
    }

    public void setNbwords(int nbWords) {
        this.nbWords = nbWords;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public Book_Chapter getBook_chapter() {
        return book_chapter;
    }

    public void setBook_chapter(Book_Chapter book_chapter) {
        this.book_chapter = book_chapter;
    }

}