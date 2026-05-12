





import java.util.List;
import java.util.ArrayList;

public class book  {

    private float rate;
    private String catygory;
    private String keywords;
    private String author;
    private String title;



    public book(
        float rate,        String catygory,        String keywords,        String author,        String title    ) {
        this.rate = rate;
        this.catygory = catygory;
        this.keywords = keywords;
        this.author = author;
        this.title = title;
    }


    public float getRate() {
        return rate;
    }

    public void setRate(float rate) {
        this.rate = rate;
    }
    public String getCatygory() {
        return catygory;
    }

    public void setCatygory(String catygory) {
        this.catygory = catygory;
    }
    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}