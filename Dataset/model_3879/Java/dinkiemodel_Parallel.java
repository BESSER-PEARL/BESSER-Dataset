





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_Parallel extends Statement {

    private int nrOfThreads;





    private List<dinkiemodel_Statement> dinkiemodel_statements;


    public dinkiemodel_Parallel(
        int nrOfThreads    ) {
        super(
        );
        this.nrOfThreads = nrOfThreads;
        this.dinkiemodel_statements = new ArrayList<>();
    }

    public dinkiemodel_Parallel(
        int nrOfThreads        ArrayList<dinkiemodel_Statement> dinkiemodel_statements    ) {
        this.nrOfThreads = nrOfThreads;
        this.dinkiemodel_statements = dinkiemodel_statements;
    }

    public int getNrofthreads() {
        return nrOfThreads;
    }

    public void setNrofthreads(int nrOfThreads) {
        this.nrOfThreads = nrOfThreads;
    }

    public List<dinkiemodel_Statement> getDinkiemodel_statements() {
        return dinkiemodel_statements;
    }

    public void addDinkiemodel_statement(Dinkiemodel_statement dinkiemodel_statement) {
        this.dinkiemodel_statements.add(dinkiemodel_statement);
    }

}