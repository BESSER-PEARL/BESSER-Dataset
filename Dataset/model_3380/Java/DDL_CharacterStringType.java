





import java.util.List;
import java.util.ArrayList;

public class DDL_CharacterStringType extends Type {

    private int length;



    public DDL_CharacterStringType(
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