





import java.util.List;
import java.util.ArrayList;

public class railDsl_Signal extends SegmentObject {

    private boolean shunting;
    private boolean main;





    private railDsl_Signal raildsl_signal;


    public railDsl_Signal(
        boolean shunting,        boolean main    ) {
        super(
        );
        this.shunting = shunting;
        this.main = main;
    }


    public boolean getShunting() {
        return shunting;
    }

    public void setShunting(boolean shunting) {
        this.shunting = shunting;
    }
    public boolean getMain() {
        return main;
    }

    public void setMain(boolean main) {
        this.main = main;
    }

    public railDsl_Signal getRaildsl_signal() {
        return raildsl_signal;
    }

    public void setRaildsl_signal(railDsl_Signal raildsl_signal) {
        this.raildsl_signal = raildsl_signal;
    }

}