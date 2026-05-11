





import java.util.List;
import java.util.ArrayList;

public class railDsl_TrainRoute extends Declaration {

    private boolean locked;
    private String kind;





    private railDsl_Signal raildsl_signal;




    private railDsl_Signal raildsl_signal;




    private railDsl_TrainRoute raildsl_trainroute;


    public railDsl_TrainRoute(
        boolean locked,        String kind    ) {
        super(
        );
        this.locked = locked;
        this.kind = kind;
    }


    public boolean getLocked() {
        return locked;
    }

    public void setLocked(boolean locked) {
        this.locked = locked;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public railDsl_Signal getRaildsl_signal() {
        return raildsl_signal;
    }

    public void setRaildsl_signal(railDsl_Signal raildsl_signal) {
        this.raildsl_signal = raildsl_signal;
    }
    public railDsl_Signal getRaildsl_signal() {
        return raildsl_signal;
    }

    public void setRaildsl_signal(railDsl_Signal raildsl_signal) {
        this.raildsl_signal = raildsl_signal;
    }
    public railDsl_TrainRoute getRaildsl_trainroute() {
        return raildsl_trainroute;
    }

    public void setRaildsl_trainroute(railDsl_TrainRoute raildsl_trainroute) {
        this.raildsl_trainroute = raildsl_trainroute;
    }

}