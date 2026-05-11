





import java.util.List;
import java.util.ArrayList;

public class afpText_BPF extends structuredField {

    private String PFName;



    public afpText_BPF(
        String PFName    ) {
        super(
        );
        this.PFName = PFName;
    }


    public String getPfname() {
        return PFName;
    }

    public void setPfname(String PFName) {
        this.PFName = PFName;
    }


}