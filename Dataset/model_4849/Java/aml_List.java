





import java.util.List;
import java.util.ArrayList;

public class aml_List  {

    private String group;





    private List<aml_EObject> aml_eobjects;




    private aml_DocumentRoot aml_documentroot;


    public aml_List(
        String group    ) {
        this.group = group;
        this.aml_eobjects = new ArrayList<>();
    }

    public aml_List(
        String group        ArrayList<aml_EObject> aml_eobjects    ) {
        this.group = group;
        this.aml_eobjects = aml_eobjects;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<aml_EObject> getAml_eobjects() {
        return aml_eobjects;
    }

    public void addAml_eobject(Aml_eobject aml_eobject) {
        this.aml_eobjects.add(aml_eobject);
    }
    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }

}