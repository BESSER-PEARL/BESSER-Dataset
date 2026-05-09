





import java.util.List;
import java.util.ArrayList;

public class petrinetv1_Place  {

    private int tokens;
    private String name;
    private int initialTokens;



    public petrinetv1_Place(
        int tokens,        String name,        int initialTokens    ) {
        this.tokens = tokens;
        this.name = name;
        this.initialTokens = initialTokens;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
        this.initialTokens = initialTokens;
    }


}