





import java.util.List;
import java.util.ArrayList;

public class jcl_statements_Control extends Statement {

    private String endName;



    public jcl_statements_Control(
        String endName    ) {
        super(
        );
        this.endName = endName;
    }


    public String getEndname() {
        return endName;
    }

    public void setEndname(String endName) {
        this.endName = endName;
    }


}