





import java.util.List;
import java.util.ArrayList;

public class fmpl_Read extends Expression {

    private int initBit;
    private int length;



    public fmpl_Read(
        int initBit,        int length    ) {
        super(
        );
        this.initBit = initBit;
        this.length = length;
    }


    public int getInitbit() {
        return initBit;
    }

    public void setInitbit(int initBit) {
        this.initBit = initBit;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}