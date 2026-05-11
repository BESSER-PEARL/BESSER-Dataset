





import java.util.List;
import java.util.ArrayList;

public class mathCompiler_Var extends Expression {

    private String id;



    public mathCompiler_Var(
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