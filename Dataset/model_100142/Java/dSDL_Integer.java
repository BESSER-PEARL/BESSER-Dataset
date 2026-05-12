





import java.util.List;
import java.util.ArrayList;

public class dSDL_Integer extends Type {

    private String integer;
    private int length;



    public dSDL_Integer(
        String integer,        int length    ) {
        super(
        );
        this.integer = integer;
        this.length = length;
    }


    public String getInteger() {
        return integer;
    }

    public void setInteger(String integer) {
        this.integer = integer;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}