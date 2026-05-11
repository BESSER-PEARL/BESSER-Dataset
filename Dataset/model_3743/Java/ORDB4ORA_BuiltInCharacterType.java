





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_BuiltInCharacterType extends BuiltInType {

    private String Descriptor;
    private int Size_Max;
    private int Size_Min;
    private String Semantic;
    private int Size_Def;



    public ORDB4ORA_BuiltInCharacterType(
        String Descriptor,        int Size_Max,        int Size_Min,        String Semantic,        int Size_Def    ) {
        super(
        );
        this.Descriptor = Descriptor;
        this.Size_Max = Size_Max;
        this.Size_Min = Size_Min;
        this.Semantic = Semantic;
        this.Size_Def = Size_Def;
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
    public String getSemantic() {
        return Semantic;
    }

    public void setSemantic(String Semantic) {
        this.Semantic = Semantic;
    }
    public int getSize_def() {
        return Size_Def;
    }

    public void setSize_def(int Size_Def) {
        this.Size_Def = Size_Def;
    }


}