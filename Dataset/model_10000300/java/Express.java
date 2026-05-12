





import java.util.List;
import java.util.ArrayList;

public class Express  {

    private String SecondSitting;
    private String General;



    public Express(
        String SecondSitting,        String General    ) {
        this.SecondSitting = SecondSitting;
        this.General = General;
    }


    public String getSecondsitting() {
        return SecondSitting;
    }

    public void setSecondsitting(String SecondSitting) {
        this.SecondSitting = SecondSitting;
    }
    public String getGeneral() {
        return General;
    }

    public void setGeneral(String General) {
        this.General = General;
    }


}