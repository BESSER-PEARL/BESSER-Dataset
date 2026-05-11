





import java.util.List;
import java.util.ArrayList;

public class debugSeq_Sequence  {

    private String pname;
    private String name;
    private String info;
    private String disable;





    private debugSeq_Sequences debugseq_sequences;


    public debugSeq_Sequence(
        String pname,        String name,        String info,        String disable    ) {
        this.pname = pname;
        this.name = name;
        this.info = info;
        this.disable = disable;
    }


    public String getPname() {
        return pname;
    }

    public void setPname(String pname) {
        this.pname = pname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public String getDisable() {
        return disable;
    }

    public void setDisable(String disable) {
        this.disable = disable;
    }

    public debugSeq_Sequences getDebugseq_sequences() {
        return debugseq_sequences;
    }

    public void setDebugseq_sequences(debugSeq_Sequences debugseq_sequences) {
        this.debugseq_sequences = debugseq_sequences;
    }

}