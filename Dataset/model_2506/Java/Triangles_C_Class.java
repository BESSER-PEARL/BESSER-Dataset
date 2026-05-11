





import java.util.List;
import java.util.ArrayList;

public class Triangles_C_Class extends AbstractClass {






    private Triangles_A_Class triangles_a_class;




    private Triangles_Container triangles_container;




    private List<Triangles_A_Class> triangles_a_classs;


    public Triangles_C_Class(
    ) {
        super(
        );
        this.triangles_a_classs = new ArrayList<>();
    }

    public Triangles_C_Class(
        ArrayList<Triangles_A_Class> triangles_a_classs    ) {
        this.triangles_a_classs = triangles_a_classs;
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
    public List<Triangles_A_Class> getTriangles_a_classs() {
        return triangles_a_classs;
    }

    public void addTriangles_a_class(Triangles_a_class triangles_a_class) {
        this.triangles_a_classs.add(triangles_a_class);
    }

}