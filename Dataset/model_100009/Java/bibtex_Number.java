





import java.util.List;
import java.util.ArrayList;

public class bibtex_Number  {

    private String number;





    private bibtex_Article bibtex_article;




    private bibtex_Techreport bibtex_techreport;


    public bibtex_Number(
        String number    ) {
        this.number = number;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public bibtex_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibtex_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }
    public bibtex_Techreport getBibtex_techreport() {
        return bibtex_techreport;
    }

    public void setBibtex_techreport(bibtex_Techreport bibtex_techreport) {
        this.bibtex_techreport = bibtex_techreport;
    }

}