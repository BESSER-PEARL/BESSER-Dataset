





import java.util.List;
import java.util.ArrayList;

public class ScoreServiceJDBCTest  {

    private String PASS;
    private String URL;
    private String DELETE;
    private String USER;



    public ScoreServiceJDBCTest(
        String PASS,        String URL,        String DELETE,        String USER    ) {
        this.PASS = PASS;
        this.URL = URL;
        this.DELETE = DELETE;
        this.USER = USER;
    }


    public String getPass() {
        return PASS;
    }

    public void setPass(String PASS) {
        this.PASS = PASS;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }
    public String getDelete() {
        return DELETE;
    }

    public void setDelete(String DELETE) {
        this.DELETE = DELETE;
    }
    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }


}