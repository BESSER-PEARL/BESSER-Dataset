





import java.util.List;
import java.util.ArrayList;

public class guigraph_Place extends GuiGraphNode {

    private boolean provideAsInterface;
    private int initialTokens;



    public guigraph_Place(
        boolean provideAsInterface,        int initialTokens    ) {
        super(
        );
        this.provideAsInterface = provideAsInterface;
        this.initialTokens = initialTokens;
    }


    public boolean getProvideasinterface() {
        return provideAsInterface;
    }

    public void setProvideasinterface(boolean provideAsInterface) {
        this.provideAsInterface = provideAsInterface;
    }
    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
        this.initialTokens = initialTokens;
    }


}