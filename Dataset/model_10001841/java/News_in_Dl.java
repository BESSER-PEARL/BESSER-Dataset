





import java.util.List;
import java.util.ArrayList;

public class News_in_Dl  {

    private None Update_news;
    private None Opens_news;
    private String Hyperlink;



    public News_in_Dl(
        None Update_news,        None Opens_news,        String Hyperlink    ) {
        this.Update_news = Update_news;
        this.Opens_news = Opens_news;
        this.Hyperlink = Hyperlink;
    }


    public None getUpdate_news() {
        return Update_news;
    }

    public void setUpdate_news(None Update_news) {
        this.Update_news = Update_news;
    }
    public None getOpens_news() {
        return Opens_news;
    }

    public void setOpens_news(None Opens_news) {
        this.Opens_news = Opens_news;
    }
    public String getHyperlink() {
        return Hyperlink;
    }

    public void setHyperlink(String Hyperlink) {
        this.Hyperlink = Hyperlink;
    }


}