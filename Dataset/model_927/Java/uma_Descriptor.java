





import java.util.List;
import java.util.ArrayList;

public class uma_Descriptor extends BreakdownElement {

    private String isSynchronizedWithSource;





    private List<uma_Guidance> uma_guidances;




    private List<uma_Guidance> uma_guidances;


    public uma_Descriptor(
        String isSynchronizedWithSource    ) {
        super(
        );
        this.isSynchronizedWithSource = isSynchronizedWithSource;
        this.uma_guidances = new ArrayList<>();
        this.uma_guidances = new ArrayList<>();
    }

    public uma_Descriptor(
        String isSynchronizedWithSource        ArrayList<uma_Guidance> uma_guidances,        ArrayList<uma_Guidance> uma_guidances    ) {
        this.isSynchronizedWithSource = isSynchronizedWithSource;
        this.uma_guidances = uma_guidances;
        this.uma_guidances = uma_guidances;
    }

    public String getIssynchronizedwithsource() {
        return isSynchronizedWithSource;
    }

    public void setIssynchronizedwithsource(String isSynchronizedWithSource) {
        this.isSynchronizedWithSource = isSynchronizedWithSource;
    }

    public List<uma_Guidance> getUma_guidances() {
        return uma_guidances;
    }

    public void addUma_guidance(Uma_guidance uma_guidance) {
        this.uma_guidances.add(uma_guidance);
    }
    public List<uma_Guidance> getUma_guidances() {
        return uma_guidances;
    }

    public void addUma_guidance(Uma_guidance uma_guidance) {
        this.uma_guidances.add(uma_guidance);
    }

}