





import java.util.List;
import java.util.ArrayList;

public class afpText_EDI extends structuredField {

    private String IndxName;



    public afpText_EDI(
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