





import java.util.List;
import java.util.ArrayList;

public class DDL_BitStringType extends Type {

    private int length;



    public DDL_BitStringType(
        int length    ) {
        super(
        );
        this.length = length;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}