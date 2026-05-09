





import java.util.List;
import java.util.ArrayList;

public class trace_Events_Events  {






    private List<C_doCExitEventOccurrence> c_docexiteventoccurrences;




    private List<C_doCEntryEventOccurrence> c_docentryeventoccurrences;




    private List<A_doAExitEventOccurrence> a_doaexiteventoccurrences;


    public trace_Events_Events(
    ) {
        this.c_docexiteventoccurrences = new ArrayList<>();
        this.c_docentryeventoccurrences = new ArrayList<>();
        this.a_doaexiteventoccurrences = new ArrayList<>();
    }

    public trace_Events_Events(
        ArrayList<C_doCExitEventOccurrence> c_docexiteventoccurrences,        ArrayList<C_doCEntryEventOccurrence> c_docentryeventoccurrences,        ArrayList<A_doAExitEventOccurrence> a_doaexiteventoccurrences    ) {
        this.c_docexiteventoccurrences = c_docexiteventoccurrences;
        this.c_docentryeventoccurrences = c_docentryeventoccurrences;
        this.a_doaexiteventoccurrences = a_doaexiteventoccurrences;
    }


    public List<C_doCExitEventOccurrence> getC_docexiteventoccurrences() {
        return c_docexiteventoccurrences;
    }

    public void addC_docexiteventoccurrence(C_docexiteventoccurrence c_docexiteventoccurrence) {
        this.c_docexiteventoccurrences.add(c_docexiteventoccurrence);
    }
    public List<C_doCEntryEventOccurrence> getC_docentryeventoccurrences() {
        return c_docentryeventoccurrences;
    }

    public void addC_docentryeventoccurrence(C_docentryeventoccurrence c_docentryeventoccurrence) {
        this.c_docentryeventoccurrences.add(c_docentryeventoccurrence);
    }
    public List<A_doAExitEventOccurrence> getA_doaexiteventoccurrences() {
        return a_doaexiteventoccurrences;
    }

    public void addA_doaexiteventoccurrence(A_doaexiteventoccurrence a_doaexiteventoccurrence) {
        this.a_doaexiteventoccurrences.add(a_doaexiteventoccurrence);
    }

}