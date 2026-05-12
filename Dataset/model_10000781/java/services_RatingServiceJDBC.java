





import java.util.List;
import java.util.ArrayList;

public class services_RatingServiceJDBC  {

    private String URL;
    private String SELECT_AVERAGE_RATING;
    private String PASSWORD;
    private String INSERT_RATING;
    private String USER;
    private String SELECT_RATING;



    public services_RatingServiceJDBC(
        String URL,        String SELECT_AVERAGE_RATING,        String PASSWORD,        String INSERT_RATING,        String USER,        String SELECT_RATING    ) {
        this.URL = URL;
        this.SELECT_AVERAGE_RATING = SELECT_AVERAGE_RATING;
        this.PASSWORD = PASSWORD;
        this.INSERT_RATING = INSERT_RATING;
        this.USER = USER;
        this.SELECT_RATING = SELECT_RATING;
    }


    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getSelect_average_rating() {
        return SELECT_AVERAGE_RATING;
    }

    public void setSelect_average_rating(String SELECT_AVERAGE_RATING) {
        this.SELECT_AVERAGE_RATING = SELECT_AVERAGE_RATING;
    }
    public String getPassword() {
        return PASSWORD;
    }

    public void setPassword(String PASSWORD) {
        this.PASSWORD = PASSWORD;
    }
    public String getInsert_rating() {
        return INSERT_RATING;
    }

    public void setInsert_rating(String INSERT_RATING) {
        this.INSERT_RATING = INSERT_RATING;
    }
    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }
    public String getSelect_rating() {
        return SELECT_RATING;
    }

    public void setSelect_rating(String SELECT_RATING) {
        this.SELECT_RATING = SELECT_RATING;
    }


}