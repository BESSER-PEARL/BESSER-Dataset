





import java.util.List;
import java.util.ArrayList;

public class error3_AbstractComponent  {

    private String name;





    private List<error3_Provided> error3_provideds;




    private List<error3_Required> error3_requireds;


    public error3_AbstractComponent(
        String name    ) {
        this.name = name;
        this.error3_provideds = new ArrayList<>();
        this.error3_requireds = new ArrayList<>();
    }

    public error3_AbstractComponent(
        String name        ArrayList<error3_Provided> error3_provideds,        ArrayList<error3_Required> error3_requireds    ) {
        this.name = name;
        this.error3_provideds = error3_provideds;
        this.error3_requireds = error3_requireds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<error3_Provided> getError3_provideds() {
        return error3_provideds;
    }

    public void addError3_provided(Error3_provided error3_provided) {
        this.error3_provideds.add(error3_provided);
    }
    public List<error3_Required> getError3_requireds() {
        return error3_requireds;
    }

    public void addError3_required(Error3_required error3_required) {
        this.error3_requireds.add(error3_required);
    }

}