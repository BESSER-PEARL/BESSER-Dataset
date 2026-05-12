





import java.util.List;
import java.util.ArrayList;

public class bibTeX_NumberField  {

    private String number;





    private bibTeX_Article bibtex_article;


    public bibTeX_NumberField(
        String number    ) {
        this.number = number;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public bibTeX_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibTeX_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }

}