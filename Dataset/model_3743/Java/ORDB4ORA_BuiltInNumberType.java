





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_BuiltInNumberType extends BuiltInType {

    private String Descriptor;
    private int Precision_Mn;
    private int Scale_Min;
    private int Scale_Max;
    private int Precision_Max;



    public ORDB4ORA_BuiltInNumberType(
        String Descriptor,        int Precision_Mn,        int Scale_Min,        int Scale_Max,        int Precision_Max    ) {
        super(
        );
        this.Descriptor = Descriptor;
        this.Precision_Mn = Precision_Mn;
        this.Scale_Min = Scale_Min;
        this.Scale_Max = Scale_Max;
        this.Precision_Max = Precision_Max;
    }


    public String getDescriptor() {
        return Descriptor;
    }

    public void setDescriptor(String Descriptor) {
        this.Descriptor = Descriptor;
    }
    public int getPrecision_mn() {
        return Precision_Mn;
    }

    public void setPrecision_mn(int Precision_Mn) {
        this.Precision_Mn = Precision_Mn;
    }
    public int getScale_min() {
        return Scale_Min;
    }

    public void setScale_min(int Scale_Min) {
        this.Scale_Min = Scale_Min;
    }
    public int getScale_max() {
        return Scale_Max;
    }

    public void setScale_max(int Scale_Max) {
        this.Scale_Max = Scale_Max;
    }
    public int getPrecision_max() {
        return Precision_Max;
    }

    public void setPrecision_max(int Precision_Max) {
        this.Precision_Max = Precision_Max;
    }


}