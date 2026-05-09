





import java.util.List;
import java.util.ArrayList;

public class helloworld123_Thing extends NamedElement {

    private int id;





    private List<helloworld123_RelatedTo> helloworld123_relatedtos;




    private helloworld123_RelatedTo helloworld123_relatedto;




    private helloworld123_RelatedTo helloworld123_relatedto;


    public helloworld123_Thing(
        int id    ) {
        super(
        );
        this.id = id;
        this.helloworld123_relatedtos = new ArrayList<>();
    }

    public helloworld123_Thing(
        int id        ArrayList<helloworld123_RelatedTo> helloworld123_relatedtos    ) {
        this.id = id;
        this.helloworld123_relatedtos = helloworld123_relatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<helloworld123_RelatedTo> getHelloworld123_relatedtos() {
        return helloworld123_relatedtos;
    }

    public void addHelloworld123_relatedto(Helloworld123_relatedto helloworld123_relatedto) {
        this.helloworld123_relatedtos.add(helloworld123_relatedto);
    }
    public helloworld123_RelatedTo getHelloworld123_relatedto() {
        return helloworld123_relatedto;
    }

    public void setHelloworld123_relatedto(helloworld123_RelatedTo helloworld123_relatedto) {
        this.helloworld123_relatedto = helloworld123_relatedto;
    }
    public helloworld123_RelatedTo getHelloworld123_relatedto() {
        return helloworld123_relatedto;
    }

    public void setHelloworld123_relatedto(helloworld123_RelatedTo helloworld123_relatedto) {
        this.helloworld123_relatedto = helloworld123_relatedto;
    }

}