





import java.util.List;
import java.util.ArrayList;

public class error3_NestedComponent extends AbstractComponent {






    private List<error3_Level2> error3_level2s;




    private error3_RecursiveComponen error3_recursivecomponen;


    public error3_NestedComponent(
    ) {
        super(
        );
        this.error3_level2s = new ArrayList<>();
    }

    public error3_NestedComponent(
        ArrayList<error3_Level2> error3_level2s    ) {
        this.error3_level2s = error3_level2s;
    }


    public List<error3_Level2> getError3_level2s() {
        return error3_level2s;
    }

    public void addError3_level2(Error3_level2 error3_level2) {
        this.error3_level2s.add(error3_level2);
    }
    public error3_RecursiveComponen getError3_recursivecomponen() {
        return error3_recursivecomponen;
    }

    public void setError3_recursivecomponen(error3_RecursiveComponen error3_recursivecomponen) {
        this.error3_recursivecomponen = error3_recursivecomponen;
    }

}