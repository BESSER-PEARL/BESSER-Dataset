





import java.util.List;
import java.util.ArrayList;

public class bibtex_Series  {

    private String series;





    private bibtex_Inbook bibtex_inbook;




    private bibtex_Book bibtex_book;




    private bibtex_Inproceedings bibtex_inproceedings;


    public bibtex_Series(
        String series    ) {
        this.series = series;
    }


    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
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
    public bibtex_Inproceedings getBibtex_inproceedings() {
        return bibtex_inproceedings;
    }

    public void setBibtex_inproceedings(bibtex_Inproceedings bibtex_inproceedings) {
        this.bibtex_inproceedings = bibtex_inproceedings;
    }

}