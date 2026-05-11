





import java.util.List;
import java.util.ArrayList;

public class cobol_literals_NationalLiteral extends DBCSLiteral {

    private String value;



    public cobol_literals_NationalLiteral(
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