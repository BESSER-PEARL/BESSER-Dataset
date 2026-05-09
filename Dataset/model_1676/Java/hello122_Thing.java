





import java.util.List;
import java.util.ArrayList;

public class hello122_Thing extends NamedElement {

    private int id;





    private hello122_Base hello122_base;




    private hello122_RelatedTo hello122_relatedto;




    private List<hello122_RelatedTo> hello122_relatedtos;




    private hello122_RelatedTo hello122_relatedto;


    public hello122_Thing(
        int id    ) {
        super(
        );
        this.id = id;
        this.hello122_relatedtos = new ArrayList<>();
    }

    public hello122_Thing(
        int id        ArrayList<hello122_RelatedTo> hello122_relatedtos    ) {
        this.id = id;
        this.hello122_relatedtos = hello122_relatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public hello122_Base getHello122_base() {
        return hello122_base;
    }

    public void setHello122_base(hello122_Base hello122_base) {
        this.hello122_base = hello122_base;
    }
    public hello122_RelatedTo getHello122_relatedto() {
        return hello122_relatedto;
    }

    public void setHello122_relatedto(hello122_RelatedTo hello122_relatedto) {
        this.hello122_relatedto = hello122_relatedto;
    }
    public List<hello122_RelatedTo> getHello122_relatedtos() {
        return hello122_relatedtos;
    }

    public void addHello122_relatedto(Hello122_relatedto hello122_relatedto) {
        this.hello122_relatedtos.add(hello122_relatedto);
    }
    public hello122_RelatedTo getHello122_relatedto() {
        return hello122_relatedto;
    }

    public void setHello122_relatedto(hello122_RelatedTo hello122_relatedto) {
        this.hello122_relatedto = hello122_relatedto;
    }

}