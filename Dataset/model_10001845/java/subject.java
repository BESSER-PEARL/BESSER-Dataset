





import java.util.List;
import java.util.ArrayList;

public class subject  {

    private int id;
    private String name;





    private admin admin;




    private claas1 claas1;


    public subject(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public admin getAdmin() {
        return admin;
    }

    public void setAdmin(admin admin) {
        this.admin = admin;
    }
    public claas1 getClaas1() {
        return claas1;
    }

    public void setClaas1(claas1 claas1) {
        this.claas1 = claas1;
    }

}