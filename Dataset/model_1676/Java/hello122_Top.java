





import java.util.List;
import java.util.ArrayList;

public class hello122_Top  {

    private String id;





    private List<hello122_Child> hello122_childs;




    private hello122_Base hello122_base;


    public hello122_Top(
        String id    ) {
        this.id = id;
        this.hello122_childs = new ArrayList<>();
    }

    public hello122_Top(
        String id        ArrayList<hello122_Child> hello122_childs    ) {
        this.id = id;
        this.hello122_childs = hello122_childs;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<hello122_Child> getHello122_childs() {
        return hello122_childs;
    }

    public void addHello122_child(Hello122_child hello122_child) {
        this.hello122_childs.add(hello122_child);
    }
    public hello122_Base getHello122_base() {
        return hello122_base;
    }

    public void setHello122_base(hello122_Base hello122_base) {
        this.hello122_base = hello122_base;
    }

}