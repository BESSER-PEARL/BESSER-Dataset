





import java.util.List;
import java.util.ArrayList;

public class expressions_NumberValue extends AExpression {

    private String numValue;



    public expressions_NumberValue(
        String numValue    ) {
        super(
        );
        this.numValue = numValue;
    }


    public String getNumvalue() {
        return numValue;
    }

    public void setNumvalue(String numValue) {
        this.numValue = numValue;
    }


}