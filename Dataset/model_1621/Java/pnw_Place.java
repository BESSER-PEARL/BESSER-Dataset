





import java.util.List;
import java.util.ArrayList;

public class pnw_Place extends NetElement, NamedElement {

    private int noOfTokens;



    public pnw_Place(
        int noOfTokens    ) {
        super(
        );
        this.noOfTokens = noOfTokens;
    }


    public int getNooftokens() {
        return noOfTokens;
    }

    public void setNooftokens(int noOfTokens) {
        this.noOfTokens = noOfTokens;
    }


}