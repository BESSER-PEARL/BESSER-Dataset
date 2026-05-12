





import java.util.List;
import java.util.ArrayList;

public class services_ScoreServiceJDBC  {

    private String SELECT_SCORE;
    private String URL;
    private String PASSWORD;
    private String USER;
    private String INSERT_SCORE;



    public services_ScoreServiceJDBC(
        String SELECT_SCORE,        String URL,        String PASSWORD,        String USER,        String INSERT_SCORE    ) {
        this.SELECT_SCORE = SELECT_SCORE;
        this.URL = URL;
        this.PASSWORD = PASSWORD;
        this.USER = USER;
        this.INSERT_SCORE = INSERT_SCORE;
    }


    public String getSelect_score() {
        return SELECT_SCORE;
    }

    public void setSelect_score(String SELECT_SCORE) {
        this.SELECT_SCORE = SELECT_SCORE;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getPassword() {
        return PASSWORD;
    }

    public void setPassword(String PASSWORD) {
        this.PASSWORD = PASSWORD;
    }
    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }
    public String getInsert_score() {
        return INSERT_SCORE;
    }

    public void setInsert_score(String INSERT_SCORE) {
        this.INSERT_SCORE = INSERT_SCORE;
    }


}