





import java.util.List;
import java.util.ArrayList;

public class afpText_TileSetColor extends triplet {

    private String SIZE4;
    private String CVAL1;
    private String CVAL2;
    private String CVAL4;
    private String CSPACE;
    private String SIZE3;
    private String SIZE1;
    private String SIZE2;
    private String RESERVED;
    private String CVAL3;



    public afpText_TileSetColor(
        String SIZE4,        String CVAL1,        String CVAL2,        String CVAL4,        String CSPACE,        String SIZE3,        String SIZE1,        String SIZE2,        String RESERVED,        String CVAL3    ) {
        super(
        );
        this.SIZE4 = SIZE4;
        this.CVAL1 = CVAL1;
        this.CVAL2 = CVAL2;
        this.CVAL4 = CVAL4;
        this.CSPACE = CSPACE;
        this.SIZE3 = SIZE3;
        this.SIZE1 = SIZE1;
        this.SIZE2 = SIZE2;
        this.RESERVED = RESERVED;
        this.CVAL3 = CVAL3;
    }


    public String getSize4() {
        return SIZE4;
    }

    public void setSize4(String SIZE4) {
        this.SIZE4 = SIZE4;
    }
    public String getCval1() {
        return CVAL1;
    }

    public void setCval1(String CVAL1) {
        this.CVAL1 = CVAL1;
    }
    public String getCval2() {
        return CVAL2;
    }

    public void setCval2(String CVAL2) {
        this.CVAL2 = CVAL2;
    }
    public String getCval4() {
        return CVAL4;
    }

    public void setCval4(String CVAL4) {
        this.CVAL4 = CVAL4;
    }
    public String getCspace() {
        return CSPACE;
    }

    public void setCspace(String CSPACE) {
        this.CSPACE = CSPACE;
    }
    public String getSize3() {
        return SIZE3;
    }

    public void setSize3(String SIZE3) {
        this.SIZE3 = SIZE3;
    }
    public String getSize1() {
        return SIZE1;
    }

    public void setSize1(String SIZE1) {
        this.SIZE1 = SIZE1;
    }
    public String getSize2() {
        return SIZE2;
    }

    public void setSize2(String SIZE2) {
        this.SIZE2 = SIZE2;
    }
    public String getReserved() {
        return RESERVED;
    }

    public void setReserved(String RESERVED) {
        this.RESERVED = RESERVED;
    }
    public String getCval3() {
        return CVAL3;
    }

    public void setCval3(String CVAL3) {
        this.CVAL3 = CVAL3;
    }


}