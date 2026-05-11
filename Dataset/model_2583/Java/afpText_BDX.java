





import java.util.List;
import java.util.ArrayList;

public class afpText_BDX extends structuredField {

    private String DMXName;



    public afpText_BDX(
        String DMXName    ) {
        super(
        );
        this.DMXName = DMXName;
    }


    public String getDmxname() {
        return DMXName;
    }

    public void setDmxname(String DMXName) {
        this.DMXName = DMXName;
    }


}