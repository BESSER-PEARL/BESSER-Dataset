





import java.util.List;
import java.util.ArrayList;

public class RecordBook  {

    private String recordList;





    private Poker poker;


    public RecordBook(
        String recordList    ) {
        this.recordList = recordList;
    }


    public String getRecordlist() {
        return recordList;
    }

    public void setRecordlist(String recordList) {
        this.recordList = recordList;
    }

    public Poker getPoker() {
        return poker;
    }

    public void setPoker(Poker poker) {
        this.poker = poker;
    }

}