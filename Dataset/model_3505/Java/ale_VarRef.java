





import java.util.List;
import java.util.ArrayList;

public class ale_VarRef extends Expression {

    private String ID;



    public ale_VarRef(
        String ID    ) {
        super(
        );
        this.ID = ID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }


}