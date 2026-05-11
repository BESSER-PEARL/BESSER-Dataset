





import java.util.List;
import java.util.ArrayList;

public class toppkg_TopClass1  {






    private List<Subpkg2Class1> subpkg2class1s;




    private List<Subpkg1Class1> subpkg1class1s;




    private List<toppkg_TopClass2> toppkg_topclass2s;




    private toppkg_TopClass2 toppkg_topclass2;


    public toppkg_TopClass1(
    ) {
        this.subpkg2class1s = new ArrayList<>();
        this.subpkg1class1s = new ArrayList<>();
        this.toppkg_topclass2s = new ArrayList<>();
    }

    public toppkg_TopClass1(
        ArrayList<Subpkg2Class1> subpkg2class1s,        ArrayList<Subpkg1Class1> subpkg1class1s,        ArrayList<toppkg_TopClass2> toppkg_topclass2s    ) {
        this.subpkg2class1s = subpkg2class1s;
        this.subpkg1class1s = subpkg1class1s;
        this.toppkg_topclass2s = toppkg_topclass2s;
    }


    public List<Subpkg2Class1> getSubpkg2class1s() {
        return subpkg2class1s;
    }

    public void addSubpkg2class1(Subpkg2class1 subpkg2class1) {
        this.subpkg2class1s.add(subpkg2class1);
    }
    public List<Subpkg1Class1> getSubpkg1class1s() {
        return subpkg1class1s;
    }

    public void addSubpkg1class1(Subpkg1class1 subpkg1class1) {
        this.subpkg1class1s.add(subpkg1class1);
    }
    public List<toppkg_TopClass2> getToppkg_topclass2s() {
        return toppkg_topclass2s;
    }

    public void addToppkg_topclass2(Toppkg_topclass2 toppkg_topclass2) {
        this.toppkg_topclass2s.add(toppkg_topclass2);
    }
    public toppkg_TopClass2 getToppkg_topclass2() {
        return toppkg_topclass2;
    }

    public void setToppkg_topclass2(toppkg_TopClass2 toppkg_topclass2) {
        this.toppkg_topclass2 = toppkg_topclass2;
    }

}