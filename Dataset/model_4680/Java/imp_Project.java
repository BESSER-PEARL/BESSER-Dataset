





import java.util.List;
import java.util.ArrayList;

public class imp_Project extends Expr {

    private boolean ismethodcall;



    public imp_Project(
        boolean ismethodcall    ) {
        super(
        );
        this.ismethodcall = ismethodcall;
    }


    public boolean getIsmethodcall() {
        return ismethodcall;
    }

    public void setIsmethodcall(boolean ismethodcall) {
        this.ismethodcall = ismethodcall;
    }


}