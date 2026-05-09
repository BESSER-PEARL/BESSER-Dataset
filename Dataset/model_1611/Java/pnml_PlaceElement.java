





import java.util.List;
import java.util.ArrayList;

public class pnml_PlaceElement extends Element {

    private int tokens;
    private String name;



    public pnml_PlaceElement(
        int tokens,        String name    ) {
        super(
        );
        this.tokens = tokens;
        this.name = name;
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


}