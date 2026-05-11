





import java.util.List;
import java.util.ArrayList;

public class pcm_parameter_CharacterisedVariable extends Variable {

    private String characterisationType;



    public pcm_parameter_CharacterisedVariable(
        String characterisationType    ) {
        super(
        );
        this.characterisationType = characterisationType;
    }


    public String getCharacterisationtype() {
        return characterisationType;
    }

    public void setCharacterisationtype(String characterisationType) {
        this.characterisationType = characterisationType;
    }


}