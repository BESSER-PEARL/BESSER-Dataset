





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Article extends Publication {

    private String title;
    private int year;
    private String month;
    private int fromPage;
    private int number;
    private String volume;
    private int toPage;



    public sistedesMM_Article(
        String title,        int year,        String month,        int fromPage,        int number,        String volume,        int toPage    ) {
        super(
        );
        this.title = title;
        this.year = year;
        this.month = month;
        this.fromPage = fromPage;
        this.number = number;
        this.volume = volume;
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
    public int getFrompage() {
        return fromPage;
    }

    public void setFrompage(int fromPage) {
        this.fromPage = fromPage;
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
    public int getTopage() {
        return toPage;
    }

    public void setTopage(int toPage) {
        this.toPage = toPage;
    }


}