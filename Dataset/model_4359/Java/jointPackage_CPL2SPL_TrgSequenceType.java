





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgSequenceType extends TrgTypeExpression {

    private String type;
    private int size;
    private String modifier;



    public jointPackage_CPL2SPL_TrgSequenceType(
        String type,        int size,        String modifier    ) {
        super(
        );
        this.type = type;
        this.size = size;
        this.modifier = modifier;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }


}