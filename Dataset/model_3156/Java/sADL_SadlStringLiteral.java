





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlStringLiteral extends SadlExplicitValueLiteral {

    private String literalString;



    public sADL_SadlStringLiteral(
        String literalString    ) {
        super(
        );
        this.literalString = literalString;
    }


    public String getLiteralstring() {
        return literalString;
    }

    public void setLiteralstring(String literalString) {
        this.literalString = literalString;
    }


}