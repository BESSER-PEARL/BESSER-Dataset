





import java.util.List;
import java.util.ArrayList;

public class stochasticpetrinet_Place extends Node {

    private int tokens;



    public stochasticpetrinet_Place(
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