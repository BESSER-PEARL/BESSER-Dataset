





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJClass extends SJNamedElement {






    private smallJava_SJMember smalljava_sjmember;




    private smallJava_SJClass smalljava_sjclass;




    private List<smallJava_SJMember> smalljava_sjmembers;




    private smallJava_SJProgram smalljava_sjprogram;




    private smallJava_SJNew smalljava_sjnew;




    private smallJava_SJSymbol smalljava_sjsymbol;


    public smallJava_SJClass(
    ) {
        super(
        );
        this.smalljava_sjmembers = new ArrayList<>();
    }

    public smallJava_SJClass(
        ArrayList<smallJava_SJMember> smalljava_sjmembers    ) {
        this.smalljava_sjmembers = smalljava_sjmembers;
    }


    public smallJava_SJMember getSmalljava_sjmember() {
        return smalljava_sjmember;
    }

    public void setSmalljava_sjmember(smallJava_SJMember smalljava_sjmember) {
        this.smalljava_sjmember = smalljava_sjmember;
    }
    public smallJava_SJClass getSmalljava_sjclass() {
        return smalljava_sjclass;
    }

    public void setSmalljava_sjclass(smallJava_SJClass smalljava_sjclass) {
        this.smalljava_sjclass = smalljava_sjclass;
    }
    public List<smallJava_SJMember> getSmalljava_sjmembers() {
        return smalljava_sjmembers;
    }

    public void addSmalljava_sjmember(Smalljava_sjmember smalljava_sjmember) {
        this.smalljava_sjmembers.add(smalljava_sjmember);
    }
    public smallJava_SJProgram getSmalljava_sjprogram() {
        return smalljava_sjprogram;
    }

    public void setSmalljava_sjprogram(smallJava_SJProgram smalljava_sjprogram) {
        this.smalljava_sjprogram = smalljava_sjprogram;
    }
    public smallJava_SJNew getSmalljava_sjnew() {
        return smalljava_sjnew;
    }

    public void setSmalljava_sjnew(smallJava_SJNew smalljava_sjnew) {
        this.smalljava_sjnew = smalljava_sjnew;
    }
    public smallJava_SJSymbol getSmalljava_sjsymbol() {
        return smalljava_sjsymbol;
    }

    public void setSmalljava_sjsymbol(smallJava_SJSymbol smalljava_sjsymbol) {
        this.smalljava_sjsymbol = smalljava_sjsymbol;
    }

}