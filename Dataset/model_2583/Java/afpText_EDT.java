





import java.util.List;
import java.util.ArrayList;

public class afpText_EDT extends structuredField {

    private String DocName;



    public afpText_EDT(
        String DocName    ) {
        super(
        );
        this.DocName = DocName;
    }


    public String getDocname() {
        return DocName;
    }

    public void setDocname(String DocName) {
        this.DocName = DocName;
    }


}