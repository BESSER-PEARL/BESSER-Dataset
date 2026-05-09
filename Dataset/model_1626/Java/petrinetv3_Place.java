





import java.util.List;
import java.util.ArrayList;

public class petrinetv3_Place  {

    private int initialTokens;
    private String name;





    private petrinetv3_Net petrinetv3_net;


    public petrinetv3_Place(
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

    public petrinetv3_Net getPetrinetv3_net() {
        return petrinetv3_net;
    }

    public void setPetrinetv3_net(petrinetv3_Net petrinetv3_net) {
        this.petrinetv3_net = petrinetv3_net;
    }

}