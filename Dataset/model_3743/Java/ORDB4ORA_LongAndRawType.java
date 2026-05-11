





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_LongAndRawType extends BuiltInType {

    private String Descriptor;
    private int Size_Max;
    private int Size_Min;



    public ORDB4ORA_LongAndRawType(
        String Descriptor,        int Size_Max,        int Size_Min    ) {
        super(
        );
        this.Descriptor = Descriptor;
        this.Size_Max = Size_Max;
        this.Size_Min = Size_Min;
    }


    public String getDescriptor() {
        return Descriptor;
    }

    public void setDescriptor(String Descriptor) {
        this.Descriptor = Descriptor;
    }
    public int getSize_max() {
        return Size_Max;
    }

    public void setSize_max(int Size_Max) {
        this.Size_Max = Size_Max;
    }
    public int getSize_min() {
        return Size_Min;
    }

    public void setSize_min(int Size_Min) {
        this.Size_Min = Size_Min;
    }


}