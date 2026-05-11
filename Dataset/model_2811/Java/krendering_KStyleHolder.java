





import java.util.List;
import java.util.ArrayList;

public class krendering_KStyleHolder  {

    private String id;





    private krendering_KRenderingLibrary krendering_krenderinglibrary;




    private List<krendering_KStyle> krendering_kstyles;


    public krendering_KStyleHolder(
        String id    ) {
        this.id = id;
        this.krendering_kstyles = new ArrayList<>();
    }

    public krendering_KStyleHolder(
        String id        ArrayList<krendering_KStyle> krendering_kstyles    ) {
        this.id = id;
        this.krendering_kstyles = krendering_kstyles;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public krendering_KRenderingLibrary getKrendering_krenderinglibrary() {
        return krendering_krenderinglibrary;
    }

    public void setKrendering_krenderinglibrary(krendering_KRenderingLibrary krendering_krenderinglibrary) {
        this.krendering_krenderinglibrary = krendering_krenderinglibrary;
    }
    public List<krendering_KStyle> getKrendering_kstyles() {
        return krendering_kstyles;
    }

    public void addKrendering_kstyle(Krendering_kstyle krendering_kstyle) {
        this.krendering_kstyles.add(krendering_kstyle);
    }

}