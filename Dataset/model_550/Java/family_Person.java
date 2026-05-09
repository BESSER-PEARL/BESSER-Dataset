





import java.util.List;
import java.util.ArrayList;

public class family_Person  {

    private String name;
    private String fechaNacimiento;
    private String eCivil;
    private String provincia;





    private family_Family family_family;


    public family_Person(
        String name,        String fechaNacimiento,        String eCivil,        String provincia    ) {
        this.name = name;
        this.fechaNacimiento = fechaNacimiento;
        this.eCivil = eCivil;
        this.provincia = provincia;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFechanacimiento() {
        return fechaNacimiento;
    }

    public void setFechanacimiento(String fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }
    public String getEcivil() {
        return eCivil;
    }

    public void setEcivil(String eCivil) {
        this.eCivil = eCivil;
    }
    public String getProvincia() {
        return provincia;
    }

    public void setProvincia(String provincia) {
        this.provincia = provincia;
    }

    public family_Family getFamily_family() {
        return family_family;
    }

    public void setFamily_family(family_Family family_family) {
        this.family_family = family_family;
    }

}