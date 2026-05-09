





import java.util.List;
import java.util.ArrayList;

public class petriNet_Place extends Node {

    private int noTokens;



    public petriNet_Place(
        int noTokens    ) {
        super(
        );
        this.noTokens = noTokens;
    }


    public int getNotokens() {
        return noTokens;
    }

    public void setNotokens(int noTokens) {
        this.noTokens = noTokens;
    }


}