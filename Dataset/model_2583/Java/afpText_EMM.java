





import java.util.List;
import java.util.ArrayList;

public class afpText_EMM extends structuredField {

    private String MMName;



    public afpText_EMM(
        String MMName    ) {
        super(
        );
        this.MMName = MMName;
    }


    public String getMmname() {
        return MMName;
    }

    public void setMmname(String MMName) {
        this.MMName = MMName;
    }


}