





import java.util.List;
import java.util.ArrayList;

public class noop_NewInstance extends Expression {






    private List<noop_Index> noop_indexs;




    private noop_Constructor noop_constructor;




    private noop_NoopClass noop_noopclass;


    public noop_NewInstance(
    ) {
        super(
        );
        this.noop_indexs = new ArrayList<>();
    }

    public noop_NewInstance(
        ArrayList<noop_Index> noop_indexs    ) {
        this.noop_indexs = noop_indexs;
    }


    public List<noop_Index> getNoop_indexs() {
        return noop_indexs;
    }

    public void addNoop_index(Noop_index noop_index) {
        this.noop_indexs.add(noop_index);
    }
    public noop_Constructor getNoop_constructor() {
        return noop_constructor;
    }

    public void setNoop_constructor(noop_Constructor noop_constructor) {
        this.noop_constructor = noop_constructor;
    }
    public noop_NoopClass getNoop_noopclass() {
        return noop_noopclass;
    }

    public void setNoop_noopclass(noop_NoopClass noop_noopclass) {
        this.noop_noopclass = noop_noopclass;
    }

}