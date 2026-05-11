





import java.util.List;
import java.util.ArrayList;

public class siddhi_EveryAbsentPatternSource extends AbsentPatternSourceChain {






    private siddhi_BasicAbsentPatternSource siddhi_basicabsentpatternsource;




    private siddhi_RightAbsentPatternSource siddhi_rightabsentpatternsource;




    private siddhi_LeftAbsentPatternSource siddhi_leftabsentpatternsource;


    public siddhi_EveryAbsentPatternSource(
    ) {
        super(
        );
    }



    public siddhi_BasicAbsentPatternSource getSiddhi_basicabsentpatternsource() {
        return siddhi_basicabsentpatternsource;
    }

    public void setSiddhi_basicabsentpatternsource(siddhi_BasicAbsentPatternSource siddhi_basicabsentpatternsource) {
        this.siddhi_basicabsentpatternsource = siddhi_basicabsentpatternsource;
    }
    public siddhi_RightAbsentPatternSource getSiddhi_rightabsentpatternsource() {
        return siddhi_rightabsentpatternsource;
    }

    public void setSiddhi_rightabsentpatternsource(siddhi_RightAbsentPatternSource siddhi_rightabsentpatternsource) {
        this.siddhi_rightabsentpatternsource = siddhi_rightabsentpatternsource;
    }
    public siddhi_LeftAbsentPatternSource getSiddhi_leftabsentpatternsource() {
        return siddhi_leftabsentpatternsource;
    }

    public void setSiddhi_leftabsentpatternsource(siddhi_LeftAbsentPatternSource siddhi_leftabsentpatternsource) {
        this.siddhi_leftabsentpatternsource = siddhi_leftabsentpatternsource;
    }

}