





import java.util.List;
import java.util.ArrayList;

public class Newsfeed  {

    private String News;
    private String weather;
    private String Calendar;
    private String TimeID;
    private String Email;



    public Newsfeed(
        String News,        String weather,        String Calendar,        String TimeID,        String Email    ) {
        this.News = News;
        this.weather = weather;
        this.Calendar = Calendar;
        this.TimeID = TimeID;
        this.Email = Email;
    }


    public String getNews() {
        return News;
    }

    public void setNews(String News) {
        this.News = News;
    }
    public String getWeather() {
        return weather;
    }

    public void setWeather(String weather) {
        this.weather = weather;
    }
    public String getCalendar() {
        return Calendar;
    }

    public void setCalendar(String Calendar) {
        this.Calendar = Calendar;
    }
    public String getTimeid() {
        return TimeID;
    }

    public void setTimeid(String TimeID) {
        this.TimeID = TimeID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}