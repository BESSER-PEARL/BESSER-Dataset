





import java.util.List;
import java.util.ArrayList;

public class langc_IntegralLiteral extends Literal {

    private String bytes;
    private boolean signed;
    private String value;



    public langc_IntegralLiteral(
        String bytes,        boolean signed,        String value    ) {
        super(
        );
        this.bytes = bytes;
        this.signed = signed;
        this.value = value;
    }


    public String getBytes() {
        return bytes;
    }

    public void setBytes(String bytes) {
        this.bytes = bytes;
    }
    public boolean getSigned() {
        return signed;
    }

    public void setSigned(boolean signed) {
        this.signed = signed;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}