





import java.util.List;
import java.util.ArrayList;

public class myDsl_charType extends type_specifier {

    private String char_type;



    public myDsl_charType(
        String char_type    ) {
        super(
        );
        this.char_type = char_type;
    }


    public String getChar_type() {
        return char_type;
    }

    public void setChar_type(String char_type) {
        this.char_type = char_type;
    }


}