





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private int initialTokens;
    private String name;



    public petrinet_Place(
        int initialTokens,        String name    ) {
        this.initialTokens = initialTokens;
        this.name = name;
    }


    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
        this.initialTokens = initialTokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}