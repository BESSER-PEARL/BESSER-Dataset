





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XTypeLiteral extends XExpression {

    private String arrayDimensions;



    public model_xbase_XTypeLiteral(
        String arrayDimensions    ) {
        super(
        );
        this.arrayDimensions = arrayDimensions;
    }


    public String getArraydimensions() {
        return arrayDimensions;
    }

    public void setArraydimensions(String arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }


}