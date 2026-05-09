





import java.util.List;
import java.util.ArrayList;

public class mm2_Member  {

    private String name;





    private mm2_Library mm2_library;




    private List<mm2_Medium> mm2_mediums;


    public mm2_Member(
        String name    ) {
        this.name = name;
        this.mm2_mediums = new ArrayList<>();
    }

    public mm2_Member(
        String name        ArrayList<mm2_Medium> mm2_mediums    ) {
        this.name = name;
        this.mm2_mediums = mm2_mediums;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mm2_Library getMm2_library() {
        return mm2_library;
    }

    public void setMm2_library(mm2_Library mm2_library) {
        this.mm2_library = mm2_library;
    }
    public List<mm2_Medium> getMm2_mediums() {
        return mm2_mediums;
    }

    public void addMm2_medium(Mm2_medium mm2_medium) {
        this.mm2_mediums.add(mm2_medium);
    }

}