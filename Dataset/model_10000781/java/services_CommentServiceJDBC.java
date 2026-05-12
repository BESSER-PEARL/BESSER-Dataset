





import java.util.List;
import java.util.ArrayList;

public class services_CommentServiceJDBC  {

    private String SELECT_COMMENTS;
    private String URL;
    private String PASSWORD;
    private String INSERT_COMMENT;
    private String USER;



    public services_CommentServiceJDBC(
        String SELECT_COMMENTS,        String URL,        String PASSWORD,        String INSERT_COMMENT,        String USER    ) {
        this.SELECT_COMMENTS = SELECT_COMMENTS;
        this.URL = URL;
        this.PASSWORD = PASSWORD;
        this.INSERT_COMMENT = INSERT_COMMENT;
        this.USER = USER;
    }


    public String getSelect_comments() {
        return SELECT_COMMENTS;
    }

    public void setSelect_comments(String SELECT_COMMENTS) {
        this.SELECT_COMMENTS = SELECT_COMMENTS;
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
    public String getInsert_comment() {
        return INSERT_COMMENT;
    }

    public void setInsert_comment(String INSERT_COMMENT) {
        this.INSERT_COMMENT = INSERT_COMMENT;
    }
    public String getUser() {
        return USER;
    }

    public void setUser(String USER) {
        this.USER = USER;
    }


}