





import java.util.List;
import java.util.ArrayList;

public class oaam_common_FloatingPoint extends DataTypeA {

    private int nBits;
    private String endianess;



    public oaam_common_FloatingPoint(
        int nBits,        String endianess    ) {
        super(
        );
        this.nBits = nBits;
        this.endianess = endianess;
    }


    public int getNbits() {
        return nBits;
    }

    public void setNbits(int nBits) {
        this.nBits = nBits;
    }
    public String getEndianess() {
        return endianess;
    }

    public void setEndianess(String endianess) {
        this.endianess = endianess;
    }


}