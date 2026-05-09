





import java.util.List;
import java.util.ArrayList;

public class petrinetv2_Place  {

    private int initialTokens;
    private String name;





    private petrinetv2_Net petrinetv2_net;


    public petrinetv2_Place(
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

    public petrinetv2_Net getPetrinetv2_net() {
        return petrinetv2_net;
    }

    public void setPetrinetv2_net(petrinetv2_Net petrinetv2_net) {
        this.petrinetv2_net = petrinetv2_net;
    }

}