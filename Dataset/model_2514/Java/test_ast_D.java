





import java.util.List;
import java.util.ArrayList;

public class test_ast_D extends AbstractD {

    private String someQCollection;
    private String someCollection;
    private boolean someBool;
    private String name;
    private int index;
    private String someOtherBool;





    private List<C> cs;




    private D d;




    private D d;




    private A a;




    private List<A> as;




    private List<D> ds;




    private List<C> cs;




    private C c;


    public test_ast_D(
        String someQCollection,        String someCollection,        boolean someBool,        String name,        int index,        String someOtherBool    ) {
        super(
        );
        this.someQCollection = someQCollection;
        this.someCollection = someCollection;
        this.someBool = someBool;
        this.name = name;
        this.index = index;
        this.someOtherBool = someOtherBool;
        this.cs = new ArrayList<>();
        this.as = new ArrayList<>();
        this.ds = new ArrayList<>();
        this.cs = new ArrayList<>();
    }

    public test_ast_D(
        String someQCollection,        String someCollection,        boolean someBool,        String name,        int index,        String someOtherBool        ArrayList<C> cs,        ArrayList<A> as,        ArrayList<D> ds,        ArrayList<C> cs    ) {
        this.someQCollection = someQCollection;
        this.someCollection = someCollection;
        this.someBool = someBool;
        this.name = name;
        this.index = index;
        this.someOtherBool = someOtherBool;
        this.cs = cs;
        this.as = as;
        this.ds = ds;
        this.cs = cs;
    }

    public String getSomeqcollection() {
        return someQCollection;
    }

    public void setSomeqcollection(String someQCollection) {
        this.someQCollection = someQCollection;
    }
    public String getSomecollection() {
        return someCollection;
    }

    public void setSomecollection(String someCollection) {
        this.someCollection = someCollection;
    }
    public boolean getSomebool() {
        return someBool;
    }

    public void setSomebool(boolean someBool) {
        this.someBool = someBool;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public String getSomeotherbool() {
        return someOtherBool;
    }

    public void setSomeotherbool(String someOtherBool) {
        this.someOtherBool = someOtherBool;
    }

    public List<C> getCs() {
        return cs;
    }

    public void addC(C c) {
        this.cs.add(c);
    }
    public D getD() {
        return d;
    }

    public void setD(D d) {
        this.d = d;
    }
    public D getD() {
        return d;
    }

    public void setD(D d) {
        this.d = d;
    }
    public A getA() {
        return a;
    }

    public void setA(A a) {
        this.a = a;
    }
    public List<A> getAs() {
        return as;
    }

    public void addA(A a) {
        this.as.add(a);
    }
    public List<D> getDs() {
        return ds;
    }

    public void addD(D d) {
        this.ds.add(d);
    }
    public List<C> getCs() {
        return cs;
    }

    public void addC(C c) {
        this.cs.add(c);
    }
    public C getC() {
        return c;
    }

    public void setC(C c) {
        this.c = c;
    }

}