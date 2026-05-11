





import java.util.List;
import java.util.ArrayList;

public class guigraph_Place extends GuiGraphNode {

    private int initialTokens;



    public guigraph_Place(
        int initialTokens    ) {
        super(
        );
        this.initialTokens = initialTokens;
    }


    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
        this.initialTokens = initialTokens;
    }


}