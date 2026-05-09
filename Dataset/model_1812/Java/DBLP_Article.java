





import java.util.List;
import java.util.ArrayList;

public class DBLP_Article extends Record {

    private int number;
    private int toPage;
    private String title;
    private int year;
    private String month;
    private String volume;
    private int fromPage;



    public DBLP_Article(
        int number,        int toPage,        String title,        int year,        String month,        String volume,        int fromPage    ) {
        super(
        );
        this.number = number;
        this.toPage = toPage;
        this.title = title;
        this.year = year;
        this.month = month;
        this.volume = volume;
        this.fromPage = fromPage;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
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


}