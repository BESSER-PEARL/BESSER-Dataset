





import java.util.List;
import java.util.ArrayList;

public class CommentServiceJDBCTest  {

    private String USER;
    private String PASS;
    private String DELETE;
    private String URL;



    public CommentServiceJDBCTest(
        String USER,        String PASS,        String DELETE,        String URL    ) {
        this.USER = USER;
        this.PASS = PASS;
        this.DELETE = DELETE;
        this.URL = URL;
    }


    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }
    public String getPass() {
        return PASS;
    }

    public void setPass(String PASS) {
        this.PASS = PASS;
    }
    public String getDelete() {
        return DELETE;
    }

    public void setDelete(String DELETE) {
        this.DELETE = DELETE;
    }
    public String getUrl() {
        return URL;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }


}