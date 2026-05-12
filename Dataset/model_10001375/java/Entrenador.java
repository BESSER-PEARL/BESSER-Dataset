





import java.util.List;
import java.util.ArrayList;

public class Entrenador  {

    private int a_os_de_experiencia;
    private String nivel_de_acreditaci_n;



    public Entrenador(
        int a_os_de_experiencia,        String nivel_de_acreditaci_n    ) {
        this.a_os_de_experiencia = a_os_de_experiencia;
        this.nivel_de_acreditaci_n = nivel_de_acreditaci_n;
    }


    public int getA_os_de_experiencia() {
        return a_os_de_experiencia;
    }

    public void setA_os_de_experiencia(int a_os_de_experiencia) {
        this.a_os_de_experiencia = a_os_de_experiencia;
    }
    public String getNivel_de_acreditaci_n() {
        return nivel_de_acreditaci_n;
    }

    public void setNivel_de_acreditaci_n(String nivel_de_acreditaci_n) {
        this.nivel_de_acreditaci_n = nivel_de_acreditaci_n;
    }


}