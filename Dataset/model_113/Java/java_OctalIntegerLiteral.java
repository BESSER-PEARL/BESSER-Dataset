





import java.util.List;
import java.util.ArrayList;

public class java_OctalIntegerLiteral extends IntegerLiteral {

    private String octalValue;



    public java_OctalIntegerLiteral(
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