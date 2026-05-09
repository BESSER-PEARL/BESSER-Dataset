





import java.util.List;
import java.util.ArrayList;

public class ktest401_Line extends NamedElement {

    private String articleAid;
    private int quant;





    private ktest401_Thing ktest401_thing;




    private ktest401_Article ktest401_article;




    private ktest401_Thing ktest401_thing;


    public ktest401_Line(
        String articleAid,        int quant    ) {
        super(
        );
        this.articleAid = articleAid;
        this.quant = quant;
    }


    public String getArticleaid() {
        return articleAid;
    }

    public void setArticleaid(String articleAid) {
        this.articleAid = articleAid;
    }
    public int getQuant() {
        return quant;
    }

    public void setQuant(int quant) {
        this.quant = quant;
    }

    public ktest401_Thing getKtest401_thing() {
        return ktest401_thing;
    }

    public void setKtest401_thing(ktest401_Thing ktest401_thing) {
        this.ktest401_thing = ktest401_thing;
    }
    public ktest401_Article getKtest401_article() {
        return ktest401_article;
    }

    public void setKtest401_article(ktest401_Article ktest401_article) {
        this.ktest401_article = ktest401_article;
    }
    public ktest401_Thing getKtest401_thing() {
        return ktest401_thing;
    }

    public void setKtest401_thing(ktest401_Thing ktest401_thing) {
        this.ktest401_thing = ktest401_thing;
    }

}