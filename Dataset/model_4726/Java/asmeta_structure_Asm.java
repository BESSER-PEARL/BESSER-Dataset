





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_Asm extends NamedElement {

    private String isAsynchr;





    private Header header;




    private List<Initialization> initializations;




    private Initialization initialization;


    public asmeta_structure_Asm(
        String isAsynchr    ) {
        super(
        );
        this.isAsynchr = isAsynchr;
        this.initializations = new ArrayList<>();
    }

    public asmeta_structure_Asm(
        String isAsynchr        ArrayList<Initialization> initializations    ) {
        this.isAsynchr = isAsynchr;
        this.initializations = initializations;
    }

    public String getIsasynchr() {
        return isAsynchr;
    }

    public void setIsasynchr(String isAsynchr) {
        this.isAsynchr = isAsynchr;
    }

    public Header getHeader() {
        return header;
    }

    public void setHeader(Header header) {
        this.header = header;
    }
    public List<Initialization> getInitializations() {
        return initializations;
    }

    public void addInitialization(Initialization initialization) {
        this.initializations.add(initialization);
    }
    public Initialization getInitialization() {
        return initialization;
    }

    public void setInitialization(Initialization initialization) {
        this.initialization = initialization;
    }

}