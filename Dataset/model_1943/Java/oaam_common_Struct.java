





import java.util.List;
import java.util.ArrayList;

public class oaam_common_Struct extends DataTypeA {

    private boolean isAbstract;
    private int alignment;



    public oaam_common_Struct(
        boolean isAbstract,        int alignment    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.alignment = alignment;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public int getAlignment() {
        return alignment;
    }

    public void setAlignment(int alignment) {
        this.alignment = alignment;
    }


}