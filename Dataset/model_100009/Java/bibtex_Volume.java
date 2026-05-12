





import java.util.List;
import java.util.ArrayList;

public class bibtex_Volume  {

    private String volume;





    private bibtex_Article bibtex_article;




    private bibtex_Inbook bibtex_inbook;




    private bibtex_Book bibtex_book;


    public bibtex_Volume(
        String volume    ) {
        this.volume = volume;
    }


    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }

    public bibtex_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibtex_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }
    public bibtex_Inbook getBibtex_inbook() {
        return bibtex_inbook;
    }

    public void setBibtex_inbook(bibtex_Inbook bibtex_inbook) {
        this.bibtex_inbook = bibtex_inbook;
    }
    public bibtex_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibtex_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }

}