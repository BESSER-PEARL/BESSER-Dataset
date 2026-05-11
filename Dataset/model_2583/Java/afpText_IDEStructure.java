





import java.util.List;
import java.util.ArrayList;

public class afpText_IDEStructure extends triplet {

    private String FLAGS;
    private String SIZE2;
    private String SIZE1;
    private String SIZE3;
    private String FORMAT;
    private String SIZE4;



    public afpText_IDEStructure(
        String FLAGS,        String SIZE2,        String SIZE1,        String SIZE3,        String FORMAT,        String SIZE4    ) {
        super(
        );
        this.FLAGS = FLAGS;
        this.SIZE2 = SIZE2;
        this.SIZE1 = SIZE1;
        this.SIZE3 = SIZE3;
        this.FORMAT = FORMAT;
        this.SIZE4 = SIZE4;
    }


    public String getFlags() {
        return FLAGS;
    }

    public void setFlags(String FLAGS) {
        this.FLAGS = FLAGS;
    }
    public String getSize2() {
        return SIZE2;
    }

    public void setSize2(String SIZE2) {
        this.SIZE2 = SIZE2;
    }
    public String getSize1() {
        return SIZE1;
    }

    public void setSize1(String SIZE1) {
        this.SIZE1 = SIZE1;
    }
    public String getSize3() {
        return SIZE3;
    }

    public void setSize3(String SIZE3) {
        this.SIZE3 = SIZE3;
    }
    public String getFormat() {
        return FORMAT;
    }

    public void setFormat(String FORMAT) {
        this.FORMAT = FORMAT;
    }
    public String getSize4() {
        return SIZE4;
    }

    public void setSize4(String SIZE4) {
        this.SIZE4 = SIZE4;
    }


}