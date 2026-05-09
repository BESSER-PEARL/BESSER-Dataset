





import java.util.List;
import java.util.ArrayList;

public class comicBookCollection2_Series  {

    private String seriesName;





    private comicBookCollection2_Book comicbookcollection2_book;




    private List<comicBookCollection2_Book> comicbookcollection2_books;




    private comicBookCollection2_ComicBookCollection comicbookcollection2_comicbookcollection;


    public comicBookCollection2_Series(
        String seriesName    ) {
        this.seriesName = seriesName;
        this.comicbookcollection2_books = new ArrayList<>();
    }

    public comicBookCollection2_Series(
        String seriesName        ArrayList<comicBookCollection2_Book> comicbookcollection2_books    ) {
        this.seriesName = seriesName;
        this.comicbookcollection2_books = comicbookcollection2_books;
    }

    public String getSeriesname() {
        return seriesName;
    }

    public void setSeriesname(String seriesName) {
        this.seriesName = seriesName;
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
    public comicBookCollection2_ComicBookCollection getComicbookcollection2_comicbookcollection() {
        return comicbookcollection2_comicbookcollection;
    }

    public void setComicbookcollection2_comicbookcollection(comicBookCollection2_ComicBookCollection comicbookcollection2_comicbookcollection) {
        this.comicbookcollection2_comicbookcollection = comicbookcollection2_comicbookcollection;
    }

}