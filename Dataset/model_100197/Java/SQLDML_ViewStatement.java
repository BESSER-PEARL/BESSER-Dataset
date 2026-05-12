





import java.util.List;
import java.util.ArrayList;

public class SQLDML_ViewStatement extends Statement {

    private String name;



    public SQLDML_ViewStatement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}