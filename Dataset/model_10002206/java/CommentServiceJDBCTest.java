





import java.util.List;
import java.util.ArrayList;

public class CommentServiceJDBCTest  {

    private String PASS;
    private String URL;
    private String USER;
    private String DELETE;



    public CommentServiceJDBCTest(
        String PASS,        String URL,        String USER,        String DELETE    ) {
        this.PASS = PASS;
        this.URL = URL;
        this.USER = USER;
        this.DELETE = DELETE;
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
    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }
    public String getDelete() {
        return DELETE;
    }

    public void setDelete(String DELETE) {
        this.DELETE = DELETE;
    }


}