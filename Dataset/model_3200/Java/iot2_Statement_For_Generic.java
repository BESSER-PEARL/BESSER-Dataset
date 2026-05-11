





import java.util.List;
import java.util.ArrayList;

public class iot2_Statement_For_Generic extends Statement {

    private String names;





    private iot2_Block iot2_block;


    public iot2_Statement_For_Generic(
        String names    ) {
        super(
        );
        this.names = names;
    }


    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public iot2_Block getIot2_block() {
        return iot2_block;
    }

    public void setIot2_block(iot2_Block iot2_block) {
        this.iot2_block = iot2_block;
    }

}