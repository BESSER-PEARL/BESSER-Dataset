





import java.util.List;
import java.util.ArrayList;

public class comicBookCollection2_Publisher  {

    private String publishersName;





    private comicBookCollection2_Book comicbookcollection2_book;




    private comicBookCollection2_ComicBookCollection comicbookcollection2_comicbookcollection;




    private List<comicBookCollection2_Book> comicbookcollection2_books;


    public comicBookCollection2_Publisher(
        String publishersName    ) {
        this.publishersName = publishersName;
        this.comicbookcollection2_books = new ArrayList<>();
    }

    public comicBookCollection2_Publisher(
        String publishersName        ArrayList<comicBookCollection2_Book> comicbookcollection2_books    ) {
        this.publishersName = publishersName;
        this.comicbookcollection2_books = comicbookcollection2_books;
    }

    public String getPublishersname() {
        return publishersName;
    }

    public void setPublishersname(String publishersName) {
        this.publishersName = publishersName;
    }

    public comicBookCollection2_Book getComicbookcollection2_book() {
        return comicbookcollection2_book;
    }

    public void setComicbookcollection2_book(comicBookCollection2_Book comicbookcollection2_book) {
        this.comicbookcollection2_book = comicbookcollection2_book;
    }
    public comicBookCollection2_ComicBookCollection getComicbookcollection2_comicbookcollection() {
        return comicbookcollection2_comicbookcollection;
    }

    public void setComicbookcollection2_comicbookcollection(comicBookCollection2_ComicBookCollection comicbookcollection2_comicbookcollection) {
        this.comicbookcollection2_comicbookcollection = comicbookcollection2_comicbookcollection;
    }
    public List<comicBookCollection2_Book> getComicbookcollection2_books() {
        return comicbookcollection2_books;
    }

    public void addComicbookcollection2_book(Comicbookcollection2_book comicbookcollection2_book) {
        this.comicbookcollection2_books.add(comicbookcollection2_book);
    }

}