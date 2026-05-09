





import java.util.List;
import java.util.ArrayList;

public class comicBookCollection2_Artist  {

    private String name;





    private List<comicBookCollection2_Book> comicbookcollection2_books;




    private comicBookCollection2_Book comicbookcollection2_book;




    private List<comicBookCollection2_Book> comicbookcollection2_books;




    private comicBookCollection2_Book comicbookcollection2_book;




    private comicBookCollection2_ComicBookCollection comicbookcollection2_comicbookcollection;


    public comicBookCollection2_Artist(
        String name    ) {
        this.name = name;
        this.comicbookcollection2_books = new ArrayList<>();
        this.comicbookcollection2_books = new ArrayList<>();
    }

    public comicBookCollection2_Artist(
        String name        ArrayList<comicBookCollection2_Book> comicbookcollection2_books,        ArrayList<comicBookCollection2_Book> comicbookcollection2_books    ) {
        this.name = name;
        this.comicbookcollection2_books = comicbookcollection2_books;
        this.comicbookcollection2_books = comicbookcollection2_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<comicBookCollection2_Book> getComicbookcollection2_books() {
        return comicbookcollection2_books;
    }

    public void addComicbookcollection2_book(Comicbookcollection2_book comicbookcollection2_book) {
        this.comicbookcollection2_books.add(comicbookcollection2_book);
    }
    public comicBookCollection2_Book getComicbookcollection2_book() {
        return comicbookcollection2_book;
    }

    public void setComicbookcollection2_book(comicBookCollection2_Book comicbookcollection2_book) {
        this.comicbookcollection2_book = comicbookcollection2_book;
    }
    public List<comicBookCollection2_Book> getComicbookcollection2_books() {
        return comicbookcollection2_books;
    }

    public void addComicbookcollection2_book(Comicbookcollection2_book comicbookcollection2_book) {
        this.comicbookcollection2_books.add(comicbookcollection2_book);
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

}