





import java.util.List;
import java.util.ArrayList;

public class thingML_ByteLiteral extends Literal {

    private String byteValue;



    public thingML_ByteLiteral(
        String byteValue    ) {
        super(
        );
        this.byteValue = byteValue;
    }


    public String getBytevalue() {
        return byteValue;
    }

    public void setBytevalue(String byteValue) {
        this.byteValue = byteValue;
    }


}