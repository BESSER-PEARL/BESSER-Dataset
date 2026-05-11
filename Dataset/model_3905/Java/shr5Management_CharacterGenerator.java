





import java.util.List;
import java.util.ArrayList;

public class shr5Management_CharacterGenerator  {

    private String currentInstruction;
    private String characterName;
    private String state;



    public shr5Management_CharacterGenerator(
        String currentInstruction,        String characterName,        String state    ) {
        this.currentInstruction = currentInstruction;
        this.characterName = characterName;
        this.state = state;
    }


    public String getCurrentinstruction() {
        return currentInstruction;
    }

    public void setCurrentinstruction(String currentInstruction) {
        this.currentInstruction = currentInstruction;
    }
    public String getCharactername() {
        return characterName;
    }

    public void setCharactername(String characterName) {
        this.characterName = characterName;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}