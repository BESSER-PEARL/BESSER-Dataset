





import java.util.List;
import java.util.ArrayList;

public class fl_Literal extends Expr {

    private String info;



    public fl_Literal(
        String info    ) {
        super(
        );
        this.info = info;
    }


    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }


}