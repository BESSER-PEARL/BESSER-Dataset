





import java.util.List;
import java.util.ArrayList;

public class typeEmploy_  {

    private String id;





    private List<Employ_> employ_s;


    public typeEmploy_(
        String id    ) {
        this.id = id;
        this.employ_s = new ArrayList<>();
    }

    public typeEmploy_(
        String id        ArrayList<Employ_> employ_s    ) {
        this.id = id;
        this.employ_s = employ_s;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Employ_> getEmploy_s() {
        return employ_s;
    }

    public void addEmploy_(Employ_ employ_) {
        this.employ_s.add(employ_);
    }

}