





import java.util.List;
import java.util.ArrayList;

public class system  {

    private String user_id;
    private String name;





    private app app;


    public system(
        String user_id,        String name    ) {
        this.user_id = user_id;
        this.name = name;
    }


    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public app getApp() {
        return app;
    }

    public void setApp(app app) {
        this.app = app;
    }

}