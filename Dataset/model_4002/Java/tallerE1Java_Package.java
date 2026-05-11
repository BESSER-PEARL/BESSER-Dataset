





import java.util.List;
import java.util.ArrayList;

public class tallerE1Java_Package  {

    private String name;





    private tallerE1Java_Program tallere1java_program;




    private List<tallerE1Java_Class> tallere1java_classs;


    public tallerE1Java_Package(
        String name    ) {
        this.name = name;
        this.tallere1java_classs = new ArrayList<>();
    }

    public tallerE1Java_Package(
        String name        ArrayList<tallerE1Java_Class> tallere1java_classs    ) {
        this.name = name;
        this.tallere1java_classs = tallere1java_classs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tallerE1Java_Program getTallere1java_program() {
        return tallere1java_program;
    }

    public void setTallere1java_program(tallerE1Java_Program tallere1java_program) {
        this.tallere1java_program = tallere1java_program;
    }
    public List<tallerE1Java_Class> getTallere1java_classs() {
        return tallere1java_classs;
    }

    public void addTallere1java_class(Tallere1java_class tallere1java_class) {
        this.tallere1java_classs.add(tallere1java_class);
    }

}