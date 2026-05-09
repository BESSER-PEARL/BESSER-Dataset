





import java.util.List;
import java.util.ArrayList;

public class DBLP_Article extends Record {

    private int year;
    private int toPage;
    private String title;
    private String month;
    private int number;
    private int fromPage;
    private String volume;



    public DBLP_Article(
        int year,        int toPage,        String title,        String month,        int number,        int fromPage,        String volume    ) {
        super(
        );
        this.year = year;
        this.toPage = toPage;
        this.title = title;
        this.month = month;
        this.number = number;
        this.fromPage = fromPage;
        this.volume = volume;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getFrompage() {
        return fromPage;
    }

    public void setFrompage(int fromPage) {
        this.fromPage = fromPage;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }


}