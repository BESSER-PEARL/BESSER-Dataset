





import java.util.List;
import java.util.ArrayList;

public class afpText_EPM extends structuredField {

    private String PMName;



    public afpText_EPM(
        String PMName    ) {
        super(
        );
        this.PMName = PMName;
    }


    public String getPmname() {
        return PMName;
    }

    public void setPmname(String PMName) {
        this.PMName = PMName;
    }


}