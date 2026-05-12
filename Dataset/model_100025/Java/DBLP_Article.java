





import java.util.List;
import java.util.ArrayList;

public class DBLP_Article extends Record {

    private int number;
    private String month;
    private int year;
    private String volume;
    private int fromPage;
    private String title;
    private int toPage;



    public DBLP_Article(
        int number,        String month,        int year,        String volume,        int fromPage,        String title,        int toPage    ) {
        super(
        );
        this.number = number;
        this.month = month;
        this.year = year;
        this.volume = volume;
        this.fromPage = fromPage;
        this.title = title;
        this.toPage = toPage;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
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


}