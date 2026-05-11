





import java.util.List;
import java.util.ArrayList;

public class SPL_SequenceType extends TypeExpression {

    private String modifier;
    private int size;
    private String type;



    public SPL_SequenceType(
        String modifier,        int size,        String type    ) {
        super(
        );
        this.modifier = modifier;
        this.size = size;
        this.type = type;
    }


    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}