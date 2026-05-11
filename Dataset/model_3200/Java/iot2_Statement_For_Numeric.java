





import java.util.List;
import java.util.ArrayList;

public class iot2_Statement_For_Numeric extends Statement {

    private String iteratorName;





    private iot2_Block iot2_block;


    public iot2_Statement_For_Numeric(
        String iteratorName    ) {
        super(
        );
        this.iteratorName = iteratorName;
    }


    public String getIteratorname() {
        return iteratorName;
    }

    public void setIteratorname(String iteratorName) {
        this.iteratorName = iteratorName;
    }

    public iot2_Block getIot2_block() {
        return iot2_block;
    }

    public void setIot2_block(iot2_Block iot2_block) {
        this.iot2_block = iot2_block;
    }

}