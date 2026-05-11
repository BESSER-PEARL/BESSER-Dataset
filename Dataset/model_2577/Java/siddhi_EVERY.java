





import java.util.List;
import java.util.ArrayList;

public class siddhi_EVERY extends EverySequenceSourceChain, AbsentPatternSourceChain, EveryAbsentPatternSource, EveryAbsentSequenceSourceChain, LeftAbsentPatternSource, RightAbsentPatternSource {

    private String every1;





    private siddhi_Keyword siddhi_keyword;




    private siddhi_EveryPatternSourceChain siddhi_everypatternsourcechain;


    public siddhi_EVERY(
        String every1    ) {
        super(
        );
        this.every1 = every1;
    }


    public String getEvery1() {
        return every1;
    }

    public void setEvery1(String every1) {
        this.every1 = every1;
    }

    public siddhi_Keyword getSiddhi_keyword() {
        return siddhi_keyword;
    }

    public void setSiddhi_keyword(siddhi_Keyword siddhi_keyword) {
        this.siddhi_keyword = siddhi_keyword;
    }
    public siddhi_EveryPatternSourceChain getSiddhi_everypatternsourcechain() {
        return siddhi_everypatternsourcechain;
    }

    public void setSiddhi_everypatternsourcechain(siddhi_EveryPatternSourceChain siddhi_everypatternsourcechain) {
        this.siddhi_everypatternsourcechain = siddhi_everypatternsourcechain;
    }

}