





import java.util.List;
import java.util.ArrayList;

public class ftp_Fault extends FTNode {

    private String description;



    public ftp_Fault(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}