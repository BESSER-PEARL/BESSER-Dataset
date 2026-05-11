





import java.util.List;
import java.util.ArrayList;

public class afpText_IMM extends structuredField {

    private String MMPName;



    public afpText_IMM(
        String MMPName    ) {
        super(
        );
        this.MMPName = MMPName;
    }


    public String getMmpname() {
        return MMPName;
    }

    public void setMmpname(String MMPName) {
        this.MMPName = MMPName;
    }


}