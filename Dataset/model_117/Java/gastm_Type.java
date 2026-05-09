





import java.util.List;
import java.util.ArrayList;

public class gastm_Type extends GASTMSyntaxObject {

    private String isConst;



    public gastm_Type(
        String isConst    ) {
        super(
        );
        this.isConst = isConst;
    }


    public String getIsconst() {
        return isConst;
    }

    public void setIsconst(String isConst) {
        this.isConst = isConst;
    }


}