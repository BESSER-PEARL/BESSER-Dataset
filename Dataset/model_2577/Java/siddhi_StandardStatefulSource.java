





import java.util.List;
import java.util.ArrayList;

public class siddhi_StandardStatefulSource extends SequenceSource, SequenceCollectionStatefulSource, Source1OrStandardStatefulSource, PatternCollectionStatefulSource {

    private String zero_or_more;
    private String one_or_more;
    private String zero_or_one;





    private siddhi_LogicalStatefulSource siddhi_logicalstatefulsource;


    public siddhi_StandardStatefulSource(
        String zero_or_more,        String one_or_more,        String zero_or_one    ) {
        super(
        );
        this.zero_or_more = zero_or_more;
        this.one_or_more = one_or_more;
        this.zero_or_one = zero_or_one;
    }


    public String getZero_or_more() {
        return zero_or_more;
    }

    public void setZero_or_more(String zero_or_more) {
        this.zero_or_more = zero_or_more;
    }
    public String getOne_or_more() {
        return one_or_more;
    }

    public void setOne_or_more(String one_or_more) {
        this.one_or_more = one_or_more;
    }
    public String getZero_or_one() {
        return zero_or_one;
    }

    public void setZero_or_one(String zero_or_one) {
        this.zero_or_one = zero_or_one;
    }

    public siddhi_LogicalStatefulSource getSiddhi_logicalstatefulsource() {
        return siddhi_logicalstatefulsource;
    }

    public void setSiddhi_logicalstatefulsource(siddhi_LogicalStatefulSource siddhi_logicalstatefulsource) {
        this.siddhi_logicalstatefulsource = siddhi_logicalstatefulsource;
    }

}