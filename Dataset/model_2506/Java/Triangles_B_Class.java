





import java.util.List;
import java.util.ArrayList;

public class Triangles_B_Class extends AbstractClass {






    private List<Triangles_A_Class> triangles_a_classs;




    private Triangles_A_Class triangles_a_class;




    private Triangles_Container triangles_container;




    private Triangles_E_Class triangles_e_class;




    private List<Triangles_C_Class> triangles_c_classs;




    private Triangles_C_Class triangles_c_class;


    public Triangles_B_Class(
    ) {
        super(
        );
        this.triangles_a_classs = new ArrayList<>();
        this.triangles_c_classs = new ArrayList<>();
    }

    public Triangles_B_Class(
        ArrayList<Triangles_A_Class> triangles_a_classs,        ArrayList<Triangles_C_Class> triangles_c_classs    ) {
        this.triangles_a_classs = triangles_a_classs;
        this.triangles_c_classs = triangles_c_classs;
    }


    public List<Triangles_A_Class> getTriangles_a_classs() {
        return triangles_a_classs;
    }

    public void addTriangles_a_class(Triangles_a_class triangles_a_class) {
        this.triangles_a_classs.add(triangles_a_class);
    }
    public Triangles_A_Class getTriangles_a_class() {
        return triangles_a_class;
    }

    public void setTriangles_a_class(Triangles_A_Class triangles_a_class) {
        this.triangles_a_class = triangles_a_class;
    }
    public Triangles_Container getTriangles_container() {
        return triangles_container;
    }

    public void setTriangles_container(Triangles_Container triangles_container) {
        this.triangles_container = triangles_container;
    }
    public Triangles_E_Class getTriangles_e_class() {
        return triangles_e_class;
    }

    public void setTriangles_e_class(Triangles_E_Class triangles_e_class) {
        this.triangles_e_class = triangles_e_class;
    }
    public List<Triangles_C_Class> getTriangles_c_classs() {
        return triangles_c_classs;
    }

    public void addTriangles_c_class(Triangles_c_class triangles_c_class) {
        this.triangles_c_classs.add(triangles_c_class);
    }
    public Triangles_C_Class getTriangles_c_class() {
        return triangles_c_class;
    }

    public void setTriangles_c_class(Triangles_C_Class triangles_c_class) {
        this.triangles_c_class = triangles_c_class;
    }

}