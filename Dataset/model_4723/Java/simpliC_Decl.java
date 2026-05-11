





import java.util.List;
import java.util.ArrayList;

public class simpliC_Decl extends Stmt {

    private String name;



    public simpliC_Decl(
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