





import java.util.List;
import java.util.ArrayList;

public class wxyz_W extends NamedElt {

    private String propOfW;





    private wxyz_Model wxyz_model;




    private List<wxyz_W> wxyz_ws;


    public wxyz_W(
        String propOfW    ) {
        super(
        );
        this.propOfW = propOfW;
        this.wxyz_ws = new ArrayList<>();
    }

    public wxyz_W(
        String propOfW        ArrayList<wxyz_W> wxyz_ws    ) {
        this.propOfW = propOfW;
        this.wxyz_ws = wxyz_ws;
    }

    public String getPropofw() {
        return propOfW;
    }

    public void setPropofw(String propOfW) {
        this.propOfW = propOfW;
    }

    public wxyz_Model getWxyz_model() {
        return wxyz_model;
    }

    public void setWxyz_model(wxyz_Model wxyz_model) {
        this.wxyz_model = wxyz_model;
    }
    public List<wxyz_W> getWxyz_ws() {
        return wxyz_ws;
    }

    public void addWxyz_w(Wxyz_w wxyz_w) {
        this.wxyz_ws.add(wxyz_w);
    }

}