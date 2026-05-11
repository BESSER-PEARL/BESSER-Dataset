





import java.util.List;
import java.util.ArrayList;

public class errorkref_M  {

    private String id;





    private List<errorkref_I> errorkref_is;


    public errorkref_M(
        String id    ) {
        this.id = id;
        this.errorkref_is = new ArrayList<>();
    }

    public errorkref_M(
        String id        ArrayList<errorkref_I> errorkref_is    ) {
        this.id = id;
        this.errorkref_is = errorkref_is;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<errorkref_I> getErrorkref_is() {
        return errorkref_is;
    }

    public void addErrorkref_i(Errorkref_i errorkref_i) {
        this.errorkref_is.add(errorkref_i);
    }

}