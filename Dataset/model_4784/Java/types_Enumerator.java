





import java.util.List;
import java.util.ArrayList;

public class types_Enumerator extends NamedElement {

    private String literalValue;



    public types_Enumerator(
        String literalValue    ) {
        super(
        );
        this.literalValue = literalValue;
    }


    public String getLiteralvalue() {
        return literalValue;
    }

    public void setLiteralvalue(String literalValue) {
        this.literalValue = literalValue;
    }


}