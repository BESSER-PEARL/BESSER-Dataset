





import java.util.List;
import java.util.ArrayList;

public class types_Enumerator extends Declaration {

    private int literalValue;



    public types_Enumerator(
        int literalValue    ) {
        super(
        );
        this.literalValue = literalValue;
    }


    public int getLiteralvalue() {
        return literalValue;
    }

    public void setLiteralvalue(int literalValue) {
        this.literalValue = literalValue;
    }


}