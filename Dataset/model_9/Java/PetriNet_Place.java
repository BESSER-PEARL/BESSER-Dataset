





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends Element {

    private int Tokens;



    public PetriNet_Place(
        int Tokens    ) {
        super(
        );
        this.Tokens = Tokens;
    }


    public int getTokens() {
        return Tokens;
    }

    public void setTokens(int Tokens) {
        this.Tokens = Tokens;
    }


}