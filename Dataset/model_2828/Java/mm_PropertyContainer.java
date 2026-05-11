





import java.util.List;
import java.util.ArrayList;

public class mm_PropertyContainer  {






    private List<mm_Property> mm_propertys;


    public mm_PropertyContainer(
    ) {
        this.mm_propertys = new ArrayList<>();
    }

    public mm_PropertyContainer(
        ArrayList<mm_Property> mm_propertys    ) {
        this.mm_propertys = mm_propertys;
    }


    public List<mm_Property> getMm_propertys() {
        return mm_propertys;
    }

    public void addMm_property(Mm_property mm_property) {
        this.mm_propertys.add(mm_property);
    }

}