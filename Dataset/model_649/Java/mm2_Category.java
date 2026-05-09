





import java.util.List;
import java.util.ArrayList;

public class mm2_Category  {

    private String name;





    private List<mm2_Category> mm2_categorys;




    private List<mm2_Medium> mm2_mediums;




    private mm2_Library mm2_library;


    public mm2_Category(
        String name    ) {
        this.name = name;
        this.mm2_categorys = new ArrayList<>();
        this.mm2_mediums = new ArrayList<>();
    }

    public mm2_Category(
        String name        ArrayList<mm2_Category> mm2_categorys,        ArrayList<mm2_Medium> mm2_mediums    ) {
        this.name = name;
        this.mm2_categorys = mm2_categorys;
        this.mm2_mediums = mm2_mediums;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mm2_Category> getMm2_categorys() {
        return mm2_categorys;
    }

    public void addMm2_category(Mm2_category mm2_category) {
        this.mm2_categorys.add(mm2_category);
    }
    public List<mm2_Medium> getMm2_mediums() {
        return mm2_mediums;
    }

    public void addMm2_medium(Mm2_medium mm2_medium) {
        this.mm2_mediums.add(mm2_medium);
    }
    public mm2_Library getMm2_library() {
        return mm2_library;
    }

    public void setMm2_library(mm2_Library mm2_library) {
        this.mm2_library = mm2_library;
    }

}