





import java.util.List;
import java.util.ArrayList;

public class error3_RecursiveComponen extends AbstractComponent {






    private List<error3_RecursiveComponen> error3_recursivecomponens;


    public error3_RecursiveComponen(
    ) {
        super(
        );
        this.error3_recursivecomponens = new ArrayList<>();
    }

    public error3_RecursiveComponen(
        ArrayList<error3_RecursiveComponen> error3_recursivecomponens    ) {
        this.error3_recursivecomponens = error3_recursivecomponens;
    }


    public List<error3_RecursiveComponen> getError3_recursivecomponens() {
        return error3_recursivecomponens;
    }

    public void addError3_recursivecomponen(Error3_recursivecomponen error3_recursivecomponen) {
        this.error3_recursivecomponens.add(error3_recursivecomponen);
    }

}