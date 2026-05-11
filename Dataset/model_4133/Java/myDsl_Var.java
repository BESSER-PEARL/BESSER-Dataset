





import java.util.List;
import java.util.ArrayList;

public class myDsl_Var extends Expression {

    private String id;



    public myDsl_Var(
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


}