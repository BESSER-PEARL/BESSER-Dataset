





import java.util.List;
import java.util.ArrayList;

public class afpText_BDT extends structuredField {

    private String Reserved;
    private String DocName;



    public afpText_BDT(
        String Reserved,        String DocName    ) {
        super(
        );
        this.Reserved = Reserved;
        this.DocName = DocName;
    }


    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getDocname() {
        return DocName;
    }

    public void setDocname(String DocName) {
        this.DocName = DocName;
    }


}