





import java.util.List;
import java.util.ArrayList;

public class java_OctalLongLiteral extends LongLiteral {

    private String octalValue;



    public java_OctalLongLiteral(
        String octalValue    ) {
        super(
        );
        this.octalValue = octalValue;
    }


    public String getOctalvalue() {
        return octalValue;
    }

    public void setOctalvalue(String octalValue) {
        this.octalValue = octalValue;
    }


}