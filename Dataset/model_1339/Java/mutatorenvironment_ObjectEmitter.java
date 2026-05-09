





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_ObjectEmitter  {

    private None name;





    private mutatorenvironment_EClass mutatorenvironment_eclass;




    private List<mutatorenvironment_EClass> mutatorenvironment_eclasss;


    public mutatorenvironment_ObjectEmitter(
        None name    ) {
        this.name = name;
        this.mutatorenvironment_eclasss = new ArrayList<>();
    }

    public mutatorenvironment_ObjectEmitter(
        None name        ArrayList<mutatorenvironment_EClass> mutatorenvironment_eclasss    ) {
        this.name = name;
        this.mutatorenvironment_eclasss = mutatorenvironment_eclasss;
    }

    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }

    public mutatorenvironment_EClass getMutatorenvironment_eclass() {
        return mutatorenvironment_eclass;
    }

    public void setMutatorenvironment_eclass(mutatorenvironment_EClass mutatorenvironment_eclass) {
        this.mutatorenvironment_eclass = mutatorenvironment_eclass;
    }
    public List<mutatorenvironment_EClass> getMutatorenvironment_eclasss() {
        return mutatorenvironment_eclasss;
    }

    public void addMutatorenvironment_eclass(Mutatorenvironment_eclass mutatorenvironment_eclass) {
        this.mutatorenvironment_eclasss.add(mutatorenvironment_eclass);
    }

}