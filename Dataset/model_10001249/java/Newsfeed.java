





import java.util.List;
import java.util.ArrayList;

public class Newsfeed  {

    private String Calendar;
    private String News;
    private String Phone;
    private String Email;
    private String Weather;





    private Smart_mirror smart_mirror;


    public Newsfeed(
        String Calendar,        String News,        String Phone,        String Email,        String Weather    ) {
        this.Calendar = Calendar;
        this.News = News;
        this.Phone = Phone;
        this.Email = Email;
        this.Weather = Weather;
    }


    public String getCalendar() {
        return Calendar;
    }

    public void setCalendar(String Calendar) {
        this.Calendar = Calendar;
    }
    public String getNews() {
        return News;
    }

    public void setNews(String News) {
        this.News = News;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getWeather() {
        return Weather;
    }

    public void setWeather(String Weather) {
        this.Weather = Weather;
    }

    public Smart_mirror getSmart_mirror() {
        return smart_mirror;
    }

    public void setSmart_mirror(Smart_mirror smart_mirror) {
        this.smart_mirror = smart_mirror;
    }

}