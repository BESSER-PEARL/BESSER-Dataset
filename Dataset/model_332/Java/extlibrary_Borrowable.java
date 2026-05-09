





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Borrowable  {

    private int copies;





    private List<extlibrary__15NQcW60EeGkd4g88tZXfA> extlibrary__15nqcw60eegkd4g88tzxfas;


    public extlibrary_Borrowable(
        int copies    ) {
        this.copies = copies;
        this.extlibrary__15nqcw60eegkd4g88tzxfas = new ArrayList<>();
    }

    public extlibrary_Borrowable(
        int copies        ArrayList<extlibrary__15NQcW60EeGkd4g88tZXfA> extlibrary__15nqcw60eegkd4g88tzxfas    ) {
        this.copies = copies;
        this.extlibrary__15nqcw60eegkd4g88tzxfas = extlibrary__15nqcw60eegkd4g88tzxfas;
    }

    public int getCopies() {
        return copies;
    }

    public void setCopies(int copies) {
        this.copies = copies;
    }

    public List<extlibrary__15NQcW60EeGkd4g88tZXfA> getExtlibrary__15nqcw60eegkd4g88tzxfas() {
        return extlibrary__15nqcw60eegkd4g88tzxfas;
    }

    public void addExtlibrary__15nqcw60eegkd4g88tzxfa(Extlibrary__15nqcw60eegkd4g88tzxfa extlibrary__15nqcw60eegkd4g88tzxfa) {
        this.extlibrary__15nqcw60eegkd4g88tzxfas.add(extlibrary__15nqcw60eegkd4g88tzxfa);
    }

}