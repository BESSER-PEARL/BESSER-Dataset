





import java.util.List;
import java.util.ArrayList;

public class profile_UsageContext  {

    private String identifier;
    private String statusDate;
    private String status;



    public profile_UsageContext(
        String identifier,        String statusDate,        String status    ) {
        this.identifier = identifier;
        this.statusDate = statusDate;
        this.status = status;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getStatusdate() {
        return statusDate;
    }

    public void setStatusdate(String statusDate) {
        this.statusDate = statusDate;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}