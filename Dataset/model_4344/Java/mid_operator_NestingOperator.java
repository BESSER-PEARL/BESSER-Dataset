





import java.util.List;
import java.util.ArrayList;

public class mid_operator_NestingOperator extends Operator {

    private String nestedMIDPath;



    public mid_operator_NestingOperator(
        String nestedMIDPath    ) {
        super(
        );
        this.nestedMIDPath = nestedMIDPath;
    }


    public String getNestedmidpath() {
        return nestedMIDPath;
    }

    public void setNestedmidpath(String nestedMIDPath) {
        this.nestedMIDPath = nestedMIDPath;
    }


}