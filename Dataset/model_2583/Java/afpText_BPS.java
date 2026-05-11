





import java.util.List;
import java.util.ArrayList;

public class afpText_BPS extends structuredField {

    private String PsegName;



    public afpText_BPS(
        String PsegName    ) {
        super(
        );
        this.PsegName = PsegName;
    }


    public String getPsegname() {
        return PsegName;
    }

    public void setPsegname(String PsegName) {
        this.PsegName = PsegName;
    }


}