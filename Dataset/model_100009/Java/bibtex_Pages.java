





import java.util.List;
import java.util.ArrayList;

public class bibtex_Pages  {

    private String pages;





    private bibtex_Conference bibtex_conference;




    private bibtex_Inproceedings bibtex_inproceedings;




    private bibtex_Incollection bibtex_incollection;




    private bibtex_Article bibtex_article;




    private bibtex_Inbook bibtex_inbook;


    public bibtex_Pages(
        String pages    ) {
        this.pages = pages;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }

    public bibtex_Conference getBibtex_conference() {
        return bibtex_conference;
    }

    public void setBibtex_conference(bibtex_Conference bibtex_conference) {
        this.bibtex_conference = bibtex_conference;
    }
    public bibtex_Inproceedings getBibtex_inproceedings() {
        return bibtex_inproceedings;
    }

    public void setBibtex_inproceedings(bibtex_Inproceedings bibtex_inproceedings) {
        this.bibtex_inproceedings = bibtex_inproceedings;
    }
    public bibtex_Incollection getBibtex_incollection() {
        return bibtex_incollection;
    }

    public void setBibtex_incollection(bibtex_Incollection bibtex_incollection) {
        this.bibtex_incollection = bibtex_incollection;
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

}