





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_Person  {

    private String id;
    private String userId;



    public org_aries_common_Person(
        String id,        String userId    ) {
        this.id = id;
        this.userId = userId;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }


}