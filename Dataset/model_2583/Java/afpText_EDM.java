





import java.util.List;
import java.util.ArrayList;

public class afpText_EDM extends structuredField {

    private String DMName;



    public afpText_EDM(
        String DMName    ) {
        super(
        );
        this.DMName = DMName;
    }


    public String getDmname() {
        return DMName;
    }

    public void setDmname(String DMName) {
        this.DMName = DMName;
    }


}