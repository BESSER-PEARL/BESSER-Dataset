





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Named {

    private int token;



    public petrinet_Place(
        int token    ) {
        super(
        );
        this.token = token;
    }


    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }


}