





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_LongAndRawType extends BuiltInType {

    private int Size_Min;
    private String Descriptor;
    private int Size_Max;



    public ORDB4ORA_LongAndRawType(
        int Size_Min,        String Descriptor,        int Size_Max    ) {
        super(
        );
        this.Size_Min = Size_Min;
        this.Descriptor = Descriptor;
        this.Size_Max = Size_Max;
    }


    public int getSize_min() {
        return Size_Min;
    }

    public void setSize_min(int Size_Min) {
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


}