





import java.util.List;
import java.util.ArrayList;

public class iec61131_literals_Double_Byte_Character_Representation  {

    private String value;





    private Common_Character_Representation common_character_representation;


    public iec61131_literals_Double_Byte_Character_Representation(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Common_Character_Representation getCommon_character_representation() {
        return common_character_representation;
    }

    public void setCommon_character_representation(Common_Character_Representation common_character_representation) {
        this.common_character_representation = common_character_representation;
    }

}