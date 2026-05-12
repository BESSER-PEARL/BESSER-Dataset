





import java.util.List;
import java.util.ArrayList;

public class STUDENT  {

    private String password;
    private String id;





    private List<FACULTY> facultys;


    public STUDENT(
        String password,        String id    ) {
        this.password = password;
        this.id = id;
        this.facultys = new ArrayList<>();
    }

    public STUDENT(
        String password,        String id        ArrayList<FACULTY> facultys    ) {
        this.password = password;
        this.id = id;
        this.facultys = facultys;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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