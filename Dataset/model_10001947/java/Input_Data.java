





import java.util.List;
import java.util.ArrayList;

public class Input_Data  {

    private String id;
    private String Symptoms_list;





    private user user;


    public Input_Data(
        String id,        String Symptoms_list    ) {
        this.id = id;
        this.Symptoms_list = Symptoms_list;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSymptoms_list() {
        return Symptoms_list;
    }

    public void setSymptoms_list(String Symptoms_list) {
        this.Symptoms_list = Symptoms_list;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}