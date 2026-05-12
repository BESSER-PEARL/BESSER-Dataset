





import java.util.List;
import java.util.ArrayList;

public class DBLP_Article extends Record {

    private int year;
    private int fromPage;
    private String title;
    private int toPage;
    private int number;
    private String volume;
    private String month;



    public DBLP_Article(
        int year,        int fromPage,        String title,        int toPage,        int number,        String volume,        String month    ) {
        super(
        );
        this.year = year;
        this.fromPage = fromPage;
        this.title = title;
        this.toPage = toPage;
        this.number = number;
        this.volume = volume;
        this.month = month;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public int getFrompage() {
        return fromPage;
    }

    public void setFrompage(int fromPage) {
        this.fromPage = fromPage;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}