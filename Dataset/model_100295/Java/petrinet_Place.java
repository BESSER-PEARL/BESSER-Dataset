





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private int token;
    private String name;



    public petrinet_Place(
        int token,        String name    ) {
        this.token = token;
        this.name = name;
    }


    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}