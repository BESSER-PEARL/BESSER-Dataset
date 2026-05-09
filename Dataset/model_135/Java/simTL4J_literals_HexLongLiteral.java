





import java.util.List;
import java.util.ArrayList;

public class simTL4J_literals_HexLongLiteral extends LongLiteral {

    private String hexValue;



    public simTL4J_literals_HexLongLiteral(
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