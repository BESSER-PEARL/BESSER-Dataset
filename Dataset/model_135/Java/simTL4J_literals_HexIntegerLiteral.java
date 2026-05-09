





import java.util.List;
import java.util.ArrayList;

public class simTL4J_literals_HexIntegerLiteral extends IntegerLiteral {

    private String hexValue;



    public simTL4J_literals_HexIntegerLiteral(
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