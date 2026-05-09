





import java.util.List;
import java.util.ArrayList;

public class literals_HexFloatLiteral extends FloatLiteral {

    private float hexValue;



    public literals_HexFloatLiteral(
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