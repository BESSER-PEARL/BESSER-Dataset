





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_PlainMoveEntrySend  {

    private String plainmoveEntry;
    private int plainmoveSeq;
    private String plainmoveSend;





    private MachineLibrary_PlainMove machinelibrary_plainmove;


    public MachineLibrary_PlainMoveEntrySend(
        String plainmoveEntry,        int plainmoveSeq,        String plainmoveSend    ) {
        this.plainmoveEntry = plainmoveEntry;
        this.plainmoveSeq = plainmoveSeq;
        this.plainmoveSend = plainmoveSend;
    }


    public String getPlainmoveentry() {
        return plainmoveEntry;
    }

    public void setPlainmoveentry(String plainmoveEntry) {
        this.plainmoveEntry = plainmoveEntry;
    }
    public int getPlainmoveseq() {
        return plainmoveSeq;
    }

    public void setPlainmoveseq(int plainmoveSeq) {
        this.plainmoveSeq = plainmoveSeq;
    }
    public String getPlainmovesend() {
        return plainmoveSend;
    }

    public void setPlainmovesend(String plainmoveSend) {
        this.plainmoveSend = plainmoveSend;
    }

    public MachineLibrary_PlainMove getMachinelibrary_plainmove() {
        return machinelibrary_plainmove;
    }

    public void setMachinelibrary_plainmove(MachineLibrary_PlainMove machinelibrary_plainmove) {
        this.machinelibrary_plainmove = machinelibrary_plainmove;
    }

}