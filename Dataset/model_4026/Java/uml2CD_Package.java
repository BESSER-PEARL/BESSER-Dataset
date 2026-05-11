





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Package extends NamedElement {






    private List<uml2CD_Association> uml2cd_associations;




    private List<uml2CD_DataType> uml2cd_datatypes;




    private uml2CD_Package uml2cd_package;




    private List<uml2CD_Generalization> uml2cd_generalizations;


    public uml2CD_Package(
    ) {
        super(
        );
        this.uml2cd_associations = new ArrayList<>();
        this.uml2cd_datatypes = new ArrayList<>();
        this.uml2cd_generalizations = new ArrayList<>();
    }

    public uml2CD_Package(
        ArrayList<uml2CD_Association> uml2cd_associations,        ArrayList<uml2CD_DataType> uml2cd_datatypes,        ArrayList<uml2CD_Generalization> uml2cd_generalizations    ) {
        this.uml2cd_associations = uml2cd_associations;
        this.uml2cd_datatypes = uml2cd_datatypes;
        this.uml2cd_generalizations = uml2cd_generalizations;
    }


    public List<uml2CD_Association> getUml2cd_associations() {
        return uml2cd_associations;
    }

    public void addUml2cd_association(Uml2cd_association uml2cd_association) {
        this.uml2cd_associations.add(uml2cd_association);
    }
    public List<uml2CD_DataType> getUml2cd_datatypes() {
        return uml2cd_datatypes;
    }

    public void addUml2cd_datatype(Uml2cd_datatype uml2cd_datatype) {
        this.uml2cd_datatypes.add(uml2cd_datatype);
    }
    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public List<uml2CD_Generalization> getUml2cd_generalizations() {
        return uml2cd_generalizations;
    }

    public void addUml2cd_generalization(Uml2cd_generalization uml2cd_generalization) {
        this.uml2cd_generalizations.add(uml2cd_generalization);
    }

}