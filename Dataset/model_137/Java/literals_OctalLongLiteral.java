





import java.util.List;
import java.util.ArrayList;

public class literals_OctalLongLiteral extends LongLiteral {

    private boolean octalValue;



    public literals_OctalLongLiteral(
        boolean octalValue    ) {
        super(
        );
        this.octalValue = octalValue;
    }


    public boolean getOctalvalue() {
        return octalValue;
    }

    public void setOctalvalue(boolean octalValue) {
        this.octalValue = octalValue;
    }


}