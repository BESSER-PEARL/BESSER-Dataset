





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_FromAttributeOwner  {






    private uml2rdbms_FromAttribute uml2rdbms_fromattribute;




    private List<uml2rdbms_FromAttribute> uml2rdbms_fromattributes;


    public uml2rdbms_FromAttributeOwner(
    ) {
        this.uml2rdbms_fromattributes = new ArrayList<>();
    }

    public uml2rdbms_FromAttributeOwner(
        ArrayList<uml2rdbms_FromAttribute> uml2rdbms_fromattributes    ) {
        this.uml2rdbms_fromattributes = uml2rdbms_fromattributes;
    }


    public uml2rdbms_FromAttribute getUml2rdbms_fromattribute() {
        return uml2rdbms_fromattribute;
    }

    public void setUml2rdbms_fromattribute(uml2rdbms_FromAttribute uml2rdbms_fromattribute) {
        this.uml2rdbms_fromattribute = uml2rdbms_fromattribute;
    }
    public List<uml2rdbms_FromAttribute> getUml2rdbms_fromattributes() {
        return uml2rdbms_fromattributes;
    }

    public void addUml2rdbms_fromattribute(Uml2rdbms_fromattribute uml2rdbms_fromattribute) {
        this.uml2rdbms_fromattributes.add(uml2rdbms_fromattribute);
    }

}