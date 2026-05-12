





import java.util.List;
import java.util.ArrayList;

public class bibTeX_VolumeField  {

    private String volume;





    private bibTeX_Article bibtex_article;


    public bibTeX_VolumeField(
        String volume    ) {
        this.volume = volume;
    }


    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }

    public bibTeX_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibTeX_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }

}