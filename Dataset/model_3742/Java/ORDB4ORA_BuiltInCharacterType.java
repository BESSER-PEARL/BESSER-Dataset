





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_BuiltInCharacterType extends BuiltInType {

    private int Size_Max;
    private String Descriptor;
    private int Size_Min;
    private int Size_Def;
    private String Semantic;



    public ORDB4ORA_BuiltInCharacterType(
        int Size_Max,        String Descriptor,        int Size_Min,        int Size_Def,        String Semantic    ) {
        super(
        );
        this.Size_Max = Size_Max;
        this.Descriptor = Descriptor;
        this.Size_Min = Size_Min;
        this.Size_Def = Size_Def;
        this.Semantic = Semantic;
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
    public int getSize_min() {
        return Size_Min;
    }

    public void setSize_min(int Size_Min) {
        this.Size_Min = Size_Min;
    }
    public int getSize_def() {
        return Size_Def;
    }

    public void setSize_def(int Size_Def) {
        this.Size_Def = Size_Def;
    }
    public String getSemantic() {
        return Semantic;
    }

    public void setSemantic(String Semantic) {
        this.Semantic = Semantic;
    }


}