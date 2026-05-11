





import java.util.List;
import java.util.ArrayList;

public class tracker_Tag  {

    private String id;
    private boolean usainNumberUsed;
    private String idNumber;



    public tracker_Tag(
        String id,        boolean usainNumberUsed,        String idNumber    ) {
        this.id = id;
        this.usainNumberUsed = usainNumberUsed;
        this.idNumber = idNumber;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getUsainnumberused() {
        return usainNumberUsed;
    }

    public void setUsainnumberused(boolean usainNumberUsed) {
        this.usainNumberUsed = usainNumberUsed;
    }
    public String getIdnumber() {
        return idNumber;
    }

    public void setIdnumber(String idNumber) {
        this.idNumber = idNumber;
    }


}