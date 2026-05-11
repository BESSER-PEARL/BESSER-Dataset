





import java.util.List;
import java.util.ArrayList;

public class DDL_NationalCharacterStringType extends Type {

    private int length;



    public DDL_NationalCharacterStringType(
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