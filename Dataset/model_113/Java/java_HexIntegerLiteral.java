





import java.util.List;
import java.util.ArrayList;

public class java_HexIntegerLiteral extends IntegerLiteral {

    private String hexValue;



    public java_HexIntegerLiteral(
        String hexValue    ) {
        super(
        );
        this.hexValue = hexValue;
    }


    public String getHexvalue() {
        return hexValue;
    }

    public void setHexvalue(String hexValue) {
        this.hexValue = hexValue;
    }


}