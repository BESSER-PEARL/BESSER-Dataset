





import java.util.List;
import java.util.ArrayList;

public class siddhi_NOT extends LogicalAbsentStatefulSource, BasicAbsentPatternSource {

    private String not1;





    private siddhi_Keyword siddhi_keyword;




    private siddhi_LogicalAbsentStatefulSource siddhi_logicalabsentstatefulsource;


    public siddhi_NOT(
        String not1    ) {
        super(
        );
        this.not1 = not1;
    }


    public String getNot1() {
        return not1;
    }

    public void setNot1(String not1) {
        this.not1 = not1;
    }

    public siddhi_Keyword getSiddhi_keyword() {
        return siddhi_keyword;
    }

    public void setSiddhi_keyword(siddhi_Keyword siddhi_keyword) {
        this.siddhi_keyword = siddhi_keyword;
    }
    public siddhi_LogicalAbsentStatefulSource getSiddhi_logicalabsentstatefulsource() {
        return siddhi_logicalabsentstatefulsource;
    }

    public void setSiddhi_logicalabsentstatefulsource(siddhi_LogicalAbsentStatefulSource siddhi_logicalabsentstatefulsource) {
        this.siddhi_logicalabsentstatefulsource = siddhi_logicalabsentstatefulsource;
    }

}