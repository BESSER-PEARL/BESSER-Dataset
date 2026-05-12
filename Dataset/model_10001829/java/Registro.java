





import java.util.List;
import java.util.ArrayList;

public class Registro  {

    private None Auxiliar;
    private String Hora_entrada;
    private None Tipo_Mascota;
    private String Hora_salida;
    private None Cliente;





    private Mascotas mascotas;


    public Registro(
        None Auxiliar,        String Hora_entrada,        None Tipo_Mascota,        String Hora_salida,        None Cliente    ) {
        this.Auxiliar = Auxiliar;
        this.Hora_entrada = Hora_entrada;
        this.Tipo_Mascota = Tipo_Mascota;
        this.Hora_salida = Hora_salida;
        this.Cliente = Cliente;
    }


    public None getAuxiliar() {
        return Auxiliar;
    }

    public void setAuxiliar(None Auxiliar) {
        this.Auxiliar = Auxiliar;
    }
    public String getHora_entrada() {
        return Hora_entrada;
    }

    public void setHora_entrada(String Hora_entrada) {
        this.Hora_entrada = Hora_entrada;
    }
    public None getTipo_mascota() {
        return Tipo_Mascota;
    }

    public void setTipo_mascota(None Tipo_Mascota) {
        this.Tipo_Mascota = Tipo_Mascota;
    }
    public String getHora_salida() {
        return Hora_salida;
    }

    public void setHora_salida(String Hora_salida) {
        this.Hora_salida = Hora_salida;
    }
    public None getCliente() {
        return Cliente;
    }

    public void setCliente(None Cliente) {
        this.Cliente = Cliente;
    }

    public Mascotas getMascotas() {
        return mascotas;
    }

    public void setMascotas(Mascotas mascotas) {
        this.mascotas = mascotas;
    }

}