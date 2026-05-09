





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {

    private int tokenNb;



    public petrinet_Place(
        int tokenNb    ) {
        super(
        );
        this.tokenNb = tokenNb;
    }


    public int getTokennb() {
        return tokenNb;
    }

    public void setTokennb(int tokenNb) {
        this.tokenNb = tokenNb;
    }


}