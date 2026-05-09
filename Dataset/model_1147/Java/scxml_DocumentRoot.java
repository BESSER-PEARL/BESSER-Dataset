





import java.util.List;
import java.util.ArrayList;

public class scxml_DocumentRoot  {

    private String mixed;





    private List<scxml_ScxmlScxmlType> scxml_scxmlscxmltypes;


    public scxml_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.scxml_scxmlscxmltypes = new ArrayList<>();
    }

    public scxml_DocumentRoot(
        String mixed        ArrayList<scxml_ScxmlScxmlType> scxml_scxmlscxmltypes    ) {
        this.mixed = mixed;
        this.scxml_scxmlscxmltypes = scxml_scxmlscxmltypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<scxml_ScxmlScxmlType> getScxml_scxmlscxmltypes() {
        return scxml_scxmlscxmltypes;
    }

    public void addScxml_scxmlscxmltype(Scxml_scxmlscxmltype scxml_scxmlscxmltype) {
        this.scxml_scxmlscxmltypes.add(scxml_scxmlscxmltype);
    }

}