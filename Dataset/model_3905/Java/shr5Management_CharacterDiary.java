





import java.util.List;
import java.util.ArrayList;

public class shr5Management_CharacterDiary  {

    private String characterDate;





    private shr5Management_PlayerCharacter shr5management_playercharacter;


    public shr5Management_CharacterDiary(
        String characterDate    ) {
        this.characterDate = characterDate;
    }


    public String getCharacterdate() {
        return characterDate;
    }

    public void setCharacterdate(String characterDate) {
        this.characterDate = characterDate;
    }

    public shr5Management_PlayerCharacter getShr5management_playercharacter() {
        return shr5management_playercharacter;
    }

    public void setShr5management_playercharacter(shr5Management_PlayerCharacter shr5management_playercharacter) {
        this.shr5management_playercharacter = shr5management_playercharacter;
    }

}