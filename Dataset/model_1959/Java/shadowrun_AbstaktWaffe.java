





import java.util.List;
import java.util.ArrayList;

public class shadowrun_AbstaktWaffe extends AbstaktGegenstand {

    private String schadenscode;



    public shadowrun_AbstaktWaffe(
        String schadenscode    ) {
        super(
        );
        this.schadenscode = schadenscode;
    }


    public String getSchadenscode() {
        return schadenscode;
    }

    public void setSchadenscode(String schadenscode) {
        this.schadenscode = schadenscode;
    }


}