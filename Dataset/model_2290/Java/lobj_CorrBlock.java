





import java.util.List;
import java.util.ArrayList;

public class lobj_CorrBlock  {

    private String id;





    private List<lobj_TitleMeta> lobj_titlemetas;


    public lobj_CorrBlock(
        String id    ) {
        this.id = id;
        this.lobj_titlemetas = new ArrayList<>();
    }

    public lobj_CorrBlock(
        String id        ArrayList<lobj_TitleMeta> lobj_titlemetas    ) {
        this.id = id;
        this.lobj_titlemetas = lobj_titlemetas;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<lobj_TitleMeta> getLobj_titlemetas() {
        return lobj_titlemetas;
    }

    public void addLobj_titlemeta(Lobj_titlemeta lobj_titlemeta) {
        this.lobj_titlemetas.add(lobj_titlemeta);
    }

}