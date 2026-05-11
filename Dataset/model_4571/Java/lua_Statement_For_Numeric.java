





import java.util.List;
import java.util.ArrayList;

public class lua_Statement_For_Numeric extends Statement {

    private String iteratorName;



    public lua_Statement_For_Numeric(
        String iteratorName    ) {
        super(
        );
        this.iteratorName = iteratorName;
    }


    public String getIteratorname() {
        return iteratorName;
    }

    public void setIteratorname(String iteratorName) {
        this.iteratorName = iteratorName;
    }


}