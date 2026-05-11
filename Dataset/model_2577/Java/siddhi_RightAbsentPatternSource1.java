





import java.util.List;
import java.util.ArrayList;

public class siddhi_RightAbsentPatternSource1 extends RightAbsentPatternSource {

    private String fb;





    private siddhi_EveryAbsentPatternSource siddhi_everyabsentpatternsource;




    private siddhi_RightAbsentPatternSource siddhi_rightabsentpatternsource;


    public siddhi_RightAbsentPatternSource1(
        String fb    ) {
        super(
        );
        this.fb = fb;
    }


    public String getFb() {
        return fb;
    }

    public void setFb(String fb) {
        this.fb = fb;
    }

    public siddhi_EveryAbsentPatternSource getSiddhi_everyabsentpatternsource() {
        return siddhi_everyabsentpatternsource;
    }

    public void setSiddhi_everyabsentpatternsource(siddhi_EveryAbsentPatternSource siddhi_everyabsentpatternsource) {
        this.siddhi_everyabsentpatternsource = siddhi_everyabsentpatternsource;
    }
    public siddhi_RightAbsentPatternSource getSiddhi_rightabsentpatternsource() {
        return siddhi_rightabsentpatternsource;
    }

    public void setSiddhi_rightabsentpatternsource(siddhi_RightAbsentPatternSource siddhi_rightabsentpatternsource) {
        this.siddhi_rightabsentpatternsource = siddhi_rightabsentpatternsource;
    }

}