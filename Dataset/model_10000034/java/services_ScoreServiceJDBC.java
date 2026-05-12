





import java.util.List;
import java.util.ArrayList;

public class services_ScoreServiceJDBC  {

    private String PASSWORD;
    private String INSERT_SCORE;
    private String URL;
    private String USER;
    private String SELECT_SCORE;



    public services_ScoreServiceJDBC(
        String PASSWORD,        String INSERT_SCORE,        String URL,        String USER,        String SELECT_SCORE    ) {
        this.PASSWORD = PASSWORD;
        this.INSERT_SCORE = INSERT_SCORE;
        this.URL = URL;
        this.USER = USER;
        this.SELECT_SCORE = SELECT_SCORE;
    }


    public String getPassword() {
        return PASSWORD;
    }

    public void setPassword(String PASSWORD) {
        this.PASSWORD = PASSWORD;
    }
    public String getInsert_score() {
        return INSERT_SCORE;
    }

    public void setInsert_score(String INSERT_SCORE) {
        this.INSERT_SCORE = INSERT_SCORE;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }
    public String getSelect_score() {
        return SELECT_SCORE;
    }

    public void setSelect_score(String SELECT_SCORE) {
        this.SELECT_SCORE = SELECT_SCORE;
    }


}