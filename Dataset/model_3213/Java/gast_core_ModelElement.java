





import java.util.List;
import java.util.ArrayList;

public class gast_core_ModelElement extends Identifier {

    private int sissyId;
    private String status;



    public gast_core_ModelElement(
        int sissyId,        String status    ) {
        super(
        );
        this.sissyId = sissyId;
        this.status = status;
    }


    public int getSissyid() {
        return sissyId;
    }

    public void setSissyid(int sissyId) {
        this.sissyId = sissyId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}