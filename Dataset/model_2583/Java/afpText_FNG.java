





import java.util.List;
import java.util.ArrayList;

public class afpText_FNG extends structuredField {

    private String PatData;



    public afpText_FNG(
        String PatData    ) {
        super(
        );
        this.PatData = PatData;
    }


    public String getPatdata() {
        return PatData;
    }

    public void setPatdata(String PatData) {
        this.PatData = PatData;
    }


}