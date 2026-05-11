





import java.util.List;
import java.util.ArrayList;

public class debugSeq_SequenceCall extends Expression {

    private String seqname;



    public debugSeq_SequenceCall(
        String seqname    ) {
        super(
        );
        this.seqname = seqname;
    }


    public String getSeqname() {
        return seqname;
    }

    public void setSeqname(String seqname) {
        this.seqname = seqname;
    }


}