





import java.util.List;
import java.util.ArrayList;

public class afpText_EDG extends structuredField {

    private String DEGName;



    public afpText_EDG(
        String DEGName    ) {
        super(
        );
        this.DEGName = DEGName;
    }


    public String getDegname() {
        return DEGName;
    }

    public void setDegname(String DEGName) {
        this.DEGName = DEGName;
    }


}