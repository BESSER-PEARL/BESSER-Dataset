





import java.util.List;
import java.util.ArrayList;

public class siddhi_PatternSource  {






    private siddhi_PatternSourceChain siddhi_patternsourcechain;




    private siddhi_LogicalAbsentStatefulSource siddhi_logicalabsentstatefulsource;




    private siddhi_StandardStatefulSource siddhi_standardstatefulsource;




    private siddhi_LogicalStatefulSource siddhi_logicalstatefulsource;


    public siddhi_PatternSource(
    ) {
    }



    public siddhi_PatternSourceChain getSiddhi_patternsourcechain() {
        return siddhi_patternsourcechain;
    }

    public void setSiddhi_patternsourcechain(siddhi_PatternSourceChain siddhi_patternsourcechain) {
        this.siddhi_patternsourcechain = siddhi_patternsourcechain;
    }
    public siddhi_LogicalAbsentStatefulSource getSiddhi_logicalabsentstatefulsource() {
        return siddhi_logicalabsentstatefulsource;
    }

    public void setSiddhi_logicalabsentstatefulsource(siddhi_LogicalAbsentStatefulSource siddhi_logicalabsentstatefulsource) {
        this.siddhi_logicalabsentstatefulsource = siddhi_logicalabsentstatefulsource;
    }
    public siddhi_StandardStatefulSource getSiddhi_standardstatefulsource() {
        return siddhi_standardstatefulsource;
    }

    public void setSiddhi_standardstatefulsource(siddhi_StandardStatefulSource siddhi_standardstatefulsource) {
        this.siddhi_standardstatefulsource = siddhi_standardstatefulsource;
    }
    public siddhi_LogicalStatefulSource getSiddhi_logicalstatefulsource() {
        return siddhi_logicalstatefulsource;
    }

    public void setSiddhi_logicalstatefulsource(siddhi_LogicalStatefulSource siddhi_logicalstatefulsource) {
        this.siddhi_logicalstatefulsource = siddhi_logicalstatefulsource;
    }

}