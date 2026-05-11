





import java.util.List;
import java.util.ArrayList;

public class fl_Apply extends Expr {

    private String name;



    public fl_Apply(
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