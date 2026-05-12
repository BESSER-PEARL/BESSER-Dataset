





import java.util.List;
import java.util.ArrayList;

public class services_ScoreServiceJDBC  {

    private String PASSWORD;
    private String SELECT_SCORE;
    private String INSERT_SCORE;
    private String USER;
    private String URL;



    public services_ScoreServiceJDBC(
        String PASSWORD,        String SELECT_SCORE,        String INSERT_SCORE,        String USER,        String URL    ) {
        this.PASSWORD = PASSWORD;
        this.SELECT_SCORE = SELECT_SCORE;
        this.INSERT_SCORE = INSERT_SCORE;
        this.USER = USER;
        this.URL = URL;
    }


    public String getPassword() {
        return PASSWORD;
    }

    public void setPassword(String PASSWORD) {
        this.PASSWORD = PASSWORD;
    }
    public String getSelect_score() {
        return SELECT_SCORE;
    }

    public void setSelect_score(String SELECT_SCORE) {
        this.SELECT_SCORE = SELECT_SCORE;
    }
    public String getInsert_score() {
        return INSERT_SCORE;
    }

    public void setInsert_score(String INSERT_SCORE) {
        this.INSERT_SCORE = INSERT_SCORE;
    }
    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }


}