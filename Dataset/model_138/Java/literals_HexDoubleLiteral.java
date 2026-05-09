





import java.util.List;
import java.util.ArrayList;

public class literals_HexDoubleLiteral extends DoubleLiteral {

    private float hexValue;



    public literals_HexDoubleLiteral(
        float hexValue    ) {
        super(
        );
        this.hexValue = hexValue;
    }


    public float getHexvalue() {
        return hexValue;
    }

    public void setHexvalue(float hexValue) {
        this.hexValue = hexValue;
    }


}