





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {

    private int tokensCount;



    public petrinet_Place(
        int tokensCount    ) {
        super(
        );
        this.tokensCount = tokensCount;
    }


    public int getTokenscount() {
        return tokensCount;
    }

    public void setTokenscount(int tokensCount) {
        this.tokensCount = tokensCount;
    }


}