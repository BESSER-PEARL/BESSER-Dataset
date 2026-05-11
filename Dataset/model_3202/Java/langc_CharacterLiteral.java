





import java.util.List;
import java.util.ArrayList;

public class langc_CharacterLiteral extends Literal {

    private String value;



    public langc_CharacterLiteral(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}