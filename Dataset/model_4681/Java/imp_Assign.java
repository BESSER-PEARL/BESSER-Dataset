





import java.util.List;
import java.util.ArrayList;

public class imp_Assign extends Stmt {

    private String name;



    public imp_Assign(
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