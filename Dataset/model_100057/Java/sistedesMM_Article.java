





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Article extends Publication {

    private String volume;
    private int fromPage;
    private String month;
    private int toPage;
    private String title;
    private int year;
    private int number;



    public sistedesMM_Article(
        String volume,        int fromPage,        String month,        int toPage,        String title,        int year,        int number    ) {
        super(
        );
        this.volume = volume;
        this.fromPage = fromPage;
        this.month = month;
        this.toPage = toPage;
        this.title = title;
        this.year = year;
        this.number = number;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
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
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}