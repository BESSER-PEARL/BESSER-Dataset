





import java.util.List;
import java.util.ArrayList;

public class afpText_BDI extends structuredField {

    private String IndxName;



    public afpText_BDI(
        String IndxName    ) {
        super(
        );
        this.IndxName = IndxName;
    }


    public String getIndxname() {
        return IndxName;
    }

    public void setIndxname(String IndxName) {
        this.IndxName = IndxName;
    }


}