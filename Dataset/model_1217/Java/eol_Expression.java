





import java.util.List;
import java.util.ArrayList;

public class eol_Expression extends EOLElement {

    private boolean inBrackets;



    public eol_Expression(
        boolean inBrackets    ) {
        super(
        );
        this.inBrackets = inBrackets;
    }


    public boolean getInbrackets() {
        return inBrackets;
    }

    public void setInbrackets(boolean inBrackets) {
        this.inBrackets = inBrackets;
    }


}