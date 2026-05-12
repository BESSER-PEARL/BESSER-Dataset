





import java.util.List;
import java.util.ArrayList;

public class Query  {

    private String requestId;
    private None user;



    public Query(
        String requestId,        None user    ) {
        this.requestId = requestId;
        this.user = user;
    }


    public String getRequestid() {
        return requestId;
    }

    public void setRequestid(String requestId) {
        this.requestId = requestId;
    }
    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }


}