





import java.util.List;
import java.util.ArrayList;

public class java_HexFloatLiteral extends FloatLiteral {

    private float hexValue;



    public java_HexFloatLiteral(
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