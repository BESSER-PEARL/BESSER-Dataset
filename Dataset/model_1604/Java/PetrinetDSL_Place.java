





import java.util.List;
import java.util.ArrayList;

public class PetrinetDSL_Place extends Node {






    private List<PetrinetDSL_Token> petrinetdsl_tokens;


    public PetrinetDSL_Place(
    ) {
        super(
        );
        this.petrinetdsl_tokens = new ArrayList<>();
    }

    public PetrinetDSL_Place(
        ArrayList<PetrinetDSL_Token> petrinetdsl_tokens    ) {
        this.petrinetdsl_tokens = petrinetdsl_tokens;
    }


    public List<PetrinetDSL_Token> getPetrinetdsl_tokens() {
        return petrinetdsl_tokens;
    }

    public void addPetrinetdsl_token(Petrinetdsl_token petrinetdsl_token) {
        this.petrinetdsl_tokens.add(petrinetdsl_token);
    }

}