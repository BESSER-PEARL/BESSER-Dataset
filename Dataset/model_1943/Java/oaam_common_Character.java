





import java.util.List;
import java.util.ArrayList;

public class oaam_common_Character extends DataTypeA {

    private int nBits;
    private String encoding;



    public oaam_common_Character(
        int nBits,        String encoding    ) {
        super(
        );
        this.nBits = nBits;
        this.encoding = encoding;
    }


    public int getNbits() {
        return nBits;
    }

    public void setNbits(int nBits) {
        this.nBits = nBits;
    }
    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }


}