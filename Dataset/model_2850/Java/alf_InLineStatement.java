





import java.util.List;
import java.util.ArrayList;

public class alf_InLineStatement extends Statement {

    private String id;





    private alf_Name alf_name;


    public alf_InLineStatement(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }

}