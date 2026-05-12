





import java.util.List;
import java.util.ArrayList;

public class Manager2  {

    private String password;
    private String name;
    private int id;





    private List<Employee1> employee1s;


    public Manager2(
        String password,        String name,        int id    ) {
        this.password = password;
        this.name = name;
        this.id = id;
        this.employee1s = new ArrayList<>();
    }

    public Manager2(
        String password,        String name,        int id        ArrayList<Employee1> employee1s    ) {
        this.password = password;
        this.name = name;
        this.id = id;
        this.employee1s = employee1s;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Employee1> getEmployee1s() {
        return employee1s;
    }

    public void addEmployee1(Employee1 employee1) {
        this.employee1s.add(employee1);
    }

}