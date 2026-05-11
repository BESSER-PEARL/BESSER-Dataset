





import java.util.List;
import java.util.ArrayList;

public class afpText_EPG extends structuredField {

    private String PageName;



    public afpText_EPG(
        String PageName    ) {
        super(
        );
        this.PageName = PageName;
    }


    public String getPagename() {
        return PageName;
    }

    public void setPagename(String PageName) {
        this.PageName = PageName;
    }


}