





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_BuiltInNumberType extends BuiltInType {

    private int Scale_Min;
    private int Precision_Mn;
    private int Precision_Max;
    private int Scale_Max;
    private String Descriptor;



    public ORDB4ORA_BuiltInNumberType(
        int Scale_Min,        int Precision_Mn,        int Precision_Max,        int Scale_Max,        String Descriptor    ) {
        super(
        );
        this.Scale_Min = Scale_Min;
        this.Precision_Mn = Precision_Mn;
        this.Precision_Max = Precision_Max;
        this.Scale_Max = Scale_Max;
        this.Descriptor = Descriptor;
    }


    public int getScale_min() {
        return Scale_Min;
    }

    public void setScale_min(int Scale_Min) {
        this.Scale_Min = Scale_Min;
    }
    public int getPrecision_mn() {
        return Precision_Mn;
    }

    public void setPrecision_mn(int Precision_Mn) {
        this.Precision_Mn = Precision_Mn;
    }
    public int getPrecision_max() {
        return Precision_Max;
    }

    public void setPrecision_max(int Precision_Max) {
        this.Precision_Max = Precision_Max;
    }
    public int getScale_max() {
        return Scale_Max;
    }

    public void setScale_max(int Scale_Max) {
        this.Scale_Max = Scale_Max;
    }
    public String getDescriptor() {
        return Descriptor;
    }

    public void setDescriptor(String Descriptor) {
        this.Descriptor = Descriptor;
    }


}