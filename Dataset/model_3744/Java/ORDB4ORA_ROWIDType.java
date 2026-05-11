





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_ROWIDType extends BuiltInType {

    private int Size_Min;
    private int Size_Max;
    private String Descriptor;



    public ORDB4ORA_ROWIDType(
        int Size_Min,        int Size_Max,        String Descriptor    ) {
        super(
        );
        this.Size_Min = Size_Min;
        this.Size_Max = Size_Max;
        this.Descriptor = Descriptor;
    }


    public int getSize_min() {
        return Size_Min;
    }

    public void setSize_min(int Size_Min) {
        this.Size_Min = Size_Min;
    }
    public int getSize_max() {
        return Size_Max;
    }

    public void setSize_max(int Size_Max) {
        this.Size_Max = Size_Max;
    }
    public String getDescriptor() {
        return Descriptor;
    }

    public void setDescriptor(String Descriptor) {
        this.Descriptor = Descriptor;
    }


}