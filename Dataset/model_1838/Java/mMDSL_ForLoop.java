





import java.util.List;
import java.util.ArrayList;

public class mMDSL_ForLoop  {

    private int start;
    private int stop;
    private int interval;





    private List<mMDSL_Statement> mmdsl_statements;




    private mMDSL_LoopStatement mmdsl_loopstatement;


    public mMDSL_ForLoop(
        int start,        int stop,        int interval    ) {
        this.start = start;
        this.stop = stop;
        this.interval = interval;
        this.mmdsl_statements = new ArrayList<>();
    }

    public mMDSL_ForLoop(
        int start,        int stop,        int interval        ArrayList<mMDSL_Statement> mmdsl_statements    ) {
        this.start = start;
        this.stop = stop;
        this.interval = interval;
        this.mmdsl_statements = mmdsl_statements;
    }

    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public int getStop() {
        return stop;
    }

    public void setStop(int stop) {
        this.stop = stop;
    }
    public int getInterval() {
        return interval;
    }

    public void setInterval(int interval) {
        this.interval = interval;
    }

    public List<mMDSL_Statement> getMmdsl_statements() {
        return mmdsl_statements;
    }

    public void addMmdsl_statement(Mmdsl_statement mmdsl_statement) {
        this.mmdsl_statements.add(mmdsl_statement);
    }
    public mMDSL_LoopStatement getMmdsl_loopstatement() {
        return mmdsl_loopstatement;
    }

    public void setMmdsl_loopstatement(mMDSL_LoopStatement mmdsl_loopstatement) {
        this.mmdsl_loopstatement = mmdsl_loopstatement;
    }

}