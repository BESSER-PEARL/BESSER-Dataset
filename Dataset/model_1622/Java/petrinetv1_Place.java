





import java.util.List;
import java.util.ArrayList;

public class petrinetv1_Place  {

    private int initialTokens;
    private int tokens;
    private String name;





    private petrinetv1_Net petrinetv1_net;


    public petrinetv1_Place(
        int initialTokens,        int tokens,        String name    ) {
        this.initialTokens = initialTokens;
        this.tokens = tokens;
        this.name = name;
    }


    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
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

    public petrinetv1_Net getPetrinetv1_net() {
        return petrinetv1_net;
    }

    public void setPetrinetv1_net(petrinetv1_Net petrinetv1_net) {
        this.petrinetv1_net = petrinetv1_net;
    }

}