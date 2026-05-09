





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_CollectionLiteralExp  {

    private String kind;
    private boolean simpleRange;



    public ocl_expressions_CollectionLiteralExp(
        String kind,        boolean simpleRange    ) {
        this.kind = kind;
        this.simpleRange = simpleRange;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public boolean getSimplerange() {
        return simpleRange;
    }

    public void setSimplerange(boolean simpleRange) {
        this.simpleRange = simpleRange;
    }


}