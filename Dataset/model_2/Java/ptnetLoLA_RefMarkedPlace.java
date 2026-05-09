





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_RefMarkedPlace extends PlaceReference {

    private int token;





    private ptnetLoLA_Marking ptnetlola_marking;


    public ptnetLoLA_RefMarkedPlace(
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

    public ptnetLoLA_Marking getPtnetlola_marking() {
        return ptnetlola_marking;
    }

    public void setPtnetlola_marking(ptnetLoLA_Marking ptnetlola_marking) {
        this.ptnetlola_marking = ptnetlola_marking;
    }

}