





import java.util.List;
import java.util.ArrayList;

public class hello121_Thing extends NamedElement {

    private int id;





    private hello121_Base hello121_base;


    public hello121_Thing(
        int id    ) {
        super(
        );
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public hello121_Base getHello121_base() {
        return hello121_base;
    }

    public void setHello121_base(hello121_Base hello121_base) {
        this.hello121_base = hello121_base;
    }

}