





import java.util.List;
import java.util.ArrayList;

public class pn_Place extends NamedElement, NetElement {

    private int noOfTokens;



    public pn_Place(
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