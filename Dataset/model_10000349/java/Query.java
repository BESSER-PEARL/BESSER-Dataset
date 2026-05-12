





import java.util.List;
import java.util.ArrayList;

public class Query  {

    private None user;
    private String requestId;



    public Query(
        None user,        String requestId    ) {
        this.user = user;
        this.requestId = requestId;
    }


    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }
    public String getRequestid() {
        return requestId;
    }

    public void setRequestid(String requestId) {
        this.requestId = requestId;
    }


}