





import java.util.List;
import java.util.ArrayList;

public class petri_Place extends Node {

    private int tokens;



    public petri_Place(
        int tokens    ) {
        super(
        );
        this.tokens = tokens;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }


}