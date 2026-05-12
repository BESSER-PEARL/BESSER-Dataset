





import java.util.List;
import java.util.ArrayList;

public class STUDENT  {

    private String id;





    private List<FACULTY> facultys;


    public STUDENT(
        String id    ) {
        this.id = id;
        this.facultys = new ArrayList<>();
    }

    public STUDENT(
        String id        ArrayList<FACULTY> facultys    ) {
        this.id = id;
        this.facultys = facultys;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<FACULTY> getFacultys() {
        return facultys;
    }

    public void addFaculty(Faculty faculty) {
        this.facultys.add(faculty);
    }

}