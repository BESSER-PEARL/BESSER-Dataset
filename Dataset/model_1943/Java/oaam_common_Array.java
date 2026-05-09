





import java.util.List;
import java.util.ArrayList;

public class oaam_common_Array extends DataTypeA {

    private int nElements;
    private int alignment;



    public oaam_common_Array(
        int nElements,        int alignment    ) {
        super(
        );
        this.nElements = nElements;
        this.alignment = alignment;
    }


    public int getNelements() {
        return nElements;
    }

    public void setNelements(int nElements) {
        this.nElements = nElements;
    }
    public int getAlignment() {
        return alignment;
    }

    public void setAlignment(int alignment) {
        this.alignment = alignment;
    }


}