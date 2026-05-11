





import java.util.List;
import java.util.ArrayList;

public class qm_QualityModelElement  {

    private String qualifiedName;





    private List<qm_Source> qm_sources;


    public qm_QualityModelElement(
        String qualifiedName    ) {
        this.qualifiedName = qualifiedName;
        this.qm_sources = new ArrayList<>();
    }

    public qm_QualityModelElement(
        String qualifiedName        ArrayList<qm_Source> qm_sources    ) {
        this.qualifiedName = qualifiedName;
        this.qm_sources = qm_sources;
    }

    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public List<qm_Source> getQm_sources() {
        return qm_sources;
    }

    public void addQm_source(Qm_source qm_source) {
        this.qm_sources.add(qm_source);
    }

}