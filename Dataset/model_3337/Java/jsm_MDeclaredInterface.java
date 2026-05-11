





import java.util.List;
import java.util.ArrayList;

public class jsm_MDeclaredInterface extends AbstractMDeclaredType, AbstractMInterface {






    private List<jsm_AbstractMInterface> jsm_abstractminterfaces;


    public jsm_MDeclaredInterface(
    ) {
        super(
        );
        this.jsm_abstractminterfaces = new ArrayList<>();
    }

    public jsm_MDeclaredInterface(
        ArrayList<jsm_AbstractMInterface> jsm_abstractminterfaces    ) {
        this.jsm_abstractminterfaces = jsm_abstractminterfaces;
    }


    public List<jsm_AbstractMInterface> getJsm_abstractminterfaces() {
        return jsm_abstractminterfaces;
    }

    public void addJsm_abstractminterface(Jsm_abstractminterface jsm_abstractminterface) {
        this.jsm_abstractminterfaces.add(jsm_abstractminterface);
    }

}