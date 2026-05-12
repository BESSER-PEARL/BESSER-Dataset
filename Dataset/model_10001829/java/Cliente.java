





import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private int Tel_fono;
    private String C_dula;





    private List<Mascotas> mascotass;




    private List<Registro> registros;


    public Cliente(
        int Tel_fono,        String C_dula    ) {
        this.Tel_fono = Tel_fono;
        this.C_dula = C_dula;
        this.mascotass = new ArrayList<>();
        this.registros = new ArrayList<>();
    }

    public Cliente(
        int Tel_fono,        String C_dula        ArrayList<Mascotas> mascotass,        ArrayList<Registro> registros    ) {
        this.Tel_fono = Tel_fono;
        this.C_dula = C_dula;
        this.mascotass = mascotass;
        this.registros = registros;
    }

    public int getTel_fono() {
        return Tel_fono;
    }

    public void setTel_fono(int Tel_fono) {
        this.Tel_fono = Tel_fono;
    }
    public String getC_dula() {
        return C_dula;
    }

    public void setC_dula(String C_dula) {
        this.C_dula = C_dula;
    }

    public List<Mascotas> getMascotass() {
        return mascotass;
    }

    public void addMascotas(Mascotas mascotas) {
        this.mascotass.add(mascotas);
    }
    public List<Registro> getRegistros() {
        return registros;
    }

    public void addRegistro(Registro registro) {
        this.registros.add(registro);
    }

}