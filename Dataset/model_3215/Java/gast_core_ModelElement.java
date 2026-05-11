





import java.util.List;
import java.util.ArrayList;

public class gast_core_ModelElement extends Identifier {

    private String status;
    private int sissyId;



    public gast_core_ModelElement(
        String status,        int sissyId    ) {
        super(
        );
        this.status = status;
        this.sissyId = sissyId;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getSissyid() {
        return sissyId;
    }

    public void setSissyid(int sissyId) {
        this.sissyId = sissyId;
    }


}