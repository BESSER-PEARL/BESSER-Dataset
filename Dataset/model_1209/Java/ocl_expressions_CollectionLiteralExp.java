





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_CollectionLiteralExp  {

    private boolean simpleRange;
    private String kind;



    public ocl_expressions_CollectionLiteralExp(
        boolean simpleRange,        String kind    ) {
        this.simpleRange = simpleRange;
        this.kind = kind;
    }


    public boolean getSimplerange() {
        return simpleRange;
    }

    public void setSimplerange(boolean simpleRange) {
        this.simpleRange = simpleRange;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}