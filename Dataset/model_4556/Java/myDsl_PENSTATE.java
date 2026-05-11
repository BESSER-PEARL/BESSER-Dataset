





import java.util.List;
import java.util.ArrayList;

public class myDsl_PENSTATE extends CMD {

    private String penState;



    public myDsl_PENSTATE(
        String penState    ) {
        super(
        );
        this.penState = penState;
    }


    public String getPenstate() {
        return penState;
    }

    public void setPenstate(String penState) {
        this.penState = penState;
    }


}