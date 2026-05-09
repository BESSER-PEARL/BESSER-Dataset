





import java.util.List;
import java.util.ArrayList;

public class oaam_common_Integer extends DataTypeA {

    private int nBits;
    private boolean signed;
    private String endianess;



    public oaam_common_Integer(
        int nBits,        boolean signed,        String endianess    ) {
        super(
        );
        this.nBits = nBits;
        this.signed = signed;
        this.endianess = endianess;
    }


    public int getNbits() {
        return nBits;
    }

    public void setNbits(int nBits) {
        this.nBits = nBits;
    }
    public boolean getSigned() {
        return signed;
    }

    public void setSigned(boolean signed) {
        this.signed = signed;
    }
    public String getEndianess() {
        return endianess;
    }

    public void setEndianess(String endianess) {
        this.endianess = endianess;
    }


}