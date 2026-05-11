





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Enumeration extends DataType {






    private uml2CD_Parameter uml2cd_parameter;




    private uml2CD_Package uml2cd_package;




    private List<uml2CD_EnumerationLiteral> uml2cd_enumerationliterals;


    public uml2CD_Enumeration(
    ) {
        super(
        );
        this.uml2cd_enumerationliterals = new ArrayList<>();
    }

    public uml2CD_Enumeration(
        ArrayList<uml2CD_EnumerationLiteral> uml2cd_enumerationliterals    ) {
        this.uml2cd_enumerationliterals = uml2cd_enumerationliterals;
    }


    public uml2CD_Parameter getUml2cd_parameter() {
        return uml2cd_parameter;
    }

    public void setUml2cd_parameter(uml2CD_Parameter uml2cd_parameter) {
        this.uml2cd_parameter = uml2cd_parameter;
    }
    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public List<uml2CD_EnumerationLiteral> getUml2cd_enumerationliterals() {
        return uml2cd_enumerationliterals;
    }

    public void addUml2cd_enumerationliteral(Uml2cd_enumerationliteral uml2cd_enumerationliteral) {
        this.uml2cd_enumerationliterals.add(uml2cd_enumerationliteral);
    }

}