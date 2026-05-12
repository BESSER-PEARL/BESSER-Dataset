





import java.util.List;
import java.util.ArrayList;

public class STUDENT  {

    private String id;
    private String password;





    private List<FACULTY> facultys;


    public STUDENT(
        String id,        String password    ) {
        this.id = id;
        this.password = password;
        this.facultys = new ArrayList<>();
    }

    public STUDENT(
        String id,        String password        ArrayList<FACULTY> facultys    ) {
        this.id = id;
        this.password = password;
        this.facultys = facultys;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<FACULTY> getFacultys() {
        return facultys;
    }

    public void addFaculty(Faculty faculty) {
        this.facultys.add(faculty);
    }

}